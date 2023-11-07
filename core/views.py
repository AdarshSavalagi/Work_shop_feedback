from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .models import CustomUser
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
import json,os
from supporting.send_mail import create


def loginView(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            department = form.cleaned_data['department']
            if CustomUser.objects.filter(email=email).exists():
                user = authenticate(request, username=email,
                                    password='11111111')
                user.department = department
                user.save()
                if user is not None:
                    login(request, user)
                    return redirect('feedback')
            else:
                name = form.cleaned_data['name']
                phone_number = form.cleaned_data['phone_number']
                user = CustomUser(first_name=name, phone_number=phone_number,
                                  department=department, real_user=False, username=email, email=email)
                user.save()
                user.set_password('11111111')
                user.save()
                login(request, user)
                return redirect('feedback')
    return render(request, 'index.html', {'form': UserRegisterForm()})


@login_required(login_url='/')
def take_feedback(request):
    if request.method == 'POST':
        feedback_dict = request.POST.dict()
        del feedback_dict['csrfmiddlewaretoken']
        user = request.user
        user.feedback = feedback_dict
        user.save()
        print(feedback_dict)
        return redirect('quiz')

    with open(os.path.join('static', 'feedback.json'), 'r') as file:
        data = json.load(file)
    return render(request, 'feedback.html', context={'data': data})

@login_required(login_url='/')
def take_quiz(request):
    with open(os.path.join('static','quiz_questions.json'),'r') as file:
        data = json.load(file)
    if request.method == 'POST':
        quiz_dict = request.POST.dict()
        del quiz_dict['csrfmiddlewaretoken']
        user = request.user
        user.quiz = quiz_dict
        num=0
        for index,i in enumerate(quiz_dict.keys()):
            if int(quiz_dict[i])==data[index]['answer']:
                num+=2
        user.quiz_marks=num
        user.save()
        return redirect('certificate')
    
    return render(request, 'quiz.html', context={'data': data})

@login_required(login_url='/')
def certificate(request):
    with open(os.path.join('static','quiz_questions.json'),'r') as file:
        data = json.load(file)
    return render(request,'certificate.html',{'real_user':request.user.real_user,'marks':request.user.quiz_marks,'user_answer':request.user.quiz,'data':data})

@login_required(login_url='/')
def generate_certificate(request):
    if request.method == 'POST':
        # Call your create function to generate the image bytes
        text = request.user.first_name
        image_bytes = create(os.path.join('supporting','icriis.jpg'), text)

        # Create an HTTP response with the image bytes
        response = HttpResponse(content_type='image/jpeg')  
        response['Content-Disposition'] = 'attachment; filename="certificate.jpeg"'
        response.write(image_bytes)

        return response
    return HttpResponse('Invalid request')
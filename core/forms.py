from django import forms

from .models import CustomUser


class UserRegisterForm(forms.Form):
    name = forms.CharField(max_length=50, required=True, help_text='Full name', widget=forms.TextInput(
        attrs={'placeholder': 'Enter your name', 'class': "bg-gray-200 appearance-none border-2 border-gray-200 rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-purple-500"}))
    email = forms.EmailField(required=True, help_text='Email', widget=forms.TextInput(
        attrs={'placeholder': 'Enter your Email', 'class': "bg-gray-200 appearance-none border-2 border-gray-200 rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-purple-500"}))
    phone_number = forms.CharField(max_length=25, help_text='Phone', required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Enter your Phone', 'class': "bg-gray-200 appearance-none border-2 border-gray-200 rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-purple-500"}))
    department = forms.CharField(max_length=50, help_text='Department', widget=forms.TextInput(
        attrs={'placeholder': 'Enter your Department', 'class': "bg-gray-200 appearance-none border-2 border-gray-200 rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-purple-500"}))


from django.urls import path
from .views import *

urlpatterns = [
    path('',loginView,name='login'),
    path('feedback/',take_feedback,name='feedback'),
    path('quiz/',take_quiz,name='quiz'),
    path('certificate/',certificate,name='certificate'),
    path('download-certificate/',generate_certificate,name='download_certificate'),

]
from django.contrib import admin
from .models import CustomUser


class adminView(admin.ModelAdmin):
    list_display=['first_name','email','has_attended_quiz']
    search_fields=['first_name']
    list_per_page=100
    
admin.site.register(CustomUser,adminView)
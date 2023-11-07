import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'feedback.settings')
django.setup()

import pandas as pd
from core.models import CustomUser

df = pd.read_excel('static/data.xlsx') 

def createdb():
    for _, row in df.iterrows():
        name = row[1]
        email = row[2]
        phone = row[3]
        user = CustomUser(first_name=name, username=email, email=email, phone_number=phone)
        user.save()
        user.set_password('11111111')
        user.save()
        print(f"user: {name} saved")

if __name__ == '__main__':
    createdb()
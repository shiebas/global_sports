# admin_session_test.py
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'global_sports.settings')
django.setup()

from django.test import Client
client = Client()

# First request should set both cookies
response = client.get('/admin/login/',
                     HTTP_HOST='neetiesister.pythonanywhere.com',
                     secure=True)
print("Status:", response.status_code)
print("Cookies:", response.cookies)  # Should show both csrftoken and sessionid
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'global_sports.settings')
django.setup()

from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()
user = User.objects.first()

if user:
    refresh = RefreshToken.for_user(user)
    print(f"""
    JWT Setup Successful!
    Access Token: {refresh.access_token}
    Refresh Token: {refresh}
    """)
else:
    print("Error: No users exist. Create one with:")
    print("python manage.py createsuperuser")
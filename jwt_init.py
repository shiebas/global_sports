import os
import django
import sys
from django.core.exceptions import ImproperlyConfigured

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'global_sports.settings')

try:
    django.setup()
except ImproperlyConfigured as e:
    print(f"Error configuring Django: {str(e)}")
    sys.exit(1)

def generate_jwt_for_user():
    """Generate JWT tokens for the first available user"""
    try:
        from geography.models import User
        from rest_framework_simplejwt.tokens import RefreshToken
        from django.core.exceptions import ObjectDoesNotExist

        try:
            # Get the first active superuser if available, else first user
            user = User.objects.filter(is_active=True).order_by('-is_superuser').first()

            if not user:
                raise ObjectDoesNotExist("No users exist in the database")

            refresh = RefreshToken.for_user(user)

            return {
                'access': str(refresh.access_token),
                'refresh': str(refresh),
                'user_id': user.id,
                'username': user.username
            }

        except ObjectDoesNotExist:
            print("Error: No users exist in the database.")
            print("Create one with: python manage.py createsuperuser")
            return None

    except ImportError as e:
        print(f"Import Error: {str(e)}")
        print("Make sure you have installed:")
        print("- django-rest-framework-simplejwt")
        print("- Your custom User model is properly configured")
        return None

if __name__ == "__main__":
    tokens = generate_jwt_for_user()
    if tokens:
        print("\nJWT Setup Successful!")
        print(f"User: {tokens['username']} (ID: {tokens['user_id']})")
        print(f"Access Token: {tokens['access']}")
        print(f"Refresh Token: {tokens['refresh']}\n")
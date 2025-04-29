import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'global_sports.settings')
django.setup()

# Now test JWT
try:
    from rest_framework_simplejwt.authentication import JWTAuthentication
    print("✓ JWT is properly configured!")
except ImportError:
    print("✗ Error: djangorestframework-simplejwt not installed")
except Exception as e:
    print(f"✗ Configuration error: {str(e)}")
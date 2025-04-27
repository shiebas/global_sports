import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'b%+w_2m9k2*enr^=k8rrwjiot4*te%#o9cs^gs(ay8ozo6l@)@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ALLOWED_HOSTS = ['neetiesister.pythonanywhere.com']

AUTH_USER_MODEL = 'geography.User'

# Application definition

INSTALLED_APPS = [
    'geography',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'global_sports.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'global_sports.wsgi.application'
PRODUCTION = True

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'NeetieSister$global_sports',
        'USER': 'NeetieSister',
        'PASSWORD': 'hermia12345',  # From Databases tab
        'HOST': 'NeetieSister.mysql.pythonanywhere-services.com',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES', innodb_strict_mode=1",
            'connect_timeout': 10,
        },
        'TEST': {
            'CHARSET': 'utf8mb4',
            'COLLATION': 'utf8mb4_unicode_ci',
        },
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '/home/NeetieSister/global_sports/static_prod'  # Absolute path
STATICFILES_DIRS = [
    '/home/NeetieSister/global_sports/static_src',  # Absolute path
]

# Ensure they don't point to the same directory
print(f"STATIC_ROOT: {STATIC_ROOT}")  # Should be different from STATICFILES_DIRS
print(f"STATICFILES_DIRS: {STATICFILES_DIRS}")
# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# default static files settings for PythonAnywhere.
# see https://help.pythonanywhere.com/pages/DjangoStaticFiles for more info
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
LOGIN_REDIRECT_URL = '/admin/'  # Where to redirect after login
LOGOUT_REDIRECT_URL = '/login/'  # Where to redirect after logout
LOGIN_URL = '/login/'  # For login_required decorator

CSRF_COOKIE_SECURE = True # Set to True in production with HTTPS
CSRF_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 30 * 24 * 60 * 60
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SAMESITE = 'Lax'  # Prevents some cross-window issues
CSRF_FAILURE_VIEW = 'django.views.csrf.csrf_failure'
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')  # For PythonAnywhere



# Create directories if they don't exist
os.makedirs(STATIC_ROOT, exist_ok=True)
os.makedirs(STATICFILES_DIRS[0], exist_ok=True)

ADMIN_SITE_HEADER = "SAFA Administration"  # Custom header

#DEBUG = True

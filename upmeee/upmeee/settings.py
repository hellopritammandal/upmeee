"""
Django settings for upmeee project.

Generated by 'django-admin startproject' using Django 4.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-kj7b4qjodswv6454no45@15t5jfil0=z_i=ces9g_-qjsqk7yb'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*',]


# Application definition

INSTALLED_APPS = [
    'material',
    'material.admin',
#    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'backend',
    'contact',
#    'froala_editor',
    'ckeditor',

]






MATERIAL_ADMIN_SITE = {
    'HEADER':  ('UpMeee'),  # Admin site header
    'TITLE':  ('UpMeee'),  # Admin site title
    'FAVICON':  "assets/img/root/favicon.png",  # Admin site favicon (path to static should be specified)
    'MAIN_BG_COLOR':  'blue',  # Admin site main color, css color should be specified
    'MAIN_HOVER_COLOR':  'blue',  # Admin site main hover color, css color should be specified
    'PROFILE_PICTURE':  "assets/img/root/favicon.png",  # Admin site profile picture (path to static should be specified)
    'PROFILE_BG':  "",  # Admin site profile background (path to static should be specified)
    'LOGIN_LOGO':  "assets/img/root/favicon.png",  # Admin site logo on login page (path to static should be specified)
    'LOGOUT_BG':  "",  # Admin site background on login/logout pages (path to static should be specified)
    'SHOW_THEMES':  True,  #  Show default admin themes button
    'TRAY_REVERSE': True,  # Hide object-tools and additional-submit-line by default
    'NAVBAR_REVERSE': True,  # Hide side navbar by default
    'SHOW_COUNTS': True, # Show instances counts for each model
    'APP_ICONS': {  # Set icons for applications(lowercase), including 3rd party apps, {'application_name': 'material_icon_name', ...}
       'backend': 'apps',
       'contact': 'contacts',
        },
    'MODEL_ICONS': {  # Set icons for models(lowercase), including 3rd party models, {'model_name': 'material_icon_name', ...}
        'teammember': 'people_outline',
        'contactformsubmission': 'contact_mail',
        'portfolio': 'collections',
        'blog': 'note_add',
        'portfoliocategory': 'arrow_drop_down_circle',
        'faqcategory': 'arrow_drop_down_circle',
        'review': 'rate_review',
        'faq': 'edit',
        'leadsubmission': 'contact_phone',
        'client': 'picture_in_picture',
        'servicelocation': 'edit_location',


    }
}


























MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'upmeee.middleware.RedirectOn404Middleware',
]

ROOT_URLCONF = 'upmeee.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR,  'backend/templates'),
            os.path.join(BASE_DIR,  'templates')],
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

WSGI_APPLICATION = 'upmeee.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'upmeee',
        'USER': 'root',  # XAMPP default MySQL user
        'PASSWORD': '',  # XAMPP default MySQL password (usually empty)
        'HOST': 'localhost',
        'PORT': '3306',  # XAMPP MySQL default port
    }
}
# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-IN'  # Use 'en-IN' for English in India

TIME_ZONE = 'Asia/Kolkata'  # Set the timezone to India Standard Time (IST)

USE_I18N = True

USE_TZ = True



# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


# Media Files Handel
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')



# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'whatznotall@gmail.com'
EMAIL_HOST_PASSWORD = 'lobiagybgjpujfei'
DEFAULT_FROM_EMAIL = 'whatznotall@gmail.com'
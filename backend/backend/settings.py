"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-6-*4--!b1@#x*a#@i_fs_@5+%72i#mn5fm35nkwil_^l!$f&4f"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "accounts",
    "products",
    "cart",
    "payments",
    "history",
    "mpesa",
    "django_daraja",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "backend.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "backend.wsgi.application"

AUTH_USER_MODEL = "accounts.CustomUser"


# Caching
BACKEND = "django.core.cache.backends.redis.RedisCache"

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379",
    }
}

SESSION_ENGINE =  "django.contrib.sessions.backends.cached_db"

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Paypal Payments
PAYPAL_MODE = "sandbox"
PAYPAL_CLIENT_ID = (
    "AWX0aEQAporwIK576vKnvZWRkcvlic0udzcB1Tmzi9wlvd43jXSgqmrMxOLNOJx2ooBZdeWuJzSGj1Hl"
)
PAYPAL_CLIENT_SECRET = (
    "ENoAuoVxxXfrJXdiGomgWnww3Qw5pIk0gS-tVmIPc1rkNCnAjucRZN9mDqWyFVvxv2rm1yTkeV2oUKk_"
)

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]
# Mpesa Payments
MPESA_ENVIRONMENT = "sandbox"
MPESA_CONSUMER_KEY = "iQIcJA192nTBHpQtISegp5OsbTO0NFzNpkES6H6XWgBL58Ye"
MPESA_CONSUMER_SECRET = "p28QUhLQlKdwkTg2pNO2GF3SAAz77hLaFRkZqJeYU0Jn7lZUDfFX6IKnnCQHJxkE"

MPESA_SHORTCODE = 174379
MPESA_EXPRESS_SHORTCODE = "MPESA Express"

MPESA_SHORTCODE_TYPE = 'till_number'

MPESA_PASSKEY = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'

MPESA_CALLBACK_URL = 'https://yourdomain.com/mpesa/callback/'


AUTH_USER_MODEL = "accounts.CustomUser"

CART_SESSION_ID = "cart"


# Frameworks


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

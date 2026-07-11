from pathlib import Path
from django.utils.translation import gettext_lazy as _
import dj_database_url
import os
import base64
import json
import tempfile

# Load .env only in local development (Railway injects env vars directly)
try:
    from dotenv import load_dotenv, find_dotenv
    ENV_FILE = find_dotenv()
    if ENV_FILE:
        load_dotenv(ENV_FILE)
except ImportError:
    pass

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = os.environ.get('SECRET_KEY')

# Strictly boolean: only 'True' (case-sensitive) enables debug mode.
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# Always include the known production domains. Also merge any extra hosts
# from the ALLOWED_HOSTS env var so Railway variables still work as expected.
_PRODUCTION_HOSTS = [
    'www.matiasetcheverry.com',
    'matiasetcheverry.com',
    'drme-web-production.up.railway.app',
    'healthcheck.railway.app',
]
_env_hosts = [h.strip() for h in os.environ.get('ALLOWED_HOSTS', '').split(',') if h.strip()
              and not h.strip().startswith('${{')]  # ignore broken Railway self-references
ALLOWED_HOSTS = list(dict.fromkeys(_PRODUCTION_HOSTS + _env_hosts + ['localhost', '127.0.0.1']))


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'pages',
    'appointments',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Serve static files in production
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'app.wsgi.application'


# Database
# Railway provides DATABASE_URL; fall back to SQLite for local dev.
_database_url = os.environ.get('DATABASE_URL')
if _database_url:
    DATABASES = {
        'default': dj_database_url.parse(_database_url, conn_max_age=600)
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# Internationalization
LANGUAGE_CODE = 'es-ar'
TIME_ZONE = 'America/La_Paz'
USE_I18N = True
USE_TZ = True
USE_L10N = True

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]


# Static files — WhiteNoise serves them directly from gunicorn (no nginx needed)
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'


# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Available languages
LANGUAGES = [
    ('en', _('English')),
    ('es', _('Spanish')),
]


# CUSTOM USER MODEL
AUTH_USER_MODEL = 'core.User'
LOGIN_URL = 'login'


# AUTH0 Configuration
AUTH0_DOMAIN = os.environ.get("AUTH0_DOMAIN")
AUTH0_CLIENT_ID = os.environ.get("AUTH0_CLIENT_ID")
AUTH0_CLIENT_SECRET = os.environ.get("AUTH0_CLIENT_SECRET")


# Google Service Account
# In production: set GOOGLE_SERVICE_ACCOUNT_B64 to the base64-encoded JSON file.
# In local dev: GOOGLE_SERVICE_ACCOUNT_FILE can point to the JSON file directly.
GOOGLE_SERVICE_ACCOUNT_B64 = os.environ.get("GOOGLE_SERVICE_ACCOUNT_B64")
GOOGLE_SERVICE_ACCOUNT_FILE = os.environ.get(
    "GOOGLE_SERVICE_ACCOUNT_FILE",
    str(BASE_DIR / 'calendariomedico-458621-532ee85d60df.json')
)

if GOOGLE_SERVICE_ACCOUNT_B64:
    # Decode the base64 string and write to a temp file so Google SDK can read it
    _sa_json = base64.b64decode(GOOGLE_SERVICE_ACCOUNT_B64).decode('utf-8')
    _sa_tmp = tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False)
    _sa_tmp.write(_sa_json)
    _sa_tmp.flush()
    GOOGLE_SERVICE_ACCOUNT_FILE = _sa_tmp.name


# Security settings (only in production)
if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    X_FRAME_OPTIONS = 'DENY'


# EMR API Configuration
EMR_API_BASE_URL = os.environ.get('EMR_API_BASE_URL', 'http://localhost:8000/api')
EMR_API_TOKEN = os.environ.get('EMR_API_TOKEN', '')
EMR_API_USERNAME = os.environ.get('EMR_API_USERNAME', '')
EMR_API_PASSWORD = os.environ.get('EMR_API_PASSWORD', '')
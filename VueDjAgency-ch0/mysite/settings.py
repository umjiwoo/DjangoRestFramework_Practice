import os,json
from pathlib import Path


from django.core.exceptions import ImproperlyConfigured

BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
# -> secrets.json 파일로 이동
# secrets.json 파일 접근하기
secret_file=os.path.join(BASE_DIR,'secrets.json')

with open(secret_file) as f:
    secrets=json.loads(f.read())

def get_secret(setting):  # 비밀 변수 가져오거나 명시적으로 예외 반환
    try:
        return secrets[setting]  # secrets.json 파일에 setting 에 해당하는 키값 있으면 반환
    except KeyError:
        error_msg="Set the {} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)


SECRET_KEY=get_secret("SECRET_KEY")


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# Application definition

INSTALLED_APPS = [
    'blog.apps.BlogConfig',
    'api.apps.ApiConfig',
    'api2.apps.Api2Config',

    'rest_framework',

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

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'mysite.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db' / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# shkim

STATICFILES_DIRS = (BASE_DIR / 'static',)
# STATIC_ROOT =

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# AUTH_USER_MODEL =

# LOGGING =

# DRF
REST_FRAMEWORK = {
    # Use Django's standard 'django.contrib.auth' permissions
    # Or allow read-only access for unauthenticated users
    # 'DEFAULT_PERMISSION_CLASSES': [
    #     'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
    #     # 로그인한 유저에 대해서는 장고 모델에 대해 CRUD 가능 & 로그인하지 않은 유저는 읽기만 가능
    #     # 'AllowAny' -> 모든 사용자 CRUD 가능
    # ]
}

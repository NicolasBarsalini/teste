"""
Django settings for assessment_disc_project project.

Generated by 'django-admin startproject' using Django 4.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
SITED_ID = 1 #para o allauth



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-^%p*&5-9g4a63fm!!v5(kpwu%v&hepxp+a**=@#9&v1^s!+(!5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
#ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #crispy forms para deixar o form mais bonito
    'crispy_forms',
    
    #allauth para autenticação
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    #fim allauth, pode no futuro inserir outras formas de login, so oljar a documentação do allauth
    'disc',
    'core',
    'user_auth',
    
    #widgets_tweaks para deixar o form mais bonito
    'widget_tweaks'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',

]

ROOT_URLCONF = 'assessment_disc_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates','templates'],
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

WSGI_APPLICATION = 'assessment_disc_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
"""
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend', # padrão
    'user_auth.backends.CustomUserAuthBackend', # personalizado
]
"""
# Configuração do modelo de usuário customizado - OPCIONAL
#AUTH_USER_MODEL = 'user_auth.CustomUser'  # Substitua 'user_auth' pelo nome do seu app onde o CustomUser foi definido
AUTH_USER_MODEL = 'user_auth.CustomUser' #modo para colocar o allauth
LOGIN_REDIRECT_URL = 'user_auth:perfil'  # Ajuste o namespace e o nome da view conforme o definido no seu urls.py
ACCOUNT_SIGNUP_REDIRECT_URL = '/disc/teste_disc/' #para onde o usuario vai ser redirecionado depois de se cadastrar
ACCOUNT_EMAIL_VERIFICATION = 'none' #para não precisar confirmar o email

 #para onde o usuario vai ser redirecionado depois de logar

ACCOUNT_FORMS = {
    'signup': 'user_auth.forms.CustomAllauthSignupForm',
} #para usar o allauth, modelo dentro do user_auth/forms.py


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

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

""" 
caminho static pasta caso haja uma pasta static centralizada

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
""" 
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-sl8(jhd(^i%13&j@-!w79e-_h)9hqx4m@w$zf02+^#3ws@x)as'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Список строк, обозначающих все приложения, которые включены в данной установке Django.
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # Сторонние приложения
    'crispy_forms',
    'crispy_bootstrap5',
    'allauth',
    'allauth.account',
 #   'allauth.socialaccount',
 #   'allauth.socialaccount.providers.github',

    # Локальные приложения
    'accounts.apps.AccountsConfig',
    'pages.apps.PagesConfig',
]


# Список активизированных промежуточных ПО для использования. 
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# Конфигурация django-allauth
# URL или именованный шаблон URL, куда перенаправляются запросы после входа в систему.
LOGIN_REDIRECT_URL = 'home'
# URL или именованный шаблон URL, на который перенаправляется пользователь при выходе из системы.
ACCOUNT_LOGOUT_REDIRECT = 'home'
# Целочисленный идентификатор текущего сайта в таблице базы данных django_site. 
SITE_ID = 1
# Список классов бэкендов аутентификации (в виде строк), которые следует использовать при попытке аутентификации пользователя.
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',  
    'allauth.account.auth_backends.AuthenticationBackend',
)
# Бэкенд, который будет использоваться для отправки электронной почты. 
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# Контролирует время жизни сессии. Значение None, чтобы спросить пользователя ("Remember Me?"), False, чтобы не помнить, и True, чтобы помнить всегда.
ACCOUNT_SESSION_REMEMBER = True
# При регистрации дается пользователю ввести пароль дважды, чтобы избежать опечаток.
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False
# При регистрации пользователю необходимо ввести имя.
ACCOUNT_USERNAME_REQUIRED = False
# Определяет метод входа в систему - пользователь входит в систему, вводя свое имя пользователя, адрес электронной почты или одно из обоих.
ACCOUNT_AUTHENTICATION_METHOD = 'email'
# При регистрации пользователю необходимо указать адрес электронной почты.
ACCOUNT_EMAIL_REQUIRED = True
# Обеспечьте уникальность адресов электронной почты.
ACCOUNT_UNIQUE_EMAIL = True


ROOT_URLCONF = 'configuration.urls'


# Список, содержащий настройки для всех шаблонизаторов, используемых в Django. 
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # Каталог 'templates', в котором движок должен искать исходные файлы шаблонов, в порядке поиска.
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

WSGI_APPLICATION = 'configuration.wsgi.application'


# Словарь, содержащий настройки для базы данных Postgresql, которая будет использоваться с Django.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        # Выбираем встроенный бэкенд для базы данных postgresql
        'ENGINE': 'django.db.backends.postgresql',
        # Выбираем имя, используемой базы данных postgresql
        'NAME': 'postgres',
        # Выбираем имя пользователя, которое будет использоваться при подключении к базе      
        # данных postgresql
        'USER': 'postgres',
        # Выбираем пароль, используемый при подключении к базе данных postgresql
        'PASSWORD': 'postgres',
        # Выбираем хост для подключения базы данных postgresql
        'HOST': 'db',
        # Порт 5432 используется при подключении к базе данных postgresql
        'PORT': 5432,
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# URL, используемый при обращении к статическим файлам (CSS, JavaScript, Images).
STATIC_URL = 'static/'

# Этот параметр определяет дополнительные места, которые приложение staticfiles будет обходить
STATICFILES_DIRS = [BASE_DIR / 'static']

# Абсолютный путь к директории, в которой collectstatic будет собирать статические файлы для развертывания.
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Хранилище файлов, которое будет использоваться при сборе статических файлов с помощью команды управления collectstatic.
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Модель, используемая для представления пользователя
AUTH_USER_MODEL = 'accounts.CustomUser'


# URL или именованный шаблон URL, куда перенаправляются запросы после входа в систему.
LOGIN_REDIRECT_URL = 'home'


# URL или именованный шаблон URL, куда перенаправляются запросы после выхода из системы.
LOGOUT_REDIRECT_URL = 'home'


# Пакет шаблонов Bootstrap5 для django-crispy-forms. 
# Установка bootstrap5 как разрешенный пакет шаблонов.
CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5'

# Пакет шаблонов по умолчанию для вашего проекта django.
CRISPY_TEMPLATE_PACK = 'bootstrap5'

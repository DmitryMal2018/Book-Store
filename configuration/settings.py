from pathlib import Path
from environs import Env

env = Env()

env.read_env()


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/


# Секретный ключ для конкретной установки Django. 
SECRET_KEY = env('DJANGO_SECRET_KEY')


# Режим отладки, в режиме "production" должен быть "False"
DEBUG = env.bool("DJANGO_DEBUG", default=False)


# Список строк, представляющих имена хостов/доменов, которые может обслуживать этот Django-сайт
ALLOWED_HOSTS = ['www.MalDim.pythonanywhere.com', 'MalDim.pythonanywhere.com', 'localhost', '127.0.0.1']


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
    'debug_toolbar',

    # Локальные приложения
    'accounts.apps.AccountsConfig',
    'pages.apps.PagesConfig',
    'books.apps.BooksConfig',
]


# Список активизированных промежуточных ПО для использования. 
MIDDLEWARE = [
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
]


# Настройка кэша
# Псевдоним кэша, который будет использоваться для хранения.
CACHE_MIDDLEWARE_ALIAS = 'default'
# Целое число секунд (одна неделя), в течение которых каждая страница должна кэшироваться.
CACHE_MIDDLEWARE_SECONDS = 604800
# Название сайта, если используется несколько сайтов
CACHE_MIDDLEWARE_KEY_PREFIX = ''


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
# Этот адрес используется в заголовке From: исходящих писем
DEFAULT_FROM_EMAIL = 'admin@bookstore.com'


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
    'default': env.dj_db_url('DATABASE_URL', default='postgres://postgres@db/postgres')
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
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}


# URL-адрес, передающий медиафайлы, обслуживаемые из MEDIA_ROOT, используемый для управления сохраненными файлами.
MEDIA_URL = '/media/'

# Абсолютный путь к директории, в которой будут храниться загружаемые пользователем файлы.
MEDIA_ROOT = BASE_DIR / 'media'


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


# Настройка django-debug-toolbar.
# Список IP-адресов в виде строк.
import socket


hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
INTERNAL_IPS = [ip[:-1] + "1" for ip in ips]

DEBUG_TOOLBAR_CONFIG = {
    'IS_RUNNING_TESTS': False,
}


# Если значение True, то SecurityMiddleware перенаправляет все не-HTTPS запросы на HTTPS, кроме URL, указанных в SECURE_REDIRECT_EXEMPT
SECURE_SSL_REDIRECT = env.bool('DJANGO_SECURE_SSL_REDIRECT', default=True)


# Запрещает подключение подключение к вашему доменному имени через незащищенное соединение в течение определенного периода времени.
SECURE_HSTS_SECONDS = env.int(
    "DJANGO_SECURE_HSTS_SECONDS",
    default=2592000
)

# Это рекомендуется (при условии, что все поддомены обслуживаются исключительно с использованием HTTPS) иначе ваш сайт может быть уязвим.
SECURE_HSTS_INCLUDE_SUBDOMAINS = env.bool(
    "DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS",
    default=True
)

# Отправляет свой сайт в список предварительной загрузки браузера, установив  параметр SECURE_HSTS_PRELOAD в значение True.
SECURE_HSTS_PRELOAD = env.bool(
    "DJANGO_SECURE_HSTS_PRELOAD",
    default=True
)

# При значении True, куки будут помечены как "безопасные", т.е. браузеры могут гарантируют, что куки будут отправляться только через HTTPS-соединение.
SESSION_COOKIE_SECURE = env.bool(
    "DJANGO_SESSION_COOKIE_SECURE", 
    default=True
)

# Храненить CSRF-токены в куках (по умолчанию в Django) безопасно, но храненить его в сессии является обычной практикой в других веб-фреймворках.
CSRF_COOKIE_SECURE = env.bool(
    "DJANGO_CSRF_COOKIE_SECURE", 
    default=True
)

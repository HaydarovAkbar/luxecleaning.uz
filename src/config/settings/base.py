import os
from pathlib import Path
from decouple import config
from datetime import timedelta
from django.conf.global_settings import LANGUAGES as DJANGO_LANGUAGES


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

LOCAL_APPS = [
    # 'modeltranslation',
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

DEV_APPS = [
    'apps',
    # 'bot',
]
PROD_APPS = [
    # 'rest_framework',
    # 'corsheaders',
    # 'rest_framework.authtoken',
    # 'rest_framework_simplejwt',
    # "rest_framework_simplejwt.token_blacklist",
    # 'drf_yasg',
    'axes',
    'django_summernote',
    # 'django_filters',
    # 'django_extensions',
    # 'django_redis',
]
INSTALLED_APPS = LOCAL_APPS + PROD_APPS + DEV_APPS

MIDDLEWARE = [
    # 'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 'corsheaders.middleware.CorsMiddleware',
    'django.middleware.locale.LocaleMiddleware',  # translate
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'axes.middleware.AxesMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    # 'middleware.default_language.CustomLocaleMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'config.wsgi.application'

# Database settings

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DRF settings

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DATETIME_FORMAT': '%Y-%m-%d %H:%M:%S',
}

# JWT settings

SIMPLE_JWT = {
    "REFRESH_TOKEN_LIFETIME": timedelta(days=2),
    "ACCESS_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": False,
    'user_model': 'account.User',
}
# AXES settings

AXES_FAILURE_LIMIT = 3
AXES_LOCKOUT_PARAMETERS = ["ip_address", ["username", "user_agent"]]
AXES_COOLOFF_TIME = timedelta(minutes=1)
AXES_CACHE = 'axes'

AUTHENTICATION_BACKENDS = [
    'axes.backends.AxesBackend',
    # Django ModelBackend is the default authentication backend.
    'django.contrib.auth.backends.ModelBackend',
    # AxesStandaloneBackend should be the first backend in the
    'axes.backends.AxesStandaloneBackend',
]
# LOGGING settings

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'axes_file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'axes.log',
        }
    },
    'loggers': {
        'axes': {
            'handlers': ['axes_file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = "Asia/Tashkent"

USE_I18N = True
USE_L10N = True
USE_TZ = True

gettext = lambda s: s

LANGUAGES = (
    ('uz', gettext("O'zbek tili")),
    ('en', gettext('English')),
    ('ru', gettext('Russian')),
)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# STATIC_ROOT = BASE_DIR / 'static'

STATICFILES_DIRS = [
    BASE_DIR / "static",  # Ensure 'static' directory exists in your project
]

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# HOST = 'https://76cb-194-93-24-3.ngrok-free.app'
HOST = 'https://20bd-185-139-138-136.ngrok-free.app'

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
CSRF_TRUSTED_ORIGINS = [HOST]

# Bot settings
TOKEN = config("TOKEN")
AXES_LOCKOUT_URL = HOST + '/lockout/'


JAZZMIN_SETTINGS = {
    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "Luxe Cleaning Admin",

    # Title on the login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_header": "Luxe Cleaning",

    # Title on the brand (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_brand": "Luxe Cleaning",

    # Logo to use for your site, must be present in static files, used for brand on top left
    "site_logo": None,

    # Logo to use for your site, must be present in static files, used for login form logo (defaults to site_logo)
    "login_logo": None,

    # Logo to use for login form in dark themes (defaults to login_logo)
    "login_logo_dark": None,

    # CSS classes that are applied to the logo above
    "site_logo_classes": "img-circle",

    # Relative path to a favicon for your site, will default to site_logo if absent (ideally 32x32 px)
    "site_icon": "images/logo.svg",

    # Welcome text on the login screen
    "welcome_sign": "Welcome to the Luxe Cleaning",

    # Copyright on the footer
    "copyright": "KAMEZUKASHI",

    # List of model admins to search from the search bar, search bar omitted if excluded
    # If you want to use a single search field you dont need to use a list, you can use a simple string
    "search_model": ["auth.User", "auth.Group"],

    # Field name on user model that contains avatar ImageField/URLField/Charfield or a callable that receives the user
    "user_avatar": None,

    ############
    # Top Menu #
    ############

    # Links to put along the top menu
    "topmenu_links": [

        # Url that gets reversed (Permissions can be added)
        {"name": "Home",  "url": "admin:index", "permissions": ["auth.view_user"]},

        # external url that opens in a new window (Permissions can be added)
        {"name": "Support", "url": "https://t.me/Khaydarovakbar", "new_window": True},

        # model admin to link to (Permissions checked against model)
        {"model": "auth.User"},

        # App with dropdown menu to all its models pages (Permissions checked against models)
        {"apps": "apps"},
    ],

    #############
    # User Menu #
    #############

    # Additional links to include in the user menu on the top right ("app" url type is not allowed)
    "usermenu_links": [
        {"name": "Support", "url": "https://t.me/Khaydarovakbar", "new_window": True},
        {"model": "auth.user"}
    ],

    #############
    # Side Menu #
    #############

    # Whether to display the side menu
    "show_sidebar": True,

    # Whether to aut expand the menu
    "navigation_expanded": True,

    # Hide these apps when generating side menu e.g (auth)
    "hide_apps": [],

    # Hide these models when generating side menu (e.g auth.user)
    "hide_models": [],

    # List of apps (and/or models) to base side menu ordering off of (does not need to contain all apps/models)
    "order_with_respect_to": ["auth", "apps.about", "apps.services", "apps.footer"],

    # Custom links to append to app groups, keyed on app name
    "custom_links": {
        "books": [{
            "name": "Make Messages",
            "url": "make_messages",
            "icon": "fas fa-comments",
            "permissions": ["about.view_about"]
        }]
    },

    # Custom icons for side menu apps/models See https://fontawesome.com/icons?d=gallery&m=free&v=5.0.0,5.0.1,5.0.10,5.0.11,5.0.12,5.0.13,5.0.2,5.0.3,5.0.4,5.0.5,5.0.6,5.0.7,5.0.8,5.0.9,5.1.0,5.1.1,5.2.0,5.3.0,5.3.1,5.4.0,5.4.1,5.4.2,5.13.0,5.12.0,5.11.2,5.11.1,5.10.0,5.9.0,5.8.2,5.8.1,5.7.2,5.7.1,5.7.0,5.6.3,5.5.0,5.4.2
    # for the full list of 5.13.0 free icon classes
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "apps.about": "fas fa-info-circle",
        "apps.services": "fas fa-cogs",
        "apps.important_information": "fas fa-exclamation-triangle",
        "apps.footer": "fas fa-shoe-prints",
        "apps.why_choose_us": "fas fa-question-circle",
        "apps.dashboard": "fas fa-tachometer-alt",
        "apps.dashboard_category": "fas fa-tachometer-alt",
    },
    # Icons that are used when one is not manually specified
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",

    #################
    # Related Modal #
    #################
    # Use modals instead of popups
    "related_modal_active": False,

    #############
    # UI Tweaks #
    #############
    # Relative paths to custom CSS/JS scripts (must be present in static files)
    "custom_css": None,
    "custom_js": None,
    # Whether to link font from fonts.googleapis.com (use custom_css to supply font otherwise)
    "use_google_fonts_cdn": True,
    # Whether to show the UI customizer on the sidebar
    "show_ui_builder": False,

    ###############
    # Change view #
    ###############
    # Render out the change view as a single form, or in tabs, current options are
    # - single
    # - horizontal_tabs (default)
    # - vertical_tabs
    # - collapsible
    # - carousel
    "changeform_format": "single",
    # override change forms on a per modeladmin basis
    "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs",
                                    "apps.about": "horizontal_tabs", "apps.services": "carousel"},
    # Add a language dropdown into the admin
    # "language_chooser": True,
    # 'set_language': 'ru'
}
import os


# ====================
# = Project Settings =
# ====================

PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

ADMINS = (
    ('Johann Heller', 'johann@phyfus.com'),
)

MANAGERS = ADMINS

INTERNAL_IPS = ('127.0.0.1',)


# =========================
# = Localization Settings =
# =========================

TIME_ZONE = 'America/Los_Angeles'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = False

USE_L10N = True


# =======================
# = Media File Settings =
# =======================

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

MEDIA_URL = '/media/'


# ========================
# = Static File Settings =
# ========================

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

STATIC_URL = '/static/'

ADMIN_MEDIA_PREFIX = '/static/admin/'

STATICFILES_DIRS = ()

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# =====================
# = Security Settings =
# =====================

SECRET_KEY = '$2r=ud-(k^f9ncjd2glf%=j^a04dh%6$*oxg=981rx)ywfcbd#'


# ================
# = URL Settings =
# ================

ROOT_URLCONF = 'plog.urls'


# =====================
# = Template Settings =
# =====================

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_DIRS = [
    os.path.join(PROJECT_ROOT, 'templates'),
]


#=======================
# = Middleware Settings =
# =======================

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)


# ==================
# = Installed Apps =
# ==================

INSTALLED_APPS = (
    # Django Contrib Applications
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.humanize',
    # Third-Party Applications
    'django_extensions',
    'django_nose',
    # Local Applications
)


# ====================
# = Logging Settings =
# ====================

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


# ====================
# = Session Settings =
# ====================

SESSION_ENGINE = 'django.contrib.sessions.backends.db'
SESSION_COOKIE_HTTPONLY = True


# ==================
# = Email Settings =
# ==================

EMAIL_HOST = 'localhost'
DEFAULT_FROM_EMAIL = 'no-reply@phyfus.com'


# =====================
# = Messages Settings =
# =====================

MESSAGE_STORAGE = 'django.contrib.messages.storage.fallback.FallbackStorage'


# ====================
# = Testing Settings =
# ====================

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

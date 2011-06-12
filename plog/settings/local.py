from .base import *

# ====================
# = Project Settings =
# ====================

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# =====================
# = Database Settings =
# =====================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_ROOT, 'devdb.sqlite3'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

# ==========================
# = Debug Toolbar Settings =
# ==========================

DEBUG_TOOLBAR = True

if DEBUG_TOOLBAR:
    MIDDLEWARE_CLASSES.append('debug_toolbar.middleware.DebugToolbarMiddleware')
    INSTALLED_APPS.append('debug_toolbar')
    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': False,
    }

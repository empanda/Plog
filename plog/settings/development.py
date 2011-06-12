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
        'ENGINE': 'django.db.backends.',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

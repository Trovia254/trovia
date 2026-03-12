"""TROVIA – Development Settings"""
from .base import *  # noqa

DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Optionally load debug toolbar only if installed
try:
    import debug_toolbar  # noqa
    INSTALLED_APPS += ["debug_toolbar"]  # noqa
    MIDDLEWARE.insert(1, "debug_toolbar.middleware.DebugToolbarMiddleware")  # noqa
    INTERNAL_IPS = ["127.0.0.1"]
except ImportError:
    pass

"""TROVIA – Production Settings"""
import dj_database_url
from .base import *  # noqa

DEBUG = False

DATABASES = {
    "default": dj_database_url.config(
        default=os.environ.get("DATABASE_URL"),  # noqa
        conn_max_age=600,
        ssl_require=False,  # set True for hosted Postgres requiring SSL
    )
}

SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = "DENY"

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = os.environ.get("EMAIL_HOST", "smtp.gmail.com")  # noqa
EMAIL_PORT = int(os.environ.get("EMAIL_PORT", 587))  # noqa
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER", "")  # noqa
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD", "")  # noqa

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {"console": {"class": "logging.StreamHandler"}},
    "root": {"handlers": ["console"], "level": "WARNING"},
}

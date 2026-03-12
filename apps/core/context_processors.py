from django.conf import settings

def site_context(request):
    return {
        "SITE_NAME": settings.SITE_NAME,
        "SITE_TAGLINE": settings.SITE_TAGLINE,
        "SITE_DESCRIPTION": settings.SITE_DESCRIPTION,
        "SITE_URL": settings.SITE_URL,
    }

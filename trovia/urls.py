from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("dashboard/", include("apps.accounts.urls")),
    path("blog/", include("apps.blog.urls")),
    path("", include("apps.core.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    try:
        import debug_toolbar
        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
    except ImportError:
        pass

handler404 = "apps.core.views.error_404"
handler500 = "apps.core.views.error_500"

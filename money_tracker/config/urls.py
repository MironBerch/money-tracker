from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('', include('transactions.urls')),
    path('', include('categories.urls')),
]

handler400 = 'main.views.bad_request_view'
handler403 = 'main.views.permission_denied_view'
handler404 = 'main.views.page_not_found_view'
handler500 = 'main.views.server_error_view'


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )

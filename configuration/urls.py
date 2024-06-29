from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Django-администратор
    path('anything-but-admin/', admin.site.urls),
    # Управления пользователями
    path('accounts/', include('allauth.urls')),
    # Локальные приложения
    path('', include('pages.urls')),
    path("books/", include("books.urls")),
] 

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns

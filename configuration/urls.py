
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Django-администратор
    path('admin/', admin.site.urls),
    # Управления пользователями
    path('accounts/', include('django.contrib.auth.urls')),
    # Локальные приложения
    path('accounts/', include('accounts.urls')),
    path('', include('pages.urls')),
]

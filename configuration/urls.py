
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Django-администратор
    path('admin/', admin.site.urls),
    # Управления пользователями
    path('accounts/', include('allauth.urls')),
    # Локальные приложения
    path('', include('pages.urls')),
    path("books/", include("books.urls")),
]

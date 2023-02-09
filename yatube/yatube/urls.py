"""yatube URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# импорт include позволит использовать адреса, включенные в приложения
from django.urls import include, path

urlpatterns = [
    # Сначала проверяем все пути, которые есть в приложении posts
    path('', include('posts.urls', namespace='posts')),
    # Дорогой Джанго, если на сервер пришёл запрос ('group/'),
    # перейди в файл urls приложения posts
    # и проверь там все path() на совпадение с запрошенным URL
    path('group/', include('posts.urls')),
    path('admin/', admin.site.urls)
    ]

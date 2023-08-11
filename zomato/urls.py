"""
URL configuration for zomato project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from django.conf import settings

from django.conf.urls.static import static
from .views import display_menu, add_dish,remove_dish,update_dish
urlpatterns = [
    path('admin/', admin.site.urls),
    path('menu/', display_menu, name='menu'),
    path('add_dish/', add_dish, name='add_dish'),
    path('remove_dish/', remove_dish, name='remove_dish'),
    path('update_dish/', update_dish, name='update_dish'),
]



if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
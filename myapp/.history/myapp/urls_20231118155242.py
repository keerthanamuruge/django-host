"""
URL configuration for myapp project.

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
from django.conf.urls.static import static 
from django.contrib.staticfiles.storage import staticfiles_storage
from django.contrib import admin
from django.urls import path, re_path
from .views import home
from . import settings
from django.views.generic.base import RedirectView


favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    re_path(r'^favicon\.ico$', favicon_view),
    path("polls/", include("polls.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

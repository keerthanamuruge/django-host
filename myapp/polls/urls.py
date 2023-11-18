
from django.views.generic.base import RedirectView
from django.urls import path, re_path, include


favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)

urlpatterns = [
    re_path(r'^favicon\.ico$', favicon_view),
]
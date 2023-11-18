
from . import settings
from django.views.generic.base import RedirectView
from django.urls import path, re_path, include
from django.conf.urls.static import static 

favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)

urlpatterns = [
    re_path(r'^favicon\.ico$', favicon_view),
    path("polls/", include("polls.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
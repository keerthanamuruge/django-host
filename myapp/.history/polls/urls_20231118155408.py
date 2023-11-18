from . import settings
from django.views.generic.base import RedirectView


favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    re_path(r'^favicon\.ico$', favicon_view),
    path("polls/", include("polls.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
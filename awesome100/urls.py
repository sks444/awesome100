"""
Community URL configuration.
"""

from django_distill import distill_url
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

from log.view_log import index as log_index


def get_index():
    # The index URI regex, ^$, contains no parameters, named or otherwise.
    # You can simply just return nothing here.
    return None


urlpatterns = [

    distill_url(
        r'^$', TemplateView.as_view(template_name='index.html'),
        name='index',
        distill_func=get_index,
        distill_file='index.html',
    ),
    distill_url(
        r'log/', log_index,
        name='log',
        distill_func=get_index,
        distill_file='log/index.html',
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.conf.urls import url

from . import views

urlpatterns = [  # Ignore PycodestyleBear (W605)
    url('^comedians/$', views.ListComedian.as_view()),
    url('^comedian/(?P<pk>\d+)/$', views.DetailComedian.as_view()),
]

from django.conf.urls import url

from . import views

urlpatterns = [  # Ignore PycodestyleBear (W605)
    url('^tv_shows/$', views.ListTvShow.as_view()),
    url('^tv_show/(?P<pk>\d+)/$', views.DetailTvShow.as_view()),
]

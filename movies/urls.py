from django.conf.urls import url

from . import views

urlpatterns = [  # Ignore PycodestyleBear (W605)
    url('^movies/$', views.ListMovie.as_view()),
    url('^movie/(?P<pk>\d+)/$', views.DetailMovie.as_view()),
]

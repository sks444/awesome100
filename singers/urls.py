from django.conf.urls import url

from . import views

urlpatterns = [  # Ignore PycodestyleBear (W605)
    url('^singers/$', views.ListSinger.as_view()),
    url('^singer/(?P<pk>\d+)/$', views.DetailSinger.as_view()),
]

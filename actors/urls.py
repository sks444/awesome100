from django.conf.urls import url

from . import views

urlpatterns = [  # Ignore PycodestyleBear (W605)
    url('^actors/$', views.ListActor.as_view()),
    url('^actor/(?P<pk>\d+)/$', views.DetailActor.as_view()),
]

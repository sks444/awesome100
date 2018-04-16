from django.conf.urls import url

from . import views

urlpatterns = [  # Ignore PycodestyleBear (W605)
    url('^directors/$', views.ListDirector.as_view()),
    url('^director/(?P<pk>\d+)/$', views.DetailDirector.as_view()),
]

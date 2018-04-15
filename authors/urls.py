from django.conf.urls import url

from . import views

urlpatterns = [  # Ignore PycodestyleBear (W605)
    url('^authors/$', views.ListAuthor.as_view()),
    url('^author/(?P<pk>\d+)/$', views.DetailAuthor.as_view()),
]

from django.conf.urls import url
from hello import views

urlpatterns = [
    url(r'^hello/$', views.hello),
    url(r'^test/(?P<id>\d{2})/(?P<key>\w+)', views.test),
]

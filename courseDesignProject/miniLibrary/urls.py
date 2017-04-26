from django.conf.urls import url
from . import views

urlpatterns = [
            url(r'^topic_list/$', views.topic_list, name='topic_list'),
            url(r'^topic_list_by_category/(?P<category_id>[-\w]+)/$', views.topic_list, name='topic_list_by_category'),
            url(r'^topic_create/$', views.topic_create, name='topic_create'),
            url(r'^topic_detail/(?P<topic_id>[-\w]+)/$', views.topic_detail, name='topic_detail'),
            url(r'^download_file/$', views.download_file, name='download_file' ),
            url(r'^topic_like/(?P<topic_id>\d+)/$', views.topic_like, name='topic_like'),
            url(r'^topic_bookmark/(?P<topic_id>\d+)/$', views.topic_bookmark, name='topic_bookmark'),
        ]

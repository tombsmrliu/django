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
            url(r'^bookmark_list/$', views.bookmark_list, name='bookmark_list'),
            url(r'^remove_bookmark/(?P<topic_id>\d+)/$', views.remove_bookmark, name='remove_bookmark'),
            url(r'^topic_manage/$', views.topic_manage, name='topic_manage'),
            url(r'^topic_remove/(?P<topic_id>\d+)/$', views.topic_remove, name='topic_remove'),
            url(r'^search/$', views.topic_search, name='search'),
        ]

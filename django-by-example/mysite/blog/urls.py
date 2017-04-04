from django.conf.urls import url
from . import views


urlpatterns = [
        # 列表
        url(r'^$', views.post_list, name='post_list'),
        url(r'^tag/(?P<tag_slug>[-\w]+)/$', views.post_list, name='post_list_by_tag'),
        # url(r'^$', views.PostListView.as_view(), name='post_list'),

        # 帖子详情
        url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$', views.post_detail, name='post_detail'),

        # 通过邮件分享
        url(r'^(?P<post_id>\d+)/share/$', views.post_share, name='post_share'),
        ]

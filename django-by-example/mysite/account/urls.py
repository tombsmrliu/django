from django.conf.urls import url
from . import views
from django.contrib.auth import views as authViews

urlpatterns = [
        # 自定义认证视图
        # url(r'login/$', views.user_login, name='login'),

        # 使用内置认证视图
        url(r'login/$', 
            authViews.login,
            {'template_name':'account/login.html'},
            name='login'),


        url(r'logout/$',
            authViews.logout, 
            {'template_name':'account/logout.html'}, 
            name='logout'),


        url(r'logout-then-login/$', 
            authViews.logout_then_login, 
            name='logout_then_login'),



        url(r'password-change/$', 
            authViews.password_change, 
            {   'template_name':'account/password_change_form.html',
                'post_change_redirect':'account:password_change_done'
            },
            name='password_change'),



        url(r'password-change/done/$', 
            authViews.password_change_done, 
            name='password_change_done'),


        url(r'password-reset/$',
            authViews.password_reset,
            name='password_reset'),


        url(r'password_reset/done/$',
            authViews.password_reset_done,
            name='password_reset_done'),


        url(r'dashboard/$', views.dashboard, name='dashboard'),
        ]

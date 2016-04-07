from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^login/$', views.login_user, name='login_user'),
    url(r'^login/$', views.logout, name='logout'),
    url(r'^detail/(?P<pk>\d+)/edit/$', views.detail_edit, name='detail_edit'),
    url(r'^detail/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^accounts/register/$', views.register_user, name='register'),

]
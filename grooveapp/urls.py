from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from grooveapp import views as core_views



urlpatterns = [
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'grooveapp:login'}, name='logout'),
    url(r'^login/$', auth_views.login, name='login'),
    # url(r'^lobby/$', views.lobby, name='lobby'),
    # url(r'^lobby/(?P<name>[0-9]{1})/$', views.lobby, name='lobby'),
    url(r'^lobby/(?P<name>[0-9]+)/$', views.lobby, name='lobby'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^infostories/$', views.infostories, name='infostories'),
    url(r'^story/$', views.story, name='story'),
    url(r'^makechat/$', views.makechat, name='makechat'),
    url(r'^api/lobby_messages$', views.get_messages),
    url(r'^signup/$', core_views.signup, name='signup'),
]

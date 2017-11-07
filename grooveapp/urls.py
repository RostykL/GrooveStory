from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from grooveapp import views as core_views



urlpatterns = [
        url(r'^login/$', auth_views.login, name='login'),
        url(r'^logout/$', auth_views.logout, {'next_page': 'grooveapp:login'}, name='logout'),
        url(r'^login/$', auth_views.login, name='login'),
        url(r'^lobby/$', views.lobby, name='lobby'),
        url(r'^api/lobby_messages$', views.get_messages),
        url(r'^signup/$', core_views.signup, name='signup'),
]

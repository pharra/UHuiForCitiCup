from django.conf.urls import url

from . import views
from apiForAndroid import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.login, name='login'),
    url(r'^user$', views.user, name='user'),
    url(r'^post_login$', views.post_login, name='post_login'),
    url(r'^post_signup$', views.post_signUp, name='post_signUp'),
    url(r'^post_loginForAndroid$', views.post_loginForAndroid, name='post_loginForAndroid'),
    url(r'^post_signUpForAndroid$', views.post_signUpForAndroid, name='post_signUpForAndroid'),
    url(r'^post_sendMessage$', views.post_sendMessage, name='post_sendMessage'),
]
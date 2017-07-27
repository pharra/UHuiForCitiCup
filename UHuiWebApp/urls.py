from django.conf.urls import url

from . import views
from apiForAndroid import views as androidViews

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.login, name='login'),
    url(r'^user$', views.userPage, name='user'),
    url(r'^post_login$', views.post_login, name='post_login'),
    url(r'^post_signup$', views.post_signUp, name='post_signUp'),
    url(r'^post_sendEmailVerifyCode$', views.post_sendEmailVerifyCode, name='post_sendEmailVerifyCode'),
    url(r'^post_sendMobileVerifyCode$', views.post_sendMobileVerifyCode, name='post_sendMobileVerifyCode'),
    url(r'^post_modifyUserInfo$', views.post_modifyUserInfo, name='post_modifyUserInfo'),
    url(r'^post_search$', views.post_search, name='post_search'),
    url(r'^post_getUserCoupon$', views.post_getUserCoupon, name='post_getUserCoupon'),

    url(r'^post_loginForAndroid$', androidViews.post_loginForAndroid, name='post_loginForAndroid'),
    url(r'^post_signUpForAndroid$', androidViews.post_signUpForAndroid, name='post_signUpForAndroid'),
    url(r'^post_sendMessage$', androidViews.post_sendMessage, name='post_sendMessage'),
    url(r'^post_searchForAndroid$', androidViews.post_searchForAndroid, name='post_searchForAndroid'),
    url(r'^post_couponDetailForAndroid$', androidViews.post_couponDetailForAndroid, name='post_couponDetailForAndroid'),
    url(r'^post_ownerDetailForAndroid$', androidViews.post_ownerDetailForAndroid, name='post_ownerDetailForAndroid'),
    url(r'^post_returnInformation', androidViews.post_returnInformation, name='post_returnInformation'),
    url(r'^post_getBoughtList$',androidViews.post_getBoughtList,name='post_getBoughtList'),
    url(r'^post_getOwnList$', androidViews.post_getOwnList, name='post_getOwnList'),
    url(r'^post_getLikeList$',androidViews.post_getLikeList,name='post_getLikeList'),
    url(r'^post_getSoldList$', androidViews.post_getSoldList, name='post_getSoldList'),
    url(r'^post_likeCoupon$',androidViews.post_likeCoupon,name='post_likeCoupon'),
    url(r'^post_addCoupon$', androidViews.post_addCoupon, name='post_addCoupon'),
    url(r'^post_updatePassword$', androidViews.post_updatePassword, name='post_updatePassword'),
    url(r'^post_buyCoupon$', androidViews.post_buyCoupon, name='post_buyCoupon'),
    url(r'^post_getUsedCoupon$',androidViews.post_getUsedCoupon,name='post_getUsedCoupon'),
    url(r'^post_updateAvatar$',androidViews.post_updateAvatar,name='post_updateAvatar'),
    url(r'^post_preSearch$',androidViews.post_preSearch,name='post_preSearch'),

]

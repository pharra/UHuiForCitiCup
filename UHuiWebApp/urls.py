from django.conf.urls import url

from . import views
from apiForAndroid import views as androidViews

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.login, name='login'),
    url(r'^user$', views.userPage, name='user'),
    url(r'^mycoupons', views.myCouponsPage, name='mycoupons'),
    url(r'^search$', views.search, name='search'),
    url(r'^commodity$', views.commodity, name='commodity'),
    url(r'^mobile_appraisement$',views.mobile_appraisement,name = 'mobile_appraisement'),
    url(r'^mobile_user_setting$',views.mobile_user_setting,name = 'mobile_user_setting'),
    url(r'^mobile_user_wallet$',views.mobile_user_wallet,name = 'mobile_user_wallet'),
    url(r'^mobile_user_focus$',views.mobile_user_focus,name = 'mobile_user_focus'),
    url(r'^mobile_sell_add$',views.mobile_sell_add,name = 'mobile_sell_add'),
    url(r'^mobile_sell_final$',views.mobile_sell_final,name = 'mobile_sell_final'),
    url(r'^couponsmessage$',views.mobile_couponsmessage,name = 'mobile_couponsmessage'),
    url(r'^mobile_myboughtcoupons$', views.mobile_myboughtcoupons, name='mobile_myboughtcoupons'),


    url(r'^post_login$', views.post_login, name='post_login'),
    url(r'^post_signup$', views.post_signUp, name='post_signUp'),
    url(r'^post_sendEmailVerifyCode$', views.post_sendEmailVerifyCode, name='post_sendEmailVerifyCode'),
    url(r'^post_sendMobileVerifyCode$', views.post_sendMobileVerifyCode, name='post_sendMobileVerifyCode'),
    url(r'^post_modifyUserInfo$', views.post_modifyUserInfo, name='post_modifyUserInfo'),
    url(r'^post_search$', views.post_search, name='post_search'),
    url(r'^post_getUserCoupon$', views.post_getUserCoupon, name='post_getUserCoupon'),
    url(r'^post_getCouponForMobileIndex$', views.post_getCouponForMobileIndex, name='post_getCouponForMobileIndex'),
    url(r'^post_getCouponByCatIndex$', views.post_getCouponByCatIndex, name='post_getCouponByCatIndex'),
    url(r'^emailVerification/', views.emailVerification, name='emailVerification'),
    url(r'^post_like$', views.post_like, name='post_like'),
    url(r'^post_dislike$', views.post_dislike, name='post_dislike'),
    url(r'^post_buy$', views.post_buy, name='post_buy'),
    url(r'^post_presearch$', views.post_presearch, name='post_presearch'),

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

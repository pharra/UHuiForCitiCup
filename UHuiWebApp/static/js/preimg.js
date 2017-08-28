Vue.component('coupon-img', {
    template: '<img :src="url" >',
    props: ['imgurl'],
    data: function () {
        return {url: '/static/images/loader.gif'}
    },
    created: function () {
        var _self = this;
        var url = _self.$parent.coupon.pic;
        var img = new Image();
        img.src = url;
        img.onload = function () {
            _self.url = url;
        }
    }
});

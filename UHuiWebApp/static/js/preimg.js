Vue.component('coupon-img', {
    template: '<div class="spinnerdiv" v-if="loading">\n'+
        '<img src="/static/images/coupons_empty.png">\n' +
        ' </div> ' +
        '<img :src="url" v-else>',
    props: ['imgurl'],
    data: function () {
        return {url: '',loading:true}
    },
    created: function () {
        var _self = this;
        var url = _self.$parent.coupon.pic;
        var img = new Image();
        img.src = url;
        img.onload = function () {
            _self.loading = false;
            _self.url = url;
        }
    }
});

Vue.component('lazy-img', {
    template: '<div class="spinnerdiv" v-if="loading">\n'+
    '<div class="spinner">\n' +
        '    <div class="rect1"></div>\n' +
        '    <div class="rect2"></div>\n' +
        '    <div class="rect3"></div>\n' +
        '    <div class="rect4"></div>\n' +
        '    <div class="rect5"></div>\n' +
        '  </div> \n' +
        '  </div> ' +
        '<img :src="url" v-else>',
    props: ['imgurl'],
    data: function () {
        return {url: '',loading:true}
    },
    created: function () {
        var _self = this;
        var url = _self.imgurl;
        var img = new Image();
        img.src = url;
        img.onload = function () {
            _self.loading = false;
            _self.url = url;
        }
    }
});








/*
Vue.component('pre-img', {
        template: '<div class="spinner" v-if="loading">\n' +
        '    <div class="rect1"></div>\n' +
        '    <div class="rect2"></div>\n' +
        '    <div class="rect3"></div>\n' +
        '    <div class="rect4"></div>\n' +
        '    <div class="rect5"></div>\n' +
        '  </div> ' +
        '<img :src="imgurl" v-else-if="loaded">',
        props:['imgurl'],
        computed:{
            loading:function () {
                return !this.imgurl;
            },
            loaded:function () {
                return !this.loading;
            }
        }
    });
    let vueimg = new Vue({
        el:'.vue-img',
        data:{
            url:''
        },
        methods:{
            getimgurl:function (url) {
                let _self = this;
                let img = new Image();
                img.src = url;
                img.onload = function () {
                    _self.url = url;
                }
            }
        }
    });*/

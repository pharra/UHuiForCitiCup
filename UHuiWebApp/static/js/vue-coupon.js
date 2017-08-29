function isUnsignedInteger(a) {
    var reg = /^[1-9]\d*(.\d{1,2})?$/;
    return reg.test(a);
}

Vue.component('coupon', {
        template: '<div class="coupon-pc col-xs-4" :id="coupon.couponID">\n' +
        '                    <div class="coupon">\n' +
        '                        <div class="coupon-img">\n' +
        '                            <coupon-img></coupon-img>\n' +
        '                        </div>\n' +
        '                        <div class="coupon-content col-xs-offset-4 col-xs-8">\n' +
        '                            <div class="coupon-price">\n' +
        '                                <em>¥</em><strong class="coupon-font-value">{{ coupon.listPrice }}</strong>\n' +
        '                                <span class="coupon-font-limit">{{ coupon.discount }} </span>\n' +
        '                                <span class="coupon-detail">详情>></span>\n' +
        '                            </div>\n' +
        '\n' +
        '                            <div class="coupon-range">{{ coupon.product }}</div>\n' +
        '                            <div class="coupon-btn-box">\n' +
        '                                <div class="btn col-xs-5" v-if="like" v-on:click="changelike(\'/post_like\')">关注</div>\n' +
        '                                <div class="btn col-xs-5" v-if="dislike" v-on:click="changelike(\'/post_dislike\')">已关注</div>\n' +
        '                                <div class="btn col-xs-5 col-xs-offset-2" v-if="buy" v-on:click="post_buy">购买</div>\n' +
        '                                <div class="btn col-xs-5 col-xs-offset-7" v-if="putOffSale" v-on:click="post_putOffSale">下架</div>\n' +
        '                                <div class="btn col-xs-5 col-xs-offset-7" v-if="putOnSale" v-on:click="post_putOnSale">上架</div>\n' +
        '                            </div>\n' +
        '                            <div class="coupon-time-limt">截止时间:{{ coupon.expiredTime }}</div>\n' +
        '                        </div>\n' +
        '                    </div>\n' +
        '                </div>',
        props: ['coupon'],
        created: function () {
            var _self = this;
        },
        data: function () {
            return {stat: this.coupon.stat};
        },
        computed: {
            buy: function () {
                return this.stat === '0' || this.stat === '1';
            },
            like: function () {
                return this.stat === '0';
            },
            dislike: function () {
                return this.stat === '1';
            },
            putOnSale: function () {
                return this.stat === '3';
            },
            putOffSale: function () {
                return this.stat === '2';
            }
        },
        methods: {
            changelike: function (url) {
                var _self = this;
                $.ajax({
                    url: url,
                    type: 'POST',
                    dataType: 'json',
                    data: {'couponID': _self.coupon.couponID},
                    timeout: 3000,
                    success: function (Jsondata) {
                        var msg = Jsondata.message;
                        if (Jsondata.errno === '5') {
                            window.location.href = "/login";
                        }
                        else if (Jsondata.errno === '0') {

                            if (Jsondata.like === '0') {
                                _self.stat = '0';
                            }
                            else {
                                _self.stat = '1';
                            }

                        }
                        else {
                            alert(msg)
                        }
                    }
                })
            },
            post_buy: function () {
                var _self = this;
                $.ajax({
                    url: '/post_buy',
                    type: 'POST',
                    dataType: 'json',
                    data: {
                        "couponID": _self.coupon.couponID,
                        "sellerID": _self.coupon.sellerInfo.userid
                    },
                    timeout: 3000,
                    cache: false,
                    async: false,
                    beforeSend: LoadFunction,
                    error: erryFunction,
                    success: function succFunction(Jsondata) {
                        if (Jsondata.errno === '0') {
                            var setting = {
                                content: "购买成功",
                                button1: '确定',
                                button2: "查看我的优惠券",
                                onCancel: function () {
                                    return true;
                                },
                                onOk: function () {
                                    window.location.href = "/user";
                                    return true;
                                }
                            };
                            vueconfirm.alert(setting);
                            _self.stat = '3';
                        } else {
                            var settings = {
                                content: Jsondata.message,
                                button: '确定'
                            };
                            vuealert.alert(settings);

                        }

                    }
                });

                function LoadFunction() {
                }

                function erryFunction() {
                }


            },
            post_putOffSale: function () {
                var _self = this;
                $.ajax({
                    url: '/post_putOffSale',
                    type: 'POST',
                    dataType: 'json',
                    data: {'couponID': _self.coupon.couponID},
                    timeout: 3000,
                    cache: false,
                    success: function succFunction(Jsondata) {
                        var msg = Jsondata.message;
                        if (Jsondata.errno === '0') {
                            var setting = {
                                title: '优惠券下架',
                                content: "下架成功"
                            };
                            vuealert.alert(setting);
                            _self.stat = '3';
                        }
                        else {
                            var setting = {
                                title: '下架失败',
                                content: msg
                            };
                            vuealert.alert(setting);
                        }
                    }
                });
            },
            post_putOnSale: function () {
                var _self = this;
                var setting = {
                    title: '上架优惠券',
                    content: "输入优惠券价格",
                    onOk: function () {
                        if (isUnsignedInteger(this.message)) {
                            var msg = this.message;
                            $.ajax({
                                url: '/post_putOnSale',
                                type: 'POST',
                                dataType: 'json',
                                data: {'couponID': _self.coupon.couponID, 'listPrice': msg},
                                timeout: 3000,
                                cache: false,
                                success: function succFunction(Jsondata) {
                                    var msg = Jsondata.message;
                                    if (Jsondata.errno === '0') {
                                        var setting = {
                                            title: '优惠券上架',
                                            content: "优惠券上架成功"
                                        };
                                        vuealert.alert(setting);
                                        _self.stat = '2';
                                        _self.coupon.listPrice = Jsondata.listPrice;
                                    }
                                    else {
                                        var setting2 = {
                                            title: '上架失败',
                                            content: msg
                                        };
                                        vuealert.alert(setting2);
                                    }
                                }
                            });
                        }
                        else {
                            var setting1 = {
                                content: "请输入正确价格"
                            };
                            vuealert.alert(setting1);
                        }
                    },
                    onCancel: function () {

                    }
                };
                vueinput.alert(setting);

            }
        }

    }
);

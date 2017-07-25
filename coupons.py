# coding=utf-8
import random

from UHuiWebApp import models
import datetime

date = datetime.date(2017, 9, 10)

brand = models.Brand.objects.get(brandid=1)
cat = models.Category.objects.get(catid=1)
couponList = models.Couponlist.objects.get(listid=56)
coupon = models.Coupon(couponid='1', brandid=brand, catid=cat, listprice='5', value='5',
                       product='可口可乐摩登罐5元即领即用券', discount='满5元减5元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='2', brandid=brand, catid=cat, listprice='8', value='8',
                                      product='国产调料满46元减8元抵用券', discount='满46元减8元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='3', brandid=brand, catid=cat, listprice='10', value='10',
                                      product='得宝满69减10', discount='满69元减10元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='4', brandid=brand, catid=cat, listprice='10', value='10',
                                      product='自营国产大米面粉满88减10元抵用券', discount='满88元减10元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='5', brandid=brand, catid=cat, listprice='20', value='20',
                                      product='好奇纸尿裤指定产品无门槛抵用券', discount='满20元减20元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='6', brandid=brand, catid=cat, listprice='10', value='10',
                                      product='福临门食用油满99减10元抵用券', discount='满99元减10元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='7', brandid=brand, catid=cat, listprice='5', value='5',
                                      product='速食罐装满49减5元抵用券', discount='满49元减5元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='8', brandid=brand, catid=cat, listprice='5', value='5',
                                      product='自营进口益昌老街5元抵用券', discount='满5元减5元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='9', brandid=brand, catid=cat, listprice='1', value='1',
                                      product='自营进口海牌1元无门槛抵用券', discount='满1元减1元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='10', brandid=brand, catid=cat, listprice='100', value='100',
                                      product='美国第一户外旗舰店', discount='满199元减100元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='11', brandid=brand, catid=cat, listprice='30', value='30',
                                      product='好奇心部分产品30元无门槛券', discount='满30元减30元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='12', brandid=brand, catid=cat, listprice='5', value='5',
                                      product='屈臣氏花水5元即领即用券', discount='满5元减5元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='13', brandid=brand, catid=cat, listprice='20', value='20',
                                      product='孟乍隆无门槛20元抵用券', discount='满20元减20元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='14', brandid=brand, catid=cat, listprice='5', value='5',
                                      product='怡宝&维他满68减5元', discount='满68元减5元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='15', brandid=brand, catid=cat, listprice='10', value='10',
                                      product='南北干货满69减10元抵用券', discount='满69元减10元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='16', brandid=brand, catid=cat, listprice='20', value='20',
                                      product='茵曼官方旗舰店', discount='满20元减20元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='17', brandid=brand, catid=cat, listprice='10', value='10',
                                      product='好奇纸尿裤10元无门槛券', discount='满10元减10元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='18', brandid=brand, catid=cat, listprice='5', value='5',
                                      product='自营进口莱家饼干5元抵用券', discount='满38元减5元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='19', brandid=brand, catid=cat, listprice='15', value='15',
                                      product='指定肉脯蜜饯坚果满158减15元券', discount='满158元减15元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='20', brandid=brand, catid=cat, listprice='5', value='5',
                                      product='洁云满49减5', discount='满49元减5元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='21', brandid=brand, catid=cat, listprice='5', value='5',
                                      product='杜蕾斯旗舰店', discount='满5元减5元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='21', brandid=brand, catid=cat, listprice='5', value='5',
                                      product='可口可乐摩登罐5元即领即用券', discount='满5元减5元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='22', brandid=brand, catid=cat, listprice='8', value='8',
                                      product='国产调料满46元减8元抵用券', discount='满46元减8元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='23', brandid=brand, catid=cat, listprice='10', value='10',
                                      product='得宝满69减10', discount='满69元减10元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='24', brandid=brand, catid=cat, listprice='10', value='10',
                                      product='自营国产大米面粉满88减10元抵用券', discount='满88元减10元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='25', brandid=brand, catid=cat, listprice='20', value='20',
                                      product='好奇纸尿裤指定产品无门槛抵用券', discount='满20元减20元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='26', brandid=brand, catid=cat, listprice='10', value='10',
                                      product='福临门食用油满99减10元抵用券', discount='满99元减10元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='27', brandid=brand, catid=cat, listprice='5', value='5',
                                      product='速食罐装满49减5元抵用券', discount='满49元减5元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='28', brandid=brand, catid=cat, listprice='5', value='5',
                                      product='自营进口益昌老街5元抵用券', discount='满5元减5元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='29', brandid=brand, catid=cat, listprice='1', value='1',
                                      product='自营进口海牌1元无门槛抵用券', discount='满1元减1元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='30', brandid=brand, catid=cat, listprice='100', value='100',
                                      product='美国第一户外旗舰店', discount='满199元减100元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='31', brandid=brand, catid=cat, listprice='30', value='30',
                                      product='好奇心部分产品30元无门槛券', discount='满30元减30元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='32', brandid=brand, catid=cat, listprice='5', value='5',
                                      product='屈臣氏花水5元即领即用券', discount='满5元减5元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='33', brandid=brand, catid=cat, listprice='20', value='20',
                                      product='孟乍隆无门槛20元抵用券', discount='满20元减20元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='34', brandid=brand, catid=cat, listprice='5', value='5',
                                      product='怡宝&维他满68减5元', discount='满68元减5元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='35', brandid=brand, catid=cat, listprice='10', value='10',
                                      product='南北干货满69减10元抵用券', discount='满69元减10元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='36', brandid=brand, catid=cat, listprice='20', value='20',
                                      product='茵曼官方旗舰店', discount='满20元减20元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='37', brandid=brand, catid=cat, listprice='10', value='10',
                                      product='好奇纸尿裤10元无门槛券', discount='满10元减10元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='38', brandid=brand, catid=cat, listprice='5', value='5',
                                      product='自营进口莱家饼干5元抵用券', discount='满38元减5元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='39', brandid=brand, catid=cat, listprice='15', value='15',
                                      product='指定肉脯蜜饯坚果满158减15元券', discount='满158元减15元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='40', brandid=brand, catid=cat, listprice='5', value='5',
                                      product='洁云满49减5', discount='满49元减5元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='41', brandid=brand, catid=cat, listprice='5', value='5',
                                      product='杜蕾斯旗舰店', discount='满5元减5元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='41', brandid=brand, catid=cat, listprice='8', value='8',
                                      product='百草味满68减8抵用券', discount='满68元减8元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='42', brandid=brand, catid=cat, listprice='8', value='8',
                                      product='洁云满79减8', discount='满79元减8元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='43', brandid=brand, catid=cat, listprice='9', value='9',
                                      product='舒洁满79减9', discount='满79元减9元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='44', brandid=brand, catid=cat, listprice='5', value='5',
                                      product='7月ABC 49-5元', discount='满49元减5元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='45', brandid=brand, catid=cat, listprice='8', value='8',
                                      product='良品铺子满68减8抵用券', discount='满68元减8元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='46', brandid=brand, catid=cat, listprice='30', value='30',
                                      product='雀巢满299减30券', discount='满299元减30元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='47', brandid=brand, catid=cat, listprice='5', value='5',
                                      product='自营国产杂粮满39减5元抵用券', discount='满39元减5元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='48', brandid=brand, catid=cat, listprice='5', value='5',
                                      product='旭包鲜满49-5元', discount='满49元减5元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='49', brandid=brand, catid=cat, listprice='10', value='10',
                                      product='干电池满78元减10元', discount='满78元减10元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='50', brandid=brand, catid=cat, listprice='30', value='30',
                                      product='雅培新客满299减30券', discount='满299元减30元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='51', brandid=brand, catid=cat, listprice='10', value='10',
                                      product='奔腾满50减10', discount='满50元减10元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='52', brandid=brand, catid=cat, listprice='10', value='10',
                                      product='梅林精制午餐肉满30减10元抵用券', discount='满30元减10元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='53', brandid=brand, catid=cat, listprice='10', value='10',
                                      product='自营进口乳制品10元抵用券', discount='满168元减10元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='54', brandid=brand, catid=cat, listprice='10', value='10',
                                      product='自营进口内确蜂蜜10元抵用券', discount='满10元减10元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='55', brandid=brand, catid=cat, listprice='5', value='5',
                                      product='7月高洁丝49-5', discount='满49元减5元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='56', brandid=brand, catid=cat, listprice='10', value='10',
                                      product='ONEBUYE女装旗舰店', discount='满10元减10元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='57', brandid=brand, catid=cat, listprice='9', value='9',
                                      product='铂金及以上会员准时达券', discount='抵扣9元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限准时达服务')

coupon = models.Coupon.objects.create(couponid='58', brandid=brand, catid=cat, listprice='30', value='30',
                                      product='蜀道香满99减30抵用券', discount='满99元减30元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='59', brandid=brand, catid=cat, listprice='5', value='5',
                                      product='自营进口喜乐口5元抵用券', discount='满49元减5元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='60', brandid=brand, catid=cat, listprice='5', value='5',
                                      product='净安满19-5', discount='满19元减5元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='61', brandid=brand, catid=cat, listprice='30', value='30',
                                      product='施巴99-30', discount='满99元减30元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='61', brandid=brand, catid=cat, listprice='5', value='5',
                                      product='妙思乐5元抵用券', discount='满5元减5元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='62', brandid=brand, catid=cat, listprice='20', value='20',
                                      product='诺优能，爱他美新客券199-20', discount='满199元减20元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='63', brandid=brand, catid=cat, listprice='5', value='5',
                                      product='自营国产福锦指定商品5元抵用券', discount='满5元减5元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='64', brandid=brand, catid=cat, listprice='5', value='5',
                                      product='雅培5元无门槛', discount='满5元减5元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='65', brandid=brand, catid=cat, listprice='5', value='5',
                                      product='多拉美专营店', discount='满11元减5元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='66', brandid=brand, catid=cat, listprice='5', value='5',
                                      product='达芙妮品牌专营店', discount='满6元减5元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='67', brandid=brand, catid=cat, listprice='10', value='10',
                                      product='自营宠物宝路伟嘉99减10券', discount='满99元减10元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='68', brandid=brand, catid=cat, listprice='5', value='5',
                                      product='九易宠物专营店', discount='满5.01元减5元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='69', brandid=brand, catid=cat, listprice='5', value='5',
                                      product='7月口腔狮王59-5', discount='满59元减5元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='70', brandid=brand, catid=cat, listprice='10', value='10',
                                      product='干电池满78元减10元', discount='满78元减10元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='71', brandid=brand, catid=cat, listprice='10', value='10',
                                      product='我厨生鲜专营店', discount='满39元减10元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='72', brandid=brand, catid=cat, listprice='15', value='15',
                                      product='善味阁满99减15抵用券', discount='满99元减15元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='73', brandid=brand, catid=cat, listprice='20', value='20',
                                      product='自营锅具可恩199减20券', discount='满199元减20元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='74', brandid=brand, catid=cat, listprice='5', value='5',
                                      product='自营国产好想你满68减5抵用券', discount='满68元减5元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='75', brandid=brand, catid=cat, listprice='10', value='10',
                                      product='自营馨牌毛巾满99减10', discount='满99元减10元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='76', brandid=brand, catid=cat, listprice='5', value='5',
                                      product='瑞士军刀箱包官方店', discount='满5元减5元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='77', brandid=brand, catid=cat, listprice='5', value='5',
                                      product='黄飞红满45减5抵用券', discount='满45元减5元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='78', brandid=brand, catid=cat, listprice='5', value='5',
                                      product='自营进口啪啪通5元抵用券', discount='满49元减5元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='79', brandid=brand, catid=cat, listprice='15', value='15',
                                      product='自营进口瓦伦丁啤酒15元抵用券', discount='满199元减15元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='80', brandid=brand, catid=cat, listprice='10', value='10',
                                      product='童年时光旗舰店', discount='满25元减10元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='81', brandid=brand, catid=cat, listprice='5', value='5',
                                      product='自营进口全南&一本冲饮满5元抵用券', discount='满49元减5元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='81', brandid=brand, catid=cat, listprice='5', value='5',
                                      product='自营进口万多福5元抵用券', discount='满99元减5元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='82', brandid=brand, catid=cat, listprice='5', value='5',
                                      product='时顺酒类专营店', discount='满11元减5元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='83', brandid=brand, catid=cat, listprice='15', value='15',
                                      product='钻石快线旗舰店', discount='满35元减15元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='84', brandid=brand, catid=cat, listprice='5', value='5',
                                      product='富隆酒窖旗舰店', discount='满10元减5元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='85', brandid=brand, catid=cat, listprice='137', value='137',
                                      product='紫翔服饰专营店', discount='满299元减137元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='86', brandid=brand, catid=cat, listprice='20', value='20',
                                      product='多乐可官方旗舰店', discount='满57元减20元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='87', brandid=brand, catid=cat, listprice='100', value='100',
                                      product='伊威辅食官方旗舰店', discount='满199元减100元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='88', brandid=brand, catid=cat, listprice='20', value='20',
                                      product='长欣家化', discount='满49元减20元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='89', brandid=brand, catid=cat, listprice='188', value='188',
                                      product='DK Aromatherapy精油', discount='满400元减188元', stat='store',
                                      expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='90', brandid=brand, catid=cat, listprice='5', value='5',
                                      product='一次性品牌满55-5元', discount='满55元减5元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='91', brandid=brand, catid=cat, listprice='20', value='20',
                                      product='电子书20元抵用券', discount='满20元减20元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='92', brandid=brand, catid=cat, listprice='10', value='10',
                                      product='亲润10元无门槛', discount='满10元减10元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='93', brandid=brand, catid=cat, listprice='5', value='5',
                                      product='舒氏无门槛5元抵用券', discount='满5元减5元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='94', brandid=brand, catid=cat, listprice='4', value='4',
                                      product='摩卡部分商品立减4元', discount='满4元减4元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='95', brandid=brand, catid=cat, listprice='5', value='5',
                                      product='雀巢5元无门槛抵用券', discount='满5元减5元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='96', brandid=brand, catid=cat, listprice='5', value='5',
                                      product='洋河立减5元抵用券', discount='满5元减5元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='97', brandid=brand, catid=cat, listprice='3', value='3',
                                      product='自营哺育小黄人3元抵用券', discount='满3元减3元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='98', brandid=brand, catid=cat, listprice='10', value='10',
                                      product='孟乍隆无门槛10元抵用券', discount='满10元减10元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='99', brandid=brand, catid=cat, listprice='20', value='20',
                                      product='好奇纸尿裤全品牌299-20券', discount='满299元减20元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='100', brandid=brand, catid=cat, listprice='100', value='100',
                                      product='佰草集官方旗舰店', discount='满299元减100元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='101', brandid=brand, catid=cat, listprice='10', value='10',
                                      product='富贵鸟官方旗舰店', discount='满10元减10元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='101', brandid=brand, catid=cat, listprice='50', value='50',
                                      product='美特斯邦威官方旗舰店', discount='满199元减50元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='102', brandid=brand, catid=cat, listprice='10', value='10',
                                      product='自营进口艾美牛奶10元抵用券', discount='满99元减10元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='103', brandid=brand, catid=cat, listprice='30', value='30',
                                      product='自营锅具菲仕乐30元券', discount='满30元减30元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='104', brandid=brand, catid=cat, listprice='90', value='90',
                                      product='牛尔官方旗舰店', discount='满199元减90元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='105', brandid=brand, catid=cat, listprice='5', value='5',
                                      product='三只松鼠旗舰店', discount='满88元减5元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='106', brandid=brand, catid=cat, listprice='10', value='10',
                                      product='7月丝塔芙98-10', discount='满98元减10元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='107', brandid=brand, catid=cat, listprice='5', value='5',
                                      product='自营天然山谷5元抵用券', discount='满49元减5元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='108', brandid=brand, catid=cat, listprice='20', value='20',
                                      product='自营保健品满200减20', discount='满200元减20元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='109', brandid=brand, catid=cat, listprice='20', value='20',
                                      product='威龙葡萄酒官方旗舰店_52', discount='满20元减20元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='110', brandid=brand, catid=cat, listprice='30', value='30',
                                      product='小狗电器旗舰店', discount='满30元减30元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='111', brandid=brand, catid=cat, listprice='10', value='10',
                                      product='椰岛官方旗舰店', discount='满10元减10元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='112', brandid=brand, catid=cat, listprice='5', value='5',
                                      product='武夷古峪品牌旗舰店', discount='满5元减5元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='113', brandid=brand, catid=cat, listprice='100', value='100',
                                      product='御品汇', discount='满100元减100元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='114', brandid=brand, catid=cat, listprice='5', value='5',
                                      product='CACUSS旗舰店', discount='满5元减5元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='115', brandid=brand, catid=cat, listprice='10', value='10',
                                      product='利兹家居旗舰店', discount='满10元减10元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='116', brandid=brand, catid=cat, listprice='5', value='5',
                                      product='民间果农旗舰店', discount='满5元减5元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='117', brandid=brand, catid=cat, listprice='10', value='10',
                                      product='优尚生活家居专营店', discount='满99元减10元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='118', brandid=brand, catid=cat, listprice='20', value='20',
                                      product='大公鸡管家满168-20', discount='满168元减20元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='119', brandid=brand, catid=cat, listprice='10', value='10',
                                      product='赢旭食品专营店', discount='满100元减10元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='120', brandid=brand, catid=cat, listprice='10', value='10',
                                      product='亮健好药房专营店', discount='满99元减10元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='121', brandid=brand, catid=cat, listprice='30', value='30',
                                      product='自营进口纽仕兰乳品30元抵用券', discount='满199元减30元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='121', brandid=brand, catid=cat, listprice='5', value='5',
                                      product='百秀大药房', discount='满5元减5元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='122', brandid=brand, catid=cat, listprice='5', value='5',
                                      product='康师傅指定商品满30减5元抵用券', discount='满30元减5元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='123', brandid=brand, catid=cat, listprice='30', value='30',
                                      product='自营保健品满300减30', discount='满300元减30元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='124', brandid=brand, catid=cat, listprice='350', value='350',
                                      product='品拓家居照明旗舰店', discount='满999元减350元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='125', brandid=brand, catid=cat, listprice='5', value='5',
                                      product='特产中国•潍坊馆', discount='满99元减5元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='126', brandid=brand, catid=cat, listprice='5', value='5',
                                      product='小熊满99减5', discount='满99元减5元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='127', brandid=brand, catid=cat, listprice='5', value='5',
                                      product='楼兰蜜语品牌旗舰店', discount='满79元减5元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='128', brandid=brand, catid=cat, listprice='5', value='5',
                                      product='自营哺育宝贝可爱5元抵用券', discount='满59元减5元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='129', brandid=brand, catid=cat, listprice='8', value='8',
                                      product='自营进口荷高牛奶8元抵用券', discount='满88元减8元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='130', brandid=brand, catid=cat, listprice='5', value='5',
                                      product='7月海莎普无门槛5元', discount='满5元减5元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='131', brandid=brand, catid=cat, listprice='15', value='15',
                                      product='绿色黄金食品专营店', discount='满98元减15元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='132', brandid=brand, catid=cat, listprice='20', value='20',
                                      product='曲慕内衣旗舰店', discount='满40元减20元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='133', brandid=brand, catid=cat, listprice='3', value='3',
                                      product='森蜂园官方旗舰店_99', discount='满10元减3元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='134', brandid=brand, catid=cat, listprice='60', value='60',
                                      product='雅培部分产品满599-60', discount='满599元减60元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='135', brandid=brand, catid=cat, listprice='50', value='50',
                                      product='罗技品牌券满499元减50元', discount='满499元减50元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='136', brandid=brand, catid=cat, listprice='10', value='10',
                                      product='五仙旗舰店', discount='满10元减10元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='137', brandid=brand, catid=cat, listprice='100', value='100',
                                      product='罗技品牌券满799元减100元', discount='满799元减100元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='138', brandid=brand, catid=cat, listprice='10', value='10',
                                      product='自营想念面条满69减10元', discount='满69元减10元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='139', brandid=brand, catid=cat, listprice='5', value='5',
                                      product='自营国产草原今朝满59减5抵用券', discount='满59元减5元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='140', brandid=brand, catid=cat, listprice='10', value='10',
                                      product='六福珠宝官方旗舰店', discount='满35元减10元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='141', brandid=brand, catid=cat, listprice='10', value='10',
                                      product='博洋家纺官方旗舰店', discount='满11元减10元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='141', brandid=brand, catid=cat, listprice='5', value='5',
                                      product='优品美妆', discount='满5.1元减5元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='142', brandid=brand, catid=cat, listprice='2', value='2',
                                      product='一德堂大药房旗舰店', discount='满2.1元减2元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='143', brandid=brand, catid=cat, listprice='20', value='20',
                                      product='ELLE旗舰店', discount='满21元减20元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='144', brandid=brand, catid=cat, listprice='20', value='20',
                                      product='优禾保健食品专营店', discount='满199元减20元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='145', brandid=brand, catid=cat, listprice='20', value='20',
                                      product='偌斯斐斯童装专营店', discount='满99元减20元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='146', brandid=brand, catid=cat, listprice='10', value='10',
                                      product='鸭鸭官方旗舰店', discount='满25元减10元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='147', brandid=brand, catid=cat, listprice='20', value='20',
                                      product='凯速运动专营店', discount='满200元减20元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='148', brandid=brand, catid=cat, listprice='10', value='10',
                                      product='自营进口纽仕兰乳品10元抵用券', discount='满119元减10元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='149', brandid=brand, catid=cat, listprice='10', value='10',
                                      product='倍轻松满10减10', discount='满10元减10元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='150', brandid=brand, catid=cat, listprice='10', value='10',
                                      product='利临家居专营店', discount='满99元减10元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='151', brandid=brand, catid=cat, listprice='20', value='20',
                                      product='罗西尼手表官方旗舰店', discount='满100元减20元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='152', brandid=brand, catid=cat, listprice='10', value='10',
                                      product='罗技品牌抵用券199元减10元', discount='满199元减10元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='153', brandid=brand, catid=cat, listprice='5', value='5',
                                      product='自然堂官方旗舰店', discount='满99元减5元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='154', brandid=brand, catid=cat, listprice='10', value='10',
                                      product='7月阿莎娜89-10', discount='满89元减10元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='155', brandid=brand, catid=cat, listprice='10', value='10',
                                      product='棉之爱旗舰店', discount='满99元减10元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='156', brandid=brand, catid=cat, listprice='10', value='10',
                                      product='宜露官方旗舰店', discount='满30元减10元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='157', brandid=brand, catid=cat, listprice='5', value='5',
                                      product='美帝亚旗舰店', discount='满15元减5元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='158', brandid=brand, catid=cat, listprice='10', value='10',
                                      product='亲好贝好旗舰店', discount='满30元减10元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='159', brandid=brand, catid=cat, listprice='5', value='5',
                                      product='VENSE唯恩诗官方旗舰店', discount='满15元减5元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='160', brandid=brand, catid=cat, listprice='20', value='20',
                                      product='燕世隆进口食品专营店', discount='满59.8元减20元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='161', brandid=brand, catid=cat, listprice='30', value='30',
                                      product='日本丸永专营店', discount='满99元减30元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='161', brandid=brand, catid=cat, listprice='5', value='5',
                                      product='7月 沐浴类产品69-5', discount='满69元减5元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='162', brandid=brand, catid=cat, listprice='10', value='10',
                                      product='泉林本色官方旗舰店', discount='满99元减10元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='163', brandid=brand, catid=cat, listprice='10', value='10',
                                      product='三枪内衣专卖店', discount='满29元减10元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='164', brandid=brand, catid=cat, listprice='10', value='10',
                                      product='欣和旗舰店', discount='满99元减10元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='165', brandid=brand, catid=cat, listprice='10', value='10',
                                      product='优衣库旗舰店', discount='满100元减10元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='166', brandid=brand, catid=cat, listprice='5', value='5',
                                      product='得利斯官方旗舰店', discount='满79元减5元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='167', brandid=brand, catid=cat, listprice='5', value='5',
                                      product='素色生活旗舰店', discount='满38元减5元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='168', brandid=brand, catid=cat, listprice='40', value='40',
                                      product='自营巴黎水圣培露普娜40元抵用券', discount='满199元减40元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='169', brandid=brand, catid=cat, listprice='80', value='80',
                                      product='四特品牌满299元减80元抵用券', discount='满299元减80元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='170', brandid=brand, catid=cat, listprice='5', value='5',
                                      product='淳一品牌卷满20-5', discount='满20元减5元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='171', brandid=brand, catid=cat, listprice='200', value='200',
                                      product='富甲满999减200', discount='满999元减200元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='172', brandid=brand, catid=cat, listprice='10', value='10',
                                      product='艾泊利旗舰店', discount='满99元减10元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='173', brandid=brand, catid=cat, listprice='30', value='30',
                                      product='古今内衣官方旗舰店', discount='满288元减30元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='174', brandid=brand, catid=cat, listprice='3', value='3',
                                      product='奇强自营满30-3', discount='满30元减3元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='175', brandid=brand, catid=cat, listprice='5', value='5',
                                      product='7月米娅49-5', discount='满49元减5元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='176', brandid=brand, catid=cat, listprice='10', value='10',
                                      product='爱司盟旗舰店', discount='满10元减10元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='177', brandid=brand, catid=cat, listprice='5', value='5',
                                      product='天士力大健康专营店', discount='满5.01元减5元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='178', brandid=brand, catid=cat, listprice='10', value='10',
                                      product='亚文斯达专营店', discount='满10元减10元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='179', brandid=brand, catid=cat, listprice='20', value='20',
                                      product='养生堂旗舰店_77', discount='满21元减20元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='180', brandid=brand, catid=cat, listprice='20', value='20',
                                      product='顶瓜瓜官方旗舰店', discount='满159元减20元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='181', brandid=brand, catid=cat, listprice='20', value='20',
                                      product='mlily官方旗舰店', discount='满199元减20元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='181', brandid=brand, catid=cat, listprice='10', value='10',
                                      product='UOVO旗舰店', discount='满99元减10元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='182', brandid=brand, catid=cat, listprice='20', value='20',
                                      product='百丽童鞋专营店', discount='满199元减20元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='183', brandid=brand, catid=cat, listprice='50', value='50',
                                      product='韩都衣舍旗舰店', discount='满299元减50元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='184', brandid=brand, catid=cat, listprice='10', value='10',
                                      product='帅康厨卫满11减10', discount='满11元减10元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='185', brandid=brand, catid=cat, listprice='10', value='10',
                                      product='7月恩芝89-10', discount='满89元减10元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='186', brandid=brand, catid=cat, listprice='20', value='20',
                                      product='芬尼湾旗舰店', discount='满199元减20元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='187', brandid=brand, catid=cat, listprice='5', value='5',
                                      product='固特异车品专营店', discount='满6元减5元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='188', brandid=brand, catid=cat, listprice='5', value='5',
                                      product='家佰利旗舰店', discount='满99元减5元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='189', brandid=brand, catid=cat, listprice='5', value='5',
                                      product='卓然丽鑫化妆品专营店', discount='满39元减5元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='190', brandid=brand, catid=cat, listprice='120', value='120',
                                      product='万和满1500减120', discount='满1500元减120元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限1号店自营')

coupon = models.Coupon.objects.create(couponid='191', brandid=brand, catid=cat, listprice='100', value='100',
                                      product='博成箱包专卖店', discount='满500元减100元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='192', brandid=brand, catid=cat, listprice='50', value='50',
                                      product='Hersheson赫嫀旗舰店', discount='满200元减50元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='193', brandid=brand, catid=cat, listprice='50', value='50',
                                      product='花花公子贵宾旗舰店', discount='满199元减50元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='194', brandid=brand, catid=cat, listprice='20', value='20',
                                      product='Cleasy可立洗旗舰店', discount='满99元减20元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='195', brandid=brand, catid=cat, listprice='30', value='30',
                                      product='虞琳娜美妆专营店', discount='满149元减30元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='196', brandid=brand, catid=cat, listprice='400', value='400',
                                      product='秘芝堂旗舰店', discount='满1600元减400元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='197', brandid=brand, catid=cat, listprice='10', value='10',
                                      product='斐素FSJUICE果汁旗舰店', discount='满50元减10元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='198', brandid=brand, catid=cat, listprice='5', value='5',
                                      product='欣延健康专营店', discount='满20元减5元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='199', brandid=brand, catid=cat, listprice='40', value='40',
                                      product='优加防辐射服旗舰店', discount='满199元减40元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='200', brandid=brand, catid=cat, listprice='20', value='20',
                                      product='蒙谷香旗舰店', discount='满80元减20元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

coupon = models.Coupon.objects.create(couponid='201', brandid=brand, catid=cat, listprice='20', value='20',
                                      product='贝悦官方旗舰店', discount='满99元减20元', stat='store', expiredtime=date)
coupon.save()
models.Listitem.objects.create(couponid=coupon, listid=couponList)
models.Limit.objects.create(couponid=coupon, content='限指定店铺')

for i in range(0, 20):
    stat = 'onSale'
    couponid = str(random.randint(1, 200))
    coupon = models.Coupon.objects.get(couponid=couponid)
    coupon.stat = stat
    coupon.save()
    onSaleList = models.Couponlist.objects.get(stat='onSale', userid='1500885424mkpq')
    models.Listitem.objects.create(listid=onSaleList, couponid=coupon)

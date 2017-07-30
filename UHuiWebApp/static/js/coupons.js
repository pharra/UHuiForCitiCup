/**
 * Created by wf on 17-7-30.
 */

$("div[id^='couponsid_']").click(function () {
    var couponsid = $(this).attr(id).replace("couponsid_",'');
    window.location.href = "/commodity?couponsID="+couponsid;
});
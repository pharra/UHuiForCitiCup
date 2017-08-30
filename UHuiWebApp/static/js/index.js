/*
 $(".category-list").hover(
 function (event) {
 $($(this).children().attr("href")).css("height", $('#myCarousel').height());
 $($(this).children().attr("href")).css("width", $('#myCarousel').width());
 $($(this).children().attr("href")).removeClass("being-hidden");
 $($(this).children().attr("href")).css("left", $('#myCarousel').offset().left);
 $($(this).children().attr("href")).css("top", $('#myCarousel').offset().top);
 $('#myCarousel').addClass("being-hidden");
 },
 function () {
 $($(this).children().attr("href")).addClass("being-hidden");
 $('#myCarousel').removeClass("being-hidden");
 }
 );
 $(".category-left").css("height", $('#myCarousel').height());

 $(window).resize(function () {
 $(".category-left").css("height", $('#myCarousel').height());
 });

 */
$(function ($) {
    $.fn.autoHide = function () {
        var ele = this;
        $(document).on('click',function (e) {
            if(ele.is(':visible') && (!$(e.target)[0].isEqualNode(ele[0]) && ele.has(e.target).length === 0)){
                ele.addClass("being-hidden");
            }
            e.stopPropagation();
            return true;
        });
        return this;
    }
});

$(".login-li").click(function () {
    removechecked("#re-password");
    removechecked("#user_id");
    $(this).addClass("login-active");
    $(this).siblings().removeClass("login-active");
    $($(this).children().attr("href")).addClass("active in");
    $($(this).siblings().children().attr("href")).removeClass("active in");
});


function isPhoneNo(phone) {
    var pattern = /^1[34578]\d{9}$/;
    return pattern.test(phone);
}

function isEmail(email) {
    var emailreg = /^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+(.[a-zA-Z0-9_-])+/;
    return emailreg.test(email);
}

function CheckedCss(id) {
    var left1 = $(id).offset().left + $(id).width() + 'px';
    var top1 = $(id).offset().top + ($(id).height() / 2) + 'px';
    id = id.split('#')[1];
    var thisid = "for" + id;
    var newdom = $("<i></i>").addClass("fa fa-check").css("position", "absolute").attr("aria-hidden", "true").attr("id", thisid);
    newdom.css("left", left1);
    newdom.css("top", top1);
    newdom.css("color", "green");
    newdom.css("height", "15px");
    newdom.css("width", "15px");
    $("body").append(newdom);
}

function removechecked(id) {
    id = id.split('#')[1];
    var thisid = "#for" + id;
    $(thisid).remove();
}

function getchecked(id) {
    id = id.split('#')[1];
    var thisid = "#for" + id;
    return ($(thisid).length >= 1);
}


$('#user_id,#mobile_user_id').bind('input propertychange', function () {
    var thisid = '#' + $(this).attr('id');
    var verification_code_div = '#' + $(this).attr('id').replace('user_id', 'verification_code_div');
    var user_id_content = '#' + $(this).attr('id') + '_content';
    if (isPhoneNo($(this).val()) && $(this).val()) {

        $(verification_code_div).show();
        $(user_id_content).hide();
        removechecked(thisid);
        CheckedCss(thisid);
    } else if (isEmail($(this).val()) && $(this).val()) {
        $(verification_code_div).hide();
        $(user_id_content).hide();
        removechecked(thisid);
        CheckedCss(thisid);
    } else {
        $(verification_code_div).hide();
        $(user_id_content).hide();
        removechecked(thisid);

    }
});


$('#user_id,#mobile_user_id').blur('input propertychange', function () {
    var thisid = '#' + $(this).attr('id');
    var verification_code_div = '#' + $(this).attr('id').replace('user_id', 'verification_code_div');
    var user_id_content = '#' + $(this).attr('id') + '_content';
    if (isPhoneNo($(this).val())) {
        $(verification_code_div).show();
    } else if (isEmail($(this).val())) {
        $(verification_code_div).hide();
    } else if (!($(this).val())) {
        $(verification_code_div).hide();
        $(user_id_content).hide();

    } else {
        $(verification_code_div).hide();
        $(user_id_content).show();
    }
});


$('#re-password,#password').blur('input propertychange', function () {
    if (($('#re-password').val() === $("#password").val()) && ($('#re-password').val() !== "") && $('#password').val() !== "") {
        $('#password_content').hide();
        removechecked("#re-password");
        CheckedCss("#re-password");
        $("#signup-md5-password").val($.md5($("#re-password").val() + "UHui"));
    } else if (($('#re-password').val() === "") || ($('#password').val() === "")) {
        $('#password_content').hide();
        removechecked("#re-password");
    } else {
        $('#password_content').show();
        removechecked("#re-password");
    }
});

$('#mobile_re-password,#mobile_password').blur('input propertychange', function () {
    if (($('#mobile_re-password').val() === $("#mobile_password").val()) && ($('#mobile_re-password').val() !== "") && $('#mobile_password').val() !== "") {
        $('#mobile_password_content').hide();
        removechecked("#mobile_re-password");
        CheckedCss("#mobile_re-password");
        $("#signup-md5-password").val($.md5($("#mobile_re-password").val() + "UHui"));
    } else if (($('#mobile_re-password').val() === "") || ($('#mobile_password').val() === "")) {
        $('#mobile_password_content').hide();
        removechecked("#mobile_re-password");
    } else {
        $('#mobile_password_content').show();
        removechecked("#mobile_re-password");
    }
});


/*
$("#login-password").change(function () {
    $("#login-md5-password").val($.md5($("#login-password").val() + "UHui"));
});
*/


$('#user_id,#re-password,#password,#nickname').bind('input propertychange', function () {
    if ((isPhoneNo($('#user_id').val()) || isEmail($('#user_id').val())) && (($('#re-password').val() == $("#password").val()) && ($('#re-password').val() != "") && $('#password').val() != "") && ($('#nickname').val().length > 0)) {
        $("#login-button").attr("disabled", false);
    } else {
        $("#login-button").attr("disabled", "disabled");
    }
});
$(window).resize(function () {
    if (getchecked("#user_id")) {
        removechecked("#user_id");
        CheckedCss("#user_id");
    }
    if (getchecked("#mobile_user_id")) {
        removechecked("#mobile_user_id");
        CheckedCss("#mobile_user_id");
    }
    if (getchecked("#re-password")) {
        removechecked("#re-password");
        CheckedCss("#re-password");
    }
    if (getchecked("#mobile_re-password")) {
        removechecked("#mobile_re-password");
        CheckedCss("#mobile_re-password");
    }
});

function login_handler() {

    $.ajax({
        url: '/post_login',
        type: 'POST',
        dataType: 'json',
        data: {"username": $("#login-username").val(), "password": $.md5($("#login-password").val() + "UHui")},
        timeout: 3000,
        cache: false,
        async: false,
        beforeSend: LoadFunction,
        error: erryFunction,
        success: succFunction
    });

    function LoadFunction() {
    }

    function erryFunction() {
    }

    function succFunction(data) {
        if (data.error === "") {
            window.location.href = "/";
        } else {
            $("#login_failed_content").children().text(data.error);
            $("#login_failed_content").show();
        }

    }
};

function sign_up() {

    $.ajax({
        url: '/post_signup',
        type: 'POST',
        dataType: 'json',
        data: {
            "username": $("#user_id").val(),
            "password": $("#signup-md5-password").val(),
            "nickname": $("#nickname").val(),
            "gender": $('#genderchoice option:selected').text()
        },
        timeout: 3000,
        cache: false,
        beforeSend: LoadFunction,
        error: erryFunction,
        success: succFunction
    });

    function LoadFunction() {
    }

    function erryFunction() {
    }

    function succFunction(data) {
        if (data.errno === "1") {
            $("#login-failed").children()[0].innerHTML = data.message;
            $("#login-failed").show();
        } else if (data.errno === "0") {


            $.ajax({
                url: '/post_login',
                type: 'POST',
                dataType: 'json',
                data: {
                    "username": $("#user_id").val(),
                    "password": $("#signup-md5-password").val()
                },
                timeout: 3000,
                cache: false,
                success: succinnerFunction
            });

            function succinnerFunction(data) {
                if (data.error === "") {
                    window.location.href = "/";
                }

            }


        } else if (data.errno === "2") {
            window.location.href = "/";
        }
    }

};

$(document).ready(function () {
    $(window).scroll(function (event) {
        $("#index_navigation").css("top", $(window).scrollTop() + 'px');
    });
});


$("#singlemessage, #userinfo").click(function (event) {

    var being_hidden_message = '#for' + $(this).attr("id");
    $(being_hidden_message).toggleClass("being-hidden").autoHide();
    var offsetleft = '-' + ($(being_hidden_message).width() / 2 - $(this).parent().width() / 2) + "px";
    $(being_hidden_message).css("left", offsetleft);
    return false;
});


/*$(".edituserinfo").click(function () {
    $(this).parent().hide();
    $(this).parent().nextAll().show();
    $("#edit-userinfo-commit-div").show();
});*/

$('#newemail').blur('input propertychange', function () {
    if (isEmail($("#newemail").val())) {
        $("#newemail_button").attr("disabled", false);
        $("#newemail_content").hide();

    } else {
        $("#newemail_button").attr("disabled", "disabled");
        $("#newemail_content").show();
    }

});


$('#newtelno').blur('input propertychange', function () {
    if (isPhoneNo($("#newtelno").val())) {
        $("#newtelno_button").attr("disabled", false);
        $("#newtelno_content").hide();
    } else {
        $("#newtelno_button").attr("disabled", "disabled");
        $("#newtelno_content").show();

    }

});

$('#newemail').bind('input propertychange', function () {
    if (isEmail($("#newemail").val())) {
        $("#newemail_button").attr("disabled", false);


    } else {
        $("#newemail_button").attr("disabled", "disabled");

    }

});


$('#newtelno').blur('input propertychange', function () {
    if (isPhoneNo($("#newtelno").val())) {
        $("#newtelno_button").attr("disabled", false);

    } else {
        $("#newtelno_button").attr("disabled", "disabled");


    }

});


$('#edit_userinfo_submit').blur('input propertychange', function () {
    if ($("#newname").val() || ($("#newpassword").val() && $("#oldpassword").val()) || ($("#newemail").val() && $("#email_verification_code").val()) || ($("#newtelno").val() && $("#newphone_verification_code").val())) {
        $("#edit_userinfo_submit").attr("disabled", false);
    } else {
        $("#edit_userinfo_submit").attr("disabled", "disabled");
    }

});

function func_edit_userinfo_submit() {
    var content = {};
    if ($("#newname").val()) {
        content.nickname = $("#newname").val();
    }
    if ($("#newpassword").val() && $("#oldpassword").val()) {
        content.password = $.md5($("#newpassword").val() + 'UHui');
        content.oldPassword = $.md5($("#oldpassword").val() + 'UHui');
    }
    if ($("#newemail").val() && $("#email_verification_code").val()) {
        content.email = $("#newemail").val();
        content.email_verification_code = $("#email_verification_code").val();
    }
    if ($("#newtelno").val() && $("#newphone_verification_code").val()) {
        content.phoneNum = $("#newtelno").val();
        content.newphone_verification_code = $("#newphone_verification_code").val();
    }
    $.ajax({
        url: '/post_modifyUserInfo',
        type: 'POST',
        dataType: 'json',
        data: content,
        timeout: 3000,
        cache: false,
    });
};

function get_email_verificationcode() {
    var email = $("#newemail").val();
    $.ajax({
        url: '/post_sendEmailVerifyCode',
        type: 'POST',
        dataType: 'json',
        data: {"email": email},
        timeout: 3000,
        cache: false,
    });

};

function get_phone_verificationcode() {
    var phonenum = $("#newtelno").val();
    $.ajax({
        url: '/post_sendMobileVerifyCode',
        type: 'POST',
        dataType: 'json',
        data: {"phonenum": phonenum},
        timeout: 3000,
        cache: false,
    });

};

$(".max").click(function () {
    var str = $(this).attr("id").split("_")[0];
    var hidden_str = '#' + str + '_menu';
    $(hidden_str).removeClass(" being-hidden");
    $(hidden_str).siblings().addClass(" being-hidden");

    $(this).addClass("liactive");
    $(this).siblings().removeClass("liactive");

    var tab_content = '#tab_' + $(this).attr("id");
    $(tab_content).addClass(" in active");
    $(tab_content).siblings().removeClass(" in active");

    var tab_title = '#info_' + $(this).attr("id");
    $(tab_title).children().click();
});

var loaderPage = function () {
    $(".loader").fadeOut("slow");
};
$(function () {
    loaderPage();
});
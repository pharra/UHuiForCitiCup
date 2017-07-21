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

$(".login-li").click(function() {
    removechecked("#re-password");
    removechecked("#user_id");
    $(this).addClass("login-active");
    $(this).siblings().removeClass("login-active")
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
    id = id.split('#')[1]
    var thisid = "for" + id;
    newdom = $("<i></i>").addClass("fa fa-check").css("position", "absolute").attr("aria-hidden", "true").attr("id", thisid);
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


$('#user_id').bind('input propertychange', function() {
    if (isPhoneNo($('#user_id').val()) && $('#user_id').val()) {
        $('#verification_code_div').show();
        $('#user_id_content').hide();
        CheckedCss("#user_id");
    } else if (isEmail($('#user_id').val()) && $('#user_id').val()) {
        $('#verification_code_div').hide();
        $('#user_id_content').hide();
        CheckedCss("#user_id");
    } else {
        $('#verification_code_div').hide();
        $('#user_id_content').hide();
        removechecked("#user_id");

    }
});

$('#user_id').blur('input propertychange', function() {
    if (isPhoneNo($('#user_id').val())) {
        $('#verification_code_div').show();
    } else if (isEmail($('#user_id').val())) {
        $('#verification_code_div').hide();
    } else if (!($('#user_id').val())) {
        $('#verification_code_div').hide();
        $('#user_id_content').hide();

    } else {
        $('#verification_code_div').hide();
        $('#user_id_content').show();
    }
});


$('#re-password,#password').blur('input propertychange', function() {
    if (($('#re-password').val() == $("#password").val()) && ($('#re-password').val() != "") && $('#password').val() != "") {
        $('#password_content').hide();
        CheckedCss("#re-password");
        $("#signup-md5-password").val($.md5($("#re-password").val() + "UHui"));
    } else if (($('#re-password').val() == "") || ($('#password').val() == "")) {
        $('#password_content').hide();
        removechecked("#re-password");
    } else {
        $('#password_content').show();
        removechecked("#re-password");
    }
});


$("#login-password").blur('input propertychange', function() {
    $("#login-md5-password").val($.md5($("#login-password").val() + "UHui"));
});


$('#user_id,#re-password,#password,#nickname').bind('input propertychange', function() {
    if ((isPhoneNo($('#user_id').val()) || isEmail($('#user_id').val())) && (($('#re-password').val() == $("#password").val()) && ($('#re-password').val() != "") && $('#password').val() != "") && ($('#nickname').val().length > 0)) {
        $("#login-button").attr("disabled", false);
    } else {
        $("#login-button").attr("disabled", "disabled");
    }
});
$(window).resize(function() {
    if (getchecked("#user_id")) {
        removechecked("#user_id");
        CheckedCss("#user_id");
    }
    if (getchecked("#re-password")) {
        removechecked("#re-password");
        CheckedCss("#re-password");
    }
});

function login_handler() {

    $.ajax({
        url: '/post_login',
        type: 'POST',
        dataType: 'json',
        data: { "username": $("#login-username").val(), "password": $("#login-md5-password").val() },
        timeout: 3000,
        cache: false,
        beforeSend: LoadFunction,
        error: erryFunction,
        success: succFunction
    })

    function LoadFunction() {}

    function erryFunction() {}

    function succFunction(data) {
        if (data.error == "") {
            window.location.href = "/";
        } else {
            $("#login_failed_content").children().text(data.error)
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
    })

    function LoadFunction() {}

    function erryFunction() {}

    function succFunction(data) {
        if (data.errno == "1") {
            $("#login-failed").children()[0].innerHTML = data.message;
            $("#login-failed").show();
        } else if (data.errno == "0") {


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
                success: succFunction
            })


            function succFunction(data) {
                if (data.error == "") {
                    window.location.href = "/";
                }

            }


        } else if (data.errno == "2") {
            window.location.href = "/";
        }
    }

};

$(document).ready(function() {
    $(window).scroll(function(event) {
        $("#index_navigation").css("top", $(window).scrollTop() + 'px');


    });
});


$("#singlemessage, #userinfo").click(function() {
    var being_hidden_message = '#for' + $(this).attr("id");
    $(being_hidden_message).toggleClass("being-hidden");
    var offsetleft = '-' + ($(being_hidden_message).width() / 2 - $(this).parent().width() / 2) + "px";
    // var offsetleft = $(this).offset().left;
    // var offsettop = $(this).offset().top;
    // $(being_hidden_message).css("top",offsettop);
    // $(being_hidden_message).css("left",offsetleft);
    $(being_hidden_message).css("left", offsetleft);


});
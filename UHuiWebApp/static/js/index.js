$(".category-list").hover(
    function(event) {
        $($(this).children().attr("href")).css("height", $('#myCarousel').height());
        $($(this).children().attr("href")).css("width", $('#myCarousel').width());
        $($(this).children().attr("href")).css("left", $('#myCarousel').offset().left - 4);
        $($(this).children().attr("href")).css("top", $('#myCarousel').offset().top);
        //$('#myCarousel').addClass("being-hidden");
    },
    function() {}
);
//$(".category-left").css("height", $('#myCarousel').height());

$(window).resize(function() {
    $(".category-left").css("height", $('#myCarousel').height());
});


$(".login-li").click(function() {
    $(this).addClass("login-active");
    $(this).siblings().removeClass("login-active")
    $($(this).children().attr("href")).addClass("active in");
    $($(this).siblings().children().attr("href")).removeClass("active in");
});
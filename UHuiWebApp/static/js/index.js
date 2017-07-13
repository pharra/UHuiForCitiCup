$(".category-list-a").hover(
    function(event) {
        $($(this).attr("href")).css("height", $('#myCarousel').height());
        $($(this).attr("href")).css("width", $('#myCarousel').width());

        $($(this).attr("href")).removeClass("being-hidden");
        $($(this).attr("href")).css("left", $('#myCarousel').offset().left);
        $($(this).attr("href")).css("top", $('#myCarousel').offset().top);
        $('#myCarousel').addClass("being-hidden");
    },
    function() {
        $($(this).attr("href")).addClass("being-hidden");
        $('#myCarousel').removeClass("being-hidden");
    }
);
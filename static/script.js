$(document).ready(function(){

    function nextSlide() {
        var active = $('.owl-pagination .active').first();
        console.log(active.next());

        if (active.next().length) {
            console.log(active.next('.owl-page').first());
            active.next('.owl-page').first().find('span').click();
        } else {
            $('.owl-pagination .owl-page').first().find('span').click();
        }
    }

    setTimeout(nextSlide, 5000);

});

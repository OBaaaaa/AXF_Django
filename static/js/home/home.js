$(function () {

    initSwiperWheel();
    initSwiperMustBuy();

})

function initSwiperWheel() {

    var swiper = new Swiper('#topSwiper',{
        autoplay:2000,
        pagination:'.swiper-pagination'
    })

}

function initSwiperMustBuy() {

    var swiper = new Swiper('#swiperMenu',{
        slidesPerView:3,
    })

}
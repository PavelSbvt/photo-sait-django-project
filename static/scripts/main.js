$(document).ready(function() {
    $('.c-slider').slick({
        infinite: true,
        slidesToShow: 3,
        slidesToScroll: 1,
        draggable: true,
        arrows: false, // исправлено
        responsive: [
            {
                breakpoint: 850,
                settings: {
                    slidesToShow: 2
                }
            },
            {
                breakpoint: 600,
                settings: {
            slidesToShow: 1
                }
            }
        ]
    });

    $('#dev-arr-right').on('click', function() {
        $('.c-slider').slick('slickNext');
    });

    $('#dev-arr-left').on('click', function() {
        $('.c-slider').slick('slickPrev');
    });
});
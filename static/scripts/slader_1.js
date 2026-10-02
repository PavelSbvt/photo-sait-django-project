$(function() {
    $('.c-slider').slick({
        infinite: true,
        slidesToShow: 3,
        slidesToScroll: 1,
        draggable: true,
        arrows: false,
        responsive:[
            {
                breakpoint: 882,
                settings: {
                    slidesToShow: 2,
                }
            },
            
        ]
    });
    $('#dev-arr-right').on('click', function() {
        $('.c-slider').slick('slickNext');
    });
    $('#dev-arr-left').on('click', function() {
        $('.c-slider').slick('slickPrev');
    });
})
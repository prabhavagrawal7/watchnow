// run js when dom loads
$(() => {
    var carousels = $('.movie-con')
    var obj = {};
    carousels.each(function (i, carousel) {
        obj[carousel.id] = { "slide": 0, "slide_obj": $(carousel).children('.movie-slide') };
        obj[carousel.id]['slide_obj'][0].style.display = 'flex';
    });
    carousels.each(function (i, carousel) {
        $(carousel).children('.prev').on('click', function () {
            console.log("hello");
            carouselinfo = obj[carousel.id];
            if (carouselinfo['slide'] == 0) return;
            carouselinfo['slide'] -= 1;
            carouselinfo['slide_obj'][carouselinfo['slide']].style.display = "flex";
            carouselinfo['slide_obj'][carouselinfo['slide'] + 1].style.display = "none";
        }),
            $(carousel).children('.next').on('click', function () {
                console.log("hello");
                carouselinfo = obj[carousel.id];
                if (carouselinfo['slide'] == carouselinfo['slide_obj'].length - 1) return;
                carouselinfo['slide'] += 1;
                carouselinfo['slide_obj'][carouselinfo['slide']].style.display = "flex";
                carouselinfo['slide_obj'][carouselinfo['slide'] - 1].style.display = "none";
            })
    });
    $('.movie').hover(
        function () {
            $(this).css({'border': '2px solid #0177ff', 'z-index': 2, 'transform': 'scale(1.15)'}); 
            $(this).children('.movie-details').show(); 
        },
        function () {
            $(this).css({'border': '', 'z-index': 1, 'transform': 'scale(1.0)'}); 
            $(this).children('.movie-details').hide();
        }, 
    )
});

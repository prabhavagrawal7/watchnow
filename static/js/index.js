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
            $(this).children('.movie-details').slideDown(); 
            $(this).animate({ 'width': '363px', 'height': '203.5px'}, 200)
        },
        function () {
            $(this).children('.movie-details').slideUp();
            $(this).animate({ 'width': '330px', 'height': '185px' }, 200)
        }
    )
});

function get_tns(container, controls){
    return tns({
        container: container,
        "slideBy": 1,
        "speed": 400,
        "nav": false,
        controlsContainer: controls,
        responsive: {
            1600: {
                items: 6,
                gutter: 20
            },
            1024: {
                items: 5,
                gutter: 20
            },
            768: {
                items: 3,
                gutter: 20
            },
            480: {
                items: 2,
                gutter: 20
            }
        }
    })
}

let slider_for_you = get_tns(".book-slider-for-you", "#controls-for-you");
let slider_horror = get_tns(".book-slider-horror", "#controls-horror");
let slider_happy = get_tns(".book-slider-happy", "#controls-happy");
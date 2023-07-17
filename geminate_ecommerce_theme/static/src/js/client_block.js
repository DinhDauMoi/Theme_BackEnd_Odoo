odoo.define('geminate_ecommerce_theme.client_slider', function (require) {
"use strict";
    $(document).ready(function(){
        if($('.customer-logos').length > 0)
        {
            $('.customer-logos').slick({
                slidesToShow: 6,
                slidesToScroll: 1,
                autoplay: true,
                autoplaySpeed:2000,
                arrows: false,
                dots: false,
                pauseOnHover: false,
                responsive: [{
                    breakpoint: 768,
                    settings: {
                          slidesToShow: 4
                    }
                }, {
                    breakpoint: 520,
                    settings: {
                        slidesToShow: 3
                    }
                }]
            });
        }
    });
});
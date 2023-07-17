const swiper_1 = new Swiper('.swiper_new_pro_snippet', {
    loop:true,
    spaceBetween:40,
    slidesPerView: "auto",
    autoplay: true,
    loop: false,
    navigation: {
        nextEl: '.brand_next',
        prevEl: '.brand_prev',
    },
    breakpoints: {
        280: {
            slidesPerView: 1,
            spaceBetween: 10,
        },
        640: {
            slidesPerView: 2,
            spaceBetween: 60,
          },
        768: {
            slidesPerView: 2,
            spaceBetween: 60,
          },
        1024: {
            slidesPerView: 3,
            spaceBetween: 20,
          },
        1200: {
            slidesPerView: 4,
            spaceBetween: 20,
          },
        },
});


const swiper_2 = new Swiper('.swiper_card_snippet', {
    loop:true,
    spaceBetween:40,
    slidesPerView: "auto",
    autoplay: true,
    loop: false,
    navigation: {
        nextEl: '.brand_next',
        prevEl: '.brand_prev',
    },
    breakpoints: {
        280: {
            slidesPerView: 1,
            spaceBetween: 10,
        },
        640: {
            slidesPerView: 2,
            spaceBetween: 60,
          },
        768: {
            slidesPerView: 2,
            spaceBetween: 60,
          },
        1024: {
            slidesPerView: 3,
            spaceBetween: 20,
          },
        1200: {
            slidesPerView: 3,
            spaceBetween: 20,
          },
        },
});


const swiper_3 = new Swiper('.swiper_client_snippet', {
    spaceBetween:40,
    slidesPerView: "auto",
    autoplay: true,
    loop: false,
    breakpoints: {
        280: {
            slidesPerView: 1,
            spaceBetween: 10,
        },
        640: {
            slidesPerView: 2,
            spaceBetween: 60,
          },
        768: {
            slidesPerView: 3,
            spaceBetween: 60,
          },
        1024: {
            slidesPerView: 3,
            spaceBetween: 20,
          },
        1200: {
            slidesPerView: 4,
            spaceBetween: 20,
          },
        },
});




$(document).ready(function() {

    $('.ir-arriba').click(function() {
        $('body, html').animate({
            scrollTop: '0px'
        }, 300);
    });

    // Carrousel
    $('#recipeCarousel').carousel({
      interval: 5000
    })

    $('.carousel .carousel-item').each(function(){
        var minPerSlide = 3;
        var next = $(this).next();
        if (!next.length) {
        next = $(this).siblings(':first');
        }
        next.children(':first-child').clone().appendTo($(this));

        for (var i=0;i<minPerSlide;i++) {
            next=next.next();
            if (!next.length) {
                next = $(this).siblings(':first');
            }
            next.children(':first-child').clone().appendTo($(this));
          }
    });
    ///////

    $(window).scroll(function() {
        if ($(this).scrollTop() > 0) {
            $('.ir-arriba').slideDown(300);
        } else {
            $('.ir-arriba').slideUp(300);
        }
    });
});

    // Checker del formulario "Crear Vehículo"
    function check() {
        const edModelo = document.getElementById("edModelo");
        const edAno = document.getElementById("edAno");
        const edCv = document.getElementById("edCv");
        const edMotor = document.getElementById("edMotor");
        const edPrecio = document.getElementById("edPrecio");


        var toret = false;

        if (edModelo.value.trim().length > 0 && edCv.value.trim().length > 0 && edMotor.value.trim().length > 0 && edPrecio.value.trim().length > 0
            && edAno.value.trim().length > 0) {
            toret = true;
        }

        return toret;
    }
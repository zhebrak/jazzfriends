$(document).ready(function(){

    $('#form-submit').on('click', function() {
        $.ajax({
            method: 'POST',
            url: '/feedback/',
            data: {
                'csrfmiddlewaretoken': $('.contact-form input[name=csrfmiddlewaretoken]').val(),
                'name': $('#form-name').val(),
                'contact': $('#form-contact').val(),
                'message': $('#form-message').val()
            },
            dataType: "json",
            success: function(data) {
                var message = $('#contact-message');
                message.css('display', 'block');
                if (data['response'] == 'OK') {
                    $('#feedback').css('display', 'none');
                    message.html('<h5>Спасибо за сообщение, мы скоро ответим вам!</h5>')
                } else {
                    message.text('Пожалуйста, заполните все поля.')
                }

            }
        })
    });


    var photoCarousel = $('.photo .owl-carousel');
    $('.photo .item img').on('click', function() {
       photoCarousel.trigger('owl.next');
    });

});

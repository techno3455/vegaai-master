$('.united.modal').modal({
    allowMultiple: false,
});
// attach events
// haven't attached events over button of modal 3
$('#modal1').modal('attach events', '#call-modals');
$('#modal2').modal('attach events', '#call-modal-2');
// disable the comment bellow to call the modal 4 after click on button into modal 3
//$('#modal4').modal('attach events', '#btn-modal-3');


// Individual events - unecessary but i does it.
$('center .button').on('click', function(){
    // using the attribute data-modal to identify for what modal the button references
    modal = $(this).attr('data-modal');
    // creating the individual event attached to click over button
    $('#'+modal+'.modal').modal(
        'show'
    );
});



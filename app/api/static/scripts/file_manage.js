
var video_file_types = ['video/webm', 'video/mp4']

function chouse_file() {
    $('#file_form').click()
}

function take_file() {

    var file = $('#file_form').get(0).files[0];
    clear_file_form()
    var file_type = file.type

    if (!check_file_type(file_type)) {
        temp_error_label_active()
        return
    }

    read_file(file, file_type)
}

function read_file(file, file_type) {
    var reader = new FileReader();
    reader.onload = () => start_video_play(reader.result, file_type);
    reader.readAsDataURL(file);
    
}

function start_video_play(video_base64, file_type) {
    
    var source = document.createElement('source')
    source.src = video_base64
    source.type = file_type

    all_btns_unactive()
    stop_video()
    replace_video_source(source)
    start_video()
    
}


function clear_file_form() {
    $("#file_form").val(null)
}

$(document).ready(function() {

    $('#add_file_zone').on('dragenter', function (e){
        e.preventDefault();
        show_input_file_label()
        $(this).css('background', '#E39250');
    });

    $('#add_file_zone').on('dragover', function(e) {
        e.preventDefault()
        show_input_file_label()
        $(this).css('background', '#E39250');
    })

    
    $('#add_file_zone').on('dragleave', function (e){

        if ((this).contains(e.relatedTarget)) {
            return
        }

        e.preventDefault();
        $(this).css('background', '#fff5ee');

        show_file_label()

    });

    
    $('#add_file_zone').on('mouseenter', function (e){
        e.preventDefault();
        $(this).css('background', '#E39250');
    });

    $('#add_file_zone').on('mouseleave', function(e) {
        e.preventDefault()
        $(this).css('background', '#fff5ee');
    })

    $("#add_file_zone").on('drop', function (e){

        e.preventDefault();
        $(this).css('background', '#fff5ee');
        show_file_label()
        
        var file = e.originalEvent.dataTransfer.files[0];
        clear_file_form()
        file_type = file.type

        if (!check_file_type(file_type)) {
            temp_error_label_active()
            return
        }

        read_file(file, file_type)
    });


})

function show_file_label() {
    $('#file_label').removeClass('non_display')
    $('#error_label').addClass('non_display')
    $('#file_input_label').addClass('non_display')
}

function show_input_file_label() {
    $('#file_label').addClass('non_display')
    $('#error_label').addClass('non_display')
    $('#file_input_label').removeClass('non_display')
}

function show_error_label() {
    $('#file_label').addClass('non_display')
    $('#error_label').removeClass('non_display')
    $('#file_input_label').addClass('non_display')
}

function temp_error_label_active() {
    show_error_label()
    setTimeout(show_file_label, 500)
}

function check_file_type(file_type) {

    if (video_file_types.includes(file_type)) {
        return true
    }
    return false

}
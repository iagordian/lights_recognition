

function all_btns_unactive() {
    $('.start_denostration_btn').removeClass('active_btn')
}

function replace_video_source(data) {

    clear_video_player_sourses()
    append_video_sourse(data)
    $("#video_player").get(0).load()
    
}

function clear_video_player_sourses() {
    $('#video_player').empty()
}

function append_video_sourse(data) {
    $('#video_player').append(data)
}

function start_video() {

    record_start_video()
    $('#video_player').get(0).play()
    
}

function remove_class_num() {
    $('#video_player').removeAttr('class_num')
}

function is_video_active() {
    return $('#video_player').hasClass('active')
}

function record_stop_video() {
    $('#video_player').removeClass('active')
}

function record_start_video() {
    $('#video_player').addClass('active')
}

function clear_video_classes() {
    $('#video_player_area').removeClass('light_on')
    $('#video_player_area').removeClass('light_off')
}

function stop_video() {
    $('#video_player').get(0).pause()
}



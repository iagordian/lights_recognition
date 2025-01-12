

function start_demonstration() {

    if ($(this).hasClass('active_btn')) {
        return
    }

    record_stop_video()
    clear_video_player_sourses()
    clear_video_classes()

    url = $(this).attr('data-url')

    all_btns_unactive()
    $(this).addClass('active_btn')

    var header = {
        'url': url,
        'type': 'get'
    }
    AjaxQuery.info(header, function(data) {

        stop_video()        
        replace_video_source(data)
        start_video()
        
    })
    
}

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

function get_frame_base64() {

    var canvas = document.getElementById("canvas");
    var video = document.getElementById("video_player");
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;

    canvas
        .getContext("2d")
        .drawImage(video, 0, 0, video.videoWidth, video.videoHeight);

    var frame = canvas.toDataURL().replace('data:image/png;base64,', '')
    
    return frame

}
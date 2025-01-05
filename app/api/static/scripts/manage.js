

function start_demonstration() {

    if ($(this).hasClass('active_btn')) {
        return
    }

    record_stop_video()

    demo_video_num = $(this).attr('dem_num')

    $('.start_denostration_btn').removeClass('active_btn')
    $(this).addClass('active_btn')

    var header = {
        'url': '/get_demo_video',
        'type': 'get',
        'data': {
            demo_video_num: demo_video_num
        }
    }
    AjaxQuery.info(header, function(data) {

        stop_video()        
        replace_video_source(data)
        start_video()
        
    })
    
}

function replace_video_source(data) {

    $('#video_player').empty()
    $('#video_player').append(data)
    $("#video_player")[0].load()
    
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
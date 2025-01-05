


function start_tracking() {

    setInterval(video_tracking, 500)

}


function video_tracking() {

    if (is_video_active()) {

        send_frame()

    } 
}

function send_frame() {
    
    var frame = get_frame_base64()
    
    var header = {
        'url': '/analize_frame',
        'type': 'post',
        'contentType': "application/json; charset=utf-8",
        'data': JSON.stringify({
            'frame_base64': frame
        })
    }
    AjaxQuery.info(header, function(data) {

        
        class_num = data['class_num']
        switch_video_class(class_num)

    })

}



function switch_video_class (class_num) {

    video_classes = {
        0: 'light_off',
        1: 'light_on',
    }

    if (get_actual_video_class_num() != class_num) {

        clear_video_classes()

        $('#video_player').attr('class_num', class_num)

        actual_class = video_classes[class_num]
        $('#video_player_area').addClass(actual_class)

    }

}

function get_actual_video_class_num() {
    return Number($('#video_player').attr('class_num'))
}
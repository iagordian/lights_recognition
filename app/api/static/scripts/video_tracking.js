
const socket = new WebSocket('ws://45.89.188.16:80/analize_frame');

socket.addEventListener('open', (event) => {
    start_video()
    start_tracking()
})

socket.onmessage = (event) => {
    switch_video_class(event.data)
}

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
    if (frame == '') {
        return    
    }
    socket.send(frame)
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
    var class_num = $('#video_player').attr('class_num')

    if (class_num == undefined) {
        return undefined
    }

    return Number(class_num)
}

function get_frame_base64() {

    var canvas = document.getElementById("canvas");
    var video = document.getElementById("video_player");
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;

    canvas
        .getContext("2d")
        .drawImage(video, 0, 0, video.videoWidth, video.videoHeight);

    var frame = canvas.toDataURL()
    var frame = frame.replace('data:', '').replace(',', '').replace('image/png;base64', '')
    
    return frame

}

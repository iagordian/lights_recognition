
var demo_videos = [null, null, null, null, null, null]


function load_demo() {

    $('.btn').each(function() {
        
        if (!$(this).hasClass('active_btn')) {
            
            var demo_video_num = $(this).attr('dem_num')
            var demo_video_ind = get_demo_video_ind(demo_video_num)
            var get_demo_video_url = $(this).attr('data-url')
            var btn = $(this)

            var header = {
                'url': get_demo_video_url,
                'type': 'get'
            }
            AjaxQuery.info(header, function(data) {
        
                btn.addClass('start_denostration_btn')
                demo_videos[demo_video_ind] = data

                var text = btn.attr('text')
                btn.text(text)
                
            })
            

        }

    });

}

function start_demonstration() {

    stop_video()
    record_stop_video()
    clear_video_player_sourses()
    clear_video_classes()
    remove_class_num()

    var demo_video_num = $(this).attr('dem_num')
    var demo_video_ind = get_demo_video_ind(demo_video_num)

    all_btns_unactive()
    $(this).addClass('active_btn')

    var video_data = demo_videos[demo_video_ind]
    replace_video_source(video_data)
    start_video()

}

function get_demo_video_ind(demo_num) {
    return Number(demo_num) - 1
}
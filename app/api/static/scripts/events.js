

var main = (function () {
    
    // Привязка событий
    function _bindHandlers() {
        
        $('#main').on('click.main', '.start_denostration_btn', start_demonstration)
        $('#video_player').on('play', record_start_video)
        $('#video_player').on('pause', record_stop_video)
        $('#video_player').on('ended', record_stop_video)

        start_tracking()

    }

   // Инициализация приложения
   function init() {
     _bindHandlers();
   }

   // Возвращаем наружу
   return {
     init: init
   }

})();

$(document).ready(main.init);
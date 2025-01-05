'use strict';

var jsonData = (function () {

  // Запрос ресурсов
  // Возвращаем объект - html: текст html
  function getJSON(header) {
    return $.ajax(
      header
    ).done(function (data) {
      return data
    }).fail(function (data) {
      //show_error('Предупреждение', data['text_error']);
    });
  }

  // Возврат
  return {
    info: getJSON
  }

})();

var AjaxQueryBase = (function () {

  // Запрос ресурсов
  // Возвращаем объект - html: текст html
  function getJSON(header) {
    return $.ajax(
      header
    ).done(function (data) {
      return data
    })
  }

  // Возврат
  return {
    info: getJSON
  }
})();

var AjaxQuery = (function () {

  function getJSON(header, done_func) {
    return AjaxQueryBase.info(header).done(function(data) {
          done_func(data)
    })
  }

  // Возврат
  return {
    info: getJSON
  }

})();
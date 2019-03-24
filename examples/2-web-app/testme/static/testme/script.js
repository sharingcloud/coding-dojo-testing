/* Script */

function clickme(url) {
  var csrftoken = $("input[name=csrfmiddlewaretoken]").val()
  var $counter = $(".counter");

  $.ajax({
    url: url,
    method: 'POST',
    headers: {
      'X-CSRFToken': csrftoken,
    }
  })
    .done(function (data) {
      $counter.text(data.clicks + " click(s)")
    })
    .fail(function (xhr) {
      console.error("ERROR")
      console.error(xhr)
    })
}

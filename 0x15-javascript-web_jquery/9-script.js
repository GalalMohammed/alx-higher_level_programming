$(document).ready(function () {
  $.ajax({
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    success: function (translation) {
	    $('#hello').text(translation.hello);
    }
  });
});

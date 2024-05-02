$(document).ready(function () {
	// Fetch data from the URL
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data) {
	  // Display the translation of "hello" in the <div> with id hello
    $('DIV#hello').text(data.hello);
  });
});

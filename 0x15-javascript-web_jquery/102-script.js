$(document).ready(function () {
	// Event listener for clicks on the button with id btn_translate
  $('INPUT#btn_translate').click(function () {
	  // Get the language code entered by the user
    const languageCode = $('INPUT#language_code').val();

	  // Fetch translation from the API
    $.get(
      'https://www.fourtonfish.com/hellosalut/hello/?lang=' + languageCode,
      function (data) {
	      // Display the translation of "Hello" in the <div> with id hello
        $('DIV#hello').text(data.hello);
      }
    );
  });
});

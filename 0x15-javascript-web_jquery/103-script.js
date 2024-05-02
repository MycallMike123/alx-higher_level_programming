$(document).ready(function () {
	// Event listener for clicks on the button with id btn_translate
  function fetchTranslation() {
	  // Fetch translation from the API
    const languageCode = $('#language_code').val();
    $.get(
      `https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`,
      function (data) {
	      // Display the translation of "Hello" in the <div> with id hello
        $('#hello').text(data.hello);
      }
    );
  }

  $('#btn_translate').click(fetchTranslation);

  $('#language_code').keypress(function (event) {
    if (event.which === 13) {
      fetchTranslation();
    }
  });
});

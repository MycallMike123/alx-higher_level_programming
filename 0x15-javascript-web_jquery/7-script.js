$(document).ready(function () {
  // Fetch data from the URL
  $.get(
    'https://swapi-api.alx-tools.com/api/people/5/?format=json',
    function (data) {
	    // Extract the character name from the fetched data
      $('#character').text(data.name);
    });
});

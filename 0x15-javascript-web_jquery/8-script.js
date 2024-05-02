$(document).ready(function () {
	// Fetch data from the URL
  $.get(
    'https://swapi-api.alx-tools.com/api/films/?format=json',
    function (data) {
	    // Loop through each movie and append its title to the <ul> element
      $.each(data.results, function (index, movie) {
        $('UL#list_movies').append('<li>' + movie.title + '</li>');
      });
    });
});

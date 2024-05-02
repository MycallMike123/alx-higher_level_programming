$(document).ready(function () {
	// Event listener for clicks on the div with id update_header
  $('div#update_header').click(function () {
	  // Select the <header> element using jQuery and update its text
    $('HEADER').text('New Header!!!');
  });
});

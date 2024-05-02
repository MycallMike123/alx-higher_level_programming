$(document).ready(function (){
  // Ensure that code is executed only when document is fully loaded
  $('DIV#toggle_header').click(function () {
	  // Toggle the class between red and green
    $('header').toggleClass('red green');
  });
});

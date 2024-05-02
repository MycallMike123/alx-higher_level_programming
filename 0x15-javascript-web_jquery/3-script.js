$(document).ready(function(){
  // Event listener for clicks on the div with id red_header
  $('div#red_header').click(function(){
    // Add the class 'red' to the <header> element
    $('header').addClass('red');
  });
});

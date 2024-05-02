$(document).ready(function () {
	// Event listener for clicks on the div with id add_item
  $('DIV#add_item').click(function () {
	  // Create a new <li> element with text "Item"
    $('UL.my_list').append('<li>Item</li>');
  });
});

$(document).ready(function () {
	// Event listener for clicks on the div with id add_item
  $('#add_item').click(function () {
	  // Append the new <li> element to the UL with class my_list
    $('UL.my_list').append('<li>Item</li>');
  });
  $('#remove_item').click(function () {
	  // Event listener for clicks on the div with id remove_item
    $('UL.my_list li:last-child').remove();
  });
  $('#clear_list').click(function () {
	  // Remove all <li> elements from the UL with class my_list
    $('UL.my_list').empty();
  });
});

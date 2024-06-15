// Add a <li> element to a list when a user clicks on DIV#add_item
// tag

$(document).ready(() => {
	$('DIV#add_item').click(() => {
		$('UL.my_list').append('<li>Item</li>');
	});
});

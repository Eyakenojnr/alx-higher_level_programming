// Add, remove, and clear `LI` elements from a list when user clicks:
//
//	DIV#add_item ~> a new element is added to the list
//	DIV#remove_item ~> last element is removed
// 	DIV#clear_list ~> all elments of the list are removed

$(document).ready(() => {
	$('DIV#add_item').click(() => {
		$('UL.my_list').append('<li>Item</li>');
	});

	$('DIV#remove_item').click(() => {
		$('UL.my_list li').last().remove();
	});

	$('DIV#clear_list').click(() => {
		$('UL.my_list').empty();
	});
});

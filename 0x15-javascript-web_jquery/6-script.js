// Update text of the <header> element to "New Header!!!" when a user
// clicks on DIV#update_header

$(document).ready(() => {
	$('DIV#update_header').click(() => {
		$('header').text('New Header!!!');
	});
});

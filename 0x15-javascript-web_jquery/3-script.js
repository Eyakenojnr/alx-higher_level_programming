// Add class `red` to <header> element when user clicks on 
// DIV#red_header tag

$(document).ready(() => {
	$('DIV#red_header').click(() => {
		$('header').addClass('red');
	});
});

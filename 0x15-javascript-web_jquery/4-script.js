// Toggles the class of <header> element when user clicks on the
// DIV#toggle_header tag

$(document).ready(() => {
	$('DIV#toggle_header').click(() => {
		if ($('header').hasClass('red')) {
			$('header').removeClass('red');
			$('header').addClass('green');
		} else {
			$('header').removeClass('green');
			$('header').addClass('red');
		}
	});
});

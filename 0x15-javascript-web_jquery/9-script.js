// Fetch and display from url the value of `hello` from that fetch in
// the HTML tag DIV#hello

const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

$(document).ready(() => {
	$.get(url, (data, textStatus) => {
		$('DIV#hello').text(data.hello);
	});
});

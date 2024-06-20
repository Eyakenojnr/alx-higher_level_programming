// Fetch and print how to say "Hello" depending on the language

$(document).ready(() => {
	$('INPUT#btn_translate').click(() => {
		$('DIV#hello').empty(); // If any, remove previous output

		const url = 'https://hellosalut.stefanbohacek.dev/hello/';
		const langCode = $('INPUT#language_code').val();

		$.get(`${url}?lang=${langCode}`, (data, textStatus) => {
			data = JSON.parse(); // parse the response
			$('DIV#hello').text(data.hello);
		});
	});
});

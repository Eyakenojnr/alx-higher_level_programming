// Fetch and print how to say "Hello" depending on the language
// The transltion is fetched when the user clicks on 
// 	`INPUT#btn_translate` OR presses `ENTER` when the focus is on
// 	`INPUT#language_code`

$(document).ready(() => {
	$('INPUT#btn_translate').click(() => {
		translateHello();
	});

	$('INPUT#language_code').keypress((event) => {
		if (event.which === 13) {
			translateHello();
		}
	});

	function translateHello() {
		$('DIV#hello').empty(); // if any, remove previous output

		const url = 'https://www.fourtonfish.com/hellosalut/hello/';
		const langCode = $('INPUT#language_code').val();

		$.get(`${url}?lang=${langCode}`, (data, textStatus) => {
			data = JSON.parse(data); // parse the response
			$('DIV#hello').text(data.hello);
		});
	}
});

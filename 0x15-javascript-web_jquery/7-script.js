// Fetch a character name from URL and display in DIV#characater tag

const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json'

$(document).ready(() => {
	$.get(url, (data, textStatus) => {
		$('DIV#character').text(data.name);
	});
});

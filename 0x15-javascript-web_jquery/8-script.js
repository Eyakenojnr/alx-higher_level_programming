// Fetch and list title of all movies from URL in the UL#list_movies
// tag

const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';

$(document).ready(() => {
	$.get(url, (data, textStatus) => {
		for (const movie of data.results) {
			$('UL#list_movies').append(`<li>${movie.title}</li>`);
		}
	});
});

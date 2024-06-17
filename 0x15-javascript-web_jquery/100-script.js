// Update text color of <header> element to red without using jQuery
// API
// N/B:: The script is imported from the <head> tag, not at the end
// 	of the HTML

document.addEventListener('DOMContentLoaded', () => {
	const headerElement = document.querySelector('header');
	headerElement.style.color = '#FF0000';
});

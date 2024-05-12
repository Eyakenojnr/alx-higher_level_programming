#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movieId}`;

// Two requests are made; First, to get the movie characters which
// are all urls pointing to another JSON data in which the character
// is contained in 'name'. The second GET request requests for this
// data
request(url, (err, response, body) => {
  if (!err && response.statusCode === 200) {
    const movieData = JSON.parse(body);
    const characters = movieData.characters;

    characters.forEach((characterUrl) => {
      request(characterUrl, (err, response, body) => {
        if (!err && response.statusCode === 200) {
          const characterData = JSON.parse(body);
          console.log(characterData.name);
        } else {
          console.error('An error occurred while fetching character data.');
        }
      });
    });
  } else {
    console.error('An error occured while fetching movie data.');
  }
});

#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
  } else if (response.statusCode === 200) {
    const films = JSON.parse(body).results;
    let count = 0;

    // Iterate through films
    for (const filmIndex in films) {
      const filmChars = films[filmIndex].characters;
      // Iterate through characters of each film
      for (const charsIndex in filmChars) {
        // If selected film includes character ID 18, increment counter
        if (filmChars[charsIndex].includes('18')) {
          count++;
        }
      }
    }

    console.log(count);
  } else {
    console.error('An error occured. Status code:', response.statusCode);
  }
});

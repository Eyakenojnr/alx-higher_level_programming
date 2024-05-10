#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const id = 18

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
  } else if (response.statusCode === 200) {
    const films = JSON.parse(body);
    let count = 0;

    films['results'].forEach(film => {
      if (film['characters'].includes(`https://swapi-api.alx-tools.com/api/people/${id}/`)) {
        count++;
      }
    });

    console.log(count);
  } else {
    console.error('An error occured. Status code:', response.statusCode);
  }
});

#!/usr/bin/node

const request = require('request');
const episodeNum = process.argv[2];

request(`https://swapi-api.hbtn.io/api/films/${episodeNum}/`, (err, response, body) => {
  if (err) {
    console.error(err);
  } else if (response.statusCode === 200) {
    const data = JSON.parse(body);
    console.log(data.title);
  } else {
    console.error('Error code:', response.statusCode);
  }
});

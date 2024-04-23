#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {

    const movieData = JSON.parse(body);

    for (const characterURL of movieData.characters) {
      request.get(characterURL, (error, response, charBody) => {
        if (error) {
          console.log(error);
        } else if (response.statusCode === 200) {
          console.log(JSON.parse(charBody).name);
        }
      });
    }
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});

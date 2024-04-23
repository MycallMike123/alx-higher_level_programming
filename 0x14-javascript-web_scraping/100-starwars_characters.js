#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Error code: ' + response.statusCode);
    return;
  }

  const movieData = JSON.parse(body);

  // Function to fetch character details
  const fetchCharacter = (characterURL) => {
    request.get(characterURL, (err, res, charBody) => {
      if (err) {
        console.error(err);
      } else if (res.statusCode === 200) {
        console.log(JSON.parse(charBody).name);
      } else {
        console.error(`Error fetching character: ${characterURL}, status code: ${res.statusCode}`);
      }
    });
  };

  // Fetch and print character names
  movieData.characters.forEach(characterURL => {
    fetchCharacter(characterURL);
  });
});

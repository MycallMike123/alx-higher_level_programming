#!/usr/bin/node

const request = require('request');

const apiUrl = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(apiUrl, function (error, response, body) {
  if (!error) {
    const characters = JSON.parse(body).characters;

    printCharacters(characters, 0);
  }
});

function printCharacters (characters, index) {
  request.get(characters[index], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);

      if (index + 1 < characters.length) {
        printCharacters(characters, index + 1);
      }
    }
  });
}

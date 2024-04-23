#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
    // If statuscode is 200 (OK), proceed
    const todos = JSON.parse(body);
    const completedTasksByUser = {};

    for (const i in todos) {
      if (todos[i].completed) {
        if (completedTasksByUser[todos[i].userId] === undefined) {
          completedTasksByUser[todos[i].userId] = 1;
        } else {
          completedTasksByUser[todos[i].userId]++;
        }
      }
    }
    // Print users with completed tasks
    console.log(completedTasksByUser);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});

#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  }

  } else if (response.statusCode === 200) {
    const todos = JSON.parse(body);
    const completedTasksByUser = {};

  todos.forEach(todo => {
    if (todo.completed) {
      if (completedTasksByUser[todo.userId]) {
        completedTasksByUser[todo.userId]++;
      } else {
        completedTasksByUser[todo.userId] = 1;
      }
    }
  });

  // Print users with completed tasks
  console.log(completedTasksByUser);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});

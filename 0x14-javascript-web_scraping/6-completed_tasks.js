#!/usr/bin/node
const request = require('request');

// Send a GET request to the specified URL
request.get(process.argv[2], (_err, _response, body) => {
  const completedTasks = {};
  for (const task of JSON.parse(body)) {
    if (task.completed) {
      if (completedTasks[task.userId]) {
        completedTasks[task.userId] += 1;
      } else {
        completedTasks[task.userId] = 1;
      }
    }
  }
  console.log(completedTasks);
});

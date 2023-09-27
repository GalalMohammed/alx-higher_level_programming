#!/usr/bin/node
const request = require('request');

// Send a GET request to the specified URL
request.get(process.argv[2], (_err, _response, body) => {
  const completed_tasks = {};
  for (task of JSON.parse(body)) {
    if (task.completed) {
      if (completed_tasks[task.userId]) {
        completed_tasks[task.userId] += 1;
      } else {
        completed_tasks[task.userId] = 1;
      }
    }
  }
  console.log(completed_tasks);
});

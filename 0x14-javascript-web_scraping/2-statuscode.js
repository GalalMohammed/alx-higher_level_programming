#!/usr/bin/node
const request = require('request');

// Send a GET request to the specified URL
request.get(process.argv[2], (_err, response) => {
  console.log('code: ' + response.statusCode);
});

#!/usr/bin/node
const fs = require('fs');
const request = require('request');

// Send a GET request to the specified URL
request.get(process.argv[2], (_err, _response, body) => {
  // Write the body to the file asynchronously in utf-8 encoding
  fs.writeFile(process.argv[3], body, 'utf-8', (_err) => {});
});

#!/usr/bin/node
const request = require('request');

// Send a GET request to Star wars API
request.get(process.argv[2], (_err, _response, body) => {
  let count = 0;
  for (const i of JSON.parse(body).results) {
    for (const j of i.characters) {
      if (j.includes('18')) { count += 1; }
    }
  }
  console.log(count);
});

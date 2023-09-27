#!/usr/bin/node
const fs = require('fs');

// Write the string to the file asynchronously in utf-8 encoding
fs.writeFile(process.argv[2], process.argv[3] + '\n', 'utf-8', (err) => {
  if (err) {
    console.log(err);
  }
});

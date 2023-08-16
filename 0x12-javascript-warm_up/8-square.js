#!/usr/bin/node
let line;
if (parseInt(process.argv[2])) {
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    line = '';
    for (let j = 0; j < parseInt(process.argv[2]); j++) { line += 'X'; }
    console.log(line);
  }
} else { console.log('Missing size'); }

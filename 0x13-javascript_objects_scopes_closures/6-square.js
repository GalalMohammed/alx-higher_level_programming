#!/usr/bin/node
const _Square = require('./5-square');
module.exports = class Square extends _Square {
  charPrint (c) {
    if (c) {
      let line;
      for (let i = 0; i < this.height; i++) {
        line = '';
        for (let j = 0; j < this.width; j++) { line += c; }
        console.log(line);
      }
    } else { super.print(); }
  }
};

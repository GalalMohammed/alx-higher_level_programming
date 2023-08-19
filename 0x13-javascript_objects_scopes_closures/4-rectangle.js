#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) { this.width = w; this.height = h; }
  }

  print () {
    let line;
    for (let i = 0; i < this.height; i++) {
      line = '';
      for (let j = 0; j < this.width; j++) { line += 'X'; }
      console.log(line);
    }
  }

  rotate () {
    const temp = this.height ^ this.width;
    this.height = temp ^ this.height;
    this.width = temp ^ this.width;
  }

  double () {
    this.height *= 2;
    this.width *= 2;
  }
};

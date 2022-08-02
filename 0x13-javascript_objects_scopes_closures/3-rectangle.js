#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const chr = 'X';
    let line = '';

    for (let j = 0; j < this.width; j++) {
      line = line + chr;
    }
    for (let i = 0; i < this.height; i++) {
      console.log(line);
    }
  }
};

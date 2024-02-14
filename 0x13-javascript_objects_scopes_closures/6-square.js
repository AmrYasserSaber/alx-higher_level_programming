#!/usr/bin/node
const Squarep = require('./5-square');

class Square extends Squarep {
  charPrint (c = 'X') {
    for (let i = 0; i < this.height; i++) { console.log(c.repeat(this.width)); }
  }
}

module.exports = Square;

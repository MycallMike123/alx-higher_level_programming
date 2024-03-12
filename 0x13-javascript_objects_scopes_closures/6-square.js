#!/usr/bin/node

const SquarePrint = require('./5-square');

class Square extends SquarePrint {
	charPrint (c) {
		if (c === undefined) {
			c = 'X';
		}

		for (let a = 0; a < this.height; a++) {
			let tat = '';

			for (let b = 0; b < this.width; b++) {
				tat += c;
			}

			console.log(tat);
		}
	}
}

module.exports = Square;

#!/usr/bin/node

class Rectangle {
	constructor (w, h) {
		if ((w > 0) && (h > 0)) {
			this.width = w;
			this.height = h;
		}
	}

	print () {
		for (let a = 0; a < this.height; a++) {
			let rep = '';
			for (let b = 0; b < this.width; b++) {
				rep += 'X';
			}
			console.log(rep);
		}
	}

	rotate () {
		const tat = this.width;
		this.width = this.height;
		this.height = tat;
	}

	double () {
		this.width *= 2;
		this.height *= 2;
	}
}
  

module.exports = Rectangle;

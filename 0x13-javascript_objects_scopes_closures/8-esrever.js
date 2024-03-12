#!/usr/bin/node

exports.esrever = function (list) {
	let len = list.length - 1;
	let a = 0;

	while ((len - a) > 0) {
		const tat = list[len];
		list[len] = list[a];
		list[a] = tat;
		a++;
		len--;
	}

	return list;
};

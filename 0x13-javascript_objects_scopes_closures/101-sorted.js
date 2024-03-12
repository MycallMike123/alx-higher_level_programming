#!/usr/bin/node

const dict = require('./101-data').dict;

const total = Object.entries(dict);
const valueS = Object.values(dict);
const uniqValues = [...new Set(valueS)];
const newDictionary = {};
for (const a in uniqValues) {
	const list = [];
	for (const b in total) {
		if (total[b][1] === uniqValues[a]) {
			list.unshift(total[b][0]);
		}
	}

	newDictionary[uniqValues[a]] = list;
}

console.log(newDictionary);

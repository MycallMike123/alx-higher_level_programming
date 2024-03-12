#!/usr/bin/node

const fs = require('fs');

const arg = process.argv[2]
const firArg =
	fs.readFileSync(arg).toString();
const secArg =
	fs.readFileSync(process.argv[3]).toString();
fs.writeFileSync(process.argv[4], firArg + secArg);

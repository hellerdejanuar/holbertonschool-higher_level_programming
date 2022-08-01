#!/usr/bin/node
const n = parseInt(process.argv[2]);
const chr = 'X';
let line = '';

if (isNaN(n)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      line = line + chr;
    }
    console.log(line);
    line = '';
  }
}

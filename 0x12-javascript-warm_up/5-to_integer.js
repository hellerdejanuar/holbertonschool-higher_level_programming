#!/usr/bin/node

const num = parseInt(process.argv[2]);
const txt = 'My number: ';
const errTxt = 'Not a number';

if (isNaN(num)) {
  console.log(errTxt);
} else {
  console.log(txt + num);
}

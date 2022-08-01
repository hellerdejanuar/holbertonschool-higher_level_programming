#!/usr/bin/node

arg0 = 'undefined'
arg1 = 'undefined'
if (process.argv[2]) {
  arg0 = process.argv[2];
}
if (process.argv[3]) {
  arg1 = process.argv[3];
}

console.log(`${arg0} is ${arg1}`);

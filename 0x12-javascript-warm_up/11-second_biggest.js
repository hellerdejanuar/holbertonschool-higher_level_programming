#!/usr/bin/node
const array = process.argv.slice(2);
if (array.length <= 1) {
  console.log(0)
}
for (let i = 0; i < array.length; i++) {
  let parsedInt = parseInt(array[i]);
  if (isNaN(parsedInt)) {
    console.log(0)
    return;
  }
  else {
    array[i] = parseInt(array[i])
  }
}
console.log(array.sort()[(array.length - 1)])

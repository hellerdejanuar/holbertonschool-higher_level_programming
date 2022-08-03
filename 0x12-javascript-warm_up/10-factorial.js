#!/usr/bin/node
function factorial (n, res) {
  if (n !== 0) {
    factorial(n - 1, res);
  }
  return (res * n);
}

const n = parseInt(process.argv[2]);
console.log(factorial(n, 1));

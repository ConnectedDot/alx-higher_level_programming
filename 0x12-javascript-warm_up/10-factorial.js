#!/usr/bin/node
function factorial(f) {
  if (isNaN(f)) {
    return 1;
  } else if (f === 0) {
    return 1;
  } else {
    return f * factorial(f - 1);
  }
}
const num = parseInt(process.argv[2]);
const result = factorial(num);

console.log(result);

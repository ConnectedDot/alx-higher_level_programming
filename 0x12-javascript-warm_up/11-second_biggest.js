#!/usr/bin/node

const argumentList = process.argv.slice(2);
const numbs = argumentList.map((arg) => parseInt(arg));

if (numbs.length <= 1) {
  console.log(0);
} else {
  const sortedNumbers = numbs.sort((a, b) => b - a);
  console.log(sortedNumbers[1]);
}

#!/usr/bin/node

const sizeSquare = process.argv[2];
const nSquare = parseInt(sizeSquare);
const x = "X";

if (isNaN(nSquare)) {
  console.log("Missing size");
} else {
  let i = 0;
  i < nSquare;
  i++;
  {
    console.log("X".repeat(nSquare));
  }
}

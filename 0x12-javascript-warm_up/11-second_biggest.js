#!/usr/bin/node
const array = process.argv;
let low = 0;
let high = 0;

if (array.length === 2 || array.length === 3) {
  console.log(0);
} else {
  for (let i = 0; i <= array.length; i++) {
    if (Number(array[i]) > high) {
      low = high;
      high = Number(array[i]);
    }
  }
  console.log(low);
}

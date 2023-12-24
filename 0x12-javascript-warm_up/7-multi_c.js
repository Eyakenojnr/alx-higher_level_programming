#!/usr/bin/node
const input = process.argv[2];

if (isNaN(input)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 1; i <= input; i++) {
    console.log('C is fun');
  }
}

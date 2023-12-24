#!/usr/bin/node
const input = process.argv[2];

if (isNaN(input)) {
  console.log('Missing size');
} else {
  for (let i = 1; i <= input; i++) {
    let output = '';
    for (let j = 1; i <= input; j++) {
      output += 'X';
    }
    console.log(output);
  }
}

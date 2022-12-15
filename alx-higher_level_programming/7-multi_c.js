#!/usr/bin/node
if (process.argv.length === 2 || !parseInt(process.argv[2]) || process.argv[2] === undefined || process.argv[2] === undefined) {
  console.log('Missing number of occurrences');
} else {
  let myCounter = process.argv[2];
  while (parseInt(myCounter) !== 0) {
    console.log('C is fun');
    myCounter--;
  }
}

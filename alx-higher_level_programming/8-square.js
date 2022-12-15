#!/usr/bin/node
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  const myCounter = parseInt(process.argv[2]);
  let i = 0;
  for (i; i < myCounter; i++) {
    console.log('X'.repeat(myCounter));
  }
}

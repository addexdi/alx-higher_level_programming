#!/usr/bin/node
function add (a, b) {
  const myResult = a + b;
  console.log(myResult);
}

add(Number(process.argv[2]), Number(process.argv[3]));

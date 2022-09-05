#!/usr/bin/node
const Args = process.argv[2];
if (Args === undefined) {
  console.log('No argument');
} else {
  console.log(Args);
}

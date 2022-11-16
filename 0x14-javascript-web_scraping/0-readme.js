#!/usr/bin/node
const file = process.argv[2];
const fs = require('fs');

fs.readfile(file, 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log(data);
});

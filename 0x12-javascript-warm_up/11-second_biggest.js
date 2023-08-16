#!/usr/bin/node
if (process.argv.length < 4) { console.log(0); } else {
  const arr = []; let max; let max2;
  for (let i = 0; i < process.argv.length - 2; i++) { arr[i] = process.argv[i + 2]; }
  if (arr[0] > arr[1]) {
    max = arr[0];
    max2 = arr[1];
  } else {
    max = arr[1];
    max2 = arr[0];
  }
  for (let i = 2; i < arr.length; i++) {
    if (arr[i] > max) {
      max2 = max;
      max = arr[i];
    } else if (arr[i] > max2) { max2 = arr[i]; }
  }
  console.log(max2);
}

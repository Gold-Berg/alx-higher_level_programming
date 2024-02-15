#!/usr/bin/node
function factorial (number) {
  if (number === 0) {
    return (1);
  } else {
    return (factorial(number - 1) * number);
  }
}
const num = parseInt(process.argv[2]);
if (num) {
  const result = factorial(num);
  console.log(result);
} else {
  console.log(1);
}

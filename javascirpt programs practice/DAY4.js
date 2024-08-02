// prototypal inheritance
console.log(Array.prototype);

let myArray = ["Hi", 1, 3];

console.log(Object.getPrototypeOf(myArray));

let sportsArray = new Array("football", "VolleyBAll");

console.log(Object.getPrototypeOf(sportsArray));
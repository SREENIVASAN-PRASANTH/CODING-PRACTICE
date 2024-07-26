// 1. Spread Operator
// 1.1 Spread Operator with Arrays
let arr1 = [1, 2, 3, 4];
let arr2 = [2, 3, 4, 5];
console.log(...arr1, ...arr2);

// 1.1.1 Creating a Copy
let arr3 = [...arr1];
console.log(arr3);

// 1.1.2 Concatenation
let arr4 = [...arr1, ...arr2];
console.log(arr4);

// 1.2 Spread Operator with Objects
let obj1 = { name: "Prasanth" };
console.log({ ...obj1 });
let obj2 = { age: 23, ...obj1 };
console.log(obj2);

// 2. Rest Parameter
function add(...args) {
  let result = args[0];
  console.log(result);
}
add(1, 2, 3, 4, 5, 6, 7);
// 2.1 Destructuring arrays and objects with Rest Parameter Syntax
// 2.1.1 Arrays
let [a, b, ...args] = [1, 2, 4, 5, 6];
console.log(a);
console.log(b);
console.log(args);

// 2.1.2 Objects
let { firstName, lastName, ...args1 } = {
  firstName: "Prasanth",
  lastName: "S",
  age: "21",
  height: 6.5,
};
console.log(firstName);
console.log(lastName);
console.log(args1);

// 3. Functions
// 3.1 Default Parameters
function sum(a = 3, b = 5) {
  console.log(a + b);
}
sum(6, 7);
sum(2);
sum(2, 1, 2);
sum("a", "b");

// 4. Template Literals (Template Strings)
let fullName = "Prasanth";
console.log(`hi ${fullName}`);
a = 5;
b = 6;
console.log(`a + b = ${a + b}`);

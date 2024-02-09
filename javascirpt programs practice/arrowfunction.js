let sum = (a,b) => a + b;
console.log(sum(1,2));

let sum2 = (a,b) => {
    return a + b;
}
console.log(sum2(2,3));

let isEqual = (a,b) => {
    return a === b;
}

console.log(isEqual(2,2));

let isEqual2 = (a,b) => a === b;
console.log(isEqual2(1,2));

let greet = (name) => {
    console.log(`Hi ${name}!`);
}
greet("Prasanth");

let greet2 = (name) => `Hi ${name} how are you?`;
console.log(greet2("Jeniper"));

let square = (n) => n * n;
console.log(square(2));

let square2 = n => n * n;
console.log(square2(3));

let sayHi = () => "Hello!";
console.log(sayHi());

let createObject = name => {
    return {
        firstName : name
    }
}
console.log(createObject("Prasanth"));

let createObject2 = name => ({firstName : name});
console.log(createObject2("Santhi"));

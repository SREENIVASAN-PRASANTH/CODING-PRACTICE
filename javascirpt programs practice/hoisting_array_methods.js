//practicing HOISTING concept
/*
1)calling function before declaration for normal function no error

printName("prasanth");
function printName(name){
    console.log(name);
}

2)for function expression it throws error

printName("Prasanth");
let printName = function (name){
    console.log(name);
}


3)For arrow function also it throws error

printAnotherName("Rahul");
let printAnotherName = (anotherName) => {
    console.log(anotherName)
}


4) accesing value of a variable globally

let name = "Prasanth";
printName();
function printName(){
    console.log(name);
}



5)accesing local value of a variable

function printName(){
    let name = "Prasanth";
}

printName();
console.log(name);


6)Using the map() function

const numbers = [1,2,3,4,5];
let square = numbers.map((number) => number * number);
console.log(square);

6)Using forEach()

const arr = [1,2,3,4,5]
let count = 0;
arr.forEach((val) => {
    count = count + val;
    console.log(count);
})

7)Using reduce()

const arr = [3, 4, 5, 6];
let b = arr.reduce((accumulator, element) => accumulator + element);

console.log(b)


8)Using filter()

const arr = [7,8,9,0]
let result = arr.filter((number) => number <= 7);

console.log(result);

9)Using some() & every()

let arr = ["a", "b", "c"];
let result = arr.every((val) => val == "a");
console.log(result);

let result2 = arr.some((val) => val === "b");
console.log(result2);

10)Using reverse() to reverse values of a array

let arr = [1,2,3,4,5];
let res = arr.reverse();

console.log(res);

11)Using the flat()

let arr2 = [1,2,[[[[[4]]]]]]
console.log(arr2.flat(3));
*/
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
*/


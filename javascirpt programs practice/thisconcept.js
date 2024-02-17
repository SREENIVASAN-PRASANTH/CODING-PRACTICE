//object method this

let car = {
    color : "BLue",
    brand : "Audi",
    start : function(){
        console.log(this);
    }
}

car.start();

//this inside regular function refer window object

function start(){
    console.log(this);
}

start();

//callback function will be defined only when the car.start() is called.

let car1 = {
    color: "blue",
    brand : "Benz",
    start : function(){
        setTimeout(function(){
            console.log("Hi")
        },1000);
    }
};

car1.start();

//in console we basically have window context
//In this variable we have window
console.log(this);

//now when we try to call a function in an object it will refer to the object itself example given below

let car3 = {
    color : "Violet",
    brand : "TATA",
    start : function(){
        console.log(this);
    }
};

car3.start();

//when this is defined inside object using arrow function then it will refer to window object context.
let car4 = {
    color : "green",
    brand : "lambhorgini",
    start : () => {
        console.log(this);
    }
}

car.start()

//arrow function inside call back function

let car5 = {
    color : "green",
    brand : "Mclaran",
    start : function(){
        setTimeout(() => {
            console.log(this);
        },1000);
    }
}

car5.start();

//arrow function inside call function using findIndex method

let cars = ["Tata","Maruti","Tesla"];

let car6 = {
    color : "blue",
    brand : "Tata",
    start : function(){
        let audiIndex = cars.findIndex(
            (car) => console.log(this)
        );
    }
}

car6.start();

//In constructor this refers to instance object

function Car(color, brand){
    this.color = color;
    this.brand = brand;
    this.start = function(){
        console.log(this);
    }
}

let car7 = new Car("Red","Maruti");
car7.start();

//Arrow function inherits this from the context in which the code is defined
function Car1(color, brand){
    this.color = color;
    this.brand = brand;
    this.start = () => {
        console.log(this);
    }
}

let car8 = new Car1("white","Tata");
car8.start();

//Mutable and Immutable values

//primitive types are immutable for example numbers, boolean, string etc.
//objects are mutable for example arrays, object, functions etc.

let x = 5;
let y = x;
console.log(x);
console.log(y);
y = 10;
console.log(y);

//mutable
let a = {value : 5};
let b = a;
b.value = 10; // here we are just updating the values
console.log(a);
console.log(b);

let z = {value : 20};
b = z;
console.log(a);
console.log(b); // here we are totally refering to a new object

//variable declaration let example
//initialize is not mandatory
let v;
v = 10;
console.log(v);
v = 15;
console.log(v);

//variable declaration const
//initialization is mandatory
const d = 12;
console.log(d);

//mutating the object property

const Car12 = {
    color : "blue",
    brand : "Audi"
};

Car12.color = "Red"
console.log(Car12);

//we cant reassign a new object to the variable
Car12 = {}; // this line will raise error

let car1 = {
    color : "red",
    brand : "maruti",
    start : ()=>{
        console.log("Started");
    }
};

let car2 = {
    color : "blue",
    brand : "mahendra",
    start : ()=>{
        console.log("Started");
    }
};

let car3 = {
    color : "yellow",
    brand : "BMW",
    start : ()=>{
        console.log("Started");
    }
};


console.log(car1);
console.log(car2);
console.log(car3);


//factory function

function createCar(color,brand){
    return {
        color : color,
        brand : brand,
        start : ()=>{
            console.log("START!!");
        }
    }
}

let car4 = createCar("blue","BMW");

console.log(car4);

function createCar2(color,brand){
    return {
        color,
        brand,
        start(){
            console.log("Start");
        }
    }
};

let car5 = createCar2("white","hyundai");
console.log(car5);


//constructor function

function Car(color,brand){
    this.color = color;
    this.brand = brand;
    this.start = ()=>{
        console.log("Start");
    }
}

console.log(car1.constructor);

console.log(typeof(Car));
console.log(Car.name);
console.log(Car.length);

let car6 = new Car("pink","Nano");
console.log(car6);
car6.start();


//built in constructor functions.

//date and time

let now = new Date();

console.log(now);
console.log(typeof(now));

//string format
let date = new Date("2024-06-11");
console.log(date);


//number format
let date1 = new Date(2003,6,11,9,56,12,0);
console.log(date1);


//Instance method

console.log(date1.getFullYear());
console.log(date1.getMonth());

date1.setFullYear(2024);
console.log(date1);
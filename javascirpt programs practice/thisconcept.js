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
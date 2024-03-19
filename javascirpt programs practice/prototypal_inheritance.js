/*Diferent ways to declare an
   Array */

let myArray = ["1", 1, 2 , 3];
myArray.push("3")
console.log(myArray.length);

let myArray2 = new Array(1,2,3,4);
console.log(myArray2);


//prototype property is a shared resource among all instances that have been created using a constructor function

console.log(Array.prototype);

//accesing prototype through instance

console.log(Object.getPrototypeOf(myArray2));

//prototype in multiple instances

let sportsArray = new Array("messi","dhoni");

console.log(Object.getPrototypeOf(sportsArray));

//Prototypal inheritance
//on calling the new() operator, all the properties defined on the prototype will become accesible to the instance objects. This process is prototypal inheritance.

//Buil in function constructor
//let myFunction = new Function("para1,para2....",`code`);

let Car = new Function("color,brand",`
this.color = color;
this.brand = brand;
this.start = () =>{
    console.log("Started");
}`);

console.log(Function.prototype);

//MODERN way of writing

function Car2(color,brand){
    this.color = color;
    this.brand = brand;
    this.start = ()=>{
        console.log("Started, The car is ready to drive.");
    };
};

console.log(Object.getPrototypeOf(Car2));

let carInstance = new Car2("blue","audi");
console.log(carInstance);
carInstance.start();

console.log(Car2.prototype);

console.log(Object.getPrototypeOf(carInstance));

//adding properties and methods to prototype
function person(firstName,lastName){
    this.firstName = firstName;
    this.lastName = lastName;
}

let prasanth = new person("Prasanth","S");
console.log(prasanth);

let praveen = new person("Praveen", "Kumar");
console.log(praveen);

//instance properties = properties specific to the object eg: gender, yearOFbirth
//prototype properties = properties common among instances eg: calculate age, displayGreetings

person.prototype.displayFullname = ()=>{
    return this.firstName + " " + this.lastName;
}
console.log(Object.getPrototypeOf(prasanth));
console.log(Object.getPrototypeOf(praveen));    
console.log(Object.getPrototypeOf(prasanth) === Object.getPrototypeOf(praveen));

//Instance specific properties

console.log(Object.getOwnPropertyNames(prasanth));






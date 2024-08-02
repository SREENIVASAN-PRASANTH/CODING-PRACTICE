// prototypal inheritance
console.log(Array.prototype);

let myArray = ["Hi", 1, 3];

console.log(Object.getPrototypeOf(myArray));

let sportsArray = new Array("football", "VolleyBAll");

console.log(Object.getPrototypeOf(sportsArray));

// creating a function using constructor
let printAge = new Function(
  "name",
  `this.name = name;
    console.log(this.name);`
);

printAge("Prasanth");

console.log(Object.getPrototypeOf(printAge));

// creating An instance of a function
function getMarks(subject,marks){
    this.subject = subject;
    this.marks = marks;
    this.getMarksResult = function(){
        console.log(`${this.subject} : ${this.marks}`)
    }
}

let person1 = new getMarks("Physics",91);
person1.getMarksResult();

console.log(person1);

console.log(getMarks.prototype);

//adding properties and methods to prototype

function books(name, price){
    this.name = name;
    this.price = price;
}

let book1 = new books("Python",230);
let book2 = new books("Data Structures", 1000);

console.log(book1);
console.log(book2);

books.prototype.calculateDiscount = function(discount){
    return (discount/100) * this.price;
}

console.log(book1.calculateDiscount(20));
console.log(book2.calculateDiscount(100));

// checking prototypes of book1 and book2
console.log(
    Object.getPrototypeOf(book1) === Object.getPrototypeOf(book2)
);

// getting instance properties
console.log(
    Object.getOwnPropertyNames(book1)
);

console.log(
    Object.getOwnPropertyNames(book2)
);
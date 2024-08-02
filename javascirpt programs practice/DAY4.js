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


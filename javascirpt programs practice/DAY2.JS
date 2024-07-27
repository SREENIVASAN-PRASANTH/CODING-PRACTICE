// 1. this
// 1.1 this in Object Methods
let car = {
  name: "Maruti",
  model: "swift dezire",
  start: function () {
    console.log("broommmmm!!");
    console.log(this);
  },
};
car.start();

// 1.2 this in Regular Functions
function horn() {
  console.log("pom pom");
  console.log(this);
}
horn();

// 1.3 this in Arrow Functions
let carOff = () => {
  console.log("clink clink");
  console.log(this);
};

carOff();

// 1.3.1 Object Methods
let bike = {
  name: "Revolt",
  model: "RV400",
  start: () => {
    console.log("tan tan");
    console.log(this);
  },
};
bike.start();

// Arrow Functions with Callbacks
let scooty = {
  name: "Activa",
  model: 1234,
  start: function () {
    console.log("disss diss");
    setTimeout(function () {
      console.log(this);
    }, 1000);
  },
};
scooty.start();
// 1.4 this in Constructor Functions
// 1.4.1 Arrow Functions
// 2. Immutable and Mutable Values
// 2.1 Immutable
// 2.2 Mutable
// 3. Declaring Variables
// 3.1 let
// 3.2 const
// 3.2.1 Mutating Object properties

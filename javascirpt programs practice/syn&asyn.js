//learning about synchronous(code executed one after the other) and asynchronous operations(code doesn't wait for the execution of the before code)
/*
alert("Hi");
alert("Bye");
alert("Hello");
*/

//lets see the example for asynchronous operations

// let url = "https://apis.ccbp.in/jokes/random";

// fetch(url)
//   .then((response) => {
//     return response.json();
//   })

//   .then((jsonData) => {
//     console.log(jsonData);
//   });
// console.log("The fetch has completed");

//  o/p: The fetch has completed
// { value: 'How do you comfort a JavaScript bug? You console it' }

//NOw we  will see about javascript promises:- it is a object that gives the status of asynchronous operations.
let url = "https://apis.ccbp.in/jokes/random";

const promiseResponse = fetch(url);

// promiseResponse
// .then((response) => {
//     console.log(response);
// })
// .catch((error)=>{
//     console.log(error);
// })

promiseResponse
.then((response)=>{
    return response.json();
})
.then((jsonData) =>{
    console.log(jsonData);
})

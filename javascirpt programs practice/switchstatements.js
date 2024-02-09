let day = 5;

switch (day){
    case 0:
        console.log("Sunday");
        break;
    case 1:
        console.log("Monday");
        break;
    case 2:
        console.log("Tuesday");
        break;
        
    case 3:
        console.log("Wednesday");
        break;
    case 4:
        console.log("Thursday");
        break;
    case 5:
        console.log("Friday");
        break;
    case 6:
        console.log("Saturday");
        break;
    default:
        console.log("Wrong Input");
        break;
}

let a = 6;
let b = 9;

let operation = "add";

switch (operation){
    case "add":
        console.log(`a + b = ${a + b}`);
        break;
    
    case "subtraction":
        console.log(`a - b = ${a - b}`);
        break;
    default:
        console.log("Invalid operation");
        break;
}
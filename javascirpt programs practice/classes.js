class bottle{
    constructor(color,type){
        this.color = color;
        this.type = type;
    }

    displayBottleDetails(){
        return this.color + " " + this.type;
    }
}

let steelBottle = new bottle("black","steel");

console.log(steelBottle.displayBottleDetails);//Created a class with a constructor and then created a method in it to display the color and type of bottle

let arr = ["Prasanth", "Mohan"];
function object(name,age){
    this.name = name;
    this.age = age;
    this.getIntro = function(){
        console.log(this.name + " " + this.age);
    }
}

let obj1 = new object("Prasanth",21);
obj1.getIntro();

object.prototype.getName = function(){
    console.log(this.name);
}
obj1.getName();

object.prototype.age = 26;
console.log(obj1.age);



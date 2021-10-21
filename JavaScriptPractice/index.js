// objects in js are like dicts/maps
let person = {
    name: 'David',
    age: 19
};

person.name = 'Jeremiah';
let choice = 'name';
person[choice] = 'Raina';
person.age = 20;

console.log(person);

// arrays are a type of object
let colors = ['red', 'blue'];
colors[3] = 'green';
console.log(colors);
console.log(colors[1]);

// functions are also objects
function greet(name) {
    console.log('Hello ' + name);
}

function square(number) {
    return number * number;
}

greet(person.name);
let number = square(2);
console.log(number);
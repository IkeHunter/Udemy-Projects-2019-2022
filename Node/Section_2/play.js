// Arrow Function

// const functionName = (var1, var2, var3) => {
//     console.log(var1 + var2 + var3)
//     return var1 + var2 + var3
// };

// const functionTwo = (a, b) => a + b;

// // no variables
// const addRandom = () => 1 + 2;

// // object
// const person = {
//     name: 'John Doe', 
//     age: 21,
//     greet() {  // note syntax, not arrow function or traditional function
//         // console.log('Hi, I am ' + this.name);
//     }
// };

// const printName = ({ name }) => {  // object destructuring only takes name from person
//     console.log(name);1
// }

// printName(person)

// const { name, age } = person;
// console.log(name, age)


// // person.greet();

// const hobbies = ['Thing 1', 'Thing 2', 'Thing3']
// const [hobby1, hobby2] = hobbies;
// console.log(hobby1, hobby2);

// for (let hobby of hobbies) {
//     console.log(hobby);
// }

// console.log(hobbies.map(hobby => {
//     return 'Hobby: ' + hobby;
// }));  // transforms array and returns new one

// hobbies.push('Programming');  // can change const variable because var references address of array, address didn't change
// const copiedArray = hobbies.slice();  // copies array
// const copiedArray = [...hobbies];  //... (spread operator) takes all the elements of an array and assigns them to new array (or tuple, object, etc)
// console.log(hobbies)

// const toArray = (...args) => {  // ...args (rest operator) allows any num of arguments
//     return args;
// }

// console.log(toArray(1, 2, 3, 4));

/** ASYNC Code**/

const fetchData = () => {
    const promise = new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve('Done!');
        }, 1500);
    });
    return promise;;
};


setTimeout(() => {
    console.log('Timer is done!');
    fetchData()
        .then(text => {
            console.log(text);
            return fetchData();
        })
        .then(text2 => {
            console.log(text2);
        });
}, 300);

console.log('Hello!');
console.log('Hi!');
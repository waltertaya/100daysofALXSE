const utensils = [];
utensils.push('Dishes', 'Cups', 'Mugs', 'Spoons', 'Cooking stick');
console.log(utensils.length); // Output -> 5

utensils[8] = 'Knife';
console.log(utensils[8]); // Output -> Knife
console.log(Object.keys(utensils)); // Output -> [ '0', '1', '2', '3', '4', '8' ]
console.log(utensils.length); // Output -> 9
console.log(utensils[6]); // Output -> undefined


utensils.length = 12;
console.log(utensils); // Output -> ['Dishes', 'Cups', 'Mugs', 'Spoons', 'Cooking stick', <3 empty items>, 'Knife', <3 empty items>]
console.log(Object.keys(utensils)); // Output -> [ '0', '1', '2', '3', '4', '8' ]
console.log(utensils.length); // Output -> 12
console.log(utensils[10]) // Output -> undefined

// Reducing length - deletes elements
utensils.length = 4;
console.log(utensils); // [ 'Dishes', 'Cups', 'Mugs', 'Spoons' ]
console.log(Object.keys(utensils));  // [ '0', '1', '2', '3' ]

const marks = [23, 34, 12, 50, 22, 47, 49];
const marksPercent = marks.map((mark) => mark * 2);
console.log(marksPercent);

const sum = marksPercent.reduce((mark1, mark2) => mark1 + mark2);
console.log(sum)
console.log(`Average: ${sum / (marks.length)}`)

let newMarks = []
marks.forEach((mark) => {
    newMarks.push(mark * 2)
})
console.log(newMarks)

newMarks.reverse()

console.log(newMarks)
newMarks.sort((a, b) => a - b)
utensils.sort()

console.log(utensils)
console.log(newMarks)

const aboveAvg = newMarks.filter((value) => value >= 50)
console.log(aboveAvg)

// console.log(marks.findIndex())


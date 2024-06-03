# Arrays in JavaScript

- When setting a property on a JavaScript array when the property is a valid array index and that index is outside the current bounds of the array, the engine will update the array's length property accordingly.
- Increasing the length extends the array by adding empty slots without creating any new elements — not even undefined.
- Decreasing the length property does, however, delete elements

## Array methods and empty slots

- Array methods have different behaviors when encountering empty slots in sparse arrays. In general, older methods (e.g. forEach) treat empty slots differently from indices that contain undefined.

- Methods that have special treatment for empty slots include the following: concat(), copyWithin(), every(), filter(), flat(), flatMap(), forEach(), indexOf(), lastIndexOf(), map(), reduce(), reduceRight(), reverse(), slice(), some(), sort(), and splice(). Iteration methods such as forEach don't visit empty slots at all. Other methods, such as concat, copyWithin, etc., preserve empty slots when doing the copying, so in the end the array is still sparse.

## Copying methods and mutating methods

- The following methods create new arrays by accessing this.constructor[Symbol.species] to determine the constructor to use: concat(), filter(), flat(), flatMap(), map(), slice(), and splice() (to construct the array of removed elements that's returned).

- The following methods always create new arrays with the Array base constructor: toReversed(), toSorted(), toSpliced(), and with().

| Mutating method | Non-mutating alternative |
|-----------------|--------------------------|
| copyWithin()    | No one-method alternative|
| fill()          | No one-method alternative|
| pop()           | slice(0,_ -1)            |
| push(v1,_ v2)   | concat([v1, _v2])        |
| reverse()       | toReversed()             |
| shift()         | slice(1)                 |
| sort()          | toSorted()               |
| splice()        | toSpliced()              |
| unshift(v1,_ v2)| toSpliced(0, 0, v1, v2)  |
|                 |                          |

## Author

- **@waltertaya**

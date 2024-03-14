# Modules (CommonJS and ESM)

Node.js supports two module systems: CommonJS and ECMAScript Modules (ESM). Here's a brief explanation of each, along with code snippets for their usage.

## CommonJS

CommonJS is the traditional module system used in Node.js, and it's the default module system for Node.js versions prior to v12. In CommonJS, modules are loaded synchronously, and each module is treated as a separate scope.

### Exporting a Module

To export a function, object, or value from a module, use the `module.exports` object.

```javascript
// math.js
function add(a, b) {
  return a + b;
}

function subtract(a, b) {
  return a - b;
}

module.exports = {
  add,
  subtract,
};
```

### Importing a Module

To import a module in CommonJS, use the `require` function.

```javascript
// app.js
const math = require('./math');

console.log(math.add(2, 3)); // Output: 5
console.log(math.subtract(5, 3)); // Output: 2
```

## ECMAScript Modules (ESM)

ECMAScript Modules (ESM) is the modern module system introduced in ES6 (ES2015). It uses the `import` and `export` syntax and provides better static analysis, improved code optimization, and better support for cyclic dependencies.

Starting from Node.js v12, you can use ESM by adding `"type": "module"` in your `package.json` file or by using the `.mjs` file extension.

### Exporting a Module

To export a function, object, or value from a module, use the `export` keyword.

```javascript
// math.mjs
export function add(a, b) {
  return a + b;
}

export function subtract(a, b) {
  return a - b;
}
```

### Importing a Module

To import a module in ESM, use the `import` keyword.

```javascript
// app.mjs
import { add, subtract } from './math.mjs';

console.log(add(2, 3)); // Output: 5
console.log(subtract(5, 3)); // Output: 2
```

You can also use the following syntax to import everything from a module:

```javascript
import * as math from './math.mjs';

console.log(math.add(2, 3)); // Output: 5
console.log(math.subtract(5, 3)); // Output: 2
```

Note that you need to use the `.mjs` file extension or add `"type": "module"` in your `package.json` file to use ESM in Node.js.

Both CommonJS and ESM have their advantages and use cases. While CommonJS has been the traditional module system in Node.js, ESM is the standard for modern JavaScript development and is recommended for new projects.
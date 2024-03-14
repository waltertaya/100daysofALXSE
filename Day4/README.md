# Creating Custom Modules and the `global` Keyword

In Node.js, you can create your own custom modules to encapsulate and share related functionality across different parts of your application. Additionally, Node.js provides a `global` object that acts as a global namespace for your application.

## Creating Custom Modules

A module in Node.js is simply a reusable JavaScript file. You can create a custom module by defining functions, objects, or classes in a separate file, and then exporting them for use in other parts of your application.

Here's an example of creating a custom module called `logger.js`:

```javascript
// logger.js
function info(message) {
  console.log(`INFO: ${message}`);
}

function error(message) {
  console.error(`ERROR: ${message}`);
}

module.exports = {
  info,
  error,
};
```

To use this custom module in another file, you can import it using the `require` function:

```javascript
// app.js
const logger = require('./logger');

logger.info('Application started');
// Output: INFO: Application started

logger.error('Something went wrong');
// Output: ERROR: Something went wrong
```

You can also export a single function or object directly using `module.exports`:

```javascript
// greet.js
module.exports = function greet(name) {
  console.log(`Hello, ${name}!`);
};
```

```javascript
// app.js
const greet = require('./greet');

greet('John');
// Output: Hello, John!
```

## The `global` Keyword

The `global` object in Node.js is a special object that provides access to global variables and functions across your entire application. It serves as a global namespace, similar to the `window` object in web browsers.

You can define global variables by assigning values to properties of the `global` object:

```javascript
// app.js
global.myGlobalVariable = 'Hello, World!';

console.log(global.myGlobalVariable);
// Output: Hello, World!
```

However, it's generally recommended to avoid using global variables as much as possible, as they can lead to naming conflicts and make your code harder to maintain and reason about.

Instead of using global variables, you can define variables and functions within your modules and export them for use in other parts of your application.

In addition to global variables, Node.js provides several built-in global objects and functions, such as `console`, `process`, `setTimeout`, and `setInterval`. These global objects and functions are available in any part of your Node.js application without needing to be imported or defined.

```javascript
// app.js
console.log('Hello, World!');
// Output: Hello, World!

setTimeout(() => {
  console.log('Delayed message');
}, 2000);
// Output (after 2 seconds): Delayed message
```

While the `global` object can be useful in certain scenarios, it's generally best to use it sparingly and rely on modules and local variables whenever possible to promote better code organization, maintainability, and encapsulation.
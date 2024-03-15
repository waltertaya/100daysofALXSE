Here's a README file covering the most essential aspects of Error Handling (Types of Errors) in Node.js:

# Error Handling in Node.js

In Node.js, errors are instances of the built-in `Error` class or its subclasses. They are used to represent various types of errors that can occur during the execution of your application. Proper error handling is crucial for building robust and reliable applications.

## Types of Errors in Node.js

Node.js provides several built-in error types to help you identify and handle different kinds of errors. Here are some of the most common ones:

### 1. **SyntaxError**

This error is thrown when the JavaScript code violates the language's syntax rules. For example, when you have a missing or unexpected token in your code.

```javascript
const x = 1;
console.log(x:); // SyntaxError: Unexpected token ':'
```

### 2. **ReferenceError**

This error occurs when you try to access a variable that hasn't been defined or is out of scope.

```javascript
console.log(x); // ReferenceError: x is not defined
```

### 3. **TypeError**

A `TypeError` is thrown when an operation is performed on a value of the wrong type. For example, calling a non-function value as a function, or accessing a property of `null` or `undefined`.

```javascript
const x = null;
console.log(x.toString()); // TypeError: Cannot read property 'toString' of null
```

### 4. **RangeError**

This error is thrown when a value is not within the expected range. For example, when creating an array with a negative length or passing an invalid value to the `Number` constructor.

```javascript
const x = new Array(-1); // RangeError: Invalid array length
```

### 5. **URIError**

A `URIError` is thrown when a global URI handling function is passed an invalid parameter.

```javascript
decodeURIComponent('%'); // URIError: URI malformed
```

### 6. **EvalError**

This error is thrown when the global `eval()` function is used illegally.

### 7. **InternalError**

An `InternalError` is thrown when an internal error occurs in the Node.js runtime. These errors are typically caused by bugs in the Node.js runtime and should be reported.

### 8. **Error (generic)**

The base `Error` class is used for creating custom errors or when none of the built-in error types apply.

```javascript
throw new Error('Something went wrong');
```

## Error Handling Techniques

Node.js provides several ways to handle errors, including:

1. **try...catch statements**: This is the most common way to handle errors in Node.js. Wrap the code that might throw an error in a `try` block, and catch the error in a `catch` block.

```javascript
try {
  // Code that might throw an error
} catch (error) {
  // Handle the error
  console.error(error);
}
```

2. **Throwing errors**: You can throw your own errors using the `throw` statement, which can be caught by a `catch` block.

```javascript
function divide(a, b) {
  if (b === 0) {
    throw new Error('Cannot divide by zero');
  }
  return a / b;
}

try {
  const result = divide(10, 0);
  console.log(result);
} catch (error) {
  console.error(error.message); // 'Cannot divide by zero'
}
```

3. **Uncaught exceptions**: If an error is not caught by any `catch` block, it becomes an uncaught exception, which will cause the Node.js process to exit. You can handle uncaught exceptions using the `uncaughtException` event on the global `process` object.

```javascript
process.on('uncaughtException', (error) => {
  console.error('Uncaught exception:', error);
  // Clean up resources, log the error, etc.
  process.exit(1); // Exit the process with a non-zero status code
});
```

4. **Unhandled promise rejections**: When a promise is rejected and there is no `catch` handler attached, it becomes an unhandled promise rejection. You can handle these rejections using the `unhandledRejection` event on the global `process` object.

```javascript
process.on('unhandledRejection', (reason, promise) => {
  console.error('Unhandled promise rejection:', reason);
  // Clean up resources, log the error, etc.
});
```

By understanding and properly handling different types of errors in Node.js, you can build more robust and reliable applications that can gracefully handle unexpected situations.

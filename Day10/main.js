function greet(name) {
    if (!name) {
      const error = new Error('Name is required');
      error.stack; // Stack trace is available here
      throw error;
    }
    console.log(`Hello, ${name}!`);
  }
  
  function sayHello() {
    greet();
  }
  
  try {
    sayHello();
  } catch (err) {
    console.error('Error:', err.message);
    console.error('Stack trace:', err.stack);
  }
  // Output:
  // Error: Name is required
  // Stack trace: Error: Name is required
  //     at greet (/path/to/file.js:3:15)
  //     at sayHello (/path/to/file.js:8:3)
  //     at Object.<anonymous> (/path/to/file.js:12:1)
  //     ...
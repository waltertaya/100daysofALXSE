function greet(name, callback) {
    setTimeout(() => {
      console.log(`Hello, ${name}!`);
      callback();
    }, 2000);
  }
  
  function sayGoodbye() {
    console.log('Goodbye!');
  }
  
  greet('Alice', sayGoodbye);
  // Output:
  // Hello, Alice!
  // Goodbye!
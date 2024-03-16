// Function to simulate a deeply nested function call
function foo() {
    throw new Error('Oops! Something went wrong in foo()');
}

function bar() {
    foo();
}

function baz() {
    bar();
}

// Function with a try...catch block to handle errors
function errorHandler() {
    try {
        baz();
    } catch (error) {
        console.error('Caught Error:', error.message);
        console.error('Stack Trace:', error.stack);
    }
}

// Uncaught exception handler
process.on('uncaughtException', (error) => {
    console.error('Uncaught Exception:', error.message);
    console.error('Stack Trace:', error.stack);
    // Perform cleanup tasks if necessary
    process.exit(1); // Terminate the process with a non-zero exit code
});

// Triggering the error
errorHandler();

// Function to divide two numbers
function divide(a, b) {
    try {
        // Check if the denominator is zero
        if (b === 0) {
        // Throw a custom error
        throw new Error('Cannot divide by zero');
        }

        // Perform the division
        const result = a / b;

        // Return the result if no error occurred
        return result;
    } catch (error) {
        // Handle the error
        console.error('Error:', error.message);

        // You can also throw a different error or perform additional error handling
        throw new Error('Division failed');
    } finally {
        // This block will always execute, regardless of whether an error was thrown or not
        console.log('Division operation completed');
    }
}

// Example usage
try {
    const result = divide(10, 2);
console.log('Result:', result); // Output: Result: 5
} catch (error) {
    console.error('Error:', error.message);
}

// Another example with an error
try {
    const result = divide(10, 0);
} catch (error) {
    console.error('Error:', error.message); // Output: Error: Division failed
}

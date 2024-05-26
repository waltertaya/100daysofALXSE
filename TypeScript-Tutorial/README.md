# TypeScript Tutorial

## Introduction

- *TypeScript* is JavaScript with added syntax of the types.
- *JavaScript* is loosely typed language.
- Use TypeScript compiler which transpiles TypeScript code to JavaScript.

## Installing TypeScript Compiler

- Install the compiler using *npm* and save as dev it as dev dependencies

```bash
npm install typescript -D
```

- Or

```bash
npm install typescript --save-dev
```

- The compiler is install in the *node_modules* and can be run using:

```bash
npx tsc
```

## Configuring the compiler

- Configuring the compiler in the file *tsconfig.json*, run the command below so that the file can be created

```bash
npx tsc --init
```

## TypeScript Simple Types

- Primitive types

    1. *boolean* - true or false values
    2. *number* - whole numbers and floating point values
    3. *string* - text values like "TypeScript Rocks"
    4. *bigint* - whole numbers and floating point values, but allows larger negative and positive numbers than the number type.
    5. *symbol* are used to create a globally unique identifier.

## Type Assignment

- There are two ways TypeSript assigns variables

    1. Explicit
    2. Implicit

### Explicit Type

- Writing the type

```typescript
let age: number = 30;
let name: string = "Regy";
let voted: boolean = true
```

### Implicit Type

- TypeScript will *guess* the type of the variable based on value assigned to the variable.

```typescript
let name = "Joe Doe"
```

### Error In Type Assignment

TypeScript will throw an error if data types do not match.

```typescript
let name: string = "Waltertaya"
name = 67 // Attempts to re-assign name to type number which throw an error

let age = 45
age = "John" // throws error because type mismatch
```

## TypeScript Special Types

### Type: *any*

- *any* is a type that disables type checking and effectively allows all types to be used.
- Setting any to the special type any disables type checking:

```typescript
let y: boolean = true;
y = "string"; // will not raise type error
Math.round(y);  // will not raise type error because not a number
```

### Type: *unknown*

- *unknown* is a similar, but safer alternative to *any*.

- TypeScript will prevent unknown types from being used, as shown in the below example:

```typescript
let w: unknown = 1;
w = "string"; // no error
w = {
  runANonExistentMethod: () => {
    console.log("I think therefore I am");
  }
} as { runANonExistentMethod: () => void}
// How can we avoid the error for the code commented out below when we don't know the type?
// w.runANonExistentMethod(); // Error: Object is of type 'unknown'.
if(typeof w === 'object' && w !== null) {
  (w as { runANonExistentMethod: Function }).runANonExistentMethod();
}
// Although we have to cast multiple times we can do a check in the if to secure our type and have a safer casting
```

### Type: *never*

- *never* effectively throws an error whenever it is defined.

```typescript
let x: never = true; // Error: Type 'boolean' is not assignable to type 'never'.
```

- *never* is rarely used, especially by itself, its primary use is in advanced generics.

### Type: *undefined* & *null*

- *undefined* and null are types that refer to the JavaScript primitives undefined and null respectively.

```typescript
let y: undefined = undefined;
let z: null = null;
```

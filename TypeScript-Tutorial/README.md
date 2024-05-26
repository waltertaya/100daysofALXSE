# TypeScript Tutorial

- **@waltertaya**

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

class Jobs {
  constructor(name, salary, vacancy) {
    if (new.target === Jobs) {  // Abstract class
        throw new Error('This is an abstract class and cannot be initialized')
    }
    this._name = name;
    this._salary = salary;
    this._vacancy = vacancy;
  }

  get name() {
    return this._name;
  }

  get salary() {
    return this._salary;
  }

  get vacancy() {
    return this._vacancy;
  }

  qualified() {
    if (this._vacancy === true) {
        return (`Congratulations, you are qualified for the ${this._name} job. You will earn $ ${this._salary} per year. See you soon.`);
    } else {
        return (`Sorry, you could NOT make to the ${this._name} job. Try again next time.`)
    }
  }
}

class SoftwareEngineering extends Jobs {
  constructor(name, salary, vacancy) {
    super(name, salary, vacancy)
  }
}
let jobs = new Jobs('Backend Development', 150000, true) // Output -> Error: This is an abstract class and cannot be initialized
console.log(jobs.qualified())

let se = new SoftwareEngineering('Software Engineering', 200000, true);
// se.name = 'Software Development'   -> Do not have set method
// console.log(se.name)
// console.log(se.salary)
// console.log(se.vacancy)
console.log(se.qualified())

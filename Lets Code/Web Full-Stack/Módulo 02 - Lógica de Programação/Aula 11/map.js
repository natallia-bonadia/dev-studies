/*const vetor = ['10', '4', '21', '8']

function stringToInt(str){
  return parseInt(str)
}

const vetor2 = vetor.map(stringToInt)
console.log(vetor2)

OU

const vetor2 = vetor.map(x => parseInt(x))
console.log(vetor2)
*/

/*
const vetor3 = [3, 6, 1, 0, -10, 5, 8, 2, 7]
const vetor4 = vetor3.map(
  (num, ind) => {
    if (ind % 2 === 0) return num*2
    else return num*3 
  }
)
console.log(vetor4)

OU

const vetor3 = [3, 6, 1, 0, -10, 5, 8, 2, 7]
const vetor4 = vetor3.map(
  (num, ind) => index % 2 === 0 ? num*2 : num*3 
)
console.log(vetor4)
*/

/*
const vetor5 = [10, 25, 60, 200]
const vetor6 = vetor5.map(
  (num, ind, vetor) => num/vetor.length
)
console.log(vetor6)
*/

/*
const matriz = [
  ['3', '5', '7'],
  ['10', '20', '30'],
  ['2', '4', '6']
]

const matriz2 = matriz.map(
  line => line.map(x => parseInt(x))
)

console.log(matriz2)
*/

/*
let employees = [
  {role: 'Dev', salary: 1000},
  {role: 'Designer', salary: 800},
  {role: 'Seller', salary: 400},
  {role: 'Engineer', salary: 1000}
]

employees = employees.map(
  employee => {
    let increase
    if (employee.salary < 500) increase = 100
    else if (employee.salary < 1000) increase = 200
    else increase = 300

    return { ...employee, salary: employee.salary+increase}
    // ...employee é o mesmo que pegar cada um dos objetos completos
    // ex: {role: 'Dev', salary: 1000}
  }
)
console.log(employees)
*/

/*
// Vetor com número pré-definido de elementos
let array = new Array(20)
array.fill(10)
console.log(array)
*/
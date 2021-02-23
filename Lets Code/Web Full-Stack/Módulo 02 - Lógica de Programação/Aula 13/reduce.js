/*
let vetor = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

let soma = vetor.reduce(
  (state, num) => state+num
)
console.log(soma)

let mult = vetor.reduce(
  (state, num) => state*num
)

console.log(mult)
*/
let matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [10, 11, 12]
]

soma = matrix.reduce(
  (state, line) => [state[0]+line[0], state[1]+line[1], state[2]+line[2]]
)
console.log(soma)
/*
const alunos = [
  {nome: 'Lucas', nota: 4},
  {nome: 'Natallia', nota: 10},
  {nome: 'Gil', nota: 10},
  {nome: 'Erick', nota: 10},
]

let notaTotal = alunos.reduce((notaAcumulada, aluno) => notaAcumulada + aluno.nota, 0)
console.log(notaTotal)

let aprovados = alunos.reduce((aprovadosParcial, aluno) =>aluno.nota > 6 ? [...aprovadosParcial, aluno.nome] : aprovadosParcial, [])

console.log(aprovados)

const numeros = [1, 2, 3, 2, 1, 3, 3, 5, 4, 6]
let resultado = numeros.reduce((state, num) => state.includes(num) ? state : [...state, num], [])
console.log(resultado)
*/
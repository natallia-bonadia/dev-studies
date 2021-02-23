// 1. Dado um vetor numérico, filtre os elementos do vetor para conter apenas elementos maiores do que 5.
/*
let vetor = [9, 1, -5, 10, 7, 4, 0, -2, 8]

vetor = vetor.filter( x => x > 5)
console.log(vetor)
*/

// 2. Dado um vetor numérico, filtre os elementos do vetor para conter apenas números pares.
/*
let vetor = [9, 1, -5, 10, 7, 4, 0, -2, 8]

vetor = vetor.filter( x => x % 2 === 0)
console.log(vetor)
*/

// 3. Dado um vetor de strings, filtre os elementos do vetor para conter apenas strings com 5 caractéres ou menos.
/*
let vetor = ['abacaxi', 'banana', 'caqui', 'figo', 'laranja', 'maça', 'pera', 'uva']

vetor = vetor.filter( x => x.length <= 5)
console.log(vetor)
*/

// 4. Dado um vetor de objetos que representam pessoas, filtre as pessoas que não fazem parte do clube.
/*
const people = [
  { name: "Angelina Jolie", member: true },
  { name: "Eric Jones", member: false },
  { name: "Paris Hilton", member: true },
  { name: "Kayne West", member: false },
  { name: "Bob Ziroll", member: true }
]

const members = people.filter((x, ind) => people[ind]['member'] === true)
console.log(members)
*/

// 5. Faça um vetor filtrado somente com as pessoas que podem assistir o filme The Matrix (maiores de 18 anos).
/*
const people = [
    { name: "Angelina Jolie", age: 80 },
    { name: "Eric Jones", age: 2 },
    { name: "Paris Hilton", age: 5 },
    { name: "Kayne West", age: 16 },
    { name: "Bob Ziroll", age: 100 }
]

const older = people.filter((x, ind) => people[ind]['age'] > 18)
console.log(older)
*/

// 6. Dado o vetor:
// Utilize filter para selecionar todos os números primos do array.

const array = [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13];

function primo(x){
  let mod_x = Math.abs(x)
  let cont = 0
  for (i = 1; i <= mod_x; i++){
    if (mod_x % i === 0) cont++
  }
  return (cont === 2)
}

const filtro = array.filter(primo)

console.log(filtro)


// 7. Dado:
// Utilize filter para retornar um novo array sem números repetidos.

const numeros = [1,2,3,2,1,3,3,5,4,6]

const sem_repeticao = numeros.filter(
  (num, ind_num, vetor) => vetor.indexOf(num) === ind_num)

console.log(sem_repeticao)


// 8. Utilize o método filter para determinar quais restaurantes estão abertos no horário atual.
// Dica: utilize new Date().getHours para retornar o horário atual.
/*
const restaurantes = [
  {
    nome: 'Pizzaria do Mario',
    horario_abertura: 14,
    horario_fechamento: 23
  },
  {
    nome: 'Churrascaria do Ronaldo',
    horario_abertura: 11,
    horario_fechamento: 14,
  },
  {
    nome: 'Bar do Zeca',
    horario_abertura: 12,
    horario_fechamento: 2,
  },
  {
    nome: 'Doceria da Mara',
    horario_abertura: 8,
    horario_fechamento: 20,
  },
]

const open = restaurantes.filter(restaurante => {
  let atual = new Date().getHours()
  return (atual > restaurante['horario_abertura'] && atual < restaurante['horario_fechamento'])
})
console.log(open)
*/
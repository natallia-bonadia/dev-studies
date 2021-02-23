// 1. Use a função reduce para fazer a soma de todos os elementos de um vetor numérico.
/*
vetor = [-5, 3, 9, 0, 8, 1, 4, -2]

let soma = vetor.reduce((state, num) => state+num)
console.log(soma)
*/

// 2. Use a função reduce para transformar um vetor numérico em uma string com todos os números como caractéres.
/*
vetor = [5, 3, 9, 0, 4, 2]

let toString = vetor.reduce((state, num) => {
  return state.toString()+num})
console.log(toString)
*/
// 3. Transforme o vetor de eleitores em uma contagem de quantas pessoas parcitiparam na votação.
/*
const voters = [
    {name:'Bob' , age: 30, voted: true},
    {name:'Jake' , age: 32, voted: true},
    {name:'Kate' , age: 25, voted: false},
    {name:'Sam' , age: 20, voted: false},
    {name:'Phil' , age: 21, voted: true},
    {name:'Ed' , age:55, voted:true},
    {name:'Tami' , age: 54, voted:true},
    {name: 'Mary', age: 31, voted: false},
    {name: 'Becky', age: 43, voted: false},
    {name: 'Joey', age: 41, voted: true},
    {name: 'Jeff', age: 30, voted: true},
    {name: 'Zack', age: 19, voted: false}
]

let total_voters = voters.reduce((state, voter) => {
  if (voter.voted) state.push(voter)
  return state}, [])
console.log(`${total_voters.length} pessoas foram votar.`)
*/
// 4. Dado um vetor de produtos que tem interesse em comprar, calcule quanto custaria comprar todos os produtos a vista.
/*
const products = [
    { title: "Tesla Model S", price: 90000 },
    { title: "4 carat diamond ring", price: 45000 },
    { title: "Fancy hacky Sack", price: 5 },
    { title: "Gold fidgit spinner", price: 2000 },
    { title: "A second Tesla Model S", price: 90000 }
];

    let total = products.reduce((acumulator, product) => acumulator + product.price, 0)
    console.log(total)
*/

// 5. Dado um vetor de vetores, transforme-me o em vetor um único que contém todos os elementos:
// [[“1”, “2”, “3”],[true], [4, 5, 6]] -> [“1”, “2”, “3”, true, 4, 5, 6]
/*
vetor = [['1', '2', '3'],[true], [4, 5, 6]]

let vetor_comp = vetor.reduce((acumulator, item) => {
  for (let subItem of item){
    acumulator.push(subItem)
  } return acumulator
})
console.log(vetor_comp)
*/

// 6. Dado um vetor de eleitores em potencial, retorne um objeto representando quantos votaram por faixa etária. Agrupar as idades 18-25, 26-35, 36-55 e as demais idades.
/*
const voters = [
    {name:'Bob' , age: 30, voted: true},
    {name:'Jake' , age: 32, voted: true},
    {name:'Kate' , age: 25, voted: false},
    {name:'Sam' , age: 20, voted: false},
    {name:'Phil' , age: 21, voted: true},
    {name:'Ed' , age: 55, voted: true},
    {name:'Tami' , age: 54, voted: true},
    {name: 'Mary', age: 31, voted: false},
    {name: 'Becky', age: 43, voted: false},
    {name: 'Joey', age: 41, voted: true},
    {name: 'Jeff', age: 30, voted: true},
    {name: 'Zack', age: 19, voted: false}
]

let group_voters = voters.reduce((acumulator, voter) => {
  if (voter.age < 26) {
    acumulator.numYoungPeople++
    if (voter.voted) acumulator.numYoungVotes++}
  else if (voter.age < 36) {
    acumulator.numMidPeople++
    if (voter.voted) acumulator.numMidVotes++}
  else {
    acumulator.numOldPeople++
    if (voter.voted) acumulator.numOldVotes++}
  return acumulator
  }, {numYoungPeople: 0, numYoungVotes: 0, numMidPeople: 0, numMidVotes: 0,
numOldPeople: 0, numOldVotes: 0 })

console.log(group_voters)
*/

// 7. Faça uma implementação das funções map e filter utilizando o reduce.
/*
function map(fn, vector){
  return vector.reduce((state, element) => [...state, fn(element)] , [])
}

let result_map = map(x => 2*x, [1, 2, 3, 4, 5, 6])
console.log(result_map)

function filter(fn, vector){
  return vector.reduce((state, element) => {
    if (fn(element)) state.push(element)
    return state}, [])
}

let result_filter = filter(x => x % 2 === 0, [1, 2, 3, 4, 5, 6])
console.log(result_filter)
*/

// 8. Dada uma matriz numérica quadrada, utilize o reduce para somar a sua diagonal principal.
/*
const matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

const soma = matrix.reduce((state, line, index) => state+line[index], 0)
console.log(soma)
*/

// 9. Faça uma função que recebe um argumento e um vetor de funções. Utilize o reduce para aplicar as funções sucessivamente no argumento. Isto é, a primeira função recebe o argumento e o seu retorno é enviado como argumento para a próxima função. O último valor é o retornado pela função.
/*
const fn1 = x => x + 1

const fn2 = x => x**2

const fn3 = x => x/2

const vetor = [fn1, fn2, fn3]
const x = 5

const fn_reduce = (x, vetor) => {
  return vetor.reduce((state, element) => element(state), x)}

console.log(fn_reduce(x, vetor))
*/
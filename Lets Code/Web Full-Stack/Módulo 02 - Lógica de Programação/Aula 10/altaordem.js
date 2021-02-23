/*
function sum(a, b){
  return a+b
}

function apply (operation, a, b){
  return operation (a, b)
}

function sumX(x){
  return function(a){
    return a+x
  }
}

const sum5 = sumX(5)
const sum10 = sumX(10)
console.log(sum5(10))
console.log(sum10(10))
*/

let user1 = {name: 'Natallia', age: 31}

function userFactory(name, age){
  return {
    name, age
  }
}

let user2 = userFactory('Gil', 34)
let user3 = userFactory('Lucas', 26)
console.log(user2)
console.log(user3)

function factoryCreator(obj){
  let keys = []
  if (arguments.length === 1 && typeof obj === 'object'){
    for (key in obj){
      keys.push(key)
    
    }
  }
  else{
    for (arg of arguments){
      keys.push(arg)
    }
  }
  return function(){
    let new_obj = {}
    if (arguments.length === keys.length){
      for (let i = 0; i < keys.length; i++){
        new_obj[keys[i]] = arguments[i]
      }
    }
    else {
      throw Error(`Quantidade de argumentos diferente do numero de chaves no objeto original`)
    }
    return new_obj
  }
}

function printArguments(){
  console.log(arguments)
}

let book = {
  title: 'Lord of the Rings',
  author: 'Tolken',
  pages: 1000
}

const bookFactory = factoryCreator(book)

console.log(bookFactory('Sítio do Pica-Pau Amarelo', 'MOnteiro Lobato', 300))

const userFactory2 = factoryCreator(user1)

console.log(userFactory2('Luis', 20))

const productFactory = factoryCreator('name', 'price', 'date')
console.log(productFactory('leite', 4.00, '30/12/2020'))
// 1.Durante a Black Friday uma loja declarou descontos em produtos do seu catálogo, de acordo com a regra abaixo:

    // 5% para produtos abaixo de R$ 200,00
    // 10% para produtos abaixo de R$ 400,00
    // 15% para produtos abaixo de R$ 2000,00
    // 20% para produtos acima de R$ 2000,00
    // Com base nisso, crie um programa que recebe o preço normal dos 10 produtos mais adquiridos pelos clientes e guarde-os em um array.
    // Em seguida, utilize a função map para aplicar o desconto nos preços e, com isso, criar um array com o preço após os descontos.
/*
const precos = [350, 120, 600, 3000, 1500, 10000, 80, 2300, 380, 4700]

const precos_atualizados = precos.map(num => {
    if (num < 200) preco = num*0.95
    else if (num < 400) preco = num*0.90
    else if (num < 2000) preco = num*0.85
    else preco = num*0.80

    return preco
  }
)
console.log(precos_atualizados)
*/

// 2. Crie um script para receber dois arrays informados pelo usuário. Em ambos os casos, não existe um número definido de números para os arrays, portanto, receba os números, até que o usuário informe um valor negativo.
// Com os dois arrays, utilize a função map para multiplicá-los, elemento a elemento. É possível que os arrays tenham tamanhos diferentes, certo? Por isso, o array resultante deverá ter o tamanho do menor dos arrays.
// Exemplo 01:
// Entrada 	  	Saída
// [1, 2, 3] 		[1, 4, 9]
// [1, 2, 3, 4]
// Exemplo 02:
// Entrada 	  	Saída
// [5, 7, 3] 		[10, 14]
// [2, 2]
/*
const input = require('readline-sync')

const vetor1 = []
while (true){
  let num1 = parseInt(input.question('Digite um numero para adicionar no vetor 1: '))
  if (num1 >= 0) vetor1.push(num1)
  else break
}
const vetor2 = []
while (true){
  let num2 = parseInt(input.question('Digite um numero para adicionar no vetor 2: '))
  if (num2 >= 0) vetor2.push(num2)
  else break
}

vetor3 = []

if (vetor1 > vetor2){
  vetor3 = vetor2.map((num, ind) => {
    resp = num*vetor1[ind]
      return resp
  }
  )
}
else{
  vetor3 = vetor1.map((num, ind) => {
    resp = num*vetor2[ind]
      return resp
  }
  )
}
console.log(vetor3)

OU

const input = require('readline-sync')

const vetor1 = []
while (true){
  let num1 = parseInt(input.question('Digite um numero para adicionar no vetor 1: '))
  if (num1 >= 0) vetor1.push(num1)
  else break
}
const vetor2 = []
while (true){
  let num2 = parseInt(input.question('Digite um numero para adicionar no vetor 2: '))
  if (num2 >= 0) vetor2.push(num2)
  else break
}

const vetor3 = vetor1.length > vetor2.length ? vetor2.map((num, ind) => num*vetor1[ind]) : vetor1.map((num, ind) => num*vetor2[ind])

console.log(vetor3)

OU

const vetor3 = (vetor1.length > vetor2.length ? vetor2 : vetor1).map((num, ind) => num*(vetor1.length > vetor2.length ? vetor1 : vetor2)[ind])

console.log(vetor3)
*/

// 3. Crie uma função para gerar um número inteiro aleatório entre -10 e 10. Em seguida, utilize a função map e a função criada para construir um array com 20 números inteiros aleatórios entre -10 e 10.
/*
const random = () => Math.floor(Math.random()*21)-10

vetor = new Array(20).fill(1)
vetor = vetor.map( random )
console.log(vetor)
*/
// 4. O objeto abaixo é formado pelo nome (name), idade (age), peso (weight) e altura (height) de 5 pessoas.
// Utilize a função map para adicionar outros dois campos ao objeto acima:
//  bmi: que contém o IMC (Body Mass Index ou Índice de Massa Corporal) da pessoa (float)
//  classification: uma classificação simples do IMC da pessoa. Insira a string 'fora da faixa Normal', caso a pessoa tenha um IMC abaixo de 18,5 ou acima de 25. Insira a string 'Normal', caso a pessoa tenha um IMC entre 18,5 e 25.
/*
const people = [
  {
      name: "Angelina Jolie",
      age: 80,
      weight: 55,
      height: 1.79
  },
  {
      name: "Eric Jones",
      age: 28,
      weight: 100,
      height: 1.6
  },
  {
      name: "Paris Hilton",
      age: 34,
      weight: 79,
      height: 1.65
  },
  {
      name: "Kayne West",
      age: 26,
      weight: 83,
      height: 1.83
  },
  {
      name: "Bob Ziroll",
      age: 90,
      weight: 60,
      height: 1.65
  }
];

const people_atualizado = people.map((_, ind) => {
  people[ind]['bmi'] = parseFloat((people[ind]['weight']/people[ind]['height']**2).toFixed(2))
  if (people[ind]['bmi'] < 18,5 && people[ind]['bmi'] > 25) people[ind]['classification'] = 'fora da faixa Normal'
  else people[ind]['classification'] = 'Normal'
}
)
console.log(people)
*/

// 5. O array abaixo consiste em uma matriz cujas linhas são compostas por 3 dados de usuários de uma rede social: id, e-mail e país de origem, nessa ordem.
// Para ficar melhor de utilizar os dados dessa matriz, utilize a função map para transformá-la em um array de objetos com os campos id, email e country.
/*
const customers = [
  [1, 'isidro_von@hotmail.com', 'Switzerland'],
  [2, 'frederique19@gmail.com', 'Democratic People´s Republic of Korea'],
  [3, 'fredy54@gmail.com', 'Tunisia'],
  [4, 'braxton29@hotmail.com', 'Egypt'],
  [5, 'josh_batz60@gmail.com', 'Serbia'],
  [6, 'emie_corkery82@yahoo.com', 'Brazil']
];

const customers_atualizado = customers.map((customer) => {
  let new_customers = {    
    id: customer[0],
    email: customer[1],
    country: customer[2]
    }
    return new_customers
  })
console.log(customers_atualizado)
*/
// 6. Os dados do objeto abaixo foram obtidos por meio de uma requisição a uma API que nos fornece os dados dos posts de um blog, os quais estão armazenados em um banco de dados:
// Observe que cada post contém um id, título (title), conteúdo (content) e autor (author).
// Para renderizar essas informações no front-end da página inicial do blog, o programador (você!) deseja colocar o nome do autor em caixa alta (já que ele vai ficar bem pequeno abaixo do título) e utilizar apenas os 300 primeiros caracteres do conteúdo do post, afinal, a ideia é que o usuário tenha apenas uma noção do conteúdo daquele post (imagine que o conteúdo do post é enorme).
// Utilize a função map para aplicar essa transformação no objeto acima.
/*
const posts = [
  {
    id: 0,
    title: 'Programação Funcional',
    content: "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
    author: 'Gabriel Millitelo'
  },
  {
    id: 1,
    title: 'Funções de Alta Ordem',
    content: "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
    author: 'Lucas Maia'
  },
  {
    id: 2,
    title: 'Funções de Alta Ordem de Arrays',
    content: "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
    author: 'Felipe Cabral'
  },
  {
    id: 3,
    title: 'Função map()',
    content: "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
    author: 'Walisson Silva'
  }
]

const new_posts = posts.map(
  post => {
  return{...post, author: post['author'].toUpperCase(),
  content: post['content'].slice(0, 300)}
})
console.log(new_posts)
*/
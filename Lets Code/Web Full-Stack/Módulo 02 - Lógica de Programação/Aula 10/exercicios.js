// 1. Faça uma função para cada operação matemática básica (±*/). Em seguida faça uma função chamada calcular de alta-ordem que receba uma operação e dois números e invoque a operação usando os números como parâmetro.
/*
function somar(a, b){
  return a+b
}

function subtrair(a, b){
  return a-b
}

function multiplicar(a, b){
  return a*b
}

function dividir(a, b){
  return a/b
}

function calcular(operacao, a, b){
  return operacao(a, b)
}

console.log(calcular(dividir, 10, 2))
console.log(calcular(somar, 10, 2))
console.log(calcular(subtrair, 10, 2))
console.log(calcular(multiplicar, 10, 2))
*/

// 2. Faça uma função chamada desconto, que receba um valor porcentual (por exemplo 10 representa 10%), em seguida ela deve retornar uma função que espera um valor, e retorna esse valor com desconto. Use a sintaxe de function e não arrow. Use sua função para criar duas funções especializadas para 10% e 15% de desconto.
/*
function descontar(porcentagem){
  return function (preco){
    return preco - (porcentagem/100*preco)
  }
}

const desconto10 = descontar(10)
console.log(desconto10(100))

const desconto15 = descontar(15)
console.log(desconto15(200))
*/

// 3. Refaça o exercício acima usando arrow functions, lembre-se que o retorno é implícito nas arrows, isso gera um padrão muito interessante em funções que retornam funções (evite as chaves…).
/*
const descontar = porcentagem => preco => preco - (porcentagem/100*preco)

const desconto10 = descontar(10)
console.log(desconto10(100))

const desconto15 = descontar(15)
console.log(desconto15(100))
*/
// 4. Crie uma função que recebe outra função, que chamaremos de função de transformação, e um array. Essa função deverá criar um novo array, cujos itens serão os valores do array original, transformados pela função de transformação.
/*
const dobro = x => 2*x
const cubo = x => x**3
console.log(dobro(5))
console.log(cubo(2))

const mapa = (funcao, vetor) => {
  const vetor_transformado = []
  for (let elemento of vetor){
    vetor_transformado.push(funcao(elemento))
  }
  return vetor_transformado
}

const vetor = [9, 3, 5, 4, 1, 0]
console.log(mapa(dobro, vetor))

OU


const dobro = x => 2*x
const mapa = (funcao, vetor) => {
  const vetor2 = vetor.map((num) => funcao(num))
  return vetor2
}

const vetor = [9, 3, 5, 4, 1, 0]
console.log(mapa(dobro, vetor))
*/
// 5. Crie uma função de alta-ordem que recebe outra função, que chamaremos de função de filtragem, e um array. Essa função deverá criar um novo array cujos itens serão apenas aqueles para os quais a função de filtragem retornar true, se ela retornar false não coloque o valor no array.
/*
vetor = [30, 7, 4, 12, 10, 0, 99, -1]

const filtro = x => x % 2 === 0

const filtragem = (funcao, vetor) => {
  const vetor_filtrado = []
  for (let num of vetor){
    if (funcao(num)) vetor_filtrado.push(num) 
  }
  return vetor_filtrado
}

console.log(filtragem(filtro,vetor))

OU

vetor = [30, 7, 4, 12, 10, 0, 99, -1]

const filtro = x => x % 2 === 0

const filtragem = (filtro, vetor) => {
  const vetor_filtrado = vetor.filter(filtro)
  return vetor_filtrado
}

console.log(filtragem(filtro,vetor))
*/
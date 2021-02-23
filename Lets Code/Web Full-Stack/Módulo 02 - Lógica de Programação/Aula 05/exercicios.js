// 1. Faça uma função que recebe um número e imprime seu dobro.
/*
function dobro(a){
  b = a*2
  console.log(`O dobro de ${a} é ${b}`)
}

const readline = require('readline-sync')
let a = parseFloat(readline.question('Digite um número: '))
dobro(a)
*/

// 2. Faça uma função que recebe o valor do raio de um círculo e retorna o valor do comprimento de sua circunferência: C = 2pir.
/*
function circ(raio){
  let C = 2*3.14*raio
  console.log(`O comprimento da circunferência é ${C}.`)
}

const readline = require('readline-sync')
let raio = parseFloat(readline.question('Digite o raio: '))
circ(raio)
*/

// 3. Faça uma função para cada operação matemática básica (soma, subtração, multiplicação e divisão). As funções devem receber dois números e retornar o resultado da operação.
/*
function soma(a, b){
  let c = a + b
  console.log(`${a} + ${b} = ${c}`)
}
function subtracao(a, b){
  let c = a - b
  console.log(`${a} - ${b} = ${c}`)
}
function multiplicacao(a, b){
  let c = a * b
  console.log(`${a} x ${b} = ${c}`)
}
function divisao(a, b){
  let c = a / b
  console.log(`${a} / ${b} = ${c}`)
}

const readline = require('readline-sync')
let a = parseFloat(readline.question('Digite o valor de a: '))
let b = parseFloat(readline.question('Digite o valor de b: '))

soma(a, b)
subtracao(a, b)
multiplicacao(a, b)
divisao(a, b)
*/

// 4. Faça uma função que recebe um nome e imprime “olá, [nome]”.
/*
function ola(nome){
  console.log(`Olá, ${nome}! Prazer em te conhecer.`)
}

const readline = require('readline-sync')
nome = readline.question('Nome: ')
ola(nome)
*/

// 5. Faça uma função que recebe um nome e um horário e imprime “Bom dia, [nome]”, caso seja antes de 12h, “Boa Tarde, [nome]”, caso seja entre 12h e 18h e “Boa noite, [nome]” se for após às 18h.
/*
function cumprimento(nome, hora){
  if (hora < 12){
    console.log(`Bom dia, ${nome}`)
  }
  else if (hora < 18){
    console.log(`Boa tarde, ${nome}`)
  }
  else{
    console.log(`Boa noite, ${nome}`)
  }
}

const readline = require('readline-sync')
let nome = readline.question('Nome: ')
let hora = parseInt(readline.question('Horário: '))

cumprimento(nome, hora)
*/

// 6. Faça uma função que recebe um número e retorna true se ele é par ou false, se ele é ímpar.
/*
function par(num){
  if (num % 2 == 0){
    console.log(true)
  }
  else{
    console.log(false)
  }
}

const readline = require('readline-sync')
let num = parseInt(readline.question('Digite um número: '))
par(num)
*/
// or
/*
function par(num){
  return num % 2 == 0
}

const readline = require('readline-sync')
let num = parseInt(readline.question('Digite um número: '))
console.log(par(num))
*/
// 7. Faça uma função que sorteia 10 números aleatórios entre 0 e 100 e retorna o maior entre eles.
/*
function sortmaior(){
  let vetor = []
  for (let i = 0; i < 10; i++){
    let num = Math.floor(Math.random()*101)
    vetor.push(num)
  }
  console.log(`O vetor sorteado foi [${vetor}]`)
  let maior = 0
  for (let num of vetor){
    if (num > maior){
      maior = num
    }
  }
  console.log(`O maior número do vetor é ${maior}.`)
}

sortmaior()
*/

// 8. Faça uma função que recebe um número n de entrada, sorteia n números aleatórios entre 0 e 100 e retorna a média deles.
/*
function sorteio(n){
  let vetor = []
  for (let i = 0; i < n; i++){
    let num = Math.floor(Math.random()*101)
    vetor.push(num)
  }
  console.log(`O vetor sorteado foi [${vetor}]`)
  let soma = 0
  for (let numero of vetor){
    soma += numero
  }
  let media = soma / n
  console.log(`A média do vetor é igual a ${media.toFixed(2)}`)
}

const readline = require('readline-sync')
let n = parseInt(readline.question('Digite um número: '))
sorteio(n)
*/

// 9. Faça uma função que recebe um vetor de palavras e retorna um vetor contendo as mesmas palavras do vetor anterior, porém escritas em caixa alta.
/*
function maiusc(vetor){
  let vetormai = []
  for (let palavra of vetor){
    let palavramai = palavra.toUpperCase()
    vetormai.push(palavramai)
  }
  console.log(vetormai)
}

vetor = ['abacate', 'caqui', 'framboesa', 'laranja', 'melancia']
maiusc(vetor)
*/

// 10. Faça uma função que recebe dois vetores e retorna a soma item a item desses vetores.
// Exemplo: Se a função receber os vetores [1,4,3] e [3,5,1], então a função deve retornar [1+3, 4+5, 3+1] = [4, 9, 4].
/*
function somavetores(a, b){
  let vetorsoma = []
  for (let i in a){
    let soma = a[i] + b[i]
    vetorsoma.push(soma)
  }
  console.log(vetorsoma)
}

let a = [1, 2, 3]
let b = [7, 12, 1]

somavetores(a, b)
*/

// 11. Faça uma função que receba dois vetores e retorne o produto item a item desses vetores.
// Exemplo: Se a função receber os vetores [1,4,3] e [3,5,1], então a função deve retornar [1x3, 4x5, 3x1] = [3, 20, 3].
/*
function produtovetores(a, b){
  let vetorproduto = []
  for (let i in a){
    let produto = a[i] * b[i]
    vetorproduto.push(produto)
  }
  console.log(vetorproduto)
}

let a = [1, 0, 8, 4]
let b = [4, 12, 2, 4]

produtovetores(a, b)
*/

// 12. Faça uma função que recebe um número x e um vetor numérica e retorna um vetor cujos elementos são os itens do vetor de entrada multiplicado por x.
// Exemplo:
// Se a função receber o número 5 e o vetor [3,5,1], então a função deve retornar [5x3, 5x5, 5x1] = [15, 25, 5].
/*
function vetormult(x, vetor){
  let vetorfim = []
  for (let n of vetor){
    let resp = n*x
    vetorfim.push(resp)
  }
  console.log(vetorfim)
}

const readline = require('readline-sync')
let x = parseInt(readline.question('Digite o numero multiplicador: '))
let vetor = []
let qtd = parseInt(readline.question('Quantos numeros quer adicionar no vetor? '))
for (i = 0; i <= qtd - 1; i++){
  num = parseInt(readline.question(`${i+1}o. numero do vetor: `))
  vetor.push(num)
}

vetormult(x, vetor)
*/

// 13. Faça uma função que recebe um vetor de números e retorna a soma dos elementos desse vetor.
/*
function somavetor(vetor){
  let soma = 0
  for (let n of vetor){
    soma += n
  }
  console.log(soma)
}

somavetor([2, 5, 7, 1, -6])
*/

// 14. Faça uma função que recebe um vetor de números e retorna a média aritmética dos elementos desse vetor.
/*
function mediavetor(vetor){
  let soma = 0
  let media = 0
  for (let n of vetor){
    soma += n
    media = soma/vetor.length
  }
  console.log(media)
}

mediavetor([4, 2, 7, 10, -6, 1])
*/

// 15. Faça uma função que recebe um número e retorna o número invertido.
// Exemplo x = 32243;
// Saída esperada: 34223
/*
function inverte(num){
  let vetor = []
  for (let m of num){
    vetor.unshift(m)
  }
  return parseInt(vetor.join(''))
}

const readline = require('readline-sync')
let num = readline.question('Digite um numero: ')
console.log(inverte(num))
*/
/*
function inverte(num){
  let digitos = []
  while (num !== 0){
    digitos.unshift(num%10)
    num = Math.floor(num/10)
  }
  let novo_num = 0
  for (let i in digitos){
    novo_num += Math.pow(10, i)*digitos[i]
  }
  return novo_num
}

const readline = require('readline-sync')
let num = parseInt(readline.question('Digite um numero: '))
console.log(inverte(num))
*/
// 16. Faça uma função que recebe uma string como parâmetro e converte a primeira letra de cada palavra para maiúsculo.
// Exemplo: ‘the quick brown fox’
// Saída esperada: ‘The Quick Brown Fox’
/*
function title(frase){
  let palavras = frase.split(' ')
  let texto_final = []
  for (let letra of palavras){
    let palavra_final = letra[0].toUpperCase()+letra.slice(1)
    texto_final.push(palavra_final)
  }
  return texto_final.join(' ')
} 

console.log(title('javascript nao esta facil'))
*/

// 17. Faça uma função que recebe um número e retorna um booleano representando se ele é primo ou não.
/*
function primo(x){
  let cont = 0
  for (i = 1; i <= x/2; i++){
    if (x % i == 0){
      cont++
    }
  }
  return cont <= 1
}

console.log(primo(13))
*/

// 18. Faça uma função que recebe um argumento e retorna o seu tipo de dado (number, string, etc).
/*
function tipo(x){
  return typeof x
}

console.log(tipo(1))
console.log(tipo('1'))
console.log(tipo(true))
console.log(tipo(console.log))
*/

// 19. Faça um função que recebe um vetor de números e encontre o segundo menor e o segundo maior número, respectivamente.
// Exemplo: [1,2,3,4,5]
// Saída esperada: 2,4
/*
function segMaiMen(vetor){
  let vetor_limpo = []
  for (let num of vetor){
    if (!vetor_limpo.includes(num)) vetor_limpo.push(num)
  }
  vetor_limpo.sort((a, b) => a - b) //função para o sort ordenar numericamente
  
  if (vetor_limpo.length >= 2){
  return [vetor_limpo[1], vetor_limpo[vetor_limpo.length-2]]
  }
}

let vetor = [7, 4, 0, 3, 1, 2, 10]
console.log(segMaiMen(vetor))
*/

// 20. Faça uma função que recebe um vetor numérico e um número e retorne um vetor com os elementos de maiores que esse número.
/*
function maiores(vetor, num){
  novo_vetor = []
  for (let i of vetor){
    if (i > num)
    novo_vetor.push(i)
  }
  return novo_vetor
}

console.log(maiores([7, 2, 10, 5, -3, 9, 0], 3))
*/

// Desafio 1. Faça uma função que receba um número e calcule seu fatorial.
/*
function fatorial(num){
  let mult = 1
  for (let i = num; i >= 1; i--){
   mult *= i 
  }
  return mult
}
console.log(fatorial(7))
*/

// Super Desafio 1. Repita o exercício anterior usando recursão, ou seja, uma função que chame ela mesma, lembrando que 3! = 32!, que 2! = 21!, que 1! = 1*0! e que 0! = 1.



// Desafio 2. Faça uma função que recebe duas entradas: um input dado pelo usuário e um string que informa o tipo de dado (“idade”, “salário” ou “sexo”), e verifica se os dados digitados foram válidos, usando os seguintes critérios:
// a. Idade: entre 0 e 150;
// b. Salário: maior que 0;
// c. Sexo: M, F ou Outro.
/*
function validadeDados(input, tipo){
  if (tipo === 'idade' && input >= 0 && input <= 150)
    return true
  else if (tipo === 'salario' && input >= 0)
    return true
  else if (tipo === 'sexo' && (input === 'M' || input === 'F'))
    return true
  else
    return false
}

console.log(validadeDados('G', 'sexo'))
*/

// Desafio 3. A sequência Fibonacci é a sequência cujos dois primeiros termos são 1 e os demais são obtidos através da soma de seus dois antecessores, isso é:
// a. Fibonacci(1) = 1 e Fibonacci(2) = 2;
// b. dado qualquer número n >= 3, Fibonacci(n) = Fibonacci(n-1) + Fibonacci(n-2)
// Assim, os 10 primeiros termos da sequência Fibonacci são:
// 1, 1, 2, 3, 5, 8, 13, 21, 34, 55…
// Faça uma função que receba um número n e calcule o termo de número n da sequência Fibonacci.
/*
function fibonacci(n){
  let termo = 2
  let t1 = 1
  let t2 = 1
  let soma = 0
  while (termo != n){
    soma = t1 + t2
    t1 = t2
    t2 = soma
    termo +=1
  }
  return soma
}

console.log(fibonacci(10))
*/

// Super Desafio 3. Refaça o desafio 3 usando recursão.

function fibonacci(n){
  if (n <= 2) return 1 // caso base
  return fibonacci(n-1)+fibonacci(n-2)
}
console.log(fibonacci(8))
// 1. Crie um vetor qualquer e faça um programa que imprima cada elemento do vetor usando o for.
/*
const readline = require('readline-sync')

let vetor = [1, 3, 5, 7, 11, 13, 17]

for (let num of vetor){
  console.log(num)
}
*/

// 2. Faça um programa que imprima todos os itens de um vetor usando while e compare com o exercício 1.
/*
const readline = require('readline-sync')

let vetor = [1, 3, 5, 7, 11, 13, 17]

let cont = 0

while (cont < vetor.length){
  console.log(vetor[cont])
  cont++
}

console.log('Fim do programa!')
*/

// 3. Faça um programa que peça para o usuário digitar um número n e imprima um vetor com todos os números de 0 a n-1.
// Exemplo: se o usuário digitar 5, o programa deve imprimir [0, 1, 2, 3, 4]
/*
const readline = require('readline-sync')

let vetor = []

let num = parseInt(readline.question('Digite um número: '))
let cont = 0

while (cont < num){
  vetor.push(cont)
  cont++
}

console.log(vetor)
*/

// 4. Faça um programa que olhe todos os itens de um vetor e diga quantos deles são pares.
/*

let vetor = [2, 4, 5, 7, 8, 10, 11, 20, 35]
let cont = 0

for (let num of vetor){
  if (num % 2 == 0)
  cont++
}

console.log(`Existem ${cont} números pares no vetor.`)
*/

// 5. Faça um programa que imprima o maior número de um vetor.
/*

let vetor = [10, 99, 51, 0, -10, 3] 
let maior = 0

for (let num of vetor){
  if (num > maior)
  maior = num
}

console.log(`O maior número do vetor é ${maior}.`)
*/

// 6. Faça um programa que, dadas dois vetores de mesmo tamanho, crie um novo vetor com cada elemento igual a soma dos elementos do vetor 1 com os do vetor 2, na mesma posição.
// Exemplo:
// Dadas vetor1 = [1, 4, 5] e vetor2 = [2, 2, 3], então vetor3 = [1+2, 4+2, 5+3] = [3, 6, 8]
/*
vetor1 = [3, 5, 7, 9]
vetor2 = [2, 4, 6, 8]
vetor3 = [] 

for (let num in vetor1){
  novo = vetor1[num] + vetor2[num]
  vetor3.push(novo)
}

console.log(vetor3)
*/

// 7. Faça um programa que dados dois vetores de mesmo tamanho, imprima o produto escalar entre eles.
// OBS: produto escalar é a soma do resultado da multiplicação entre o número na posição i do vetor1 pelo número na posição i do vetor2.
/*
vetor1 = [3, 1, 7, 2]
vetor2 = [2, 4, 0, 8]
soma = 0

for (let num in vetor1){
  let produto = vetor1[num]*vetor2[num]
  soma += produto
}

console.log(`O produto escalar do vetor 1 e 2 é igual a ${soma}.`)
*/

// 8. Faça um programa que pede para o usuário digitar 5 números e, ao final, imprime um vetor com os 5 números digitados pelo usuário (sem converter os números para o tipo number).
// Exemplo: Se o usuário digitar 1, 5, 2, 3, 6, o programa deve imprimir o vetor [‘1’,‘5’,‘2’,‘3’,‘6’]
/*
const readline = require('readline-sync')

let cont = 0
let vetor = []
while (cont < 5){
  let num = readline.question('Digite um número: ')
  vetor.push(num)
  cont++
}

console.log(vetor)
*/

// 9. Pegue a lista gerada no exercício anterior e transforme cada um dos itens desse vetor em um number.
// OBS: Não é para alterar o programa anterior, mas sim o vetor gerado por ele. 
/*
let vetor1 = ['3', '2', '-9', '5', '1']
let vetor2 = []

for (let num of vetor1){
  vetor2.push(parseInt(num))
}

console.log(vetor2)
*/

// 10. Faça um programa que peça as 4 notas bimestrais e mostre a média aritmética delas, usando vetores.
/*
const readline = require('readline-sync')

let cont = 1
let soma = 0

while (cont <= 4){
  let nota = parseFloat(readline.question(`Digite a nota ${cont}: `))
  soma += nota
  cont++
}

let media = soma/4

console.log(`A média das notas é igual a ${media.toFixed(2)}.`)
*/

// 11. Sorteie um vetor de 10 números e imprima:
// a. um vetor com os 4 primeiros números;
// b. um vetor com os 5 últimos números;
// c. um vetor contendo apenas os elementos das posições pares;
// d. um vetor contendo apenas os elementos das posições ímpares;
// e. um vetor inverso do vetor sorteado (isto é, um vetor que começa com o último elemento o vetor sorteado e termina com o primeiro);
// f. um vetor inverso dos 5 primeiros números;
// g. um vetor inverso dos 5 últimos números.
/*
let vetor = []
for (let i = 0; i < 10; i++){
  let num = Math.floor(Math.random()*101)
  vetor.push(num)
}
console.log(`O vetor sorteado foi [${vetor}]`)

let vetorA = vetor.slice(0, 4)
console.log(`Vetor A: [${vetorA}].`)

let vetorB = vetor.slice(vetor.length - 5)
console.log(`Vetor B: [${vetorB}].`)

let vetorC = []
for (i = 0; i < vetor.length; i += 2){
  vetorC.push(vetor[i])
}
console.log(`Vetor C: [${vetorC}].`)

let vetorD = []
for (i = 1; i < vetor.length; i += 2){
  vetorD.push(vetor[i])
}
console.log(`Vetor D: [${vetorD}].`)

let vetorE = []
for (i = vetor.length - 1; i >= 0; i--){
  vetorE.push(vetor[i])
}
console.log(`Vetor E: [${vetorE}].`)
vetorE = []
for (let num of vetor){
  vetorE.unshift(num)
}
console.log(`Vetor E: [${vetorE}]`)

let vetorF5 = vetor.slice(0, 5)
let vetorF = []
for (let num of vetorF5){
  vetorF.unshift(num)
}
console.log(`Vetor F: [${vetorF}]`)

let vetorG = []
for (i = vetor.length - 1; i >= 5; i--){
  vetorG.push(vetor[i])
}
console.log(`Vetor G: [${vetorG}]`)
*/
// 12. Faça um programa que sorteia 10 números entre 0 e 100 e conte quantos números sorteados são maiores que 50.
/*
let vetor = []
for (let i = 0; i < 10; i++){
  let num = Math.floor(Math.random()*101)
  vetor.push(num)
}

let vetor50 = []
for (let n of vetor){
  if (n > 50)
  vetor50.push(n)
}

console.log(vetor50)
console.log(`Há ${vetor50.length} números maiores do que 50 no vetor.`)
*/
// 13. Faça um programa que sorteie 10 números entre 0 e 100 e imprima:
// a. o maior número sorteado;
// b. o menor número sorteado;
// c. a média dos números sorteados;
// d. a soma dos números sorteados.
/*
let vetor = []
for (let i = 0; i < 10; i++){
  let num = Math.floor(Math.random()*101)
  vetor.push(num)
}
console.log(`O vetor sorteado foi [${vetor}]`)

let maior = 0 
for (let num1 of vetor){
  if (num1 > maior)
  maior = num1
}
console.log(`a. O maior número sorteado é ${maior}`)

let menor = 101
for (let num2 of vetor){
  if (num2 < menor)
  menor = num2
}
console.log(`b. O menor número sorteado é ${menor}`)

let soma = 0
for (let num3 of vetor){
  soma += num3
}
let media = soma/vetor.length
console.log(`c. A média dos números sorteados é ${media}`)

console.log(`d. A soma dos números sorteado é ${soma}`)
*/
// 14. Desafio 1 - Faça um programa que peça para o usuário digitar o nome e a idade de um aluno e o número de provas que esse aluno fez. Depois, o programa deve pedir para o usuário digitar as notas de cada prova do aluno. Ao final o programa deve imprimir um vetor contendo:
// a. Nome do aluno na posição 0;
// b. Idade do aluno na posição 1;
// c. Um vetor com todas as notas na posição 2;
// d. A média do aluno na posição 3;
// e. true ou talse, caso a média seja maior que 5 ou não, na posição 4.
// Dica: Use o que você fez nos exercícios anteriores para criar esse programa.
/*
const readline = require('readline-sync')

let vetor = []
let notas = []
console.log(`Informações de aluno(a)`)
let nome = vetor.push(readline.question('Nome: '))
let idade = vetor.push(parseInt(readline.question('Idade: ')))
let quant = parseInt(readline.question('Quer inserir quantas notas? '))
for (i = 0; i < quant; i++){
  let nota = parseFloat(readline.question(`Nota ${i+1}: `))
  notas.push(nota)
}
vetor.push(notas)
let soma = 0
for (let num of notas){
  soma += num 
}
let media = soma / quant
vetor.push(media.toFixed(2))

let aprovado = media > 5 ? true : false
vetor.push(aprovado)

console.log(vetor)
*/
// 15. Desafio 2 - Faça um programa como o do item anterior, porém que imprima a média sem considerar a maior e menor nota do aluno (nesse caso o número de provas precisa ser obrigatoriamente maior que dois).
// Dica: crie uma cópia com o vetor de todas as notas antes de fazer a média.
/*
const readline = require('readline-sync')

let vetor = []
let notas = []
console.log(`Informações de aluno(a)`)
let nome = vetor.push(readline.question('Nome: '))
let idade = vetor.push(parseInt(readline.question('Idade: ')))
let quant = parseInt(readline.question('Quer inserir quantas notas? '))
for (i = 0; i < quant; i++){
  let nota = parseFloat(readline.question(`Nota ${i+1}: `))
  notas.push(nota)
}

notas.sort()
let subnotas = notas.splice(2, notas.length -1)

vetor.push(subnotas)

let soma = 0
for (let num of subnotas){
  soma += num 
}
let media = soma / (subnotas.length)
vetor.push(media.toFixed(2))

let aprovado = media > 5 ? true : false
vetor.push(aprovado)

console.log(vetor)
*/
// 16. Desafio 3 - Faça um programa que pede para o usuário digitar o CPF e verifica se ele é válido. Para isso, primeiramente o programa deve multiplicar cada um dos 9 primeiros dígitos do CPF pelos números de 10 a 2 e somar todas as respostas. O resultado deve ser multiplicado por 10 e dividido por 11. O resto dessa divisão deve ser igual ao primeiro dígito verificador (10º dígito). Em seguida, o programa deve multiplicar cada um dos 10 primeiros dígitos do CPF pelos números de 11 a 2 e repetir o procedimento anterior para verificar o segundo dígito verificador.
// Exemplo:
// Se o CPF for 286.255.878-87 o programa deve fazer primeiro:
// x = (2*10 + 8*9 + 6*8 + 2*7 + 5*6 + 5*5 + 8*4 + 7*3 + 8*2)
// Em seguida, o programa deve testar se x*10%11 == 8 (o décimo número do CPF). Se sim, o programa deve calcular:
// x = (2*11 + 8*10 + 6*9 + 2*8 + 5*7 + 5*6 + 8*5 + 7*4 + 8*3 + 8*2)
// e verificar se x*10%11 == 7 (o décimo primeiro número do CPF).
/*
function testeCPF(cpf){
  let soma = 0
  for (i = 0; i < 9; i++){
    soma += cpf[i]*(10-i)
  }
  let resto = soma*10%11
  let valido = (resto === 10 ? 0 : resto) == cpf[9] 
  
  if (valido){
    let soma = 0
    for (i = 0; i < 10; i++){
      soma += cpf[i]*(11-i)
  }
  let resto = soma*10%11
  let valido = (resto === 10 ? 0 : resto) == cpf[10]
  return valido
  }
  else{
    return false
  }
}    

console.log(testeCPF('36899553864'))
*/
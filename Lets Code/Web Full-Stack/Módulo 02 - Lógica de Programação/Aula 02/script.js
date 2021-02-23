// NPM
const readline = require('readline-sync') 

/* const idade = parseInt(readline.question('Informe sua idade: '))

console.log(idade, typeof idade)

const altura = parseFloat(readline.question('Informe sua altura: '))

console.log(altura, typeof altura) */

// 1. Faça um programa que peça as 4 notas bimestrais de um aluno e mostre a média aritmética delas.

/*
var nota1 = parseFloat(readline.question('Nota 1: '))
var nota2 = parseFloat(readline.question('Nota 2: '))
var nota3 = parseFloat(readline.question('Nota 3: '))
var nota4 = parseFloat(readline.question('Nota 4: '))
var media = (nota1+nota2+nota3+nota4)/4
console.log(media) */

// 2. Faça um programa que peça o raio de um círculo, calcule e mostre sua área.

/* var raio = parseFloat(readline.question('Raio da circunferência: '))
var area = 3.14*Math.pow(raio,2)
console.log(area) */

// 3. Faça um programa que peça a temperatura em graus Fahrenheit (F), transforme e mostre a temperatura em graus Celsius (°C).

/* var fahrenheit = parseFloat(readline.question('Temperatura em graus Fahrenheit: '))
var celsius = (5*(fahrenheit -32))/9
console.log(celsius.toFixed(2))     // Duas casas decimais */

// graus Fahreinheit (F) para graus Celsius (°C).
/* var celsius = parseFloat(readline.question('Temperatura em graus Celsius: '))
var fahrenheit = (celsius * 9/5) + 32
console.log(fahrenheit) */

const idade = 34
if (idade < 18) {
  console.log('Você é menor de idade')
} else if (idade == 34) {
  console.log('Você já é bem velho')
} else {
  console.log('Você é muito jovem')
}
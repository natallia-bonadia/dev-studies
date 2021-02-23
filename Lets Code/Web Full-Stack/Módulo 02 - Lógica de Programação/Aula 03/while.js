const readline = require('readline-sync')

/* let num = parseInt(readline.question('Digite um numero: '))
let count = 0
while (count <= num){
  console.log(count)
  count++
}

console.log('Fim do programa') */

// 1. Faça um algoritmo que peça para um usuário digitar um número e que só finaliza quando o usuário digitar 0.
/*
let num = 0

do {num = parseInt(readline.question('Digite um numero qualquer ou 0 para sair: '))
} while (num != 0)

console.log('Programa finalizado!')
*/
// 2. Peça ao usuário para digitar um número n e some todos os números de 1 a n.
/*
let n = parseInt(readline.question('Digite um numero inteiro: '))
let cont = 0
let soma = 0
while (cont <= n){
  soma += cont
  cont += 1
} 
console.log(soma)
*/
// 3. Faça um programa que peça para o usuário digitar a idade, o salário e o sexo de uma pessoa até que as entradas digitadas sejam válidas:
// Idade: entre 0 e 150;
// Salário: maior que 0;
// Gênero: M, F ou Outro.
/*
let idade, salario, sexo;
do {idade = parseInt(readline.question('Idade: '))
} while (idade < 0 || idade > 150);
do {salario = parseFloat(readline.question('Salário: '))
} while (salario < 0);
do {sexo = readline.question('Gênero: [M / F / Outro] ')
} while (sexo != 'M' && sexo != 'F' && sexo != 'Outro');
*/
// 4. Peça ao usuário para digitar um número e imprima o fatorial de n.
/*
let num = parseInt(readline.question('Digite um número: '))

let cont = 1
let soma = 1

while (cont <= num){
  soma *= cont
  cont++
}

console.log(`O fatorial de ${num} é ${soma}.`)
*/
// 5. Calcule a soma de até mil termos da série 1 + 1/2 + 1/4 + 1/8 + 1/16 + ...
//Dica! Use três variáveis:
// um contador, que começa em zero;
// uma variável para a soma de todos os termos, que também começa em zero;
// uma variável para cada termo, que começa em 1 e a cada loop é dividida por 2.
/*
let cont = 0
let soma = 0
let termo = 1

while (cont < 1000){
  soma += termo
  termo /= 2
  cont++
}

console.log(`A soma de todos os termos é ${soma}.`)
*/
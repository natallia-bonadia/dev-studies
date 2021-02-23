let numero = 4;

if (numero % 2 === 0){
  console.log('É par');
}

else{
  console.log('É ímpar!');
}

let numero2 = 7;

if (numero2 > 0){
  console.log('Positivo');
}

else if (numero2 === 0){
  console.log('Zero');
}

else{
  console.log('Negativo');
}


//Se não define a variável, ele interpreta falso
let num3;

if (num3){
  console.log('Truthy');
}

else{
  console.log('Falsy');
}

let paridade = numero % 2 ? 'ímpar' : 'par';
console.log(paridade);

let maior2 = numero2 > 0 ? numero2 : -1*numero2;
console.log(maior2);

console.log(2>1 && true);

console.log(2>1 || false)

let idade = 16;
if (idade < 12){
console.log('Criança');
}
else if (12 <= idade <= 18){
console.log('Adolescente');
}
else if (18 <= idade <= 60){
console.log('Adulto');
}

else{
console.log('Idoso');
}


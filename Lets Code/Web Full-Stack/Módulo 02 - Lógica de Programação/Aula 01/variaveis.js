// var não obedece escopo
//var nome = prompt("Digite seu nome: ");

//let respeita escopo
//let console.log(nome);
// alert("Teste");
// console.log("teste");

//constante (não modifica)
const pi = 3.1415;
//pi = 3; (apresenta erro)
let nome = 'Natallia';
console.log(typeof nome);
nome = 230;
console.log(typeof nome);

// string, number, undefined e boolean

let estaSol = true;
console.log(typeof estaSol)

let vazio = null
let soma = function(a,b){return a+b;}
console.log(soma(1,3));
let vetor = [1,2,3];
let objeto = {numero: 23};
console.log(objeto.numero);

// Javascript tem a tipagem FRACA, faz a conversão 'sozinho' da string para número
// Python tem a tipagem FORTE
console.log(1+'1');
console.log('10'/2);

// parse 'transforma' a variável na função seguida a ela
let num = parseInt('12');
let num2 = parseFloat('15.123');
console.log(parseInt('12.2'));
console.log(typeof parseInt('12A9'));

console.log(1 === '1');

// Operações numéricas

1+1
1-1
4/3
3%2
2*3

console.log(Math.pow(3,2));
console.log(Math.floor(15.3));
console.log(Math.ceil(15.3));
console.log(Math.PI)
console.log(Math.random()*5);
console.log('A'+'B'+'C');
console.log(5*'A')
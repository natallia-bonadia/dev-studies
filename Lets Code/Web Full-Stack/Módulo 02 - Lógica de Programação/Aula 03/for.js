let vetor1 = [4, 5, 2, 6, 8, 4, 0, 10]
let vetor2 = [8, 4, 2, 4, 1, 0, 6, -2]
/*
// variável i com início em 0, final em 7, incrementanto de 1 em 1
for (let i = 0; i < 7; i++){
  console.log(vetor1[i]) //acessa os elementos de acordo com o índice
}
// acessa todos os elementos, até o fim
for (let i = 0; i < vetor1.length; i++){
  console.log(vetor1[i])
}

let vetor3 = []
for (let i = 0; i < vetor1.length; i++){
  vetor3.push(vetor1[i]+vetor2[i])
}
console.log(vetor3)
*/

let vetor3 = []
/*
for (let i =0; i < vetor1.length; i++){
  vetor3 = vetor1[i] + vetor2[i]
}

console.log(vetor3)
*/

for (let num of vetor1){ //acessa os elementos do vetor
  console.log(num)
}

for (let i in vetor1){ //acessa os índices dos elementos do vetor
  console.log(i)
}

for (let i in vetor1) { //acessa os índices e elementos do vetor
  console.log(`índice ${i} : elemento ${vetor1[i]}`)
}
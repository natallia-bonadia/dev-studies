let matriz = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

// console.log(matriz[1])
// console.log(matriz[1][2])

/*
for (let i = 0; i < matriz.length; i++){
  for (let j = 0; j < matriz[i].length; j++){
    console.log(matriz[i][j])
  }
}
*/

let vetor = [1, 2, 3, 4, 5, 6, 7, 8]
/*
let [primeiro, segundo, ...resto] = vetor
console.log(primeiro)
console.log(segundo)
console.log(resto)
console.log(vetor) // permanece igual
*/
function soma_vetor(vetor){
  if (vetor.length === 0) return 0
  const [primeiro, ...resto] = vetor
  return primeiro + soma_vetor(resto)
}

console.log(soma_vetor([1, 2, 3]))

let vetor2 = [...vetor, 9, 10, 11, 12]
console.log(vetor2)
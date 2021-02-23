let vetor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
/*
vetor1 = vetor1.filter( (_, index) => index % 2 === 0 )
console.log(vetor1)

let vetor2 = [1, 0, -4, false, 7, null, 8, null, true, 4, '0', 1, 'bar', '']
let vetor3 = [1, 0, -4, false, 7, null, 8, null, true, 4, '0', 1, 'bar', '']
vetor2 = vetor2.filter( x => x )
vetor3 = vetor3.filter( x => typeof x === 'number' )
console.log(vetor2)
console.log(vetor3)
*/
const byHalf = (num, index, vector) => index < vector.length/2 || num % 2 === 0
console.log(vetor1.filter(byHalf))
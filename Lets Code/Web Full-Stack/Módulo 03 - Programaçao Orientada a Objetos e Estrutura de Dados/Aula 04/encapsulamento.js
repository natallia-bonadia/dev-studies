/*
class Retangulo {

  constructor(base, altura) {
    this._base = base
    this._altura = altura
  }

  // getter
  get base() { return this._base }

  get altura() { return this._altura }

  // setter
  set base(novaBase) {
    if (typeof(novaBase) !== 'number') throw 'O valor de base deve ser um número'
    this._base = novaBase
  }

  set altura(novaAltura) {
    if (typeof(novaAltura) !== 'number') throw 'O valor da altura deve ser um número'
    this._altura = novaAltura
  }

  get area() { return this._base * this._altura }

}

const rect = new Retangulo(5, 2)
rect.base = 15
rect.altura = 10
rect.area = 30
rect.cor = 'preto'
console.log(rect)
// rect.setBase('Pietro')
// rect.base = 'Pietro'
//console.log(rect.base)
*/


class Quadrado {
  
  constructor(lado) {
    this._lado = lado
  }

  get lado() {
    return this._lado  
  }

  set lado(novoLado) {
    if (typeof(novoLado) !== 'number' || novoLado <= 0) throw 'O valor do lado deve ser um número e maior do que zero.'
    this._lado = novoLado  
  }

  get area() {
    return this._lado**2
  }
}

const quad = new Quadrado(2)
console.log(quad)
quad.lado = 2
quad._lado = -10

console.log(quad)
console.log(quad.area)
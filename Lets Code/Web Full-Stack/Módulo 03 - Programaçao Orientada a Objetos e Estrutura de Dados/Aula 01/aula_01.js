class Quadrado {
  
  /*
  Atributos:
  + lado
  + cor
  */

  cor
  
  constructor (lado) {
    if (isNaN(lado)) throw "lado deve ser um número"
    this.lado = lado  
  }

  calcularArea() {
    const area = this.lado * this.lado
    return area
  }

  calcularPerimetro() {
    const perimetro = this.lado * 4
    return perimetro
  }
}

const quadrado1 = new Quadrado(10)
const area = quadrado1.calcularArea()
const perimetro = quadrado1.calcularPerimetro()

console.log(quadrado1)
console.log(area)
console.log(perimetro)
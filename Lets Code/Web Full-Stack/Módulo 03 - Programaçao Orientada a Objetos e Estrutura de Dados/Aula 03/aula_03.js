function Retangulo (base, altura) {
  
  this.base = base
  this.altura = altura
  
  this.calcularArea = () => {
    return this.altura * this.base
  }
}

const rect = new Retangulo(5,10)
console.log(rect)
console.log(rect.calcularArea())
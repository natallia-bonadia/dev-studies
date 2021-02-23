/*
1. Crie uma classe chamada Retangulo que deve possuir os atirbutos privados base e altura, e, além do construtor, crie um método chamado calcularArea() que retorna a área desse retângulo multiplicando base por altura.
*/
/*
class Retangulo {

  constructor(base, altura) {
    this._base = base
    this._altura = altura
  }
  
  calcularArea() {
    return this._base*this._altura
  }

}

const rect = new Retangulo(5, 10)
console.log(rect.calcularArea())
*/
/*
---------------------------------------------------------------------------------------------

2. Crie uma classe que herda de Ponto2D chamada Ponto3D que tem como atributo adicional "z", reimplemente o método calcularDistancia() na classe Ponto3D que desta vez deve receber uma outra instância de Ponto3D.

O cálculo da distância entre dois pontos 3D é dado pela raizQuadrada(x² + y² + z²)

---------------------------------------------------------------------------------------------

3. Crie uma classe chamada Ponto2D que possui os atributos x e y (ambos privados), crie o construtor dessa classe e um método calcularDistancia() que recebe como parâmetro uma outra instância de Ponto2D.

A fórmula para calcular a distância entre dois pontos é dada pela raiz quadrada de (x² + y²).

*/
/*
class Ponto2D {
  
  constructor(x, y){
    this._x = x
    this._y = y
  }

  calcularDistancia(ponto){
    if (!(ponto instanceof Ponto2D)) throw `ERRO`
    return ((ponto._x - this._x)**2 + (ponto._y - this._y)**2)**(1/2)
  }

}

class Ponto3D extends Ponto2D {
 
  constructor(x, y, z){
    super(x, y)
    this._z = z
  }

  calcularDistancia(ponto){
    if (!(ponto instanceof Ponto3D)) throw `ERRO`
    return ((ponto._x - this._x)**2 + (ponto._y - this._y)**2 + (ponto._z - this._z)**2)**(1/2)
  }

}

const ponto1 = new Ponto3D (4, 6, 1)
const ponto2 = new Ponto3D (1, 3, 9)
console.log(ponto1.calcularDistancia(ponto2))
*/
/*
---------------------------------------------------------------------------------------------

4. Crie uma classe chamada Cubo que herda da classe Quadrado da questão anterior, e tem como atributo aticional o comprimento. Crie, além do construtor, um método chamado calcularVolume que deve fazer uso do método calcularArea da super classe, multiplicando o retorno desse método pelo valor de comprimento para obter o volume final.
*/

class Quadrado {
  
  constructor(lado) {
    this._lado = lado
  }

  calcularArea() {
    return this._lado*this._lado
  }

}

class Cubo extends Quadrado {
  
  constructor(lado, comprimento) {
    super(lado)
    this._comprimento = comprimento
  }

  calcularVolume() {
    return this.calcularArea()*this._comprimento
  }

}

const cubo = new Cubo(2, 3)
console.log(cubo.calcularVolume())
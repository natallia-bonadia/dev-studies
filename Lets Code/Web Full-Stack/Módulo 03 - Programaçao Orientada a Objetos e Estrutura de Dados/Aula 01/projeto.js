const rangeCategorias = ['Lanches', 'Brasileira', 'Janponesa']

class Restaurante {

  /*Atributos
  capacidade
  categoria
  nome
  endereço
  horario de funcionamento
  menu
  */
  
  constructor (nome, categoria, capacidade, horario_abertura, horario_fechamento) {

    this._nome = nome;
    this._categoria = categoria;
    this.capacidade = capacidade;
    this.horario_abertura = horario_abertura
    this.horario_fechamento = horario_fechamento
    this.menu = []
  
  }

  get nome() { return this._nome }

  set nome() {novoNome} {
    if (typeof(novoNome) !== 'string') throw 'novoNome deve ser uma string'
  }
  addToMenu (...itemCardapios){
    this.menu.push(...itemCardapios)
  }

  introductionText() {
    return `
--------------------------------------------------------
Seja bem-vindo ao ${this.nome}!

A lotação máxima do nosso estabelecimento durante a
pandemia é de ${Math.floor(this.capacidade / 2)} pessoas.

Nosso horário de funcionamento é das ${this.horario_abertura} até às ${this.horario_fechamento}.
--------------------------------------------------------
  `}

  getFormattedMenu() {
    const formattedMenu = this.menu.reduce((currentText, currentItem, currentIdx) => {return currentText + `${currentIdx+1} - ${currentItem.toString()}\n`}, '')
    return formattedMenu
  }

  run () {
    console.log(this.introductionText())
    console.log(this.getFormattedMenu())
  }
}

class ItemCardapio {
  constructor (nome, preco, categoria) {
    this.nome = nome
    this.preco = preco
    this.categoria = categoria
  }

  toString() {
    return `${this.nome}${' '.repeat(14 - this.nome.length)}.................... R$ ${this.preco} (${this.categoria})`
  }
}

const restaurante = new Restaurante('Pietro\'s Cafe', 'Cafeteria', 50, '07:00', '18:00')
const bebida_matinal1 = new ItemCardapio('Café Coado', 4.00, 'Matinal')
const bebida_matinal2 = new ItemCardapio('Café Expresso', 5.00, 'Matinal')
const bebida_matinal3 = new ItemCardapio('Capuccino', 7.00, 'Matinal')
const bebida_matinal4 = new ItemCardapio('Chá', 5.00, 'Matinal')
const bebida_matinal5 = new ItemCardapio('Suco', 8.00, 'Matinal')
const bebida_matinal6 = new ItemCardapio('Vitamina', 10.00, 'Matinal')

restaurante.addToMenu(bebida_matinal1, bebida_matinal2, bebida_matinal3, bebida_matinal4, bebida_matinal5, bebida_matinal6)

restaurante.run()
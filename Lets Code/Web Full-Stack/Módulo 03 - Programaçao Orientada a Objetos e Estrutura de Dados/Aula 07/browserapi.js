/*
1. Crie uma classe chamada HTMLBaseElement que deve possuir os atributos:

    - tagName: string
    - id: string
    - classList: string[]
    - name: string
    - style: object

Todos os atributos são privados, e devem ser feitas as validações conforme o tipo de cada valor especificado acima.

No construtor da classe, fora o valor para tagName, nenhum é obrigatório, os valores default de cada atributo não obrigatório devem ser:

    id: undefined
    classList: []
    name: undefined
    style: {}

O atributo classList deverá poder ser manipulado através de um método addClass(className: string) que deve adicionar a classe passada como parâmetro no array em questão, e o método removeClass(className: string) para remover uma classe do array.
*/

function validaString (parametro, nomeParametro) {
  if (typeof(parametro) !== 'string') throw `${nomeParametro} deve ser uma string`
}

class HTMLBaseElement {
  constructor(tagName, id = undefined, classList = [], name = undefined, style = {}) {
      this.tagName = tagName
      this.id = id
      this.classList = classList
      name !== undefined ? this.name = name : undefined
      this.style = style
  }

  get tagName() { return this._tagName }
  set tagName(newTagName) {
    validaString(newTagName, 'tagName')
    this._tagName = newTagName
  }

  get id() { return this._id }
  set id(newId) {
    validaString(newId, 'id')
    this._id = newId
  }

  get classList() { return this._classList }
  set classList(newClassList) {
    try {
      newclassList.forEach(item => {
          validaString(item, 'item')
      })
      this._classList = newclassList
    } 
    catch (err) {
      throw "classList deve ser um array de strings"
    }
  }

  get name() { return this._name }
  set name(newName) {
    validaString(newName, 'newName')
    this._name = newName
  }

  addClassList(className) {
    validaString(className)
    if (!(this.classList.includes(className))) this.classList.push(className)
    else console.log(`Essa classe já existe.`)
  }

  removeClassList(className) {
    validaString(className, 'classname')
    let posicao = this._classList.indexOf(className)
    if (posicao >= 0){
        this._classList.splice(posicao, 1)
    }
    else {
        throw 'Este elemento não existe'
    }
  }

}

function validaChild (parametro, nomeParametro) {
  if (typeof(parametro) !== 'string') throw `${nomeParametro} deve ser uma string`
}

class HTMLParentElement extends HTMLBaseElement {

  children = []

  appendChild(child) {
      this.children.push(child)
  }

  removeChildBy(property, value) {
      const indice = this.children.findIndex(elemento => elemento[property] == value)
      if (indice === -1) throw `propriedade e/ou valor não encontrado`
      this.children.splice(indice, 1)
  }

}

class HTMLInputElement extends HTMLBaseElement {

  constructor(tagName, id = undefined, classList = [], name = undefined, style = {}, onClick) {
      super(tagName, id, classList, name, style)
      this.onClick = onClick
  }

  get onClick() { return this._onClick; }
  set onClick(newonClick) {
    if (typeof(newonClick) !== 'function') throw `onClick precisa ser uma função`
      this._onClick = newonClick
  }
}

//////////////
class HTMLTableElement extends HTMLParentElement {

  _validTags = ['thead', 'tbody', 'tfoot', 'tr', 'th']

  _validateChild(child) {
      super._validateChild(child);
      if (!this._validTags.includes(child.tagName)) throw `HTMLTableElement should have one of ${this._validTags.join(', ')}, not ${child.tagName}`;
  }

  appendChild(child) {
      this._validateChild(child);
      super.appendChild(child);
  }
}

class HTMLImageElement extends HTMLBaseElement {

  constructor(tagName, src, alt='', id = undefined, classList = [], name = undefined, style = {}) {
      super(tagName, id, classList, name, style);
      this.src = src;
      this.alt = alt;
  }

  get src() { return this._src; }
  set src(_src) {
      validarString(_src, 'src');
      this._src = _src;
  }

  get alt() { return this._alt; }
  set alt(_alt) {
      validarString(_alt, 'alt');
      this._alt = _alt;
  }
}


const h1 = new HTMLBaseElement('h1')
/* PERGUNTA
1. Crie uma classe Cliente cujos atributos são nome, idade e e-mail. Construa um método que imprima as informações tal como abaixo:
Nome: Fulano de Tal

Idade: 40

E-mail: fulano@mail.com


RESPOSTA:
*/
/*
class Clients {
  
  // Atributos:
  // name
  // age
  // email
  
  constructor(name, age, email){
    this.name = name
    this.age = age
    this.email = email
  }

  getFormatted () {
    console.log(`-----------------------------------
Nome: ${this.name}
Idade: ${this.age}
E-mail: ${this.email}
-----------------------------------\n`)
  }
}

const user1 = new Clients ('Natallia', 32, 'natallia.bonadia@gmail.com')
const user2 = new Clients ('Gil', 34, 'gilblas07@hotmail.com')

user1.getFormatted()
user2.getFormatted()


--------------------------------------------------------------------------
*/

/* PERGUNTA
2. Crie uma classe Bola cujos atributos são cor e raio. Crie um método que imprime a cor da bola. Crie um método para calcular a área dessa bola. Crie um método para calcular o volume da bola. Crie um objeto dessa classe e calcule a área e o volume, imprimindo ambos em seguida.

Obs.:

Área da esfera = 4*3.14*r*r;

Volume da esfera = 4*3.14*r*r*r/3

RESPOSTA
*/
/*
class Ball {

  // Atributos:
  // color
  // radius

  constructor(color, radius){
    this.color = color
    this.radius = radius
  }

  getColor() {
    return `A cor da bola é ${this.color}`
  }

  calculateArea() {
    return `O valor da área é ${Math.floor(4*3.14*(this.radius)**2)}`
  }

  calculateVolume() {
    return `O valor do volume é ${Math.floor(4*3.14*(this.radius**3)/3)}`
  }

  getInfos() {
    console.log(this.getColor())
    console.log(this.calculateArea())
    console.log(this.calculateVolume())
  }
}

const ball = new Ball('azul', 10)
ball.getInfos()

--------------------------------------------------------------------------
*/

/* PERGUNTA
3. Crie uma classe Retângulo cujos atributos são lado_a e lado_b. Crie um método para calcular a área desse retângulo. Crie um objeto dessa classe e calcule a área e a imprima em seguida.

RESPOSTA
*/
/*
class Rectangle {

  // Atributos:
  // side_a
  // side_b

  constructor (side_a, side_b){
    this.side_a = side_a
    this.side_b = side_b
  }

  getArea(){
    return `A área do retângulo é ${this.side_a*this.side_b}.`
  }
}

const rectangle = new Rectangle (5, 8)

console.log(rectangle.getArea())

--------------------------------------------------------------------------
*/

/* PERGUNTA
4. Crie uma classe Funcionario cujos atributos são nome e e-mail, horas trabalhadas e salário. Guarde as horas trabalhadas como um objeto (sem necessariamente utilizar classes) cujas chaves são o mês em questão e, como outro objeto, guarde o salário por hora relativo ao mês em questão. Crie um método que retorna o salário mensal do funcionário.

RESPOSTA
*/
/*
class Employee {

  // Atributos:
  // name
  // e-mail
  // worked_hours
  // salary

  constructor(name, email){
    this.name = name
    this.email = email
    this.worked_hours = {jan: 120, feb: 105, mar: 124, apr: 112, may: 115, jun: 121, jul: 112, aug: 130, sep: 107, oct: 0, nov: 113, dec: 101}
    this.salary = {jan: 60, feb: 60, mar: 60, apr: 60, may: 60, jun: 60, jul: 68, aug: 68, sep: 68, oct: 68, nov: 68, dec: 68}
    this.totalSalary = []
    this.totalYear = 0
  }

  getTotalSalary() {
    console.log(`
Funcionário(a): ${this.name}
E-mail: ${this.email}\n`)
    for (let month in this.worked_hours){
      let totalMonth = this.worked_hours[month]*this.salary[month]
      console.log(`${month}: R$ ${totalMonth}`)
      this.totalYear += totalMonth
    }
    console.log(`---------------\nTot: R$ ${this.totalYear}\n`)
  }
}

const employee = new Employee('Maria', 'maria@gmail.com')
employee.getTotalSalary()

--------------------------------------------------------------------------
*/

/* PERGUNTA
5. Crie uma classe Televisor cujos atributos são:

a. fabricante;

b. modelo;

c. canal atual;

d. lista de canais; e

e. volume.

Faça métodos para aumentar/diminuir volume, trocar o canal e sintonizar um novo canal, que adiciona um novo canal à lista de canais (somente se esse canal não estiver nesse vetor). No atributo lista de canais, devem estar armazenados todos os canais já sintonizados dessa TV.

Obs.: O volume não pode ser menor que zero e maior que cem; só se pode trocar para um canal que já esteja na lista de canais.

RESPOSTA
*/
/*
const input = require('readline-sync')

class Television {

  // Atibutos:
  // producer
  // model
  // actual_channel
  // channel_list
  // volume

  constructor(producer, model, actual_channel, volume) {
    this.producer = producer
    this.model = model
    this.actual_channel = actual_channel
    this.volume = volume
    this.channel_list = [2, 4, 5, 7, 9, 13]
  }

  tvInfos() {
    console.log(`\nInformações da Televisão\nFabricante: ${this.producer}\nModelo: ${this.model}\n`)
  }

  increaseVol() {
    if (this.volume >= 100){
      this.volume == 100
      console.log('Volume máximo')
      return
    }
    this.volume++
    console.log(`Volume ${this.volume}`)
  }

  decreaseVol() {
    if (this.volume <= 0){
      this.volume == 0
      console.log('Volume mínimo')
      return
    }
    this.volume--
    console.log(`Volume ${this.volume}`)
  }
  
  changeChannel() {
    let idx = this.channel_list.indexOf(this.actual_channel)
    if (idx == this.channel_list.length - 1) {
      this.actual_channel = this.channel_list[0]}
    else this.actual_channel = this.channel_list[idx+1]
    console.log(`Canal ${this.actual_channel}`)
  }

  addChannel(new_channel) {
    const channel = this.channel_list.filter(element => element === new_channel).length === 0
    if (channel) {this.channel_list.push(new_channel)
      console.log(`Sintonizando canal...\nCanal ${new_channel} sintonizado.`)}
    else {
      console.log(`Canal já foi sintonizado.`)}
  }
}

const television = new Television ('Samsung', 'Smart TV 65"', 7, 50)

television.tvInfos()
television.increaseVol()
television.increaseVol()
television.increaseVol()
television.increaseVol()
television.decreaseVol()
television.decreaseVol()
television.changeChannel()
television.addChannel(11)
television.changeChannel()
television.addChannel(21)
television.changeChannel()
television.changeChannel()
television.changeChannel()


--------------------------------------------------------------------------
*/

/* PERGUNTA
6. Crie uma classe ControleRemoto cujo atributo é televisão (isso é, recebe um objeto da classe do exercício anterior). Crie métodos para aumentar/diminuir volume, trocar o canal e sintonizar um novo canal, que adiciona um novo canal à lista de canais (somente se esse canal não estiver nessa lista).

RESPOSTA
*/
/*
class ControleRemoto {

  constructor(television){
    this.television = television
  }

  tvInfos() {
    this.television.tvInfos()
  }

  increaseVol() {
    this.television.increaseVol()
  }

  decreaseVol() {
    this.television.decreaseVol()
  }

  changeChannel() {
    this.television.changeChannel()
  }

  addChannel(new_channel) {
    this.television.addChannel(new_channel)
  }

}

const remoteControl = new ControleRemoto(television)

remoteControl.tvInfos()
remoteControl.increaseVol()
remoteControl.increaseVol()
remoteControl.increaseVol()
remoteControl.increaseVol()
remoteControl.decreaseVol()
remoteControl.decreaseVol()
remoteControl.changeChannel()
remoteControl.addChannel(10)
remoteControl.changeChannel()
remoteControl.addChannel(13)
remoteControl.changeChannel()
remoteControl.changeChannel()
remoteControl.changeChannel()

--------------------------------------------------------------------------
*/

/* PERGUNTA
7. Crie uma modelagem de classes para uma agenda capaz de armazenar contatos. Através dessa agenda é possível incluir, remover, buscar e listar contatos já cadastrados.

RESPOSTA
*/
/*
class ContactBook {
  
  constructor(contact) {
    this.contact = contact
    this.contacts = []
  }

  addContact(name, last_name, phone, email) {
    this.contact = {name, last_name, phone, email}
    this.contacts.push(this.contact)
  }

  contactList() {
    for (let contact of this.contacts)
    console.log(`
----------------------------------------
Nome: ${contact.name}
Sobrenome: ${contact.last_name}
Telefone: ${contact.phone}
E-mail: ${contact.email}
----------------------------------------\n`)
  }

  searchContact(name) {
    const contact = this.contacts.filter(element => element.name === name) 
      if (contact.length === 1) {
        console.log(`
----------------------------------------
Nome: ${contact[0].name}
Sobrenome: ${contact[0].last_name}
Telefone: ${contact[0].phone}
E-mail: ${contact[0].email}
----------------------------------------`)}
      else console.log('\nContato não encontrado\n')
  }

  deleteContact(name) {
    const contact = this.contacts.filter(element => element.name === name)
    if (contact.length == 1) {
    this.contacts.splice(this.contacts.indexOf(contact[0]), 1)
    console.log('Contato excluído')
    }
  }
}

const contacts = new ContactBook([])

contacts.addContact('Cibelle', 'Bonadia', '(11) 952322918', 'cibelleb@gmail.com')
contacts.addContact('Elenice', 'Ribeiro', '(11) 992870572', 'elenice.ribeiro@gmail.com')
contacts.addContact('Gil', 'Rudge', '(11) 972853999', 'gilrudge07@hotmail.com')
contacts.addContact('Juliana', 'Nogueira', '(11) 966789471', 'juliana.nogueira@hotmail.com')
contacts.addContact('Natallia', 'Bonadia', '(11) 986619333', 'natallia.bonadia@gmail.com')
contacts.addContact('Vanessa', 'Rudge', '(11) 956552384', 'vanessa.rudge@gmail.com')
contacts.contactList()
contacts.searchContact('Gil')
contacts.searchContact('Maria')
contacts.deleteContact('Vanessa')
contacts.contactList()
*/
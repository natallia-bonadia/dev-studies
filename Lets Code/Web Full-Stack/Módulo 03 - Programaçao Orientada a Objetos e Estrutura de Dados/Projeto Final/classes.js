const fs = require('fs')
const dadosCadastro = require('./projeto')
registrarPonto = require('./data')

class Empresa {
  constructor(nomeEmpresa, nome, email, senha) {
    this.nomeEmpresa = nomeEmpresa
    this.nome = nome
    this.email = email
    this.senha = senha
  }

  novaEmpresa() {
    const novaEmpresa = {
      'empresa': this.nomeEmpresa,
      'administrador': {
        'nome': this.nome,
        'e-mail': this.email,
        'senha': this.senha
      },
      'funcionarios': []
    }
    return novaEmpresa
  }
  
  // adicionarFuncionario(funcionario) {
  //   if (!(funcionario instanceof Funcionario)) throw `${funcionario} não é uma instância de Funcionário`
  //   this.funcionarios.push(funcionario) 
  // }

}

class Funcionario extends Empresa {
  constructor(nome, email, senha) {
    super(nome, email, senha)
    this.infos = []
  }

  novoFuncionario(){
    const novoFuncionario = {
      'nome': this.nome,
      'e-mail': this.email,
      'senha': this.senha,
      'informacoes': []
    }
    return novoFuncionario
  }

  registrarPonto(){
    this.infos.push(registrarPonto())
  }
}

class Informacoes {
  constructor(data, tipo){
    this.data = data
    this.tipo = tipo
  }

}

module.exports = {Empresa, Funcionario, Informacoes}
const input = require('readline-sync')
const fs = require('fs')

// Menu inicial para acessar ou criar uma conta

function menuUser(){
  const menu = (`
Seja Bem-Vindo ao Banco JS

---------------------------
         Banco JS     
---------------------------
1 - Criar conta
2 - Já sou cliente
3 - Acesso gerente
0 - Encerrar sessão
---------------------------
`)
  console.log(menu)}

// Função para criar conta

let users = JSON.parse(fs.readFileSync('users.json').toString())

function createAccount(){
  console.log(`
---------------------------
      Abra sua conta     
---------------------------

Por favor, preencha o formulario abaixo com seus dados
`)
  const account = parseInt((Math.random()+1)*100000)
  const cpf = parseInt(input.question('CPF (somente numeros): '))
  let name = input.question('Nome completo: ').toUpperCase()
  let cellphone = parseInt(input.question('Celular (somente numeros): '))
  let email = input.question('E-mail: ').toLowerCase()
  let password = parseInt(input.question('Senha (4 digitos numericos): '))
  console.log(`\n${name}, agora você é cliente do Banco JS\nO número da sua conta é: >>> ${account} <<<`)
  input.question()
  let user = {account: account, cpf: cpf, name: name, cellphone: cellphone, email: email, password: password, balance: 0, loan: 'N', valueLoan: 0}
  return(users.push(user))
}

// Função para validar conta e senha

let validAccount
let validPassword
let validUsers

function validation(){
  console.log(`
---------------------------
      Faça seu login     
---------------------------
`)
  validAccount = parseInt(input.question('Digite sua conta: '))
  validPassword = parseInt(input.question('Digite sua senha: '))
  validUsers = users.filter(
      element => element.account == validAccount && element.password == validPassword)
  return validUsers.length > 0
}

// Escolhendo a opção do menu inicial

let optionUser

do {console.log()
menuUser()
optionUser = parseInt(input.question('Escolha uma opcao: '))
} while (optionUser < 0 || optionUser > 3)

while (optionUser != 0){
  if (optionUser == 1){
    createAccount()
    do {menuUser()
      optionUser = parseInt(input.question('Escolha uma opcao: '))
      } while (optionUser < 0 || optionUser > 3)
  }

  if (optionUser == 2){
    {while (validation() == false)
    console.log('\nConta e/ou senha invalida(s). Tente novamente.')}

// Menu principal das funcionalidades bancárias

    {function menuClient(){
      const menu = (`
---------------------------
      Menu - Banco JS     
---------------------------
1 - Saldo
2 - Saque
3 - Deposito
4 - Pagamento de contas
5 - Transferencias
6 - Pedir empréstimo
7 - Alterar senha
0 - Encerrar sessão
---------------------------
`)
      console.log(menu)}

// Escolhendo a opção do menu principal

    let optionClient
    let correct
    console.log(`\n\n> Olá, ${validUsers[0].name}`)
    if (validUsers[0].loan == 'SIM')
    {console.log ('Parabéns, seu emprestimo foi aprovado!')
    validUsers[0].balance += validUsers[0].valueLoan
    validUsers[0].loan = 'N'
    validUsers[0].valueLoan = 0
    input.question()}

    if (validUsers[0].loan == 'NAO')
    {console.log ('Infelizmente o seu emprestimo não pode ser aprovado!')
    validUsers[0].loan = 'N'
    validUsers[0].valueLoan = 0
    input.question()}

    do {menuClient()
    optionClient = parseInt(input.question('Escolha uma opcao: '))
    } while (optionClient < 0 || optionClient > 7)

    while (optionClient != 0){
      if (optionClient == 1){
        console.log(`\nSeu saldo atual: R$ ${validUsers[0].balance}`)
        input.question()
      }
      else if (optionClient == 2){
        let retire = parseFloat(input.question('Digite o valor do saque: '))
        if (retire > validUsers[0].balance) console.log('Saldo insuficiente.')
        else{console.log('\nSaque realizado.\nRetire suas notas.')
        validUsers[0].balance -= retire}
        input.question()
      }
      else if (optionClient == 3){
        let deposit = parseFloat(input.question('Digite o valor do deposito: '))
        console.log('\nInsira o envelope e aguarde o comprovante.')
        input.question()
        console.log('Deposito realizado.')
        validUsers[0].balance += deposit
        input.question()
      }
      else if (optionClient == 4){
        let barCode = input.question('Digite o codigo de barras: ')
        let price = parseFloat(input.question('Digite o valor da conta: '))
        let rate = parseFloat(input.question('Digite o valor do juros e/ou multa: '))
        if ((price+rate) > validUsers[0].balance) console.log('Saldo insuficiente.')
        else {console.log('\nSeu pagamento foi realizado.')
        validUsers[0].balance -= (price+rate)}
        input.question()
      }
      else if (optionClient == 5){
        let value
        let validTransfer
        while (correct != 'S'){
        let transfer = parseInt(input.question('Digite o numero da conta para transferencia: '))
        validTransfer = users.filter(
          element => element.account == transfer)
        value = parseFloat(input.question('Valor da transferencia: '))
        console.log(`
Dados para deposito:\n
Nome: ${validTransfer[0].name}
Conta: ${validTransfer[0].account}
Valor: R$ ${value}
`)
        correct = input.question('Os dados estao corretos? [S / N] ').toUpperCase()}
        if (value > validUsers[0].balance) console.log('Saldo insuficiente.')
        else {console.log('Transferencia realizada.\nRetire o comprovante.')
        validUsers[0].balance -= value
        validTransfer[0].balance += value}
        input.question()
      }
      else if (optionClient == 6){
        validUsers[0].loan = input.question(`${validUsers[0].name.toUpperCase()}, voce confirma a solicitacao de emprestimo? [S / N] `).toUpperCase()
        validUsers[0].valueLoan = parseFloat(input.question('Valor do emprestimo? '))
        console.log('\nSolicitacao realizada. \nSe o emprestimo for autorizado pelo seu gerente o valor será creditado na sua conta em até 2 dias uteis.')
        input.question()
      }
      else if (optionClient == 7){
        let oldPass = parseInt(input.question('Digite a senha atual: '))
        if (oldPass == validUsers[0].password){
          validUsers[0].password = parseInt(input.question('Digite a nova senha de 4 digitos numericos: '))
          console.log('\nSenha modificada com sucesso.')
        }
        else console.log('Senha atual incorreta.')
        input.question()
      }
      do {menuClient()
        optionClient = parseInt(input.question('Escolha uma opcao: '))
        } while (optionClient < 0 || optionClient > 7)
      } break
    }
  }

// Acesso do gerente para liberacao de emprestimo

  let optionManager
  const menuManager = (`
---------------------------
      Menu - Banco JS      
---------------------------
1 - Pesquisar cliente
2 - Autorizar emprestimo
0 - Encerrar sessão
---------------------------
`)

  if (optionUser == 3){
    {while (validation() == false)
    console.log('\nConta e/ou senha invalida(s). Tente novamente.')}

    {console.log(`\n\n> Olá, ${validUsers[0].name.toUpperCase()}`)
    console.log(menuManager)
    do {optionManager = parseInt(input.question('Escolha uma opcao: '))
      } while (optionManager < 0 || optionManager > 2)}

    {while (optionManager != 0){
      if (optionManager == 1){
        let client = parseInt(input.question('Digite a conta do cliente: '))
        let searchClient = users.filter(
          element => element.account == client)
          console.log(`
---------------------------
Dados do cliente:\n
Nome: ${searchClient[0].name.toUpperCase()}
Conta: ${searchClient[0].account}
CPF: ${searchClient[0].cpf}
Telefone: ${searchClient[0].cellphone}
E-mail: ${searchClient[0].email}
Senha: ${searchClient[0].password}
Saldo: R$ ${searchClient[0].balance}
Pedido de emprestimo: ${searchClient[0].loan}
Valor do emprestimo: ${searchClient[0].valueLoan}
---------------------------`)
        input.question()
      }
      else if (optionManager == 2){
        let requestLoan = users.filter((
          element) => element.loan == 'S')
        if (requestLoan.length >= 1){
          let cont = 0
          while (cont < requestLoan.length){
            console.log(`
---------------------------
Dados do cliente:\n
Nome: ${requestLoan[cont].name}
Conta: ${requestLoan[cont].account}
CPF: ${requestLoan[cont].cpf}
Telefone: ${requestLoan[cont].cellphone}
E-mail: ${requestLoan[cont].email}
Senha: ${requestLoan[cont].password}
Saldo: R$ ${requestLoan[cont].balance}
Pedido de emprestimo: ${requestLoan[cont].loan}
Valor do emprestimo: ${requestLoan[cont].valueLoan}
---------------------------\n`)
            requestLoan[cont].loan = input.question('Autorizar emprestimo de cliente? [SIM / NAO] ').toUpperCase()
            cont += 1}
        input.question()
        }
        else {console.log('Nao ha pedidos de emprestimo.')
        input.question()}
      }
      do {console.log(menuManager)
        optionManager = parseInt(input.question('Escolha uma opcao: '))
        } while (optionManager < 0 || optionManager > 2)
      } break
    }  
  }
}
console.log(`\nSua sessão foi finalizada.\nObrigado por utilizar nossos servicos.\n`)

// Salvando os dados em outro arquivo

users = fs.writeFileSync('users.json', JSON.stringify(users))
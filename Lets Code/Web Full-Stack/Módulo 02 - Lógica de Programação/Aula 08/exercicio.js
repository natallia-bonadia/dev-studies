function cabecalho(){
  console.log(
`------------------------------
   Gerenciamento de Alunos
------------------------------
Escolha uma das opções abaixo:
[ 1 ] Adicionar aluno
[ 2 ] Remover aluno
[ 3 ] Atualizar aluno
[ 4 ] Exibir um aluno 
[ 5 ] Lista completa
[ 0 ] Finalizar programa`)
}

const input = require('readline-sync')

let lista_alunos = [
  {nome: 'Ana Maria', idade: 55, email: 'anamaria@gmail.com', plano: 'trimestral', frequencia: 3, valor: 400.00},
  {nome: 'Claudio', idade: 32, email: 'claudio@gmail.com', plano: 'semestral', frequencia: 2, valor: 250.00},
  {nome: 'Elaine', idade: 27, email: 'elaine@gmail.com', plano: 'mensal', frequencia: 3, valor: 500.00},
  {nome: 'Gabriel', idade: 18, email: 'gabriel@gmail.com', plano: 'trimestral', frequencia: 1, valor: 150.00},
  {nome: 'Juliana', idade: 44, email: 'juliana@gmail.com', plano: 'anual', frequencia: 2, valor: 200.00},
  {nome: 'Maria Eduarda', idade: 21, email: 'mariaeduarda@gmail.com', plano: 'mensal', frequencia: 1, valor: 180.00},
  {nome: 'Paulo', idade: 50, email: 'paulo@gmail.com', plano: 'semestral', frequencia: 2, valor: 250.00},
  {nome: 'Thais', idade: 41, email: 'thais@gmail.com', plano: 'anual', frequencia: 1, valor: 130.00}
]

let menu = true
while (true) {
  if (menu) cabecalho()
  menu = true
  let opcao = parseInt(input.question('>>> '))
  if (opcao == 1){
    console.log(`----- Adicionar aluno -----`)
    let nome = input.question('Nome: ')
    let idade = parseInt(input.question('Idade: '))
    let email = input.question('E-mail: ')
    let plano = input.question('Plano: ')
    let frequencia = parseInt(input.question('Frequencia: '))
    let valor = parseFloat(input.question('Valor por mes: '))

    let aluno = {nome, idade, email, plano, frequencia, valor}

    lista_alunos.push(aluno)
    console.log('----- Aluno adicionado -----')
    input.question('Pressione ENTER para continuar')
  }
  else if (opcao == 2){
    console.log(`----- Remover aluno -----`)
    let remover = input.question('Nome: ')
    for (let i = 0; i < lista_alunos.length; i++){
      if (lista_alunos[i].nome === remover){
        lista_alunos.splice(i, 1)
        console.log('----- Aluno removido -----')
        input.question('Pressione ENTER para continuar')
      }
    }
  }
  else if (opcao == 3){
    console.log(`----- Editar aluno -----`)
    let editar = input.question('Nome: ')
    let atributo = input.question('Item que deseja editar: ')
    for (let i = 0; i < lista_alunos.length; i++){
      if (lista_alunos[i].nome === editar){
        lista_alunos[i][atributo] = input.question('Atualizacao: ')
        console.log(lista_alunos[i])
        input.question('Pressione ENTER para continuar')
      }
    }      
  }
  else if (opcao == 4){
    console.log(`----- Exibir aluno -----`)
    let exibir = input.question('Nome: ')
    for (let i = 0; i < lista_alunos.length; i++){
      if (lista_alunos[i].nome === exibir){
        console.log(lista_alunos[i])
        input.question('Pressione ENTER para continuar')
      }
    }
  }
  else if (opcao == 5){
    console.log(lista_alunos.sort(function(a, b){
      return a.nome < b.nome ? -1 : a.nome > b.nome ? 1 : 0}))
      input.question('Pressione ENTER para continuar')
  }
  else if (opcao == 0){
    console.log(`Finalizando programa...`)
    break
  }
  else {
    console.log('Opcao invalida. Digite novamente. ')
    menu = false
  }
}
console.log(`----- Programa finalizado -----`)
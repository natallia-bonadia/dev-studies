const fs = require('fs')
const funcao = require('./funcoes')
const classe = require('./classes')
const input = require('readline-sync')

let opcaoMenuPrincipal, opcaoMenuAdm, opcaoMenuFunc
let nomeEmpresa, nomeAdm, emailAdm, senhaAdm
let nomeFunc, emailFunc, senhaFunc

let dados_cadastro = JSON.parse(fs.readFileSync('dados_cadastro.json').toString())

do {funcao.mostrarMenuPrincial()
  opcaoMenuPrincipal = parseInt(input.question('Escolha uma opcao: '))
  } while (opcaoMenuPrincipal < 0 || opcaoMenuPrincipal > 3)

while (opcaoMenuPrincipal !== 0){
  if (opcaoMenuPrincipal === 1){
    console.log(`\n==== CADASTRO DE EMPRESA ====\n`)
    nomeEmpresa = input.question('Nome da empresa: ')
    nomeAdm = input.question('Nome do administrador: ')
    emailAdm = input.question('E-mail: ')
    senhaAdm = input.question('Senha: ')
    
    console.log(`\n> Empresa cadastrada com sucesso!< \n`)
  }

  else if (opcaoMenuPrincipal === 2){
    
    do {funcao.mostrarLoginAdm()
    opcaoMenuAdm = parseInt(input.question(`Escolha uma opcao: `))
    } while (opcaoMenuAdm < 0 || opcaoMenuAdm > 4)

    while (opcaoMenuAdm !== 0){
      if (opcaoMenuAdm === 1){
        console.log(`\n== CADASTRO DE FUNCIONÁRIO ==\n`)
        nomeFunc = input.question('Nome: ')
        emailFunc = input.question('E-mail: ')
        senhaFunc = input.question('Senha: ')

        console.log(`\n> Funcionário cadastrado com sucesso!< \n`)
      }
      else if(opcaoMenuAdm === 2){
        
      }
      else if(opcaoMenuAdm === 3){
        
      }
      else if(opcaoMenuAdm === 4){
        
      }
      do {funcao.mostrarLoginAdm()
      opcaoMenuAdm = parseInt(input.question(`Escolha uma opcao: `))
      } while (opcaoMenuAdm < 0 || opcaoMenuAdm > 4)
    }
  }
  else if (opcaoMenuPrincipal === 3){
    
    do {funcao.mostrarLoginFunc()
    opcaoMenuFunc = parseInt(input.question(`Escolha uma opcao: `))
    } while (opcaoMenuFunc < 0 || opcaoMenuFunc > 3)
    
    while (opcaoMenuFunc !== 0){
      if (opcaoMenuFunc === 1){

      }
      else if(opcaoMenuFunc === 2){
        
      }
      else if(opcaoMenuFunc === 3){
        
      }
      do {funcao.mostrarLoginFunc()
      opcaoMenuFunc = parseInt(input.question(`Escolha uma opcao: `))
      } while (opcaoMenuFunc < 0 || opcaoMenuFunc > 3)
    }
  } 
  do {funcao.mostrarMenuPrincial()
    opcaoMenuPrincipal = parseInt(input.question('Escolha uma opcao: '))
    } while (opcaoMenuPrincipal < 0 || opcaoMenuPrincipal > 3)
}
console.log('Sessão finalizada.')

const cadastroEmpresa = new classe.Empresa(nomeEmpresa, nomeAdm, emailAdm, senhaAdm)
const cadastroFuncionario = new classe.Funcionario(nomeFunc, emailFunc, senhaFunc)

// dados_cadastro = fs.writeFileSync('dados_cadastro.json', JSON.stringify(dados_cadastro))

console.log(cadastroEmpresa.novaEmpresa())
console.log(cadastroFuncionario.novoFuncionario())
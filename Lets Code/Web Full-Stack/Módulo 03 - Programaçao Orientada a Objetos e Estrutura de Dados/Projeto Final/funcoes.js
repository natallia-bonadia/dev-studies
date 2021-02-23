// Menu Principal

function mostrarMenuPrincial() {
  console.log(`
============ MENU ============

[ 1 ] Cadastro de Empresa
[ 2 ] Login Administrador
[ 3 ] Login Funcionário
[ 0 ] Sair\n`)
}

// Menu Login Administrador

function mostrarLoginAdm() {
  console.log(`
===== OLA, ADMINISTRADOR =====

[ 1 ] Cadastrar Funcionário
[ 2 ] Remover Funcionário
[ 3 ] Pesquisar Funcionário
[ 4 ] Lista de Funcionários
[ 0 ] Sair\n`)
}

// Menu Login Funcionario

function mostrarLoginFunc() {
  console.log(`
===== OLA, ADMINISTRADOR =====

[ 1 ] Registrar Ponto
[ 2 ] Consultar Entradas e Saídas
[ 3 ] Consultar Banco de Horas
[ 0 ] Sair\n`)
}

function validarAdm(email, senha){
  
}

module.exports = {mostrarMenuPrincial, mostrarLoginAdm, mostrarLoginFunc}
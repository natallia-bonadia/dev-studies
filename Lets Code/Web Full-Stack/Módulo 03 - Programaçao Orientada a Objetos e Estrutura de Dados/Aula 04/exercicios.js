/*
PARTE 1

PERGUNTA
1. Assinale a alternativa que melhor descreve o conceito de encapsulamento.
Alternativas

[ ] Objeto ser passado como parâmetro de uma função.

[ ] Objeto ser imutável após ser criado.

[x] Objeto negar acesso de leitura e/ou escrita de seus atributos.

[ ] Objeto negar uso de seus métodos públicos.



-----------------------------------------------------------------------------------

PERGUNTA
2. Analise o código a seguir: 
*/
/*
class User{
  constructor(nome, senha){
    let nome_usuario = nome;
    let senha_usuario = senha;
    let logado = false;

    this.logar = (usuario_tentado, senha_tentada) => {
      if(usuario_tentado === nome_usuario && senha_tentada === senha_usuario) {
        logado = true;
        console.log('Logado!')
      }

      else{
        console.log('Usuário ou senha incorreto!')
      }
    }

    this.alterarSenha = (nova_senha) => {
      if(logado){
        senha_usuario = nova_senha;
      }

      else{
        console.log('É necessário logar primeiro!')
      }
    }
  }
}

const usuario = new User('Natallia', 1234)
usuario.comida = true

console.log(usuario)
*/
/*
O código representa uma classe usuário com atributos privados de nome, senha e logado. Assinale a alternativa que contém uma afirmação incorreta sobre o código:
Alternativas

RESPOSTA

[ ] Para alterar a senha é necessário executar o método logar primeiro.

[ ] De fora da classe não é possível descobrir o valor da variável 'senha'.

[x] É possível modificar o valor da variável logado sem usar o método logar.

[ ] Todos os métodos foram declarados no construtor por causa do escopo das variáveis declaradas com let.


-----------------------------------------------------------------------------------

PERGUNTA
3. Crie uma classe Conta que representa uma conta bancária cujo saldo e senha de acesso são informações privadas (protegidas). Adicione também os métodos depositar e sacar.

RESPOSTA
*/
/*
class Conta {

  constructor (login, senha) {
    let login_usuario = login
    let senha_usuario = senha
    let logado = false
    let saldo = 1000
  
    this.logar = (login_tentado, senha_tentada) => {
      if (login_usuario === login_tentado && senha_usuario === senha_tentada) {
        logado = true
        console.log('Logado\n')      
      }
      else console.log ('Usuário ou senha incorretos.\n')
    }

    this.depositar = (valor_deposito) => {
      saldo += valor_deposito
      console.log('Depósito realizado.\n')
    }

    this.sacar = (valor_saque) => {
      saldo -= valor_saque
      console.log('Retire suas notas.\n')
    }

    this.mostrarSaldo = () => console.log(`Seu saldo atual é ${saldo}\n`)
    
    this.mudarSenha = (nova_senha) => {
      if (logado == true){
        senha_usuario = nova_senha
        console.log('Senha alterada com sucesso.\n')
      }
      else console.log('Para alterar a senha é necessário estar logado.\n')
    }

  }
}

let usuario = new Conta ('Maria', '123456')
usuario.logar('Maria', '1234')    // Senha incorreta
usuario.logar('Maria', '123456')  // Senha e usuário corretos = login
usuario.mostrarSaldo()            // Apresenta saldo
usuario.depositar(500)            // Deposita e atualiza saldo
usuario.sacar(250)                // Saca e atualiza saldo
usuario.mostrarSaldo()            // Apresenta saldo atualizado
usuario.mudarSenha('987654')      // Modifica a senha

console.log(usuario.senha)        // undefined
console.log(usuario.saldo)        // undefined
*/
/*
---------------------------------------------------------------------------------

PARTE 2 

PERGUNTA
1. Crie uma classe chamada Usuario com os atributos

    nome
    sobrenome
    cpf
    email

Crie os métodos de acesso para esses atributos de forma que:

    nome seja sempre uma string
    sobrenome seja sempre uma string com 2+ palavras
    cpf seja uma string que contenha somente números
    email contenha um ‘@’ e um ‘.’ ao menos

Crie um método getter de forma que qualquer acesso a .nomeCompleto retorne o valor do atributo _nome concatenado com o valor de _sobrenome. O programa deve funcionar de forma similar a abaixo:

const usuario = new Usuario('Jorge', 'Silva Cunha', '12345678910', 'jorge_silva@email.com');
console.log(usuario.nomeCompleto);
Jorge Silva Cunha

PERGUNTA
2. Crie uma classe chamada Endereco com os atributos:

    apelido
    estado
    cidade
    bairro
    rua
    numero

Crie os métodos de acesso dessa classe de forma que:

    apelido, estado, cidade, bairro, rua e numero sejam sempre strings
    estado tenha apenas duas letras

Crie um método getter de forma que qualquer acesso a .enderecoCompleto retorne uma string exibindo os valores de todos os atributos da classe concatenados.

PERGUNTA
3. Altere a classe Usuario adicionando um atributo enderecos que deve ser um array (vetor) de objetos da classe Endereco, esse método deve ser privado. Além deste, crie o atributo enderecoFavorito que deve guardar uma instância da classe Endereco e também deve ser privado. Crie os métodos:

    adicionarEndereco(novoEndereco): adiciona um endereço à enderecos validando se a entrada é uma instância da classe Endereco.
    removerEndereco(apelidoEndereco): remove um endereço da lista baseado no seu nome
    atualizarEnderecoFavorito(apelidoNovoEndereco): atualiza o enderecoFavorito para o endereço com nome igual ao recebido por parâmetro, se não encontrar, mantém o valor anterior mas avisa o usuário sobre não ter encontrado.

RESPOSTA
*/

function validaString(parametro, nomeDoParametro) {
  if (typeof(parametro) !== 'string') throw `${nomeDoParametro} deve ser uma string`
}

class Endereco {
  constructor(apelido, estado, cidade, bairro, rua, numero) {

    let _apelido, _estado, _cidade, _bairro, _rua, _numero

    // Apelido

    this.setApelido = (apelido) => {
      validaString(apelido, 'apelido')
      _apelido = apelido
    }
    this.getApelido = () => _apelido

    // Estado

    this.setEstado = (estado) => {
      validaString(estado, 'estado')
      if (estado.length !== 2) throw "estado deve ter apenas duas letras"
      if (typeof(estado[0]) !== 'string' || typeof(estado[1]) !== 'string') throw "estado deve conter apenas letras";
      _estado = estado
    }
    this.getEstado = () => _estado

    // Cidade

    this.setCidade = (cidade) => {
      validaString(cidade, 'cidade')
      _cidade = cidade
    }
    this.getCidade = () => _cidade

    // Bairro

    this.setBairro = (bairro) => {
      validaString(bairro, 'bairro')
      _bairro = bairro
    }
    this.getBairro = () => _bairro

    // Rua

    this.setRua = (rua) => {
      validaString(rua, 'rua')
      _rua = rua
    }
    this.getRua = () => _rua

    // Número

    this.setNumero = (numero) => {
      validaString(numero, 'numero')
      _numero = numero
    }
    this.getNumero = () => _numero

    // Construção do Objeto

    this.criarObjeto = () => {
      return {apelido, estado, cidade, bairro, rua, numero}
    }

    // Chamando métodos para validação

    this.setApelido(apelido)
    this.setEstado(estado)
    this.setCidade(cidade)
    this.setBairro(bairro)
    this.setRua(rua)
    this.setNumero(numero)

  }

  // Endereço completo

  get enderecoCompleto() {
    return `${this.getApelido()}:
${this.getRua()}, ${this.getNumero()}
${this.getBairro()} - ${this.getCidade()} / ${this.getEstado()}\n`
  }

}

class Usuario {
  
  constructor(nome, sobrenome, cpf, email) {

    let _nome, _sobrenome, _cpf, _email

    let enderecos = []
    let endereco_favorito

    // Endereço

    this.getEndereco = () => enderecos
    this.getEnderecoFavorito = () => endereco_favorito.getApelido()

    this.adicionarEndereco = (endereco) => {
      if (!(endereco instanceof Endereco)) throw "endereço deve ser uma instância de Endereço"
      enderecos.push(endereco)
      if (enderecos.length === 1) {
          endereco_favorito = endereco
      }
    }
    
    this.removerEndereco = (apelido) => {
      const indiceEndereco = enderecos.findIndex(endereco => endereco.getApelido().toLowerCase() === apelido.toLowerCase())
      if (!indiceEndereco === -1) throw `Endereço com apelido ${apelido} não cadastrado`
      enderecos.splice(indiceEndereco, 1)
      console.info(`Endereço '${apelido}' removido com sucesso!`)
    }

    this.atualizarEnderecoFavorito = (apelido) => {
      if (enderecos.length === 1) {
      console.error(`O usuário ${this.nome} só possui um endereço, portanto foi possível atualizar`)
      return
      }
      const enderecoEncontrado = enderecos.find(endereco => endereco.getApelido().toLowerCase() === apelido.toLowerCase())
      if (!enderecoEncontrado) throw `Endereço com apelido ${apelido} não cadastrado`
      endereco_favorito = enderecoEncontrado
    }
        
    // Nome

    this.setNome = (nome) => {
      validaString(nome, 'nome')
      _nome = nome
    }
    this.getNome = () => _nome

    // Sobrenome

    this.setSobrenome = (sobrenome) => {
      validaString(sobrenome, 'sobrenome')
      if (!(sobrenome.trim()).includes(' ')) throw 'sobrenome deve conter pelo menos duas palavras'
      _sobrenome = sobrenome
    }
    this.getSobrenome = () => _sobrenome
    
    // CPF

    this.setCpf = (cpf) => {
      validaString(cpf, 'cpf')
      if (cpf.length !== 11) throw "cpf deve conter 11 dígitos"
        const ehValido = cpf.split('').reduce((acc, char) => {
            return acc && (typeof(parseInt(char)) === 'number')}, true);
        if (!ehValido) throw "todos os caracteres do cpf devem ser números"
      _cpf = cpf
    }
    this.getCpf = () => _cpf
  
    // E-mail

    this.setEmail = (email) => {
      validaString(email, 'email')
      if (!(email.trim()).includes('.')) throw 'email deve conter pelo menos um ponto'
      let validaEmail = (email.split('')).filter(element => element === '@').length
      if (validaEmail != 1) throw 'email deve conter um "@"'
      _email = email
    }
    this.getEmail = () => _email

    // Chamando métodos para validação
    
    this.setNome(nome)
    this.setSobrenome(sobrenome)
    this.setCpf(cpf)
    this.setEmail(email)
  
  }

  // Informações completas

  get nomeCompleto () {
    return `\nNome completo: ${this.getNome()} ${this.getSobrenome()}\n`
  }

}

const user = new Usuario('Natallia', 'Ribeiro Bonadia', '36899553864', 'natallia.bonadia@gmail.com')
const endereco1 = new Endereco ('Casa', 'SP', 'São Paulo', 'Interlagos', 'Rua Américo Cioffi', '172')
const endereco2 = new Endereco ('Gil', 'SP', 'São Paulo', 'Tremembé', 'Rua Mateus Garcia', '405')
const endereco3 = new Endereco ('Escola', 'SP', 'São Paulo', 'Pinheiros', 'Avenida Faria Lima', '172')

user.adicionarEndereco(endereco1)
user.adicionarEndereco(endereco2)
user.adicionarEndereco(endereco3)

console.log(user.getEnderecoFavorito())

user.atualizarEnderecoFavorito('Gil')
console.log(user.getEnderecoFavorito())

user.removerEndereco('Escola')
user.removerEndereco('Trabalho')
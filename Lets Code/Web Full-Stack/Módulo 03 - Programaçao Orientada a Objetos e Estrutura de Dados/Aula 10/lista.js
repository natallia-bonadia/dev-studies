/*
1. Faça um programa para gerenciar uma to-do list, crie uma classe para representar a lista de tarefas toDoLisue faça uso da estrutura de fila para incluir tarefas e remover tarefas considerando toDoListue as primeiras tarefas adicionadas, são as primeiras a serem executadas e tão logo, as primeiras removidas da lista. O programa deve funcionar da seguinte forma:
*/

/*
class Queue {
  
  constructor() {
    let list = []
  
    this.add = parametro => list[list.length] = parametro
  
    this.remove = () => {
    if (list.length > 0) {
      let element = list[0]
      list.splice(0, 1)
      console.log(element)
    }
    else {
      console.log("Não existem mais tarefas a fazer")
    }}
  }  
}

let todoList = new Queue()

todoList.add('Lavar o carro');
todoList.add('Levar o cachorro para passear');
todoList.remove()
// Out: 'Lavar o carro'
todoList.add('Fazer o almoço');
todoList.add('Lavar a louça');
todoList.remove()
// Out: 'Levar o cachorro para passear'
todoList.remove()
// Out: 'Fazer o almoço'
todoList.remove()
// Out: 'Lavar a louça'
todoList.remove() 
// Out: 'Não existem tarefas a fazer!!'
*/

/*
2. Crie uma classe chamada Queue (Fila) que possui os métodos push() para inserir elementos e pop() para retirar elementos. Além deste, crie um método chamado pushQueue() que recebe um objeto da classe Queue como parâmetro e usando apenas os métodos push e pop, transfira os elementos da fila recebida como parâmetro para a atual (this). Crie também um método toString() para exibir os elementos da fila. Ex:
*/
/*
class Queue {

  constructor() {
    this.list = []
  }

  push = parametro => this.list[this.list.length] = parametro 
  
  pop = () => {
    let element = this.list[0]
    this.list.splice(0, 1)
    return element
  }

  pushQueue = queue => {
    while (queue.list.length > 0) {
      this.push(queue.pop())
    }
  }

  toString = () => console.log(this.list)
}


const q1 = new Queue();
q1.push(1);
q1.push(2);
q1.push(3);
q1.push(4);
console.log(q1.list)

const q2 = new Queue()
q2.push(15)
q2.push(16)
q2.push(17)
q2.push(18)
console.log(q2.list)

q1.pushQueue(q2)
q1.toString()
// Out: [1, 2, 3, 4, 15, 16, 17, 18]
*/

/*
3. Crie uma classe chamada Estacionamento que deve possui três atributos:

    primeiroAndar: string[]
    segundoAndar: string[]
    terceiroAndar: string[]

Cada um desses atributos deve se comportar como uma fila.
Crie um método chamado estacionar() que deve receber uma string representando a placa de um carro (sem necessidade de validação) e armazenar o carro em um dos três andares. Cada andar tem o limite de 15 carros, se o primeiroAndar estiver cheio, deve armazenar no segundoAndar, e se este estiver cheio, o terceiroAndar começa a armazenar esses carros, o método deve imprimir no console em que andar cada carro foi adicionado. Se todos os três andares estiverem lotados, exiba uma mensagem de erro.

Crie também um método liberarVaga() que desaloca um carro do estacionamento.
*/
/*
class Estacionamento {
  constructor() {
    this.primeiroAndar = []
    this.segundoAndar = []
    this.terceiroAndar = []
  }

  estacionar = placa => {
    if (this.primeiroAndar.length < 15) {
      this.primeiroAndar.push(placa)
      console.log('Seu carro foi estacionado no primeiro andar')
    }
    else {
      console.log('Primeiro andar lotado')
      if (this.segundoAndar.length < 15) {
        this.segundoAndar.push(placa)
        console.log('Seu carro foi estacionado no segundo andar')
      }
      else {
        console.log('Segundo andar lotado')
        if (this.terceiroAndar.length < 15) {
          this.terceiroAndar.push(placa)
          console.log('Seu carro foi estacionado no terceiro andar')
        }
        else {
        console.log('Estacionamento lotado')
        }
      }
    }
  }

  liberarVaga = () => {
    const unirArray = [...this.primeiroAndar, ...this.segundoAndar, ...this.terceiroAndar]
    if (unirArray.length > 0) {
      unirArray.splice(0, 1)
      console.log('1 vaga liberada')
      this.primeiroAndar = unirArray.splice(0,15)
      this.segundoAndar = unirArray.splice(0,15)
      this.terceiroAndar = unirArray.splice(0,15)
    }
    else console.log('O estacionamento está vazio')
  }

  mostrarVagas = () => {
    console.log(`1º andar: ${this.primeiroAndar}`)
    console.log(`2º andar: ${this.segundoAndar}`)
    console.log(`3º andar: ${this.terceiroAndar}`)
  }
  
}

const est = new Estacionamento
est.estacionar('A')
est.estacionar('B')
est.estacionar('C')
est.estacionar('D')
est.estacionar('E')
est.estacionar('F')
est.estacionar('G')
est.estacionar('H')
est.estacionar('I')
est.estacionar('J')
est.estacionar('K')
est.estacionar('L')
est.estacionar('M')
est.estacionar('N')
est.estacionar('O')
est.estacionar('P')
est.estacionar('Q')
est.estacionar('R')
est.estacionar('S')
est.estacionar('T')
est.estacionar('U')
est.estacionar('W')
est.estacionar('Y')
est.estacionar('X')
est.estacionar('Z')
est.liberarVaga()
est.estacionar('1')
est.estacionar('2')
est.estacionar('3')
est.liberarVaga()
est.estacionar('4')
est.liberarVaga()
est.liberarVaga()
est.mostrarVagas()
*/

/* 4. Crie uma classe chamada Cozinha, com uma lista pedidos que deve ser incializada no construtor da classe como um array vazio, comportando-se como uma fila. Crie um método confirmarPedido() que recebe um pedido como parâmetro e adiciona à pedidos. Crie um método terminarPedido() que retira um pedido do array pedidos. A lista de pedidos da cozinha não deve ultrapassar 10 pedidos, caso haja tentativa de adicionar o 11º, use o throw para lançar um erro.

Crie uma classe Atendente, com o método anotarPedido() que deve receber um pedido (string) como parâmetro e armazena num array pedidosAConfirmar que deve ser atributo da classe e se comportar como uma fila. Crie também um método chamado enviarPedido que recebe uma instância da classe Cozinha e um pedido (string), e deve chamar o método confirmarPedido da cozinha passando o pedido que foi recebido o primeiro pedido de pedidosAConfirmar como parâmetro. Caso a lista de pedidos ainda não tenha atingido o limite, o método deve também remover o pedido do array pedidosAConfirmar, caso contrário, o item fica no array. */

class Cozinha {
  constructor() {
    this.listaPedidos = []
  }

  confirmarPedido = pedido => {
    if (this.listaPedidos.length >= 3) throw 'Lista com 10 pedidos, aguarde para enviar o próximo'
    else this.listaPedidos.push(pedido)
    console.log(this.listaPedidos)
  }

  terminarPedido = () => {
    let element = this.listaPedidos[0]
    this.listaPedidos.splice(0,1)
    return element
  }
}

class Atendente {
  constructor() {
    this.pedidosAConfirmar = []    
  }

  anotarPedido = pedido => {
    this.pedidosAConfirmar.push(pedido)
  }

  enviarPedido = cozinha => {
    try {
      let element = this.pedidosAConfirmar[0]
      this.pedidosAConfirmar.splice(0,1)
      cozinha.confirmarPedido(element)
    }
    catch {
      console.log('O pedido não pôde ser enviado. Tente novamente mais tarde.')
    } 
  }
}


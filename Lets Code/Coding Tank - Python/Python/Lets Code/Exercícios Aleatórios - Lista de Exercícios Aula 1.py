### EXERCÍCIOS ALEATÓRIOS - LISTA DE EXERCÍCIOS DA AULA 1 ###

'''
1) Defina, com suas palavras, o que é um algoritmo.

É uma sequência de regras e tarefas que solucionam um problema.

----------

2) Cite alguns algoritmos que você pode encontrar no seu dia a dia de trabalho ou estudo.

Fazer uma transferência bancária, tomar banho, cozinhar legumes, pesquisar uma palavra no
dicionário, dirigir até o trabalho, fazer compras no mercado, praticar um exercício físico, etc...

----------

3) Faça um algoritmo para calcular a média de 5 notas de um aluno

aluno = input('Digite o nome do aluno: ')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: ')) 
n3 = float(input('Digite a terceira nota: '))
n4 = float(input('Digite a quarta nota: '))
n5 = float(input('Digite a quinta nota: '))
m = (n1+n2+n3+n4+n5)/5
print(f'A média de {aluno} é {m:.2f}.')

----------

4) Cite três tipos de dados e dê três exemplos de cada.

Strings (str): 'Cobra', 'Milk Shake', '4.17'
Inteiros (int): -2, 0, 1530
Booleanas (bool): False e True

----------

5) Qual tipo de dado (variável) que você julga mais correto para representar:
a. Conta bancária;
b. Nome de um livro;
c. Largura e comprimento de um quarto;
d. Placa de um carro;
e. Quantidade de filhos de uma pessoa.

a. float
b. str
c. float
d. str
e. int

----------

6) Dado o algoritmo abaixo, o que estará armazenado nas variáveis A, B e C,
respectivamente, ao final?
    A <- 0
    B <- 1
    C <- A + B
    A <- A + 1
    B <- A + B + C

B) 1, 3, 1

----------

7) As ordens dos comandos de um algoritmo são importantes? De forma sucinta,
justifique e dê um exemplo.

Sim, pois na maioria das vezes para executar um comando é necessário ter
algum resultado ou resposta anterior.
Exemplo: Calcular a quantidade de tinta para pintar uma parede,
sendo que 1 m² precisa de 1.5 litros de tinta

# passo 1: pedir os dados da parede
altura = float(input('Digite a altura da parede em metros: '))
largura = float(input('Digite a largura da parede em metros: '))

# passo 2: calcular a área da parede
A = (altura*largura)

# passo 3: calcular a quantidade de tinta necessária
T = A/1.5

# passo 4: apresentar a quantidade de tinta necessária
print(f'Será necessário {T:.2f} litros de tinta.')

----------

8) Explique, de forma sucinta, a diferença entre linguagens naturais (inglês, português)
e as linguagens de programação (python, Java).

A linguagem natural — tanto escrita, quanto falada — é repleta de regras e ambiguidades,
que dependem inclusive do idioma. A linguagem de programação desenvolve sistemas digitais
que sejam capazes de entender a linguagem humana a partir de uma linguagem formal.
'''

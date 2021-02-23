### EXERCÍCIOS AULA 18 - FUNÇÕES (PARTE 1) ###

'''
1) O que é e pra quê serve uma função?

Para evitar repetição de código e tornar o programa mais enxuto e legível.

----------

2) Pra quê serve os parâmetros de uma função? Pra quê serve o retorno de uma função?
Em que situação é útil utilizar o retorno?

Os parâmetros servem para deixar a função o mais genérica possível, podendo ser utilizada em diversos casos.
O retorno de uma função é utilizado para declarar a informação a ser retornada pela função, sem apresentá-la em uma variável.
O retorno é útil quando não queremos o resultado de uma variável que está no meio da função na tela,
apenas precisamos desse resultado dentro do nosso programa em uma variável para jogar em outra equação.

----------

3) Faça uma função que recebe um número e imprime seu dobro.

def dobro(a):
    print(f'O dobro de {a} é {a*2}.')

dobro(int(input('Digite um número para descobrir o seu dobro: ')))

----------

4) Faça uma função que recebe um nome e imprime "olá, [nome]".

def nome(n):
    print(f'Olá, {n}!')

nome(input('Digite seu nome: '))

----------

5) Faça uma função que recebe um nome e um horário e imprima:
    "Bom dia, [nome]", caso seja antes de 12h;
    "Boa Tarde, [nome]", caso seja entre 12h e 18h;
    "Boa noite, [nome]" se for após às 18h.

def saudaçao(n, h):
    if h <= 12:
        print(f'Bom dia, {n}! São {h} horas.')
    elif 12 <= h <= 18:
        print(f'Boa tarde, {n}! São {h} horas.')
    else:
        print(f'Boa noite, {n}! São {h} horas.')

n = input('Digite seu nome: ').strip().title()
h = int(input('Que horas são? '))
saudaçao(n, h)

----------

6) Faça uma função que recebe um número e retorna True se ele é par ou False, se ele é ímpar.

def parouimpar(n):
    if n % 2 == 0:
        return True
    else:
        return False
    
resposta = parouimpar(int(input('Digite um número: ')))
print(resposta)

----------

7) Faça uma função que recebe uma lista de números e retorna a soma dos elementos dessa lista.

def somalista(lista):
    soma = sum(lista)
    print(f'A soma dos elementos da lista é {soma}.')

lista = []
num = 0
while True:
    num = int(input('Digite um número ou 0 para parar: '))
    lista.append(num)
    if num == 0:
        break

somalista(lista)

----------

8) Faça uma função que receba duas listas e retorne o produto item a item dessas listas.
Exemplo: Se a função receber as listas [1,4,3] e [3,5,1], então a
função deve retornar [1x3, 4x5, 3x1] = [3, 20, 3].

def produtolista(lista1, lista2):
    cont = 0
    lista3 = []
    for c in lista1:
        produto = c * lista2[cont]
        cont += 1
        lista3.append(produto)
    print('-'*30)
    print(f'O produto de cada elemento da lista 1 com a lista 2 é {lista3}.')

lista1 =[]
lista2 =[]
q = int(input('Quantos elementos você quer adicionar em cada lista? '))
for c in range(0,q):
    n = lista1.append(int(input(f'Digite o número {c} da lista 1: ' )))
print('-'*30)
for c in range(0,q):
    n = lista2.append(int(input(f'Digite o número {c} da lista 2: ' )))

produtolista(lista1, lista2)
'''
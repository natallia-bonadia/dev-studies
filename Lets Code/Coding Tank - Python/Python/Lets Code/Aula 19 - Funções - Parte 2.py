### EXERCÍCIOS AULA 18 - FUNÇÕES (PARTE 2) ###

'''
1) Faça uma função que receba um texto e retorno o reverso desse texto. Não use reverse().
Exemplo
input: "1234abcd"
output: "dcba4321"

def reverso(texto):
  saida = ''
  idx = len(texto) - 1
  while idx >= 0: 
    saida = saida + texto[idx]
    idx = idx - 1
  return saida

entrada = input('>>')
print( reverso(entrada) )

----------

2) Faça uma função que receba uma lista com uma quantidade indeterminada de números e informe quantos números sem repetição existem na lista.
Exemplo
input: [1,2,3,3,3,3,4,5]
output: 4 números sem repetição

def cont_unicos(L):
  idx = 0
  qtdade_unicos = 0
  while idx < len(L):
    num_aparicoes = 0
    
    idx2 = 0
    while idx2 < len(L):
      if L[idx] == L[idx2]:
        num_aparicoes = num_aparicoes + 1
      idx2 = idx2 + 1

    if num_aparicoes == 1:
      qtdade_unicos = qtdade_unicos + 1

    idx = idx + 1
  return qtdade_unicos

lista = [1, 2, 4, 5, 5]
cont_unicos(lista)

----------

3) Faça uma função que receba uma lista com uma quantidade indeterminada de números e informe qual o maior número dessa lista. Não use o max().

def maior(L):
  idx = 0
  maior = L[0] # chute 
  while idx < len(L):
    if L[idx] > maior:
      maior = L[idx]
    idx = idx + 1
  return maior

lista = [3, 9, 4, 5, 4]
maior(lista)

----------

4) Faça uma função recursiva que apresente os números entre 1 e N, sendo N um número informado pelo usuário.

def f(cont, N):
  if cont == N: # caso base
    print(cont)
  else: # caso recursivo
    print(cont)
    return f(cont + 1, N)

N = int(input('>>'))
f(1, N)

----------

5) Faça uma função recursiva que retorne o fatorial de um número informado pelo usuário. O fatorial de um número N (N!) é a multiplicação dos números entre 1 e N. Quando N = 0, N! = 1.

def f(N): # iterativo
  cont = N
  fat = 1
  while cont >= 1:
    fat = fat * cont
    cont = cont - 1
  return fat


def f_recursivo(N):
  if N == 1: # caso base
    return N
  else:
    return N * f(N-1) # caso recursivo

num = int(input('>>'))
f_recursivo(num)
'''
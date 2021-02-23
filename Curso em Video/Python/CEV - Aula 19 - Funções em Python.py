### Curso em Vídeo - Exercícios Aula 19 - Funções em Python ###

'''
096) Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(c, l):
  a = c * l
  print(f'A área do terreno é {a}m².')


print('-'*25)
print(f'{"Área de Terreno":^25}')
print('-'*25)
c = float(input('Digite o comprimento (m): '))
l = float(input('Digite a largura (m): '))
area(c, l)

----------

097) Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
Ex: escreva(‘Olá, Mundo!’)
Saída:
~~~~~~~~~~~~~~~
  Olá, Mundo!
~~~~~~~~~~~~~~~ 

def escreva(txt):
  cont = len(txt) + 4
  print(f'~'*cont)
  print(f'  {txt}')
  print(f'~'*cont)


txt = str(input('Digite o título: '))
escreva(txt)

----------

098) Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada

from time import sleep

def contador(inicio, fim, passo):
  print('-'*40)
  print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
  sleep(3)
  if inicio < fim:
    for c in range(inicio, fim+1, passo):
      print(f'{c} ', end='', flush=True)
      sleep(0.5)
    print('FIM!')
  else:
    if passo < 0:
      for c in range(inicio, fim-1, passo):
        print(f'{c} ', end='', flush=True)
        sleep(0.5)
    else:
      for c in range(inicio, fim-1, passo*-1):
        print(f'{c} ', end='', flush=True)
        sleep(0.5)
  print('FIM!')
 

contador(1, 10, 1)
contador (10, 0, -2)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)

----------

099) Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

RESPOSTA COM LISTAS 

def maior(lista):
  print('-'*30)
  print(f'O maior número digitado foi {max(lista)}.')
  

lista = []
while True:
  num = int(input('Digite um número ou 999 para finalizar: '))
  if num == 999:
    break
  lista.append(num)
maior(lista)

RESPOSTA COM PARÂMETROS

from time import sleep
def maior(* num):
  cont = maior = 0
  print('-'*30)
  print('\nAnalisando os números...')
  for valor in num:
    print(f'{valor}', end=' ', flush=True)
    sleep(1)
    if cont == 0:
      maior = valor
    else:
      if valor > maior:
        maior = valor
    cont += 1
  print(f'\nForam informados {cont} valores ao todo.')
  print(f'O maior valor informado foi {maior}.')
  

maior(2, 9, 4, 3, 5)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()

----------

100) Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint
from time import sleep
def sorteia(lista):
  print(f'Os valores sorteados foram: ', end="")
  while True:
    sort = randint(1,10)
    if sort not in lista:
      lista.append(sort)
      print(f'{sort} ', end="", flush=True)
      sleep(1)
    if len(lista) == 5:
      break
  print('FIM!')


def somapar(lista):
  soma = 0
  print('Os número pares são ', end="")
  for valor in lista:
    if valor % 2 == 0:
      print(f'{valor} ', end="")
      soma += valor
  print(f'\nSomando esses valores temos {soma}.')


numeros = []
sorteia(numeros)
somapar(numeros)

----------

101) Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

def voto(ano):
  from datetime import date
  atual = date.today().year
  idade = atual - ano
  if idade < 16:
    return f'Com {idade} anos: VOTO NEGADO.'
  elif 16 <= idade <= 18 or idade > 65:
    return f'Com {idade} anos: VOTO OPCIONAL.'
  else:
    return f'Com {idade} anos: VOTO OBRIGATÓRIO.'


print('-'*30)
nasc = int(input('Que ano você nasceu? '))
print(voto(nasc))

----------

102) Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(n, show=False):
  """
  -> Calcula o Fatorial de um número.
  :param n: O número a ser calculado.
  :param show: (opcional) Mostrar ou não a conta.
  :return: O valor do Fatorial de um número n.
  """
  f = 1
  for c in range(n, 0, -1):
    if show:
      print(c, end="")
      if c > 1:
        print(f' x ', end="")
      else:
        print(' = ', end="")
    f *= c
  return f


print(fatorial(5, show=True))
help(fatorial)

----------

103) Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha (jog='<desconhecido>', gol=0):
  print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')


n = str(input('Nome do jogador: '))
g = str(input('Número de gols: '))
if g.isnumeric():
  g = int(g)
else:
  g = 0
if n.strip() == '':
  ficha(gol=g)
else:
  ficha(n, g)

----------

104) Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)

def leiaInt(msg):
    while True:
        number = input(msg)
        if number.isdigit():
            return int(number)
        else:
            print('\033[0;31mErro! Digite um número inteiro válido\033[m')

n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')

----------

105) Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
– Quantidade de notas
– A maior nota
– A menor nota
– A média da turma
– A situação (opcional)

def notas(*n, sit=False):
  """
  -> Função para analisar notas e situações de vários alunos.
  :param n: uma ou mais notas dos alunos (aceita várias)
  :param sit: valor opcional, indica se deve ou não adicionar a situação
  :return: dicionário com várias informações sobre a situação da turma
  """

  r = {}
  r['total'] = len(n)
  r['maior'] = max(n)
  r['menor'] = min(n)
  r['media'] = sum(n)/len(n)
  if sit:
    if r['media'] >= 7:
      r['situaçao'] = 'BOA'
    elif r['media'] >= 5:
      r['situaçao'] = 'RAZOÁVEL'
    else:
      r['situaçao'] = 'RUIM'
  return r

resposta = notas(9, 5.5, 7.5, 9, 8.5, sit=True)
print(resposta)
# help(notas)

----------

106) Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.

def ajuda(com):
  help(com)

def titulo(msg, cor=0):
  tamanho = len(msg) + 4
  print('~' * tamanho)
  print(f'  {msg}')
  print('~' * tamanho)

comando = ''
while True:
  titulo('SISTEMA DE AJUDA PyHELP')
  comando = str(input('Função ou Biblioteca > '))
  if comando.upper() == 'FIM':
    break
  else:
    ajuda(comando)
titulo('ATÉ LOGO!')

----------
'''
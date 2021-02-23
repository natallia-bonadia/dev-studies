### Curso em Vídeo - Exercícios Aula 18 - Dicionários em Python ###
'''
090) Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

dic = {}
dic['nome'] = str(input('Nome: '))
dic['média'] = float(input(f'Média de {dic["nome"]}: '))
if dic['média'] >= 7:
  dic['situação']='Aprovado'
else:
  dic['situação']='Reprovado'
print('-'*20)
for k, v in dic.items():
  print(f' - {k} é igual a {v}')

----------

091) Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter
dic = {}
for c in range(0,4):
  dic[f'Jogador {c+1}'] = f'{randint(1,6)}'
for k, v in dic.items():
  print(f'{k} tirou {v} no dado.')
  sleep(1)
ranking = sorted(dic.items(), key=itemgetter(1), reverse=True)
print('-'*22)
print('RANKING DOS JOGADORES')
print('-'*22)
for i, v in enumerate(ranking):
  print(f'{i+1}° lugar: {v[0]} com {v[1]} pontos.')
  sleep(1)

----------

092) Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import date
cadastro = {}
data_atual = date.today().year
cadastro['nome']=(str(input('Nome: ')))
nascimento = int(input('Ano de Nascimento: '))
cadastro['idade']=data_atual - nascimento
cadastro['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
while True:
  if cadastro['ctps'] == 0:
    break
  else:
    cadastro['contratação'] = int(input('Ano de Contratação: '))
    cadastro['salário'] = float(input('Salário: R$ '))
    cadastro['aposentadoria'] = cadastro['idade'] + ((cadastro['contratação'] + 35) - data_atual)
    break
print('-'*20)
print('     CADASTRO')
for k, v in cadastro.items():
  print(f'- {k} é igual a {v}')
print('-'*20)

----------

093) Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

dic = {}
gols = []
nome = str(input('Nome do jogador: '))
dic['nome'] = nome
partidas = int(input(f'Quantas partidas {nome} jogou? '))
for p in range(0,partidas):
  gol = int(input(f'Quantos gols na partida {p}? '))
  gols.append(gol)
soma = sum(gols)
dic['gols'] = gols
dic ['total'] = soma
print('-'*30)
print(dic)
print('-'*30)
for c, v in dic.items():
  print(f'O campo {c} tem valor {v}')
print('-'*30)
print(f'O jogador {nome} jogou {partidas} partidas.')
for k, v in enumerate(gols):
  print(f'  => Na partida {k}, fez {v} gols.')
print(f'Foi um total de {soma} gols.')

----------

094) Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média

lista = []
pessoa = {}
soma = 0
while True:
  pessoa.clear()
  pessoa['nome'] = str(input('Nome: '))
  while True:
    pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper().strip()[0]
    if pessoa['sexo'] in 'FM':
      break
    else:
      print('ERRO! Digite apenas M ou F.')
  pessoa['idade'] = int(input('Idade: '))
  soma += pessoa['idade']
  lista.append(pessoa.copy())
  while True:
    cont = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if cont in 'SN':
      break
    else:
      print('ERRO! Digite apenas S ou N.')
  if cont == 'N':
    break
print('-'*20)
print(f'Ao todo temos {len(lista)} pessoas cadastradas.')
print('-'*20)
media = soma / len(lista)
print(f'A média de idade é de {media:.2f} anos.')
print('-'*20)
print(f'As mulheres cadastradas foram ', end='')
for p in lista:
  if p['sexo'] in 'F':
    print(f'{p["nome"]} ',end='')
print()
print('-'*20)
print(f'Lista das pessoas que tem a idade acima da média: ')
for p in lista:
  if p['idade'] >= media:
    for k, v in p.items():
      print(f'{k} = {v};', end=' ')
    print()
print('-'*20)
print('<<< PROGRAMA ENCERRADO >>>')

----------

095) Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

jogador = {}
lista = []
partidas = []
while True:
  jogador.clear()
  nome = str(input('Nome do jogador: '))
  jogador['nome'] = nome
  tot = int(input(f'Quantas partidas {nome} jogou? '))
  partidas.clear()
  for p in range(0,tot):
    partidas.append(int(input(f'  Quantos gols na partida {p+1}? ')))  
  jogador['gols'] = partidas[:]
  jogador['total'] = sum(partidas)
  lista.append(jogador.copy())
  cont = str(input('Quer continuar? [S/N] ')).upper().split()[0]
  if cont == 'N':
    break
print('-'*40)
print('cod nome           partidas     gols')
print('-'*40)
for k, v in enumerate(lista):
  print(f'{k:>3} ', end='')
  for d in v.values():
    print(f'{str(d):<15}', end='')
  print()
print('-'*40)
while True:
  busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
  if busca == 999:
    break
  if busca >= len(lista):
    print(f'ERRO! Não existe jogador com código {busca}.')
  else:
    print(f' -- Levantamento do Jogador {lista[busca]["nome"]} --')
    for i, g in enumerate(lista[busca]['gols']):
      print(f'       No jogo {i+1} fez {g} gols.')
  print('-'*40)
print("<<< PROGRAMA ENCERRADO >>>")
'''

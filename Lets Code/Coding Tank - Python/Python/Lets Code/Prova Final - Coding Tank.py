### PROVA FINAL - CODING TANK ###
'''
1) Gerador de senha
Escreva uma função que gere uma senha aleatória para o usuário.
O programa deve perguntar para o usuário quantas letras e quantos
números desejará nessa senha, e a senha retornada deve ter aleatoriamente
letras maiúsculas e minúsculas. A ordem entre letras e números não precisa ser aleatória.
Como dica utilize o código dado

import random

def geradordesenha(numeros,letras):
    for c in range(0,numeros):
        listanum.append(random.randint(0,9))
    alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',\
         'p', 'q', 'r', 's', 't', 'u', 'w', 'y', 'x', 'z']
    for c in range(0,letras):
        listalet.append(random.choice(alfabeto))
    for c, v in enumerate(listalet):
        if c % 2 == 0:
            print(f'{v}',end='')
        else:
            print(f'{v.upper()}',end='')
    for c in listanum:
        print(f'{c}',end='')

print('~'*30)
print(f'{"GERADOR DE SENHA":^30}')
print('~'*30)
numeros = int(input('Quantos números você quer adicionar na senha? '))
letras = int(input('Quantas letras você quer adicionar na senha? '))
listanum = []
listalet = []
geradordesenha(numeros,letras)

----------

2) Pedra, papel, tesoura
Faça uma função que funcione como o jogo "pedra, papel, tesoura", onde um usuário joga contra o computador. A escolha do usuário é fornecida através do comando input(), enquanto que a do computador é escolhida aleatoriamente. O programa deve perguntar se o usuário quer jogar novamente.
Regras do jogo:
    papel vence pedra
    pedra vence tesoura
    tesoura vence papel
Como dica, utilize o código dado:

def jokempo(j, c): 
    if j == 'pedra':
        if c == 'pedra':
            print('Escolhi PEDRA. Empatou!')
        elif c == 'papel':
            print('Escolhi PAPEL. Ganhei!')
        elif c == 'tesoura':
            print('Escolhi TESOURA. Você ganhou!')
    if j == 'papel':
        if c == 'pedra':
            print('Escolhi PEDRA. Você ganhou!')
        elif c == 'papel':
            print('Escolhi PAPEL. Empatou!')
        elif c == 'tesoura':
            print('Escolhi TESOURA. Ganhei!')
    if j == 'tesoura':
        if c == 'pedra':
            print('Escolhi PEDRA. Ganhei!')
        elif c == 'papel':
            print('Escolhi PAPEL. Você ganhou!')
        elif c == 'tesoura':
            print('Escolhi TESOURA. Empatou!')

from random import choice
from time import sleep
l = ['pedra', 'papel', 'tesoura']

j = str(input('Escolha: pedra, papel ou tesoura\n>>> '))
c = choice(l)
sleep(1)
print('Analisando sua escolha...')
sleep(2)
jokempo(j, c)
'''



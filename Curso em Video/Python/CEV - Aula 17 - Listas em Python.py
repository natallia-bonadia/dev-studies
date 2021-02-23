### Curso em Vídeo - Exercícios Aula 17 - Listas em Python ###

'''
078) Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

RESPOSTA 1 (APRESENTA APENAS A PRIMEIRA POSIÇÃO DOS NÚMEROS MAIOR E DO MENOR)

listanum = []
for c in range (0,5):
    listanum.append(int(input(f'Digite um valor para a posição {c + 1}: ')))

print('=-' * 20)
print(f'Você digitou os valores {listanum}.')
print(f'O número {max(listanum)} foi o maior na posição {listanum.index(max(listanum)) + 1}\
 e o {min(listanum)} foi o menor na posição {listanum.index(min(listanum)) + 1}.')

RESPOSTA 2 (COMPLETO)

listanum = []
maior = 0
menor = 0

for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        maior = menor = listanum[c]
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        if listanum[c] < menor:
            menor = listanum[c]
print('-'*20)
print(f'Você digitou os números {listanum}.')
print(f'O maior número digitado foi {maior} nas posições ', end='')
posmaior = posmenor = 0
for i, v in enumerate(listanum):
    if v == maior:
        posmaior = i
        print(f'{i}...', end=' ')
print(f'\nO menor número digitado foi {menor} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == menor:
        posmenor = i
        print(f'{i}...', end=' ')

----------

079) Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores
únicos digitados, em ordem crescente.

numeros = []
while True:
    n = int(input('Digite um número: '))
    if n not in numeros:
        numeros.append(n)
    else:
        print('Esse número já foi adicionado anteriormente.')    
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
# print(numeros.sort()) --> não está dando certo
print(f'Você digitou os números {sorted(numeros)}.')

----------

080) Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já
na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

lista = []
for c in range(0,5):
    n = int(input('Digite um número: '))
    if c == 0:
        lista.append(n)
    elif n > lista[-1]:
        lista.append(n)    
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
        pos += 1
print('-'*30)
print(f'Os valores digitados em ordem foram {lista}.')

----------

081) Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostra:
a) Quantos números foram digitados
b) A lista de valores, ordenada de forma decrescente
c) Se o valor 5 foi digitado e está ou não na lista

l = []
while True:
    n = int(input('Digite um número: '))
    l.append(n)
    continuar = str(input('Quer continuar? [S/N] '))
    if continuar in 'Nn':
        break
print('~'*20)   
print(f'A) Foram digitados {len(l)} números.')
print('~'*20)
l.sort(reverse=True)
print(f'B) A lista em ordem decrescente é {l}.')
print('~'*20)
if 5 in l:
    print(f'C) O valor 5 está na lista.')
else: print(f'C) O valor 5 não está na lista.')

----------

082) Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas 
extras que vão contar apenas os valores pares e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.

lista = []
par = []
impar = []

while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    cont = str(input('Quer continuar? [S/N] '))
    if cont in 'Nn':
        break
for c in lista:
    if c % 2 == 0:
        par.append(c)
    else:
        impar.append(c)

print(f'A lista completa é {lista}.\nA lista de números pares é {par}.\nA lista de números ímpares é {impar}.')

----------

083) Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos
e fechados na ordem correta.

expressao = str(input('Digite a expressão: '))
lista = []
for simbolo in expressao:
    if simbolo == '(':
        lista.append('(')
    elif simbolo == ')':
        if len(lista) > 0:
            lista.pop() # para cada ) ele retira um (
        else:
            lista.append(')')
            break
if len(lista) == 0: # se sobrar um ou mais parênteses é porque a expressão está inválida
    print('Sua expressão está válida.')
else:
    print('Sua expressão está inválida.')

----------

084) Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final mostre:
A) Quantas pessoas foram cadastradas. 
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.

peq = []
princ = []
mai = men = 0
while True:
    peq.append(str(input('Nome: ')))
    peq.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = peq[1]
    else:
        if peq[1] > mai:
            mai = peq[1]
        if peq[1] < men:
            men = peq[1]
    princ.append(peq[:])
    continuar = str(input('Quer continuar? [S/N] '))
    peq.clear()
    print('-'*10)
    if continuar in 'Nn':
        break
print(f'Ao todo foram cadastradas {len(princ)} pessoas.')
print(f'O maior peso cadastrado foi {mai} kg de ', end='')
for p in princ:
    if p[1] == mai:
        print(f'{p[0]} ', end='')
print(f'\nO menor peso cadastrado foi {men} kg de ', end='')
for p in princ:
    if p[1] == men:
        print(f'{p[0]} ', end='')

----------

085) Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

geral = [[], []]
for p in range(0,7):
    num = int(input(f'Digite o {p+1}° valor: '))
    if num % 2 == 0:
        geral[0].append(num)
    else:
        geral[1].append(num)

print(f'Os valores pares digitados foram {sorted(geral[0])}')
print(f'Os valores ímpares digitados foram {sorted(geral[1])}')

----------

086) Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

matriz = [[], [], []]
for l in range(0,3):
    for c in range(0,3):
        matriz[l].append(int(input(f'Posição {l} x {c}: ')))
print('-'*20)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^3}]', end='')
    print()

----------

087) Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.

matriz = [[], [], []]
somapar = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l].append(int(input(f'Posição {l} x {c}: ')))
print('-'*20)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^3}]', end='')
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
    print()
print('-'*20)
print(f'A soma de todos os valores pares é {somapar}.')
print(f'A soma dos valores da terceira coluna é {matriz[0][2]+matriz[1][2]+matriz[2][2]}.')
print(f'O maior valor da segunda linha é {max(matriz[1])}.')

----------

088) Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

print('-'*30)
print(f'{"MEGA SENA":^30}')
print('-'*30)
from random import randint
lista = []
jogos = []
quant = int(input('Quantidade de jogos: '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-'*30)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
print('-'*30)
print(f'{"BOA SORTE!":^30}')

----------

089) Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

lista = []

while True:
    nome = str(input('Nome: '))
    nota1= float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    cont = str(input('Quer continuar? [S/N]: '))
    lista.append([nome, nota1, nota2, media])
    if cont in 'Nn':
        break
print('-'*30)
print(f'{"N°":<5}{"Nome":<13}{"Média":^8}')
print('-'*30)
for i, a in enumerate(lista):
    print(f'{i:<5}{a[0]:<13}{a[3]:^8.1f}')
print('-'*30)
while True:
    opçao = int(input('Mostrar as notas de qual aluno? (999 interrompe): '))
    if opçao == 999:
        print('Finalizando...')
        break
    if opçao <= len(lista)-1:
        print(f'Notas de {lista[opçao][0]}: {lista[opçao][1]} e {lista[opçao][2]}.')
    print('-'*30)
print('Sessão finalizada.')
'''
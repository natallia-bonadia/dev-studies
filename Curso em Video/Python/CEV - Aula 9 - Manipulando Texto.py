### Curso em Vídeo - Exercícios Aula 9 - Manipulando Texto ###

'''
022) Crie um programa que leia o nome completo de uma pessoa e mostre:
– O nome com todas as letras maiúsculas e minúsculas.
– Quantas letras ao todo (sem considerar espaços).
– Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome comleto: ')).strip()

print('Analisando seu nome...')
print(f'Nome com todas as letras maiúsculas: {nome.upper()}.')
print(f'Nome com todas as letras minúsculas: {nome.lower()}.')
print(f'Ao todo o nome tem {len(nome) - nome.count(" ")} letras.')
# OUTRO MODELO DE RESPOSTA
# print(f'Ao todo o nome tem {len(nome.replace(" ",""))} letras.')
# substitui espaços por sem espaços
divisao = nome.split()
print(f'O primeiro nome é {divisao[0]} e tem {len(divisao[0])} letras.')
# OUTRO MODELO DE RESPOSTA
# print(f'O primeiro nome tem {nome.find(" ")} letras.')
# encontra o primeiro espaço e da seu índice, que será igual a quantidade de letras do primeiro nome

----------

023) Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

RESPOSTA 1

n = int(input('Digite um número de até 4 dígitos: '))
nmilhar = n + 10000
nstring = str(nmilhar)

print(f'Milhar: {nstring[1]} \nCentena: {nstring[2]} \nDezena: {nstring[3]} \nUnidade: {nstring[4]}')
 
OU RESPOSTA 2

n = str(input('Digite um número de até 4 dígitos: ')) 
q = len(n)

if q == 1:
    print(f'A unidade de {n} é {n[0]}.')
elif q == 2:
    print(f'A unidade de {n} é {n[1]}.')
    print(f'A dezena de {n} é {n[0]}.')
elif q == 3:
    print(f'A unidade de {n} é {n[2]}.')
    print(f'A dezena de {n} é {n[1]}.')
    print(f'A centena de {n} é {n[0]}.')
elif q == 4:
    print(f'A unidade de {n} é {n[3]}.')
    print(f'A dezena de {n} é {n[2]}.')
    print(f'A centena de {n} é {n[1]}.')
    print(f'O milhar de {n} é {n[0]}.')
else:
    print('Número inválido.')

OU RESPOSTA 3

n = int(input('Digite um número de até 4 dígitos: '))
u = n % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10

print(f'Unidade: {u} \nDezena: {d} \nCentena: {c} \nMilhar: {m}')

----------

024) Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

RESPOSTA 1

cidade = str(input('Digite o nome da sua cidade: '))
capitalizada = cidade.capitalize()
divisao = capitalizada.split()
if divisao[0] == 'Santo':
    print('O nome da cidade começa com Santo.')
else:
    print('O nome da cidade não começa com Santo.')

OU RESPOSTA 2

cidade = str(input('Digite o nome da sua cidade: ')).strip()
cap = cidade.capitalize()
print(cidade[:5].capitalize() == 'Santo')

----------

025) Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nome = str(input('Digite seu nome completo: ')).strip()
title = nome.title()
print(f'Seu nome tem Silva? {"Silva" in title}')
# print(f'Seu nome tem Silva? {"Silva" in nome.title()}')

----------

026) Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a
letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece
a última vez.

frase = str(input('Digite uma frase: ')).strip()
min = frase.lower()
a = min.count('a')
print(f'Na frase aparecem {a} vezes a letra "A".')
print(f'O primeiro "A" apareceu na posição {min.find("a")+1}.')
print(f'O último "A" apareceu na posição {min.rfind("a")+1}.')

----------

027) Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o
primeiro e o último nome separadamente. 

nome = str(input('Digite seu nome: ')).strip().title()
divisao = nome.split()
print('Muito prazer em te conhecer!')
print(f'Seu primeiro nome é: {divisao[0]}.')
print(f'Seu último nome é: {divisao[-1]}.')
'''
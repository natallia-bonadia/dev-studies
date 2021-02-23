### EXERCÍCIOS ALEATÓRIOS - AULA 17 - EXERCÍCIOS (LISTAS E DICIONÁRIOS) ###

'''
1) Aproveite o código abaixo e faça um script que leia um número entre 1 e 100
do usuário e compare com o número sorteado. Enquanto o usuário não acertar o número,
peça uma nova tentativa. Caso o chute do usuário for menor que o número a ser adivinhado,
informe "Chute muito baixo", caso contrário "Chute muito alto".
import random
num_sorteado = random.randint(1, 100)

from random import randint
computador = randint(1,100)
print('-'*20)
print('Já escolhi um número de 1 a 100, vamos ver se você adivinha...')
print('-'*20)
n = int(input('Digite um número de 1 a 100: '))
while computador != n:
    if computador > n:
        n = int(input('Chute muito baixo. Tente novamente... '))
    else:
        n = int(input('Chute muito alto. Tente novamente... '))
print(f'Parabéns, você acertou!')

----------

2) Considerando o código fornecido abaixo, crie um script que simule um programa de aposta.
Esse programa de aposta permite ao usuário escolher 15 números entre 1 e 100. Caso o usuário
marque 15 pontos ele ganha R$1.000.000,00 (1 milhão); se marcar 14 ou 13 ganha R$100.000,00 (100 mil);
caso o jogador pontue de 12 a 10, ganha R$2.000,00 (2 mil). Menos de 10 pontos, não há premiação.

import random
print('-'*30)
numeros_loto = []
for i in range(15):
    num = random.randint(1, 100)
    while num in numeros_loto:
        num = random.randint(1, 100)
    numeros_loto.append(num)
loto = sorted(numeros_loto)

cont =0
for i in range(0,15):
    usuario = int(input('Escolha um número de 1 a 100: '))
    if usuario in numeros_loto:
        cont += 1
    else:
        print('Esse número não foi sorteado.')
print('-'*30)
print(f'Os números sorteados foram: {loto}.')
print('-'*30)
if cont == 15:
    print('PARABÉNS. Você acertou todos os números e ganhou R$ 1.000.000,00.') 
if 13 <= cont <= 14:
    print(f'PARABÉNS. Você acertou {cont} números e ganhou R$ 100.000,00.')
if 10 <= cont <= 12:
    print(f'PARABÉNS. Você acertou {cont} números e ganhou R$ 2.000,00.')
else:
    print(f'Não foi dessa vez. Você acertou apenas {cont}. Tente novamente.')
       
----------

3) Uma startup de transportes aéreos alternativos criou um mapa com as cidades que possuem sua cobertura de atendimento.
O mapa informa o tempo de viagem entre as cidades atenDidas usando o app. As setas indicam as viagens que podem ser
realizadas entre as cidades conectadas. Cidades sem conexão não possuem viagens. Seu trabalho é representar o mapa usando listas.
Considerando que preço da viagem é R$ 12,75 por minuto. Descubra (programaticamente) o custo das viagens entre as cidades.
# Dica: [[2, 3, 5], [0, 1, 2], [3, 4, 0]]

# SP = índice 0
# BH = índice 1
# Curitiba = índice 2
# RJ = índice 3

mapa = [[0, 45, 30, 30], [45, 0, 75, 0], [30, 75, 0, 0], [30, 0, 0, 0]]
#             0                 1               2              3
origem = int(input('Escolha a origem:\n[ 1 ] São Paulo\n[ 2 ] Belo Horizonte\n[ 3 ] Curitiba\n[ 4 ] Rio de Janeiro\n>>> '))
destino= int(input('Escolha o destino:\n[ 1 ] São Paulo\n[ 2 ] Belo Horizonte\n[ 3 ] Curitiba\n[ 4 ] Rio de Janeiro\n>>> '))

tempo = mapa[origem-1][destino-1]

if tempo == 0:
    print('Rota não existente')
else:
    print(f'O valor total da viagem é R$ {tempo*12.75:.2f}')

'''

### Curso em Vídeo - Exercícios Aula 10 - Condições ###

'''
028) Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário
tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário
venceu ou perdeu.

import random
import time
lista = [0, 1]
n = random.randint(0, 5)
print('Acabei de escolher um número...')
time.sleep(2)
m = (int(input('Digite um número de 0 a 5 para ver se você acerta: ')))
print('Hum... Será?')
time.sleep(2)
if n == m:
    print('Parabéns, você acertou!')
else:
    print(f'Errou! O número era {n}.')

----------

029) Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo
que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

vel = float(input('Digite a velocidade do carro em km/h: '))
if vel > 80:
    print(f'Você foi multado no valor de R$ {(vel - 80)*7}.')
else:
    print('Parabéns, você não ultrapassou 80 km/h.')

----------

030) Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

n = int(input('Digite um número inteiro: '))
if n%2 == 0:
    print(f'O número {n} é par.')
else:
    print(f'O número {n} é ímpar.')

----------

031) Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

d = float(input('Digite a distância da viagem em km: ')) 
if d <= 200:
    preco1 = 0.5*d
    print(f'O preço da passagem é R$ {preco1}.')
else:
    preco2 = 0.45*d
    print(f'O preço da passagem é R$ {preco2}.')

----------

032) Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

RESPOSTA 1

ano = int(input('Digite um ano para descobrir se ele é bissexto: '))
if ano %400 == 0:
    print(f'O ano {ano} é bissexto.')
elif ano%4 == 0 and ano%100 !=0:
    print(f'O ano {ano} é bissexto.')
else:
    print(f'O ano {ano} não é bissexto.')

RESPOSTA 2

from datetime import date
ano = int(input('Digite um ano qualquer ou 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é bissexto.')
else:
    print(f'O ano {ano} não é bissexto.')

----------

033) Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

RESPOSTA 1

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

if n1 > n2 and n1 > n3 and n2 > n3:
    print(f'O número maior é {n1} e o menor é {n3}.')
elif n1 > n2 and n1 > n3 and n3 > n2:
    print(f'O número maior é {n1} e o menor é {n2}.')
elif n2 > n3 and n2 > n1 and n3 > n1:
    print(f'O número maior é {n2} e o menor é {n1}.')
elif n2 > n3 and n2 > n1 and n1 > n3:
    print(f'O número maior é {n2} e o menor é {n3}.')
elif n3 > n1 and n3 > n2 and n2 > n1:
    print(f'O número maior é {n3} e o menor é {n1}.')
else:
    print(f'O número maior é {n3} e o menor é {n2}.')

RESPOSTA 2

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
# testando menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2     # se essa condição for verdadeira, o menor será substituido
if n3 < n1 and n3 < n2:
    menor = n3     # se essa condição for verdadeira, o menor será substituido
print(f'O menor valor digitado foi {menor}.')
# testanto maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print(f'O maior valor digitado foi {maior}.')   

----------

034) Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00,
calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

si = float(input('Digite o salário inicial: '))
if si > 1250.00:
    print(f'O salário final será {si*1.1:.2f}.')
else:
    print(f'O salário final será {si*1.15:.2f}.')

----------

035) Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

reta1 = float(input('Digite o tamanho da reta 1: '))
reta2 = float(input('Digite o tamanho da reta 2: '))
reta3 = float(input('Digite o tamanho da reta 3: '))

# a soma de duas das retas precisa ser maior que a terceira (para todas as retas)
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Essas retas PODEM formar um triângulo.')
else:
    print('Essas retas NÃO PODEM formar um triângulo.')
'''

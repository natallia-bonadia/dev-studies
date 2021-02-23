### Curso em Vídeo - Exercícios Aula 8 - Utilizando Módulos ###

'''
016) Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

RESPOSTA 1

import math
n = float(input('Digite um valor: '))
print(f'O número real escolhido é {n} e sua porção inteira é {math.trunc(n)}.')

OU RESPOSTA 2

from math import trunc
n = float(input('Digite um valor: '))
print(f'O número real escolhido é {n} e sua porção inteira é {trunc(n)}.')

OU RESPOSTA 3

n = float(input('Digite um valor: '))
print(f'O número real escolhido é {n} e sua porção inteira é {int(n)}.')

----------

017) Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
Calcule e mostre o comprimento da hipotenusa.

RESPOSTA 1

co = float(input('Digite o cateto oposto do triângulo: '))
ca = float(input('Digite o cateto adjacente do triângulo: '))
h = (co**2 + ca**2)**0.5
print(f'A hipotenusa desse triângula é {h:.2f}.')

OU RESPOSTA 2

from math import hypot 
co = float(input('Digite o cateto oposto do triângulo: '))
ca = float(input('Digite o cateto adjacente do triângulo: '))
print(f'A hipotenusa desse triângulo é {hypot(co, ca):.2f}.')

OU RESPOSTA 3

import math
co = float(input('Digite o cateto oposto do triângulo: '))
ca = float(input('Digite o cateto adjacente do triângulo: '))
print(f'A hipotenusa desse triângulo é {math.hypot(co, ca):.2f}.')

----------

018) Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo. 

import math
ag = float(input('Digite um ângulo em graus: '))
ar = math.radians(ag)
print(f'O seno de {ag} é {math.sin(ar):.2f}, o cosseno é {math.cos(ar):.2f} e a tangente é {math.tan(ar):.2f}.')

----------

019) Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,
lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

a1 = (input('Digite o nome do primeiro aluno: '))
a2 = (input('Digite o nome do segundo aluno: '))
a3 = (input('Digite o nome do terceiro aluno: '))
a4 = (input('Digite o nome do quarto aluno: '))

import random
aescolhido = random.choice([a1, a2, a3, a4])
print('=-'*20)
print(f'O nome sorteado foi: {aescolhido}.')

----------

020) O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random
n1 = input('Digite o nome do primeiro aluno: ')
n2 = input('Digite o nome do segundo aluno: ')
n3 = input('Digite o nome do terceiro aluno: ')
n4 = input('Digite o nome do quarto aluno: ')

lista = [n1, n2, n3, n4]
ordem = random.sample(lista, 4)
print(f'A ordem de apresentação será {ordem}.')

----------

021) Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

Não consegui
'''

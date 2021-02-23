### Curso em Vídeo - Exercícios Aula 14 - Estrutura de Repetição While ###

'''
057) Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input('Informe seu sexo [F/M]: ')).strip().upper()[0]
while sexo != 'M' and sexo != 'F':
    print('Resposta incorreta. Tente novamente...')
    sexo = str(input('Informe seu sexo [F/M]: ')).strip().upper()[0]
print(f'Sexo {sexo} resitrado. Agradecemos sua participação!')

----------

058) Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites
foram necessários para vencer.

from random import randint
escolhacomp = randint(0,11)
escolhajog = int(input('Qual número de 0 a 10 você acha que eu escolhi? '))
cont = 1
# print(escolhacomp)
while escolhacomp != escolhajog:
    cont = cont + 1
    if escolhacomp > escolhajog:
        escolhajog = int(input('Meu número é maior. Tente mais uma vez: '))
    else:
        escolhajog = int(input('Meu número é menor. Tente mais uma vez: '))
print(f'ACERTOU! Você precisou de {cont} tentativas.')

----------

059) Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
opçao = 0

while opçao !=5:
    print("""======= MENU =======
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do programa""")
    opçao = int(input('Digite uma das opções: '))
    if opçao == 1:
        print(f'A soma entre {n1} e {n2} é {n1+n2}.')
    elif opçao == 2:
        print(f'A multiplicação entre {n1} e {n2} é {n1*n2}.')
    elif opçao == 3:
        if n1 > n2:
            print(f'O número maior é {n1}.')
        else:
            print(f'O número maior é {n2}.')
    elif opçao == 4:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    elif opçao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente.')
print('='*40)
print('Agradecemos sua participação. Programa finalizado.')    

----------

060) Faça um programa que leia um número qualquer e mostre o seu fatorial.

RESPOSTA 1

from time import sleep
numero = int(input('Digite um número para descobrir seu fatorial: '))

c = 1
fatorial = 1
while c <= numero:
    fatorial = fatorial*c
    print(f'{fatorial} →', end=' ')
    c += 1
print(f'O fatorial do número {numero} é {fatorial}.')

RESPOSTA 2

numero = int(input('Digite um número para descobrir seu fatorial: '))
fatorial = 1

for c in range(numero, 0, -1):
    fatorial = fatorial*c
    
print(fatorial)

----------

061) Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos
da progressão usando a estrutura while.

termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
c = 0
while c < 10:
    print(f'{termo} → ', end='')
    termo += razao
    c += 1
print('Fim')

----------

062) Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando
ele disser que quer mostrar 0 termos.

termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
c = 0
total = 0
mais = 10
while mais != 0:
    total += mais
    while c < total:
        print(f'{termo} → ', end='')
        termo += razao
        c += 1
    print('Pausa')
    mais = int(input('Gostaria de ver mais quantos termos? '))
print(f'Progressão finalizada com {total} termos.')

----------

063) Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 

print(f'=-'*12)
print('Sequência de Fibonacci')
print(f'=-'*12)
n = int(input('Digite a quantidade de elementos: '))
t1 = 0
t2 = 1
print(f'{t1} → {t2} → ', end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(f'{t3} → ', end='')
    t1 = t2
    t2 = t3
    cont +=1

print('Fim')

----------

064) Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999,
que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

from time import sleep
soma = 0
cont = 0
n = int(input('Digite um número inteiro ou 999 para finalizar: '))
while n != 999:
    soma += n
    n = int(input('Digite um número inteiro ou 999 para finalizar: '))
    cont += 1
print('Finalizando...')
sleep (1)
print(f'A soma dos {cont} números digitados foi {soma}.')

----------

065) Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual
foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

continuar = 's'
cont = 0
soma = 0
maior = 0
menor = 0
while continuar != 'N':
    n = int(input('Digite um número: '))
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
media = soma/cont
print(f'O maior valor foi {maior} e o menor, {menor}')
print(f'A media é {media}.')
'''

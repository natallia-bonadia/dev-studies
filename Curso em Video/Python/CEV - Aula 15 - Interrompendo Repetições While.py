### Curso em Vídeo - Exercícios Aula 15 - Interrompendo Repetições While ###

'''
066) Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999,
que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

cont = soma = 0
while True:
    n = int(input('Digite um número inteiro ou 999 para parar: '))
    if n == 999:
        break
    cont += 1
    soma += n
print('~'*20)
print(f'Você digitou {cont} números inteiros e a soma deles é {soma}.')

----------

067) Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo. 

numero = 1
while True:
    print('-'*20)
    numero = int(input('Quer ver a tabuada de qual valor?: '))
    if numero < 0:
        break
    print('~'*15)
    print('    TABUADA')
    print('~'*15)   
    for c in range(0,11):
        mult = c*numero
        print(f'{numero} x {c:2} = {mult:2}')
        
print('Fim do programa.')

----------

068) Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. 

import random
contador = 0
while True:
    print('-'*30)
    print('        PAR OU ÍMPAR')
    print('-'*30)
    parouimpar = int(input('Digite (1) PAR ou (2) ÍMPAR: '))
    while parouimpar != 1 and parouimpar != 2:
        parouimpar = int(input('Digite (1) PAR ou (2) ÍMPAR: '))
    numerojogador = int(input('Escolha um número: '))
    numerocomputador = random.randint(0, 11)
    resultado = numerojogador + numerocomputador
    if parouimpar == 1 and resultado % 2 == 0:
        contador += 1
        print(f'Eu escolhi {numerocomputador} e você {numerojogador} (total {resultado}), então essa >> VOCÊ GANHOU! <<')
    elif parouimpar == 2 and resultado % 2 != 0:
        contador += 1
        print(f'Eu escolhi {numerocomputador} e você {numerojogador} (total {resultado}), então essa >> VOCÊ GANHOU! <<')
    else:
        break
print(f'Eu escolhi {numerocomputador} e você {numerojogador} (total {resultado}), então essa >> EU GANHEI! <<\n\
GAME OVER! Você venceu {contador} vezes seguidas!')

----------

069) Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos. 

print('-'*20)
print('      CADASTRO')
print('-'*20)
conttotal = pessoas18 = homenstot = mulheres20 = 0
while True:
    conttotal += 1
    idade = int(input(f'Digite a idade da pessoa {conttotal}: '))
    sexo = str(input(f'Digite o sexo da pessoa {conttotal} [F/M]: ')).strip().upper()[0]
    while sexo not in 'FM':
        sexo = str(input(f'Digite o sexo da pessoa {conttotal}: [F/M] ')).strip().upper()[0]
    if idade >= 18:
        pessoas18 += 1
    if sexo == 'M':
        homenstot += 1
    if sexo == 'F' and idade < 20:
        mulheres20 += 1
    print('-'*20)
    continuar = str(input('Você quer continuar? [S/N]: ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Você quer continuar? [S/N]: ')).strip().upper()[0]
    print('-'*20)
    if continuar == 'N':
        break
print('Fim dos cadastros.')

print(f'A) {pessoas18} pessoas tem mais de 18 anos.')
print(f'B) Foram cadastrados {homenstot} homens.')
print(f'C) Foram cadastradas {mulheres20} mulheres com menos de 20 anos.')

----------

070) Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato. 

print('-'*30)
print('CADASTRO DE PRODUTOS E PREÇOS')
print('-'*30)
preçototal = milreais = maisbarato = cont = 0
produtomaisbarato = ''
while True:
    cont += 1
    produto = str(input('Produto: ')).strip().upper()
    preço = float(input('Digite o preço: R$ '))
    preçototal += preço
    print('-'*20)
    continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if preço > 1000:
        milreais += 1
    if cont == 1 or preço < maisbarato:
        maisbarato = preço
        produtomaisbarato = produto
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
    print('-'*20)


print(f'O valor total gasto é de R$ {preçototal}.')
print(f'{milreais} produtos custam mais de R$ 1000,00.')
print(f'O produto mais barato é {produtomaisbarato}.')

----------

071) Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado
(número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. 
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

RESPOSTA 1

print('-'*30)
print('         BANCO PYTHON')
print('-'*30)

ccinquenta = cvinte = cdez = cum = 0
saque = int(input('Valor do saque: R$ '))
while saque >= 50:
    ccinquenta += 1
    saque -= 50
while saque >= 20:
    cvinte += 1
    saque -= 20
while saque >= 10:
    cdez += 1
    saque -= 10
while saque >= 1:
    cum += 1
    saque -= 1
print(f'Restante do saque {saque}')
print(f'{ccinquenta} cédulas de R$ 50 \n{cvinte} cédulas de R$ 20 \n{cdez} cédulas de R$ 10 \n{cum} cédulas de R$ 1')

RESPOSTA 2

print('-'*30)
print('         BANCO PYTHON')
print('-'*30)

totced = 0
saque = int(input('Valor do saque: R$ '))
cedula = 50
while True:
    if saque >= cedula:
        saque -= cedula
        totced += 1
    else:
        if totced > 0:
            print(f'Total: {totced} cédulas de R$ {cedula}.')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totced = 0
        if saque == 0:
            break
print('-'*30)
print('Sessão finalizada. Volte sempre!')
'''
### Curso em Vídeo - Exercícios Aula 12 - Condições Aninhadas ###

'''
036) Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa,
o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então
o empréstimo será negado.

casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite seu salário: '))
periodo = int(input('Digite em quanos anos quer pagar: '))

parcela = casa/(periodo*12)
limite = salario*0.3
print(f'O limite do seu salário é R$ {limite} e sua parcela é R$ {parcela:.2f}.')
if parcela > limite:
    print('Desculpe, mas seu empréstimo não pôde ser aprovado.')
else:
    print('Parabéns, o empréstimo foi aprovado.')

----------

037) Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será
a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal. 

n = int(input('Digite um número: '))
print('Escolha a base de conversão: \n1 - Binário \n2 - Octal \n3 - Hexadecimal')
base = int(input('>>> '))

if base == 1:
    print(f'{n} convertido para binário é igual a {bin(n)[2:]}.')
elif base == 2:
    print(f'{n} convertido para octal é igual a {oct(n)[2:]}.')
elif base == 3: 
    print(f'{n} convertido para hexadecimal é igual a {hex(n)[2:]}.')
else:
    print('Opção inválida. Tente novamente!')

----------

038) Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
– O primeiro valor é maior
– O segundo valor é maior
– Não existe valor maior, os dois são iguais

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

if n1 > n2:
    print(f'O número maior é {n1} e o menor é {n2}.')
elif n1< n2:
    print(f'O número maior é {n2} e o menor é {n1}.')
else:
    print('Os números são iguais.')

----------

039) Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo
do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
genero = str(input('Qual seu sexo? F / M: '))
ano = int(input('Digite seu ano de nascimento: '))
ano_atual = date.today().year
if genero == 'F':
    print('Você não precisa se alistar.')
elif genero == 'M':
    if ano_atual - ano == 18:
        print('Você precisa se alistar esse ano.')
    elif ano_atual - ano < 18:
        print(f'Faltam {(ano_atual - ano - 18)*-1} anos para você se alistar.')
        print(f'Você se alistará em {ano + 18}.')
    else:
        print(f'Já se passaram {ano_atual - ano - 18} ano(s) do seu alistamento.')
        print(f'Você deveria ter se alistado em {ano + 18}.')

----------

040) Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
de acordo com a média atingida:
– Média abaixo de 5.0: REPROVADO
– Média entre 5.0 e 6.9: RECUPERAÇÃO
– Média 7.0 ou superior: APROVADO

n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))

media = (n1+n2)/2
print(f'A média é: {media:.2f}.')
if media < 5:
    print('Você foi \033[31mREPROVADO\033[m')
elif 5 <= media <= 6.9:
    print('Você está de \033[33mRECUPERAÇÃO\033[m') 
else:
    print('Você foi \033[32mAPROVADO\033[m')

----------

041) A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
e mostre sua categoria, de acordo com a idade:
– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
– Acima de 25 anos: MASTER

from datetime import date
atual = date.today().year
ano = (int(input('Digite o ano de nascimento do atleta: ')))
idade = atual - ano
print('='*20)

if idade <= 9:
    print('CATEGORIA MIRIM')
elif idade <= 14:
    print('CATEGORIA INFANTIL')
elif idade <= 19:
    print('CATEGORIA JUNIOR')
elif idade <= 20:
    print('CATEGORIA SÊNIOR')
else:
    print('CATEGORIA MASTER')

----------

042) 

r1 = float(input('Valor da reta 1: '))
r2 = float(input('Valor da reta 2: '))
r3 = float(input('Valor da reta 3: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 == r3:
        print('Essas retas formam um triângulo EQUILÁTERO.')
    elif r1 != r2 and r2 != r3 and r1 != r3:     # Também pode ser usado: >> r1 != r2 != r3 != r1 <<
        print('Essas retas formam um triângulo ESCALENO.')
    else:
        print('Essas retas formam um triângulo ISÓSCELES.')
else:
    print('Essas retas não podem formar um triângulo.')

----------

043) Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC)
e mostre seu status, de acordo com a tabela abaixo:
– IMC abaixo de 18,5: Abaixo do Peso
– Entre 18,5 e 25: Peso Ideal
– 25 até 30: Sobrepeso
– 30 até 40: Obesidade
– Acima de 40: Obesidade Mórbida 

peso = float(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura em m: '))

IMC = peso/(altura**2)
print(f'{IMC:.2f}')
if IMC < 18.5:
    print('ABAIXO DO PESO')
elif 18.5 <= IMC <= 25:
    print('PESO IDEAL')
elif 25 < IMC < 30:
    print('SOBREPESO')
elif 30 <= IMC <= 40:
    print('OBESIDADE')
else: 
    print('OBESIDADE MÓRBIDA')

----------

044) Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal
e condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal 
– 3x ou mais no cartão: 20% de juros

preço = float(input('Digite o preço do produto: R$ '))
print('='*40)
print(f'{"FORMAS DE PAGAMENTO":^40}')
print('='*40)
print('1 - à vista em dinheiro ou cheque \n2 - à vista no cartão \n3 - em até 2x no cartão \n4 - 3x ou mais') 
pag = int(input('Digite a forma de pagamento: '))

if pag == 1:
    print(f'10% de desconto: R$ {preço*0.9:.2f}')
elif pag == 2:
    print(f'5% de desconto: R$ {preço*0.95:.2f}')
elif pag == 3:
    parcela = preço / 2
    print(f'Sem desconto: R$ {preço:.2f} em 2 parcelas de R$ {parcela:.2f}.')
elif pag == 4:
    q = int(input('Em quantas parcelas? '))
    parcela = preço / q
    print(f'20% de juros: R$ {preço*1.2:.2f} em {q} parcelas de {parcela:.2f}')
else:
    print('Opção inválida. Tente novamente...')

----------

045) Crie um programa que faça o computador jogar Jokenpô com você.

from random import choice
from time import sleep
l = ['pedra', 'papel', 'tesoura']

j = str(input('Escolha: pedra, papel ou tesoura\n>>> '))
c = choice(l)
sleep(2)
print('Analisando sua escolha...')
sleep(2)

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
'''
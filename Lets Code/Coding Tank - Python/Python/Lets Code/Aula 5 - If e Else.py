### EXERCÍCIOS ALEATÓRIOS - AULA 5 - EXERCÍCIOS FIXAÇÃO IF / ELSE ###

'''
1) Analise o fluxograma e escreva o script correspondente.

x = 10
y = -1
if x % 2 == 0:
    print('y = 1')
else:
    print('y == 0')

----------

2) Analise o fluxograma e escreva o script correspondente.

x = int(input('Valor de x: '))
if 0 <= x <= 10:
    x = x**2
    print(x)
elif 10 < x <= 20:
    x = x**3
    print(x)
elif x > 20:
    x = -1
    print(x)

----------

3) Analise o fluxograma e escreva o script correspondente.

opçao = int(input('Escolha uma bebida:\n[1] - Coca-Cola\n[2] - Pepsi\n[3] - Guaraná\n[4] - Chá\n>>> '))
if opçao == 1:
    print('Você escolheu Coca-Cola.')
elif opçao == 2:
    print('Você escolheu Pepsi.')
elif opçao == 3:
    print('Você escolheu Guaraná.')
elif opçao == 4: 
    print('Você escolheu Chá.')

----------

4) Identifique o(s) erro(s) no código abaixo e corrija:

idade = int(input('Idade: '))
if 0 <= idade <= 10:
  print('vc é uma criança')
elif 11 <= idade <= 12:
  print('vc é pré-adolescente')
elif 13 <= idade <= 17:
  print('vc é adolescente')
elif idade >= 18:
  print('vc já é adulto')

----------

5) Identifique o(s) erro(s) no código abaixo e corrija. O que o código esse script faz?

x = int(input('Valor de x: '))
if (x % 2 == 0):
    print('Par')
    if 0 <= x <= 10:
        print(f'O número {x} é par entre 0 e 10')
else:
    print('Ímpar')
    if 0 <= x <= 10:
        print(f'O número {x} é ímpar entre 0 e 10')


O código retorna se o valor de x é par ou ímpar e se está entre 0 e 10.

----------

6) Faça um programa que receba um número (entre 0 e 10) e devolve o número escrito por extenso. Exemplo:
input: 2
output: dois

n = int(input('Número inteiro entre 0 e 10: '))
while n < 0 or n > 10:
    n = int(input('Número inteiro entre 0 e 10: '))
if n == 0:
    print(f'{n} = zero')
if n == 1:
    print(f'{n} = um')
if n == 2:
    print(f'{n} = dois')
if n == 3:
    print(f'{n} = três')
if n == 4:
    print(f'{n} = quatro')
if n == 5:
    print(f'{n} = cinco')
if n == 6:
    print(f'{n} = seis')
if n == 7:
    print(f'{n} = sete')
if n == 8:
    print(f'{n} = oito')
if n == 9:
    print(f'{n} = nove')
if n == 10:
    print(f'{n} = dez')

----------

7) Faça um script que simule uma calculadora simples. O usuário informa dois número e depois digita o símbolo
da operação artimética a ser realizada (+, -, *, /). Por exemplo, o usuário digita 5, 6 e por fim +. O script
apresenta o resultado da operação 5 + 6.
Exemplo:
input: 5 
input: 6
input: +
output: 11

n1 = float(input('Digite o primeiro termo: '))
n2 = float(input('Digite o segundo termo: '))
operaçao = str(input('Operação: ')).strip()[0]
if operaçao == '+':
    resultado = n1 + n2
if operaçao == '-':
    resultado = n1 - n2
if operaçao == '*':
    resultado = n1 * n2
if operaçao == '/':
    resultado = n1 / n2
print(f'O resultado da operação é {resultado}.')

----------

8) Faça um script que receba um número referente a um dia da semana (1 à 7) e devolva o nome do dia. Exemplo:
input: 1
output: domingo

n = int(input('Escolha de 1 a sete para descobrir o dia da semana: '))
while n < 1 or n > 7:
    n = int(input('Escolha de 1 a sete para descobrir o dia da semana: '))
if n == 1:
    print('DOMINGO')
if n == 2:
    print('SEGUNDA-FEIRA')
if n == 3:
    print('TERÇA-FEIRA')
if n == 4:
    print('QUARTA-FEIRA')
if n == 5:
    print('QUINTA-FEIRA')
if n == 6:
    print('SEXTA-FEIRA')
if n == 7:
    print('SÁBADO')

----------

9) Faça um script que receba o mês e o dia de nascimento do usuário e informe o seu signo astrológico
de acordo com a tabela a seguir:
Signo 	Intervalo
Áries 	21 março a 20 abril
Touro 	21 abril a 20 maio
Gêmeos 	21 maio a 20 junho
Câncer 	21 junho a 22 julho
Leão 	23 julho a 22 agosto
Virgem 	23 agosto a 22 setembro
Libra 	23 setembro a 22 outubro
Escorpião 	23 outubro a 21 novembro
Sagitário 	22 novembro a 21 dezembro
Capricórnio 	22 dezembro a 20 janeiro
Aquário 	21 janeiro a 18 fevereiro
Peixes 	19 fevereiro a 20 março
Exemplo:
input: 13
input: agosto
output: Leão

dia = int(input('Indique o dia de nascimento: '))
mes = str(input('Indique o mês de nascimento: ')).lower().strip()

if mes == 'março' and dia >= 21 or mes == 'abril' and dia <= 20:
    print('Áries')
elif mes == 'abril' and dia >= 21 or mes == 'maio' and dia <= 20:
    print('Touro')
elif mes == 'maio' and dia >= 21 or mes == 'junho' and dia <= 20:
    print('Gêmeos')
elif mes == 'junho' and dia >= 21 or mes == 'julho' and dia <= 22:
    print('Câncer')
elif mes == 'julho' and dia >= 23 or mes == 'agosto' and dia <= 22:
    print('Leão')
elif mes == 'agosto' and dia >= 23 or mes == 'setembro' and dia <= 22:
    print('Virgem')
elif mes == 'setembro' and dia >= 23 or mes == 'outubro' and dia <= 22:
    print('Libra')
elif mes == 'outubro' and dia >= 23 or mes == 'novembro' and dia <= 21:
    print('Escorpião')
elif mes == 'novembro' and dia >= 22 or mes == 'dezembro' and dia <= 21:
    print('Sagitário')
elif mes == 'dezembro' and dia >= 22 or mes == 'janeiro' and dia <= 20:
    print('Capricórnio')
elif mes == 'janeiro' and dia >= 21 or mes == 'fevereiro' and dia <= 18:
    print('Aquário')
elif mes == 'fevereiro' and dia >= 19 or mes == 'março' and dia <= 20:
    print('Peixes')

----------

10) Faça um script que informe se uma letra válida digitada como entrada é maiúscula ou minúscula. Exemplo:
Exemplo 1:
input: a
output: letra minúscula

Exemplo 2:
input: D
output: letra maiúscula

Exemplo 3:
input: $
output: não é uma letra

letra = str(input('Digite uma letra: ')).strip()[0]
if 'a' < letra < 'z':
    print('A letra é minúscula.')
else:
    print('A letra é maiúscula.')

'''
### EXERCÍCIOS AULA 8 - LAÇOES DE REPETIÇÃO FOR ###
'''
1) Analise o fluxograma e escreva o script correspondente:

x = 0
while x < 10:
    print (x)
    x = x + 1
print('Fim')

----------

2) Analise o fluxograma e escreva o script correspondente:

x = 0
y = 10
while x < y:
    if x % 2 == 0:
        print ('x é {}'.format(x))
        x = x + 1
        y = y - 1
    else:
        print ('y é {}'.format(y))
        x = x + 1
        y = y - 1
print ('x é {} e y é {}'.format(x, y))

----------

3) Analise o fluxograma e escreva o script correspondente:

x = 0
y = 0
while x < 10:
    if x % 2 == 0:
        if y < 5:
            y += 1
    else:
        x += 1
print(f'O valor de x é {x} e de y é {y}.')

----------

4) Faça um script que some dois números, desde que sejam ímpares maiores que 10.
Use um laço para não aceitar números diferentes do especificado.

while True:
    n1 = int(input('Digite um número ímpar e maior do que 10: '))
    n2 = int(input('Digite outro número ímpar e maior do que 10: '))
    print('-'*30)
    if n1 % 2 != 0 and n1 > 10 and n2 % 2 != 0 and n2 > 10:
        break
soma = n1 + n2
print(f'A soma dos números é {soma}.')
print('-'*30)

----------

5) Faça um script que imprima na tela todos os pares entre 0 e 1000.
Quantos pares existem nesse intervalo?

cont = 0
for c in range(0,1001):
    if c % 2 == 0:
        cont += 1
        print(f'{c}', end='... ')
print(f'\nNesse intervalo existem {cont} números pares.')

----------

6) Faça um script que reproduza o padrão usando "*" a seguir de acordo com o
número de linhas desejadas pelo usuário. Dica: print(5 * '@')

Exemplo 1
input: 3
output: *
        **
        ***

Exemplo 2
input: 5
output: *
        **
        ***
        ****
        *****

linhas = int(input('Quantas linhas você gostaria de reproduzir? '))
for c in range(0,linhas+1):
    print(f'{"*"*c}')

----------

7) Faça um script que informe o fatorial de um número:

Exemplo
input: 5
output: 1*2*3*4*5

fatorial = int(input('Você quer descobrir o fatorial de qual número? '))
mult = 1
for c in range(1,fatorial+1):
    mult = mult*c
print(f'O fatorial de {fatorial} é {mult}.')

----------

8) Informe, de forma decrescente todos os pares entre N (número fornecido pelo usuário) e -N.

Exemplo
input: 5
output: 4
        2
        0
        -2
        -4

num = int(input('Digite um número: '))
for c in range(num, -num-1, -1):
    if c % 2 == 0:
        print(f'{c}...', end=' ')
'''
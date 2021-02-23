### Curso em Vídeo - Exercícios Aula 6 - Tipos Primitivos e Saída de Dados ###

'''
003) Crie um programa que leia dois números e mostre a soma entre eles.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
soma = n1 + n2
print('A soma entre {} e {} é igual a {}.'.format(n1, n2, soma))

----------

004) Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
e todas as informações possíveis sobre ele.

Resposta 1
x = input('Digite algo: ')
print('O tipo primitivo desse valor é:', type(x))
print('É composto apenas por letras?', x.isalpha())
print('É composto apenas por números?', x.isnumeric())
print('É alfanumérico?', x.isalnum())
print('É composto apenas por espaços?', x.isspace())
print('Tem apenas letras minúsculas?', x.islower())
print('Tem apenas letras maiúsculas?', x.isupper())
print('Somente a primeira letra é maiúscula?', x.istitle())

OU

Resposta 2

x = input('Digite algo: ')
print(f'O tipo primitivo desse valor é: {type(x)}.')
print(f'É composto apenas por letras? {x.isalpha()}.')
print(f'É composto apenas por números? {x.isnumeric()}.')
print(f'É alfanumérico? {x.isalnum()}.')
print(f'É composto apenas por espaços? {x.isspace()}.')
print(f'Tem apenas letras minúsculas? {x.islower()}.')
print(f'Tem apenas letras maiúsculas? {x.isupper()}.')
print(f'Somente a primeira letra é maiúscula? {x.istitle()}.')

OU

RESPOSTA 3

x = input('Digite algo: ')
print('O tipo primitivo do valor é: {}.'.format(type(x)))
print('É composto apenas por letras? {}.'.format(x.isalpha()))
print('É composto apenas por números? {}.'.format(x.isnumeric()))
print('É alfanumérico? {}.'.format(x.isalnum()))
print('É composto apenas por espaços? {}.'.format(x.isspace()))
print('Tem apenas letras minúsculas? {}.'.format(x.islower()))
print('Tem apenas letras maiúsculas? {}.'.format(x.isupper()))
print('Somente a primeira letra é maiúscula? {}.'.format(x.istitle()))
'''
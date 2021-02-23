### Curso em Vídeo - Exercícios Aula 13 - Repetições em Python - For ###

'''
046) Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0,
com uma pausa de 1 segundo entre eles.

from time import sleep
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('Feliz Ano Novo!!!')

----------

047) Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50. 

for c in range(1, 51):
    if c % 2 == 0:
        print(c)

----------

048) Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.

soma = 0
cont = 0
for c in range(1,501,2):
    if c % 3 == 0:
        cont += 1
        soma += c

print(f'A soma de todos os {cont} valores solicitados é {soma}.')

----------

049) Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

n = int(input('Digite um número para encontrar sua tabuada: '))
for c in range(0,11):
    print(f'{n} x {c} = {n*c}')

----------

050) Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for ímpar, desconsidere-o.

soma = 0
for c in range(1,7):
    n = int(input(f'Digite o {c}° valor: '))
    if n % 2 == 0:
        soma += n
print(f'A soma dos números pares digitados é: {soma}.')

----------

051) Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

print('======== Progressão Aritimética ========')
termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
ultimo = termo + (9*razao)
for c in range(termo, ultimo+1, razao):
    print(f'{c}', end=' → ')
print('Fim!')

----------

052) Faça um programa que leia um número inteiro e diga se ele é ou não um número primo. 

n = int(input('Digite um número: '))
total = 0
for c in range(1,n+1):
    if n % c == 0:
        total += 1
if total == 2:
    print(f'O número {n} É PRIMO.')
else:
    print(f'O número {n} NÃO É PRIMO.')

----------

053) Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

frase = str(input('Digite uma frase: ')).strip().upper()
unida = frase.replace(' ','')
inverso = unida[::-1]
# OUTRA FORMA DE REVERTER A FRASE

inverso = ''
for letra in range(len(unida)-1, -1, -1):
    inverso = inverso + unida[letra]

print(f'O inverso de {unida} é {inverso}.')
if inverso == unida:
    print('Temos um palíndromo.')
else:
    print('A frase digitada não é um palíndromo')

----------

054) Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade
e quantas já são maiores.

from datetime import date
cont1 = 0
cont2 = 0
for c in range(0,7):
    ano = int(input('Digite o ano de nascimentoda pessoa {c}: '))
    ano_atual = date.today().year
    if ano_atual - ano >= 21:
        cont1 += + 1
    else:
        cont2 += 1
print(f'{cont1} pessoas são maiores de idade e {cont2} são menores.')

----------

055) Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0
for c in range(1,6):
    p = float(input(f'Peso da pessoa {c} em kg: '))
    if c == 1:
        maior = p
        menor = p
    else:
        if p > maior:
            maior = p
        if p < menor:
            menor = p
print(f'O maior peso lido foi de {maior}kg e o menor foi {menor}kg.')

----------

056) Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo,
qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

somamedia = 0
maioridade = 0
nomemaisvelho = ''
cont_mulher = 0
for c in range (1,5):
    print(f'----- {c} PESSOA -----')
    nome = str(input(f'Nome da pessoa {c}: ')).strip()
    idade = int(input(f'Idade da pessoa {c}: '))
    sexo = str(input(f'Sexo da pessoa {c} (F/M): ')).strip()
    somamedia += idade
    if sexo in 'Mm':
        if idade > maioridade:
            maioridade = idade
            nomemaisvelho = nome
    if sexo in 'Ff':
        if idade < 20:
            cont_mulher += 1

media = somamedia/4
print('-'*20)
print(f'A média das idades do grupo é de {media} anos.')
print('-'*20)
print(f'O nome do homem mais velho é {nomemaisvelho}.')
print('-'*20)
print(f'{cont_mulher} mulheres tem menos de 20 anos.')
'''
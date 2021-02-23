### Curso em Vídeo - Exercícios Aula 16 - Tuplas em Python ###

'''
072) Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

numeros = ('zero', 'um', 'dois', 'três', 'quatro',
'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete',
'dezoito', 'dezenove', 'vinte')
teclado = int(input('Digite um número de 0 a 20: '))
while teclado < 0 or teclado > 20:
    teclado = int(input('Digite um número de 0 a 20: '))
resposta = numeros[teclado]
print(f'O número que você escolheu foi {resposta}.')

----------

073) Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro
de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time do Palmeiras.

times = ('Atlético-MG', 'Internacional', 'São Paulo', 'Palmeiras',
'Vasco da Gama', 'Flamengo', 'Fluminense', 'Sport Recife', 'Santos',
'Fortaleza', 'Athletico-PR', 'Ceará SC', 'Atlético-GO', 'Grêmio',
'Corinthians', 'Coritiba', 'Bragantino-SP', 'Botafogo', 'Goiás', 'Bahia')
print(f'A) {times[:4]}')
print('-'*20)
print(f'B) {times[-4:]}')
print('-'*20)
# SABENDO O LEN: print(f'B) {times[16:]}')
print(f'C) {sorted(times)}')
print('-'*20)
palmeiras = times.index('Palmeiras') + 1
print(f'D) O Plameiras está na {palmeiras}ª colocação.')
print('-'*20)

----------

074) Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint
n = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print(f'Eu sorteei os valores {n}.')
print('-'*20)
print(f'O maior valor sorteado foi {max(n)} e o menor foi {min(n)}.')
print('-'*20)

----------

075) Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.

numeros = (int(input('Digite o primeiro número: ')), int(input('Digite o segundo número: ')),
int(input('Digite o terceiro número: ')), int(input('Digite o quarto número: ')))
print(numeros)
print('-'*20)
print(f'A) O número 9 apareceu {numeros.count(9)} vezes.')
print('-'*20)
if 3 in numeros:
    posiçao = numeros.index(3) + 1
    print(f'B) O número 3 aparece na {posiçao} posição.')
else: 
    print(f'B) O número 3 não aparece na tupla.')
print('-'*20)
print(f'C) Os números ', end='')
for c in numeros:
    if c % 2 == 0:
        print(f'{c}', end=' ')
print(f'são pares.') 
print('-'*20)

----------

076) Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

RESPOSTA 1

lojinha = ('Biquiní', 99.90, 'Maiô', 119.90, 'Saída de praia', 89.90,
'Bolsa de praia', 79.90, 'Esteira', 89.90, 'Óculos de sol', 159.90)
print('-'*40)
print(f'{"LOJINHA DO MAR":^38}')
print('-'*40)
print(f'{lojinha[0]:.<30}R$', end='')
print(f'{lojinha[1]:>7.2f}')
print(f'{lojinha[2]:.<30}R$', end='')
print(f'{lojinha[3]:>7.2f}')
print(f'{lojinha[4]:.<30}R$', end='')
print(f'{lojinha[5]:>7.2f}')
print(f'{lojinha[6]:.<30}R$', end='')
print(f'{lojinha[7]:>7.2f}')
print(f'{lojinha[8]:.<30}R$', end='')
print(f'{lojinha[9]:>7.2f}')
print(f'{lojinha[10]:.<30}R$', end='')
print(f'{lojinha[11]:>7.2f}')
print('-'*40)

RESPOSTA 2

lojinha = ('Biquiní', 99.90, 'Maiô', 119.90, 'Saída de praia', 89.90,
'Bolsa de praia', 79.90, 'Esteira', 89.90, 'Óculos de sol', 159.90)
print('-'*40)
for posiçao in range(0, len(lojinha)):
    if posiçao % 2 == 0:
        print(f'{lojinha[posiçao]:.<30}R$ ', end='')
    else:
        print(f'{lojinha[posiçao]:>6.2f}')
print('-'*40)

----------

077) Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar,
para cada palavra, quais são as suas vogais.

palavras = ('cachorro', 'gato', 'coelho', 'cavalo', 'vaca', 'porco', 'zebra', 'pássaro', 'urso')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos → ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
'''

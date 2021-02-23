### EXERCÍCIOS ALEATÓRIOS - AULA 12 - FIXAÇÃO ###

'''
1) Faça um programa que peça 10 números para o usuário e guarde os números em uma lista.
Com a lista preenchida descubra quantos números são pares.

lista = []
par = []
for c in range(0,10):
    lista.append(int(input('Digite um número: ')))
for c in lista:
    if c % 2 == 0:
        par.append(c)

print(f'A lista apenas com números pares é {par} e contém {len(par)} elementos.')

----------

2) Faça um script que leia 10 números do usuário e devolva duas listas:
uma com os números ímpares e outra com os números pares.
Exemplo
input 1: 5
input 2: 4
(etc...): 6.. 7.. 1.. 2.. 3.. 7..
input 9: 4
input 10: 8
output: lista com ímpares: [5, 7, 1, 3, 7]
        lista com pares: [4, 6, 2, 4, 8]

lista = []
pares = []
impares = []

for c in range(0,10):
    lista.append(int(input('Digite um número: ')))
for c in lista:
    if c % 2 == 0:
        pares.append(c)
    else:
        impares.append(c)
print(f'Lista com números pares: {pares}.')
print(f'Lista com números impares: {impares}.')

----------

3) Faça um script que leia números do usuário, enquanto ele não digitar 0.
Armazene esses números em uma lista e ao final informe quantos números foram digitados, ignorando o 0.
Exemplo
input: 2
input: 4
input: -1
input: -5
input: 0
output: Você digitou 4 números

lista = []
while True:
    n = int(input('Digite um número ou 0 (zero) para parar: '))
    if n == 0:
        break
    lista.append(n) 
print(f'Foram digitados {len(lista)} elementos.')

----------
4) Faça um script que lê 10 números e mostra na tela aqueles que são maiores que a média.

lista = []
maiores = []
for c in range(0,10):
    lista.append(int(input('Digite um número: ')))
media = sum(lista)/10
for c in lista:
    if c > media:
        maiores.append(c)
print(f'Os números acima da média são: {maiores}.')

----------

5) Crie duas listas sobre um time de futebol com 11 jogadores:
uma lista com a idade dos jogadores e outra com as alturas.
Mostre na tela a idade do jogador mais alto.

idade = []
altura = []
for c in range(0,11):
    idade.append(int(input(f'Digite a idade do jogador {c+1}: ')))
    altura.append(int(input(f'Digite a altura do jogador {c+1} (em cm): ')))

pos = altura.index(max(altura))

print(f'O jogador mais alto tem {max(altura)} cm e {idade[pos]} anos.')
'''

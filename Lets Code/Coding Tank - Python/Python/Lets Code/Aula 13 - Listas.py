### EXERCÍCIOS ALEATÓRIOS - AULA 13 - FIXAÇÃO ###

'''
1) Implemente um script que leia 10 números do usuário e informe se ali há algum número repetido.

numeros = []
for c in range(0,10):
    n = int(input('Digite um número: '))
    if n not in numeros:
        numeros.append(n)
    else:
        print('Esse número já foi adicionado anteriormente.')

repetidos = 10 - len(numeros)
print(f'Foram digitados {repetidos} números repetidos.')

----------

2) Faça um programa que, dadas duas listas de mesmo tamanho, crie uma nova lista com cada
elemento igual a soma dos elementos da lista 1 com os da lista 2, na mesma posição.
Exemplo:
Dadas lista1 = [1, 4, 5] e lista2 = [2, 2, 3], então lista3 = [1+2, 4+2, 5+3] = [3, 6, 8]

print('-'*30)
lista1 = []
lista2 = []
q = int(input('Quantos elementos você quer adicionar em cada lista? '))
for c in range(0,q):
    n = lista1.append(int(input(f'Adicione o item {c} na lista 1: ')))
print('-'*30)
for d in range(0,q):
    n = lista2.append(int(input(f'Adicione o item {d} na lista 2: ')))
print('-'*30)
print(f'Lista 1 = {lista1}')
print('-'*30)
print(f'Lista 2 = {lista2}')
cont = 0
lista3 = []
for c in lista1:
    soma = c + lista2[cont]
    cont += 1
    lista3.append(soma)
print('-'*30)
print(f'A soma de cada elemento da lista 1 com a lista 2 é {lista3}.')

----------

3) Dada a lista abaixo, faça um script que informe o somatório dos números em L.

L = [[1, 2], [3, 4], [5, 6], [7, 8]] 
somatotal = 0
for c in L:
    soma = c[0] + c[1]
    somatotal += soma

print(f'A soma de todos os elementos da lista L é {somatotal}.')

----------

4) Faça um script que recebe um texto de entrada e exibe o texto ao contrário.
Exemplo: 
input: teste
output: etset

texto = str(input('Digite um texto: ')).strip().lower()
junto = texto.replace(' ','')
inverso = junto[::-1]

print(f'O texto digitado de forma invertida é: {inverso}')

----------

5) Agora faça um script que recebe uma palavra e informa se é um palíndromo,
ou seja, se a palavra é igual a ela mesma ao contrário.

Exemplo 1
input: Ana
output: é palindromo

Exemplo 2
input: abacaxi
output: não é palindromo

texto = str(input('Digite um texto: ')).strip().lower()
junto = texto.replace(' ','')
inverso = junto[::-1]
print('-'*20)
print(f'Texto digitado: {junto}')
print(f'Texto invertido: {inverso}')
print('-'*20)
if inverso == junto:
    print('O texto É UM PALÍNDROMO.')
else:
    print('O texto NÃO É PALÍNDROMO.')

'''
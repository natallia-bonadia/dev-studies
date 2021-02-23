### EXERCÍCIOS ALEATÓRIOS - DESAFIO 1 ###

'''
1) Dada uma lista qualquer com uma quantidade indeterminada de números, faça um script que exiba essa
lista ordenada de forma crescente.
Dica: comece com uma lista de três elementos - len(lista)=3 - e tente generalizar o loop para len(lista)=N depois.

Exemplo 1
L = [4, 1, 2]
output: [1, 2, 4]

Exemplo 2
L = [7, 8, 6, 5, 1, 2]
output: [1, 2, 5, 6, 7, 8]

Exemplo 3
L = [1, -2, 3, -4, 5, -6]
output: [-6, -4, -2, 1, 3, 5]

# PARA 3 ELEMENTOS
lista = []
for c in range(0,3):
    n = int(input('Digite um número: '))
    if c == 0:
        lista.append(n)
    elif n > lista[-1]:
        lista.append(n)    
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
        pos += 1
print('-'*30)
print(f'Os valores digitados em ordem foram {lista}.')

# PARA N ELEMENTOS
lista = []
q = int(input('Quantos elementos você quer adicionar na lista? '))
for c in range(0,q):
    n = int(input('Digite um número: '))
    if c == 0:
        lista.append(n)
    elif n > lista[-1]:
        lista.append(n)    
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
        pos += 1
print('-'*30)
print(f'Os valores digitados em ordem foram {lista}.')
'''










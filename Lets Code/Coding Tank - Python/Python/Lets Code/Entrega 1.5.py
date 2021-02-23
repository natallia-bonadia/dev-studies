### ENTREGA 1.5 ###
'''
1) Faça um script que receba 10 números inteiros do usuário e devolva o maior e o menor deles.
Exemplo
input 1: 1
input 2: 6
(etc) inputs: 7.. 8.. 9.. -12.. 32.. 3.. 
input 9: 4
input 10: 5
output: o maior é 32
        o menor é -12

lista = []
for n in range(0,10):
    lista.append(int(input('Digite um número: ')))
print('=-'*40)
print(f'A lista formada em ordem de digitação é {lista}.')
print('=-'*40)
print(f'O maior número da lista é {max(lista)} e o menor número da lista é {min(lista)}.')
print('=-'*40)

----------

2) Faça um script que receba 10 números inteiros do usuário e devolva a soma dos números inseridos em entradas ímpares.
Exemplo
input 1: 2
input 2: 5
(etc...): 6.. 9.. 8.. 7.. 4.. 4..
input 9: 12
input 10: 3
output: 2+6+8+4+12
O output do exemplo retorna a soma entre os números fornecidos nas entradas ímpares (input 1, input 3, input 5, input 7 e input 9).

lista = []
for n in range(0,10):
    lista.append(int(input('Digite um número: ')))
soma = lista[1]+lista[3]+lista[5]+lista[7]+lista[9]
print('=-'*40)
print(f'Os elementos inseridos nos índices ímpares são: {lista[1]}, {lista[3]}, {lista[5]}, {lista[7]} e {lista[9]}.')
print(f'A soma desses elementos é {soma}.')
print('=-'*40)
'''

### EXERCÍCIOS AULA 9 - LISTAS ###

'''
1) Pra quê serve uma lista? Em quais situações são úteis?

Para armazenar uma sequência de variáveis, sejam elas int, float, bool ou str.
Elas são úteis quando queremos organizar dados em um único lugar e acessá-los de forma fácil.
----------

2) Qual a relação entre posição e índice de um item em uma lista?

A posição de um elemento em uma lista se inicia em 1 (primeiro) e vai até o último (n),
assim como nomeamos as colocações de um campeonato, por exemplo. Já o índice se inicia no 0
(linguagem Python), portanto seu último elemento terá o índice n-1.
----------

3) Faça um script que peça para o usuário digitar um número N e imprima uma lista com todos os números de 0 a N-1.
Exemplo
input: 5
output: [0, 1, 2, 3, 4]

N = int(input('Digite um número: '))
for lista in range (0,N):
    print(lista)
----------

4) Faça um programa que leia nome e idade de 5 pessoas e coloque os nomes em uma lista e as idades em outra.
Apresente as duas listas preenchidas.

nome = []
idade = []

for c in range (0,5):
    n = nome.append(input('Digite um nome: '))
    i = idade.append(input('Digite a idade: '))

print(nome)
print(idade)
----------

5) Faça um programa que peça 10 números para o usuário e guarde os números em uma lista.
Imprima os itens da lista preenchida de trás para frente.

lista = []
for n in range (0,10):
    lista.append(int(input('Digite um número: ')))

lista.sort(reverse=True)
print('A lista dos números digitados em ordem decrescente é {}.'.format(lista))
'''
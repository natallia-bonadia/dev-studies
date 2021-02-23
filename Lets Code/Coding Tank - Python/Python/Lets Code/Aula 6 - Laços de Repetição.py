### EXERCÍCIOS AULA 6 - LAÇOS DE REPETIÇÃO ###

'''
1) Defina de forma sucinta a diferença entre comandos de repetição e controle de fluxo.

O controle de fluxo serve para tomar decisões entre duas ou mais opções, já o laço de repetição
apenas executa uma ação quando a condição imposta se torna verdadeira.
----------

2) Analise o algoritmo abaixo e diga qual será o valor de x ao final.
1. x <- 0
2. enquanto x é menor que 5, x <- x + 1
3. apresente o valor de x

x é igual a 5.
----------

3) Analise o código abaixo e diga quais serão os valores de x e y ao final.
1. x <- 1
2. y <- 0
3. enquanto x é menor que 5, y <- y + 2
4. apresente o valor de x e y

Como o algoritmo possui um laço infinito, o valor de x será 1 e de y será sempre uma progressão
aritmética com início em 2 e razão 2.
----------

4) O que faz um laço ser infinito?

Quando a condição do algoritmo nunca é atingida.
----------

5) Identifique qual dos algoritmos é um laço infinito:
- Algoritmo 1
1. x <- 1
2. enquanto x é diferente de 0, apresente o valor de x
- Algoritmo 2
1. x <- 1
2. enquanto x é diferente de 0, x <- x + 1
- Algoritmo 3
1. numero <- ler número
2. enquanto numero é menor que 10, apresente o valor de numero e ler número

1 e 2.
----------

6) Faça um algoritmo que peça ao usuário um número e imprima todos os números de um até o número dado.
Exemplo:
input: 5
output: 1 2 3 4 5

x = int(input('Digite um número: '))
c = 0
while c < x:
    c = c + 1
    print(c)
----------

7) Faça um algoritmo que peça para um usuário digitar um número e que só finaliza quando o usuário digitar 0.

x = int(input('Digite um número: '))
while x != 0:
    print('Ops! Tente novamente...')
    x = int(input('Digite um número: '))
else:
    print('Parabéns!')
----------

8) Faça um programa que peça para o usuário digitar a idade, o salário e o sexo de uma pessoa até que as entradas
digitadas sejam válidas.
Idade: entre 0 e 150;
Salário: maior que 0;
Gênero: M, F ou Outro.

idade = int(input('Digite sua idade: '))

while idade < 0 or idade > 150:
    print('Ops! Tente novamente...')
    idade = int(input('Digite sua idade: '))
else:
    print('Vamos para a próxima pergunta.')

salario = float(input('Digite seu salário: '))
while salario < 0:
    print('Ops! Tente novamente...')
    salario = float(input('Digite seu salário: '))
else:
    print('Vamos para a última pergunta.')

genero = input('Digite seu gênero (F, M ou outro): ')
while genero != 'F' and genero != 'M' and genero != 'outro':
    print('Ops! Tente novamente...')
    genero = input('Digite seu gênero (F, M ou outro): ')
else:
    print('Agradecemos sua participação!')
----------

9) Peça ao usuário para digitar um número n e some todos os números de 1 a n.
Exemplo 1:
input: 4
output: 10
Exemplo 2:
input: 3
output: 6

num = int(input('Digite um número: '))
c = 0
s = 0

while c < num:
    c = c + 1
    s = s + c
    print(s)
'''
### EXERCÍCIOS AULA 7 - LAÇOS DE REPETIÇÃO EM PYTHON ###

'''
1) Faça um script que peça ao usuário um número e imprima todos os números de um até o número dado.
Exemplo:
input: 5
output: 1 2 3 4 5 

x = int(input('Digite um número: '))
c = 0
while c < x:
    c = c + 1
    print(c)
----------

2) Faça um script que peça para um usuário digitar um número e que só finaliza quando o usuário digitar 0.

x = int(input('Digite um número: '))
while x != 0:
    print('Ops! Tente novamente...')
    x = int(input('Digite um número: '))
else:
    print('Parabéns!')
----------

3) Faça um programa que peça para o usuário digitar a idade, o salário e o sexo de uma pessoa até que as entradas
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

4) Peça ao usuário para digitar um número n e some todos os números de 1 a n.
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
----------

5) Faça um script que imprima a tabuada do 9 (de 9x1 a 9x10) usando loops.

c = 0
v = 9
while c < 10:
    m = c*v
    print('{} x {} = {}'.format(v, c, m))
    c = c + 1
----------

6) Faça um script que peça para um usuário digitar um número e que só finaliza
quando o usuário digitar 0. Ao final imprima a soma de todos os números digitados.
Exemplo
input: 5
input: 1
input: 0
output: 6

n = int(input('Digite um número: '))
s = 0

while n != 0:
    s = s + n
    n = int(input('Digite um número: '))

print('A soma dos números digitados é igual a {}.'.format(s))
----------

7) Faça um programa que recebe um número inteiro do usuário e imprime na tela a
quantidade de divisores desse número e quais são eles.

n = int(input('Digite um número: '))
c = 0
s = 0

while c < n:
    c = c + 1
    if n%c == 0:
        print('Divisor do número {} é {}'.format(n, c))
        s = s + 1

print('A quantidade de divisores é: {}'.format(s))
----------

8) Desafio! - Calcule a soma de até mil termos da série 1 + 1/2 + 1/4 + 1/8 + 1/16 + ...
Dica: Use três variáveis:
• um contador, que começa em zero;
• uma variável para a soma de todos os termos, que também começa em zero;
• uma variável para cada termo, que começa em 1 e a cada loop é dividida por 2.
A repetição da soma de mil termos pode ser feita com a função while contador < 1000.

c = 0
soma = 0
div = 1

while c < 1000:
    c = c + 1
    soma = soma + div
    div = float(div*(1/2))

print('A soma de todos os termos da PG é {}.'.format(soma))
'''
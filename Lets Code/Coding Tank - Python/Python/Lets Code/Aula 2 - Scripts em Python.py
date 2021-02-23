### EXERCÍCIOS AULA 2 - SCRIPTS EM PYTHON ###

'''
1) Faça um script que mostra a média de duas notas.

A = int(input("Digite a média 1:"))
B = int(input("Digite a média 2:"))
resultado = (A + B) / 2
print(resultado)
----------

2) Faça um script para somar dois números e multiplicar o resultado
pelo primeiro número.

A = int(input("Digite um número:"))
B = int(input("Digite um número:"))
resultado = (A + B) * A
print(resultado)
----------

3) Escreva um script para ler um valor (do teclado) e escrever
(na tela) o seu antecessor.

A = int(input("Digite um número:"))
resultado = A - 1
print(resultado)
----------

4) Escreva um script para ler o salário mensal atual de um funcionário
e o percentual de reajuste. Calcular e escrever o valor do novo salário.

A = float(input("Digite o salário mensal:"))
B = float(input("Digite o percentual de reajuste:"))
reajuste = (B / 100) + 1
resultado = A * reajuste
print(resultado)
----------

5) Escreva um script que armazene o valor 10 em uma variável A e o
valor 20 em uma variável B. A seguir (utilizando apenas atribuições
entre variáveis) troque os seus conteúdos fazendo com que o valor que
está em A passe para B e vice-versa. Ao final, escrever os valores que
ficaram armazenados nas variáveis.

A = 10
B = 20
aux = A
A = B
B = aux
print(A)
print(B)
----------

6) Faça um script que peça um nome e uma idade. Ao final, informe o
ano de nascimento dessa pessoa.

from datetime import date
data_atual = date.today()
ano_atual = data_atual.year
nome = input("Digite seu nome:")
idade = int(input("Digite sua idade:"))
ano_nascimento = ano_atual-idade
print(ano_nascimento)
----------

7) Faça um script que receba um número e informe:
O dobro desse número
O número ao quadrado
O número ao cubo

A = int(input("Digite um número:"))
dobro = A*2
print(dobro)
quadrado = A**2
print(quadrado)
cubo = A**3
print(cubo)
----------

8) Faça um script que converta graus Fahrenheit para Celsius.
Dica: C = (5 * (F-32) / 9)

A = float(input("Digite a temperatura em Fahrenheit:"))
C = 5 * (A - 32) / 9
print(C)
'''
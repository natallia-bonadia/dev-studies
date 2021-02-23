### Curso em Vídeo - Exercícios Aula 7 - Operadores Aritméticos ###

'''
005) Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e
seu antecessor.

n = int(input('Digite um número: '))
print(f'O número digitado é {n}, seu antecessor é {n-1} e seu sucessor é {n+1}.')

----------

006) Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

RESPOSTA 1
n = float(input('Digite um número para descobrir seu dobro, triplo e raiz quadrada: '))
print(f'O dobro de {n} é {n*2}; \nO tpriplo de {n} é {n*3}; \nA raiz quadrada de {n} é {n**(1/2):.2f}.')
OU 
RESPOSTA 2
n = float(input('Digite um número para descobrir seu dobro, triplo e raiz quadrada: '))
print(f'O dobro de {n} é {n*2}; \nO tpriplo de {n} é {n*3}; \nA raiz quadrada de {n} é {pow(n, 1/2):.2f}.')
# a potência pode ser feita também {pow(n, 2)}

----------

007) Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre
a sua média.

n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))
m = (n1 + n2) / 2
print(f'A média entre as notas {n1} e {n2} é igual a {m:.2f}.')

----------

008) Escreva um programa que leia um valor em metros e o exiba convertido em
centímetros e milímetros.

v = float(input('Digite um valor em metros: '))
km = v * 0.001
hm = v * 0.01
dam = v * 0.1
dm = v * 10
cm = v * 100
mm = v * 1000
print(f'{v:.1f} metros corresponde a \n{km:.3f} km \n{hm:.3f} hm \n{dam:.3f} dam \n{dm:.1f} dm \n{cm:.1f} cm \n{mm:.1f} mm')

----------

009) Faça um programa que leia um número inteiro qualquer e mostre na tela
a sua tabuada.

n = int(input('Digite um número para encontrar sua tabuada: '))
print('-' * 15)
print(f'{n} x 0 = {n * 0:2} \n{n} x 1 = {n * 1:2} \n{n} x 2 = {n * 2:2} \n{n} x 3 = {n * 3:2}')
print(f'{n} x 4 = {n * 4:2} \n{n} x 5 = {n * 5:2} \n{n} x 6 = {n * 6:2} \n{n} x 7 = {n * 7:2}')
print(f'{n} x 8 = {n * 8:2} \n{n} x 9 = {n * 9:2}')
print('-' * 15)

----------

010) Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre
quantos dólares ela pode comprar.

n = float(input('Quanto dinheiro você tem na carteira? R$ '))
d = n/5.31
e = n/6.29
l = n/6.87
print(f'Você pode comprar US$ {d:.2f} ou € {e:.2f} ou £ {l:.2f}.')    

----------

011) Faça um programa que leia a altura e a largura de uma parede em metros, calcule
a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro
de tinta pinta uma área de 2m².

h = float(input('Digite a altura da parede: '))
l = float(input('Digite a largura da parede: '))
A = h * l
tinta = A / 2
print(f'Para pintar uma parede de {A:.2f} metros quadrados, ', end='')
print(f'você vai precisar de {tinta:.2f} litros de tinta.')

----------

012) Faça um algoritmo que leia o preço de um produto e mostre seu novo preço,
com 5% de desconto.

p = float(input('Qual o preço do produto? R$ '))
d = p * 0.95
print(f'Com 5% de desconto seu produto ficará R$ {d:.2f}.')

----------

013) Faça um algoritmo que leia o salário de um funcionário e mostre seu novo
salário, com 15% de aumento.

nome = input('Digite o nome do funcionário: ')
s1 = float(input(f'Digite o salário de {nome}: '))
s2 = s1 * 1.15
print(f'O novo salário de {nome} será R${s2:.2f}.')

----------

013 EXTRA) Faça um algoritmo que leia o valor de um produto para pagamento à vista
com desconto e a prazo com acréscimo.

p = float(input('Insira o preço do produto R$ '))
dv = float(input('Insira a porcentagem de desconto para pagamento à vista '))
dp = float(input('Insira a porcentagem de acréscimo para pagamento a prazo '))
pv = p - (p*dv/100)
pp = p + (p*dp/100)
print(f'O valor à vista com {dv} % de desconto será R$ {pv:.2f}.\nO valor a prazo com {dv} % de acréscimo será R$ {pp:.2f}.')

----------

014) Escreva um programa que converta uma temperatura digitando em graus Celsius e
converta para graus Fahrenheit.

C = float(input('Qual a temperatura em °Celsius? '))
F = ((9*C)/5)+32
print(f'A temperatura de {C} °C corresponde a {F} °F.')

----------

015) Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o
carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Digite a km percorrida: '))
d = int(input('Digite a quantidade de dias que o carro ficou alugado: '))
pkm = km*0.15
pd = d*60
print(f'O valor total do aluguel é de {pkm+pd:.2f}')
'''
### EXERCÍCIOS ALEATÓRIOS - LISTA DE EXERCÍCIOS AULA 2 ###

'''
1) Escreva um script que dado o raio de um círculo, calcule a sua circunferência.

r = float(input('Digite o raio de um círculo para descobrir sua circunferência: '))
pi = 3.14
C = 2*pi*r
print(f'Considerando pi = 3.14, o valor da circunferência é {C}.')

----------

2) Faça um script que, dado a posição inicial (Si), tempo (t) e velocidade (v), calcule a posição final
de um automóvel percorrendo um caminho em linha reta a partir da fórmula S = Si + vt.

Si = float(input('Digite a posição inicial do automóvel em km: '))
t = float(input('Digite o tempo de deslocamento em h: '))
v = float(input('Digite a velocidade do automóvel em km/h: '))

S = Si + (v * t)

print(f'A posição final do automóvel é {S} km.')

----------

3) Faça um script que calcula o preço total de uma lavanderia. Inicialmente, deve ser perguntado o total
de camisas, calças e meias (par), sendo o valor da lavagem de cada um de acordo com:
    Camisa - R$ 12
    Calça - R$ 20
    Meia (par) - R$ 5.50

print('=== Ordem de Serviço - Lavanderia ===')
print( )

camisas = int(input('Total de camisas: '))
calças = int(input('Total de calças: '))
meias = int(input('Total de pares de meia: '))

print(f'Total do Serviço: R$ {camisas*12 + calças*20 + meias*5.5:.2f}.')

----------

4) Faça um script que peça o peso e altura de uma pessoa e calcule seu IMC (Índice de Massa Corporal).
Dica:IMC = Peso/Altura²

print('=== CALCULE SEU IMC ===')
peso = float(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura em m: '))

IMC = peso/altura**2
print(f'{IMC:.2f}')
if IMC < 18.5:
    print('Classificação: MAGREZA')
elif 18.5 <= IMC <= 24.9:
    print('Classificação NORMAL')
elif 25 <= IMC <= 29.9:
    print('Classificação SOBREPESO')
elif 30 <= IMC <= 39.9:
    print('Classificação OBESIDADE')
else:
    print('Classificação OBESIDADE GRAVE')

----------

5) De forma sucinta, defina o que é um script. O que diferencia um script de um algoritmo em português?

Um algoritmo é a ordem lógica das operações que serão executadas para solucionar um problema, já o script
é o conjunto de instruções que será utilizado para fazer o algoritmo funcionar.
Logo, o script varia de acordo com a linguagem utilizada, mas o algoritmo não, pois a mesma lógica pode ser
utilizada em diversas linguagens.
'''
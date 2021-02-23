### EXERCÍCIOS ALEATÓRIOS - REVISÃO ###

'''
1) Uma companhia de energia elétrica precisa da sua ajuda para calcular o preço a ser cobrado
pela energia fornecida. O valor do kWh é R$0,79, porém o preço mínimo é de R$27,90.
Dado a quantidade de kWh consumido, informe o valor a ser pago.

kwh = float(input('Digite o consumo mensal em kWh: '))
preço = kwh*0.79
if preço < 27.9:
    print(f'O seu consumo foi {kwh:.2f} kWh, portanto você pagará o valor mínimo que é R$ 27.90.')
else:
    print(f'O seu consumo foi {kwh:.2f} kWh, portanto o total da sua conta é R$ {preço:.2f}.')

----------

2) Calcule a soma de até mil termos da série 1 + 1/2 + 1/4 + 1/8 + 1/16 + ...

soma = 0
contador = 0
inicio = 1

while contador < 1000:
    soma = soma + inicio
    inicio = inicio*0.5
    contador = contador + 1
print(f'A soma dos 1000 primeiros termos dessa PG é {soma}.')

----------

3) Faça um script que informe a tabuada de um número N fornecido como entrada.

n = int(input('Digite um número para encontrar sua tabuada: '))
print('=-' *10)
print(f'{n} x 0 = {n*0:2}')
print(f'{n} x 1 = {n*1:2}')
print(f'{n} x 2 = {n*2:2}')
print(f'{n} x 3 = {n*3:2}')
print(f'{n} x 4 = {n*4:2}')
print(f'{n} x 5 = {n*5:2}')
print(f'{n} x 6 = {n*6:2}')
print(f'{n} x 7 = {n*7:2}')
print(f'{n} x 8 = {n*8:2}')
print(f'{n} x 9 = {n*9:2}')
print('=-' *10)

----------

4) Faça um script para perguntar o nome e a idade de 10 pessoas e informar quantos são maiores
e menores de idade.

c = 0
cmenor = 0
cmaior = 0

while c < 10:
    nome = (input('Digite um nome: '))
    idade = (int(input('Digite uma idade: ')))
    c = c + 1
    if idade >= 18:
        cmaior = cmaior + 1
    else:
        cmenor = cmenor + 1

print(f'{cmaior} das pessoas são maiores de idade.')
print(f'{cmenor} das pessoas são menores de idade.')

----------

5) O script inicialmente deverá mostrar um menu com as seguintes opções:
    Depósito
    Retirada
    Saldo
    Sair do algoritmo
Se a escolha do usuário for depósito ou retirada, o algoritmo deverá pedir o valor da operação
e atualizar automaticamente o valor existente na conta. O algoritmo deverá ser utilizado até que
o usuário escolha a opção sair do algoritmo.

from time import sleep

print('='*40)
print(f'{"BANCO PYTHON":^40}')
print('='*40)

escolha = int(input('Escolha uma das opções abaixo: \n1 - Depósito \n2 - Retirada \n3 - Saldo \n4 - Sair do algoritmo \n'))
saldo = float(1000.00)
while escolha != 4:
    if escolha == 1:
        dep = float(input('Qual o valor do depósito? R$ '))
        print('Depósito realizado.')
    elif escolha == 2:
        ret = float(input('Qual o valor da retirada? R$ '))
        print('Retire seu dinheiro.')
    elif escolha == 3:
        saldo = saldo + dep - ret
        print(f'O seu saldo é {saldo}')
    else:
        print('Opção inválida. Tente novamente...')
    sleep(2)
    escolha = int(input('Escolha uma das opções abaixo: \n1 - Depósito \n2 - Retirada \n3 - Saldo \n4 - Sair do algoritmo \n'))
print('Finalizando...')
sleep(2)
print('Sessão finalizada.')

----------

6) Faça um algoritmo que leia uma quantidade indeterminada de números inteiros positivos terminada pelo número 0 (zero).
Ao final, o algoritmo deve mostrar a média aritmética de todos os números lidos (excluindo o zero).

lista = []
n = int(input('Digite um número inteiro: '))
while n != 0:
    lista.append(n)
    n = int(input('Digite um número inteiro: '))
else:
    print(f'A média dos números digitados é {sum(lista)/len(lista)}')
'''    


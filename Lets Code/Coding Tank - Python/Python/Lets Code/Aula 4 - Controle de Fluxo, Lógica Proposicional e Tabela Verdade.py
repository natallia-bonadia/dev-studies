### EXERCÍCIOS AULA 4 e 5 - CONTROLE DE FLUXO, LÓGICA PROPOSICIONAL E TABELA VERDADE ###

'''
1) Faça um script que leia dois números e informe o maior deles.

numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite um número: "))

if numero1>numero2:
    print("O número maior é {}.".format(numero1))
elif numero2>numero1:
    print("O número maior é {}.".format(numero2))
else:
    print("Os números são iguais")
----------

2) Faça um script que leia um número e informe se ele é par ou ímpar.

numero = int(input("Digite um número para descobrir se ele é par ou ímpar:"))
resultado = numero%2
if resultado==0:
    print("O número é par.")
if resultado!=0:
    print("O número é ímpar.")
----------

3) Faça um script que informe se uma pessoa está apta para dirigir um carro.
Uma pessoa só pode dirigir se for maior de idade e se tiver carteira de motorista.
Dica: carteira pode ser variável lógica.

idade = int(input("Digite a sua idade:"))
carteira = input("Você possui carteira de motorista?")
while carteira != "sim" and carteira != "não":
    print("Ops! Vamos tentar de novo...")
    carteira = input("Você possui carteira de motorista?")
if idade >= 18 and carteira == "sim":
    print("Você está apto(a) para dirigir")
else:
    print("Você não está apto(a) para dirigir")
----------

4) Faça um script que faça o login de uma pessoa no servidor ABC.
O usuário é "admin" e a senha é "admin123".

usuario = input("Digite seu usuário:")
senha = input("Digite sua senha:")

if usuario=="admin" and senha=="admin123":
    print("Logado com sucesso.")
----------

5) Em termos de número de comparações, explique qual dos dois scripts
é o que realiza menos comparações:
- Script 1
idade = int(input())
if idade >= 18:
  print('Vc é adulto')
if idade >= 13 and idade <= 17:
  print('Vc é adolescente')
- Script 2
idade = int(input())
if idade >= 18:
  print('Vc é adulto')
else:
  if idade >= 13 and idade <= 17:
    print('Vc é adolescente')

O script 2 tem mais comparações, pois uma condição depende da outra.
----------

6) Uma empresa irá aplicar um reajuste nos salários de seus funcionários de acordo com as seguintes regras:
Salário até R$2800,00 (incluindo): aumento de 20%;
Salários entre R 2800,00 e R$7000,00: aumento de 15%;
Salários entre R 7000,00 e R$15000,00: aumento de 10%;
Salários de R$15000,00 em diante: aumento de 5%.
Dado o salário de um funcionário, informe: o salário antes do reajuste;
o percentual de aumento aplicado; o valor do aumento e o novo salário.

funcionario = input("Nome do funcionário:")
salario_anterior = float(input("Digite o salário anterior:"))

if salario_anterior <= 2800:
    salario_novo = salario_anterior*1.2
    valor_aumento = salario_novo - salario_anterior
    print("O salário anterior de",funcionario,"é R$",salario_anterior,", com o reajuste de 20% terá um aumento de R$",valor_aumento,"e o salário novo será R$",salario_novo,".")
if salario_anterior > 2800 and salario_anterior <= 7000:
    salario_novo = salario_anterior*1.15
    valor_aumento = salario_novo-salario_anterior
    print("O salário anterior de",funcionario,"é R$",salario_anterior,", com o reajuste de 15% terá um aumento de R$",valor_aumento,"e o salário novo será R$",salario_novo,".") if salario_anterior > 7000 and salario_anterior <= 15000: salario_novo = salario_anterior1.1 valor_aumento = salario_novo-salario_anterior print("O salário anterior de",funcionario,"é R$",salario_anterior,", com o reajuste de 10% terá um aumento de R$",valor_aumento,"e o salário novo será R$",salario_novo,".")
if salario_anterior > 15000.00:
    salario_novo = salario_anterior*1.05
    valor_aumento = salario_novo-salario_anterior
    print("O salário anterior de",funcionario,"é R$",salario_anterior,", com o reajuste de 5% terá um aumento de R$",valor_aumento,"e o salário novo será R$",salario_novo,".")
----------

7) Faça um script de menu que mostra na tela, com o título de "Menu Principal" e mais três opções:
1 - Fim; 2 - Cadastro; 3 - Consulta.
O programa recebe um input do teclado a opção desejada e mostra uma mensagem confirmando a opção escolhida.
Caso a opção escolhida seja inválida, mostrar uma mensagem de erro "Opção Inválida".

print("Menu Principal")
print("Escolha uma das opções abaixo:")
opcao = int(input("1 - Fim, 2 - Cadastro, 3 - Consulta "))
while opcao!=1 and opcao!=2 and opcao!=3:
    print("Opção inválida. Vamos tentar de novo...")
    opcao = int(input("1 - Fim, 2 - Cadastro, 3 - Consulta "))
if opcao==1:
    print("Finalizando pedido. Obrigado!")
if opcao==2:
    print("Iniciando cadastro...")
if opcao==3:
    print("O que gostaria de consultar?")
'''
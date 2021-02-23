### EXERCÍCIOS AULA 15 - DICIONÁRIOS (PARTE 1) ###

'''
1) Qual a diferença entre índices de uma lista e chaves de um dicionário?

O índice se refere a posição do elemento dentro de uma lista, já a chave pode ser de qualquer tipo e apresenta
a definição do elemento no dicionário.

----------

2) Crie um dicionário cujas chaves são os meses do ano e os valores são a duração (em dias) de cada mês.

ano2020 = {'Janeiro': 31, 'Fevereiro': 29, 'Março': 31, 'Abril': 30, 'Maio': 31, 'Junho': 30, \
    'Juho': 31, 'Agosto': 31, 'Setembro': 30, 'Outubro': 31, 'Novembro': 30, 'Dezembro': 31}

print(ano2020)

----------

3) Faça um script que receba os valores do nome, idade e e-mail de uma pessoa e guarde-os em um dicionário com
as chaves ‘nome’, ‘idade’ e ‘email’, respectivamente. Exiba as informações desse dicionário.

dados = {}

n = str(input('Nome: '))
i = int(input('Idade: '))
e = str(input('E-mail: '))

dados.update({'Nome':n})
dados.update({'Idade':i})
dados.update({'E-mail':e})

for chave in dados:
    print(dados[chave])


----------

4) Faça um programa que leia 10 números do usuário e os coloque corretamente no dicionário D abaixo.
D = {'pares': [], 'impares':[]}

D = {'pares': [], 'impares':[]}
c = 0
while c < 10:
    n = int(input('Digite um número inteiro: '))
    if n % 2 == 0:
        D['pares'].append(n)
    else:
        D['impares'].append(n)
    c = c + 1

print(D)

----------

5) Analise a tabela a seguir e a represente usando um dicionário.
Nome 	    Idade
Ana 	    25
Maria 	    34
Vitória 	22
João 	    32

dados = {'nomes':['Ana', 'Maria', 'Vitória', 'João'], 'idades':[25, 34, 22, 32]}

for n in dados:
    print(dados[n])

----------

6) Usando o dicionário resultante do exercício 5, descubra a média de idades.

dados = {'nomes':['Ana', 'Maria', 'Vitória', 'João'], 'idades':[25, 34, 22, 32]}

media = sum(dados['idades'])/len(dados['idades'])

print(f'A média das idades é igual a {media}.')

'''
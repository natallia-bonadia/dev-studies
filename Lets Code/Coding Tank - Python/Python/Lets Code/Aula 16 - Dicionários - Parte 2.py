### EXERCÍCIOS AULA 16 - DICIONÁRIOS (PARTE 2) ###

'''
1) Faça um script usando dicionários que peça para um usuário digitar um número entre 0 e 9 e imprima o número por extenso.
Exemplo
input: 3
output: três

d = {0: 'zero', 1: 'um', 2: 'dois', 3: 'três', 4: 'quatro', 5:'cinco', 6: 'seis', 7: 'sete', 8: 'oito', 9: 'nove'}
n = int(input('Digite um número de 0 a 9: '))

print(f'Por extenso esse número é \033[1m{d[n]}\033[m.')

----------

2) Faça um script que leia uma frase do usuário e use um dicionário que apresente as letras
e a frequência de aparição desta letra na frase.

Exemplo 
input: coding tank
output: {'c':1, 'o':1, 'd':1, 'i':1, 'n':2, 'g':1, 't':1, 'a':1, 'k':1}

dicionario = {}
frase = str(input('Digite uma frase qualquer: '))
frase_minuscula = frase.lower()
frase_semespaço = frase_minuscula.replace(' ', '')
for letra in frase_semespaço:
    dic_quantidade = frase_semespaço.count(letra)
    dic_letra = letra
    dicionario.update({dic_letra:dic_quantidade})

print(dicionario)

----------

3) Faça um script que leia uma frase do usuário e use um dicionário que apresente as palavras
e a frequêcia de sua aparição na frase.

Exemplo
input: bom dia dia
output: {'bom':1 'dia':2}

dicionario = {}
frase = str(input('Digite uma frase qualquer: '))
frase_minuscula = frase.lower()
lista = frase_minuscula.split()

for palavra in lista:
    dic_quantidade = lista.count(palavra)
    dic_palavra = palavra
    dicionario.update({dic_palavra:dic_quantidade})

print(dicionario)

----------

4) Dado o dicionário abaixo, descubra as médias de "homework", "quizzes" e "tests" dos três alunos.
Ao final, apresente quem foi aprovado (caso média de "tests" maior que 65)

lloyd = {
  "name": "Lloyd",
  "homework": [90.0,97.0,75.0,92.0],
  "quizzes": [88.0,40.0,94.0],
  "tests": [75.0,90.0]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}
print('-'*30)
media_lloyd = (sum(lloyd["homework"])/len(lloyd["homework"]) + \
    sum(lloyd["quizzes"])/len(lloyd["quizzes"]) + \
        sum(lloyd["tests"])/len(lloyd["tests"]))/3
if media_lloyd > 65:
    a = 'APROVADO'
else:
    a = 'REPROVADO'
print(f'A média de Lloyd é {media_lloyd:.2f} e o aluno está {a}.')
print('-'*30)
media_alice = (sum(alice["homework"])/len(alice["homework"]) + \
    sum(alice["quizzes"])/len(alice["quizzes"]) + \
        sum(alice["tests"])/len(alice["tests"]))/3
if media_alice > 65:
    a = 'APROVADA'
else:
    a = 'REPROVADA'
print(f'A média de Alice é {media_alice:.2f} e a aluna está {a}.')
print('-'*30)
media_tyler = (sum(tyler["homework"])/len(tyler["homework"]) + \
    sum(tyler["quizzes"])/len(tyler["quizzes"]) + \
        sum(tyler["tests"])/len(tyler["tests"]))/3
if media_tyler > 65:
    a = 'APROVADO'
else:
    a = 'REPROVADO'
print(f'A média de Tyler é {media_tyler:.2f} e o aluno está {a}.')
print('-'*30)

----------

5) Faça um programa de cadastro de clientes. O usuário pode escolher entre 1 - Cadastrar,
2 - Visualizar os cadastrados e 3 - Buscar um cadastro específico.
Se o usuário digitar 1, o programa deve cadastrar um novo usuário inserindo cpf, nome e email
e deve guardar esse cadastro em um dicionário cuja chave será o CPF da pessoa.
Quando o usuário digitar 2, o programa deve imprimir os usuários cadastrados; e se o usuário
digitar 3, procure um determinado usuário pelo seu CPF.
Seu sistema deve encerrar somente quando o usuário digitar 4.
Exemplo do dicionário:
‘987.654.321-00’: {‘nome’: Maria, ‘idade’: 20, ‘email’ : maria@ig.com}

# CABEÇALHO E OPÇÃO
print('='*35)
print(f'{"CADASTRO DE CLIENTES":^35}')
print('='*35)
print('[ 1 ] Cadastrar \n[ 2 ] Visualizar os cadastros \n[ 3 ] Buscar um cadastro \n[ 4 ] Finalizar')
opçao = int(input('> Escolha uma das opções acima: '))
# LISTA E DICIONÁRIO UTILIZADOS
cadastro = list()
dados = dict()
while opçao != 4:
    if opçao == 1:
        dados.clear()
        dados['CPF'] = int(input('CPF: '))
        dados['Nome'] = str(input('Nome: ')).strip().upper()
        dados['Idade'] = int(input('Idade: '))
        dados['E-mail'] = str(input('E-mail: ')).strip().lower()
        cadastro.append(dados.copy())
        print('>> CADASTRO ATUALIZADO COM SUCESSO <<')
        
    if opçao == 2:
        print(cadastro)        

    if opçao == 3:
        busca = int(input('Qual CPF deseja pesquisar? '))
        print(dados[busca])
    
    print()
    print('='*35)
    print(f'{"CADASTRO DE CLIENTES":^35}')
    print('='*35)
    print('[ 1 ] Cadastrar \n[ 2 ] Visualizar os cadastros \n[ 3 ] Buscar um cadastro \n[ 4 ] Finalizar')
    opçao = int(input('> Escolha uma das opções acima: '))

print('Sessão Finalizada.')
'''
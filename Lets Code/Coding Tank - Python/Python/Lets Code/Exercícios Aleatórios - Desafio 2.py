### EXERCÍCIOS ALEATÓRIOS 2 ###

'''
1) Faça um script que leia uma frase do usuário e use um dicionário que apresente as letras e a frequência de
aparição desta letra na frase.

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

2) Faça um programa de cadastro de clientes. O usuário pode escolher entre 1 - Cadastrar, 2 - Visualizar os cadastrados e
3 - Buscar um cadastro específico.
Se o usuário digitar 1, o programa deve cadastrar um novo usuário inserindo cpf, nome e email e deve guardar esse cadastro
em um dicionário cuja chave será o CPF da pessoa. Quando o usuário digitar 2, o programa deve imprimir os usuários cadastrados;
e se o usuário digitar 3, procure um determinado usuário pelo seu CPF. Seu sistema deve encerrar somente quando o usuário digitar 4.
Exemplo do dicionário:
{‘987.654.321-00’: {‘nome’: Maria, ‘idade’: 20, ‘email’ : maria@ig.com}}
'''
'''
# CABEÇALHO E OPÇÕES
print('='*35)
print(f'{"CADASTRO DE CLIENTES":^35}')
print('='*35)
print('[ 1 ] Cadastrar \n[ 2 ] Visualizar os cadastros \n[ 3 ] Buscar um cadastro \n[ 4 ] Finalizar')
opçao = int(input('> Escolha uma das opções acima: '))
# LISTAS E DICIONÁRIOS UTILIZADOS
lista = list()
dicionario_cpf = dict()
dicionario_dados = dict()
# OPÇÃO ESCOLHIDA
while opçao != 4:
    
    if opçao == 1:
        dicionario_dados.clear()
        dicionario_cpf.clear()
        cpf = str(input('Digite o CPF: '))
        nome = str(input('Digite o nome: '))
        idade = int(input('Digite a idade: '))
        email = str(input('Digite o e-mail: '))
        dicionario_dados.update({'Nome':nome, 'Idade':idade, 'E-mail':email})
        dicionario_cpf.update({cpf:dicionario_dados})
        lista.append(dicionario_cpf.copy())
    print('>> Dados cadastrados com sucesso. <<')
    print(' ')

    if opçao == 2:
        print(lista)

    if opçao == 3:
        pesquisa = str(input('Qual CPF deseja pesquisar? '))
        print(f'>> {dicionario_cpf[pesquisa]}')
        print('')

    print('='*35)
    print(f'{"CADASTRO DE CLIENTES":^35}')
    print('='*35)
    print('[ 1 ] Cadastrar \n[ 2 ] Visualizar os cadastros \n[ 3 ] Buscar um cadastro \n[ 4 ] Finalizar')
    opçao = int(input('> Escolha uma das opções acima: '))

'''
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



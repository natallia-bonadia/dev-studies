### EXERCÍCIOS AULA 13 e 14 - STRINGS ###

'''
1) Faça um script para ler dois vetores, os quais armazenarão o preço e a quantidade vendida de 10 produtos.
Seu programa deverá informar o valor arrecadado total e por produto.
'''
preco = []
produto = []

for n in range(0,10):
    x = preco.append(int(input(f'Preço total do produto {n+1}: ')))
    y = produto.append(str(input(f'Quantidade do produto {n+1}: ')))
    preco 
print(preco)
print(produto)
'''
----------

2) Faça um programa que simule uma pilha de livros, que inicialmente começa vazio. Um livro só poderá ser incluído no topo da pilha, assim como sua retirada, respeitando o tamanho máximo do vetor (10 livros). Usando laços, implemente opções de inserção, retirada, listagem da pilha e saida do programa.
    1: Inserir livro (se a opção escolhida for essa, perguntar o nome do livro);
    2: Remover livro;
    3: Listar livros;
    4: Sair do programa





----------

3) Escreva um programa que recebe um texto do usuário e retorna o número de espaços existentes.

Exemplo 1
input: "bom dia"
output: texto contém 1 espaço

Exemplo 2
input: "hoje é quinta-feira"
output: texto contém 2 espaços

texto = (str(input('Digite seu texto aqui: '))).strip()
print(f'A frase digitada possui {texto.count(" ")} espaços entre as palavras.')

----------

4) Faça um script que recebe um texto da entrada e exibe a maior palavra contida nesse texto.
Exemplo 1
input: "a casa do meu amigo é azul"
output: amigo é a maior palavra

texto = (str(input('Digite seu texto aqui: '))).strip()
palavras = (texto.count(' ')+1)
print(palavras)
lista = texto.split()
print(lista)
i = 0
while i < palavras:
    i = i + 1

----------

5) Faça um script que receba um texto de entrada e informe: (i) quantas letras totais (sem espaço),
(ii) quantas vogais e (iii) quantas consoantes existem.

texto = (str(input('Digite seu texto aqui: '))).strip()
textomin = texto.lower()
letras = len(textomin) - textomin.count(" ")
print('='*20)
print(f'(i) O texto possui {letras} letras.')
print('='*20)
vogais = textomin.count("a") + textomin.count("e") + textomin.count("i") + textomin.count("o") + textomin.count("u")
print(f'(ii) O texto possui {vogais} vogais.')
print('='*20)
consoantes = letras - vogais
print(f'(iii) O texto possui {consoantes} consoantes.')

'''
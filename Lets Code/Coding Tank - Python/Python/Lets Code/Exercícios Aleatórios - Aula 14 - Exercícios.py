### EXERCÍCIOS ALEATÓRIOS - AULA 14 - EXERCÍCIOS ###

'''
1) Faça um script para ler dois vetores, os quais armazenarão o preço e a quantidade vendida de 10 produtos.
Seu programa deverá informar o valor arrecadado total e por produto.

produto = []
total = []
for c in range(0,10):
  print('-'*30)
  nome = str(input(f'Produto {c}: '))
  produto.append(nome)
  preço = float(input(f'Preço {c}: R$ '))
  total.append(preço)
  
print('-'*30)
print(f'Total arrecadado: R$ {sum(total):.2f}')

for c in range(0,3):
  print(f'O valor unitário de {produto[c]} é R$ {total[c]/10:.2f}.')

----------

2) Faça um programa que simule uma pilha de livros, que inicialmente começa vazio. Um livro só poderá ser incluído no topo da pilha, assim como sua retirada, respeitando o tamanho máximo do vetor (10 livros). Usando laços, implemente opções de inserção, retirada, listagem da pilha e saida do programa.
    1: Inserir livro (se a opção escolhida for essa, perguntar o nome do livro);
    2: Remover livro;
    3: Listar livros;
    4: Sair do programa

from time import sleep
lista = []

print('-'*30)
print(f'{"LISTA DE LIVROS":^30}')
print('-'*30)
print('[ 1 ] Inserir livro\n[ 2 ] Remover livro\n[ 3 ] Listar livros\n[ 4 ] Sair do programa')

while True:
  opcao = int(input('Escolha uma das opções >>> '))
  if opcao == 1:
    lista.append(str(input('Digite o nome do livro que quer adicionar: ')))

  if opcao == 2:
    lista.remove(str(input('Digite o nome do livro que quer excluir: ')))
  
  if opcao == 3:
    for pos, livro in enumerate(lista):
      print(f'{pos} - {livro}')

  if opcao == 4:
    print('Encerrando...')
    break
sleep(2)
print('Programa finalizado. Volte sempre!')

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

frase = (str(input('Digite uma frase: ')))
fatiada = frase.split()
print(f'A maior palavra da frase é "{max(fatiada, key=len)}".')

----------

5) Faça um script que receba um texto de entrada e informe: (i) quantas letras totais (sem espaço), (ii) quantas vogais e (iii) quantas consoantes existem.

texto = (str(input('Digite seu texto aqui: '))).strip()
textomin = texto.lower()
letras = len(textomin) - textomin.count(" ")
print('='*20)
print(f'O texto possui {letras} letras.')
print('='*20)
vogais = textomin.count("a") + textomin.count("e") + textomin.count("i") + textomin.count("o") + textomin.count("u")
print(f'O texto possui {vogais} vogais.')
print('='*20)
consoantes = letras - vogais
print(f'O texto possui {consoantes} consoantes.')
'''

### ENTREGA 3 ###

'''
01) Usando dicionários, faça um robô que traduza uma linha de comando python para seu respectivo comando em português usando a tabela abaixo. Alguns exemplos estão listados ao final.
python 	português
if 	se
while 	enquanto
> 	maior que
< 	menor que
<= 	maior igual que
<= 	menor igual que
== 	igual a
!= 	diferente de
print 	imprima o valor da variável

Exemplo 1
input: if x > y
output: se x maior que y

Exemplo 2
input: while x != y
output: enquanto x diferente de y

Exemplo 3
input: print(x)
output: imprima o valor da variável x

Seu programa deve tratar dos casos básicos de programação, considere que o usuário nunca irá fornecer listas ou dicionários.

dic = {'if':'se', 'while':'enquanto', '>':'maior que', '<':'menor que', '>=':'maior igual que', '<=':'menor igual que', '==':'igual a', '!=':'diferente de', 'print':'imprima o valor da variável'}

usuario = str(input('Digite a linha de comando ou "fim" para finalizar o programa: ')).lower().split()
print('A tradução para o português é: ')
for palavras in usuario:
    if palavras in dic:
        print(f'{dic[palavras]} ', end='')
    else:
        print(f'{palavras} ', end='')

'''
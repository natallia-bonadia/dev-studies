### ENTREGA 2 ###
'''
01) Considere as listas dadas (nomes, idades e alturas). Faça um programa que imprima os elementos de
cada uma dessas listas de acordo com o exemplo a seguir. Por fim, imprima uma mensagem informando as
médias tanto de idades quanto de altura.
Maria da Silva, 23 anos, 1.78 m
Ana Santos, 45 anos, 1.77 m
(etc...)
Alan Dias, 70 anos, 1.9 m
Silvana Sampaio, 27 anos, 1.67 m
As listas são:
nomes = ['Maria da Silva', 'Ana Santos', 'Maria Santos', 'Ana Ferreira', 'João Santana', 'José Silva', 'Maria Antônia', 'Carlos Ricardo', 'Alan Dias', 'Silvana Sampaio']
idades = [23, 45, 34, 67, 19, 32, 43, 44, 70, 27]        
alturas = [1.78, 1.77, 1.65, 1.60, 1.87, 1.78, 1.75, 1.68, 1.9, 1.67]

nomes = ['Maria da Silva', 'Ana Santos', 'Maria Santos', 'Ana Ferreira', 'João Santana', 'José Silva', 'Maria Antônia', 'Carlos Ricardo', 'Alan Dias', 'Silvana Sampaio']
idades = [23, 45, 34, 67, 19, 32, 43, 44, 70, 27]        
alturas = [1.78, 1.77, 1.65, 1.60, 1.87, 1.78, 1.75, 1.68, 1.9, 1.67]

print(f'Nome: {nomes[0]:15} | Idade: {idades[0]} | Altura: {alturas[0]:.2f}')
print(f'Nome: {nomes[1]:15} | Idade: {idades[1]} | Altura: {alturas[1]:.2f}')
print(f'Nome: {nomes[2]:15} | Idade: {idades[2]} | Altura: {alturas[2]:.2f}')
print(f'Nome: {nomes[3]:15} | Idade: {idades[3]} | Altura: {alturas[3]:.2f}')
print(f'Nome: {nomes[4]:15} | Idade: {idades[4]} | Altura: {alturas[4]:.2f}')
print(f'Nome: {nomes[5]:15} | Idade: {idades[5]} | Altura: {alturas[5]:.2f}')
print(f'Nome: {nomes[6]:15} | Idade: {idades[6]} | Altura: {alturas[6]:.2f}')
print(f'Nome: {nomes[7]:15} | Idade: {idades[7]} | Altura: {alturas[7]:.2f}')
print(f'Nome: {nomes[8]:15} | Idade: {idades[8]} | Altura: {alturas[8]:.2f}')
print(f'Nome: {nomes[9]:15} | Idade: {idades[9]} | Altura: {alturas[9]:.2f}')

print( )
print('=-' * 40)
print( )
media_idades = sum(idades)/len(idades)
print(f'A média de todas as idades da lista é {media_idades:.2f}.')
print( )
print('=-' * 40)
print( )
media_alturas = sum(alturas)/len(alturas)
print(f'A média de todas as alturas da lista é {media_alturas:.2f}.')
print( )
print('=-' * 40)
'''
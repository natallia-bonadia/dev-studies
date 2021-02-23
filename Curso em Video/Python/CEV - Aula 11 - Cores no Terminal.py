### Curso em Vídeo - Exercícios Aula 11 - Cores no Terminal ###

'''
# LETRA BRANCA E FUNDO VERMELHO
\033[0;30;41m

# LETRA AMARELA SUBLINHADA E FUNDO AZUL
\033[4;33;44m

# LETRA LILÁS E FUNDO AMARELO
\033[1;35;43m

# LETRA BRANCA E FUNDO VERDE (SEM ESTILO / FORMATAÇÃO)
\033[30;42m

# LETRA CINZA E FUNDO PRETO
\033[m

# LETRA PRETA E FUNDO BRANCO
\033[7;30m
'''

print('\033[1;31;43mOlá Mundo!\033[m')

print('\033[4;30;45mMeu nome é Natallia :)\033[m')

print('\033[7;40mMeu namorado é muito fofinho!\033[m')

# NÃO CONSEGUI ESSA PARTE ABAIXO 
'''
cores = {'limpa':'\033[m}', 'azul':'\033[34m', 'amarelo':'\033[33m', 'pretoebranco':'\033[7;30m'}

nome = 'Natallia'
print(f'Olá! Muito prazer em te conhecer, {cores['azul']}{nome}{cores['limpa']}!')
'''
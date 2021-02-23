### ENTREGA 1 ###

'''
1) Vamos fazer um script para verificar quem é o assassino de um crime. Para descobrir o assassino, a polícia faz um pequeno questionário com 5 perguntas onde a resposta só pode ser sim ou não:
Mora perto da vítima?
Já trabalhou com a vítima?
Telefonou para a vítima?
Esteve no local do crime?
Devia para a vítima?
Cada resposta sim dá um ponto para o suspeito. A polícia considera que os suspeitos com 5 pontos são os assassinos, com 4 ou 3 pontos são cúmplices e 2 pontos são apenas suspeitos, necessitando outras investigações. Valores abaixo de 1 são liberados. Exemplo:
input: Mora perto da vítima? sim
input: Já trabalhou com a vítima? sim
input: Telefonou para a vítima? não
input: Esteve no local do crime? não
input: Devia para a vítima? sim
output: Você é cúmplice

print("Questionário para suspeitos do crime")
print("Responda sim ou não para cada uma das perguntas abaixo:")

p1 = input("Mora perto da vítima? ")
while p1 != "sim" and p1 != "não":
    print("Resposta inválida")
    p1 = input("Mora perto da vítima? ")
if p1 == "sim":
    p1 = 1
else:
    p1 = 0
p2 = input("Já trabalhou com a vítima? ")
while p2 != "sim" and p2 != "não":
    print("Resposta inválida")
    p2 = input("Já trabalhou com a vítima? ")
if p2 == "sim":
    p2 = 1
else:
    p2 = 0
p3 = input("Telefonou para a vítima? ")
while p3 != "sim" and p3 != "não":
    print("Resposta inválida")
    p3 = input("Telefonou para a vítima? ")
if p3 == "sim":
    p3 = 1
else:
    p3 = 0
p4 = input("Esteve no local do crime? ")
while p4 != "sim" and p4 != "não":
    print("Resposta inválida")
    p4 = input("Esteve no local do crime? ")
if p4 == "sim":
    p4 = 1
else:
    p4 = 0
p5 = input("Devia para a vítima? ")
while p5 != "sim" and p5 != "não":
    print("Resposta inválida")
    p5 = input("Devia para a vítima? ")
if p5 == "sim":
    p5 = 1
else:
    p5 = 0

ptotal = int(p1 + p2 + p3 + p4 + p5)
print("Total de respostas sim:",ptotal)

if ptotal==5:
    print("Você é assassino(a).")
elif 3 <= ptotal <= 4:
    print("Você é cúmplice.")
elif ptotal == 2:
    print("Você é suspeito(a)")
else:
    print("Você está liberado(a)")

----------

2) Um hospital quer fazer o diagnóstico de gripe ou dengue a partir de um questionário de sintomas de acordo com as perguntas abaixo. Faça um script que faça o diagnóstico deste hospital:
Sente dor no corpo?
Você tem febre?
Você tem tosse?
Está com congestão nasal?
Tem manchas pelo corpo?
Para o diagnóstico siga a seguinte tabela:
Pergunta 1 	Pergunta 2 	Pergunta 3 	Pergunta 4 	Pergunta 5 	Resultado
Sim     Sim 	  Não 	Não 	Sim 	Dengue
Sim 	Sim 	Sim 	Sim 	Não 	Gripe
Não 	Sim 	Sim 	Sim 	Não 	Gripe
Sim 	Não 	Não 	Não 	Não 	Sem Doenças
Não 	Não 	Não 	Não 	Não 	Sem Doenças

print("Questionário para diagnóstico de gripe ou dengue")
print("Responda sim ou não para cada uma das perguntas abaixo:")

p1 = input("Sente dor no corpo? ")
while p1 != "sim" and p1 != "não":
    print("Resposta inválida")
    p1 = input("Sente dor no corpo? ")
p2 = input("Você tem febre? ")
while p2 != "sim" and p2 != "não":
    print("Resposta inválida")
    p2 = input("Você tem febre? ")
p3 = input("Você tem tosse? ")
while p3 != "sim" and p3 != "não":
    print("Resposta inválida")
    p3 = input("Você tem tosse? ")
p4 = input("Está com congestão nasal? ")
while p4 != "sim" and p4 != "não":
    print("Resposta inválida")
    p4 = input("Está com congestão nasal? ")
p5 = input("Tem manchas pelo corpo? ")
while p5 != "sim" and p5 != "não":
    print("Resposta inválida")
    p5 = input("Tem manchas pelo corpo? ")

if p1=="sim" and p2=="sim" and p3=="não" and p4=="não" and p5=="sim":
    print("Você está com DENGUE.")
elif p1=="não" and p2=="sim" and p3=="sim" and p4=="sim" and p5=="não":
    print("Você está com GRIPE.")
elif p1=="sim" and p2=="sim" and p3=="sim" and p4=="sim" and p5=="não":
    print("Você está com GRIPE.")
elif p1=="sim" and p2=="não" and p3=="não" and p4=="não" and p5=="não":
    print("Você está SEM DOENÇAS.")
elif p1=="não" and p2=="não" and p3=="não" and p4=="não" and p5=="não":
    print("Você está SEM DOENÇAS.")
else:
    print("Sem diagnóstico")
'''
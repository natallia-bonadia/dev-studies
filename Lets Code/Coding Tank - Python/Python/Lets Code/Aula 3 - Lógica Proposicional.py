### EXERCÍCIOS AULA 3 - LÓGICA PROPOSICIONAL ###

### PARTE 1 ###

'''
1) Determine a negação das seguintes expressões:
a) a > b
b) a >= b
c) a >= 18 and dia == 3
d) a >= 18 and dia != 3

a) a <= b
b) a < b
c) a < 18 or dia != 3
d) a < 18 or dia == 3
----------

2) Determine se as seguintes expressões são verdadeiras ou falsas:
a) True and True
b) False and True
c) 1 == 1 and 2 == 1
d) "test" == "test"
e) 1 == 1 or 2 != 1
f) True and 1 == 1
g) False and 0 != 0
h) True or 1 == 1
i) "test" == "testing"
j) 1 != 0 and 2 == 1
k) "test" != "testing"
l) "test" == 1
m) not (True and False)
n) not (1 == 1 and 0 != 1)
o) not (10 == 1 or 1000 == 1000)
p) not (1 != 10 or 3 == 4)
q) not ("testing" == "testing" and "Zed" == "Cool Guy")
r) 1 == 1 and not ("testing" == 1 or 1 == 0)
s) "chunky" == "bacon" and not (3 == 4 or 3 == 3)
t) 3 == 3 and not ("testing" == "testing" or ( "Python" == "Fun"))

a) True
b) False
c) False
d) True
e) True
f) True
g) False
h) True
i) False
j) False
k) True
l) False
m) True
n) False
o) False
p) False
q) True
r) True
s) False
t) False
----------

3) Um alvo de dardos possui raio 10 e a parede é representada por um
sistema de coordenadas de duas dimensões, x e y, com o centro do alvo
no ponto (0,0). Escreva uma expressão lógica usando as variáveis x e y
que seja verdadeira quando o dardo atinge dentro da área do alvo,
e avalie a expressão para as seguintes coordenadas (x,y):
a) (0, 0)
b) (10, 10)
c) (6, 6)
d) (7, 8)

x = float(input("Digite a coordenada x:"))
y = float(input("Digite a coordenada y:"))

d = x2 + y2
raiz = float(d)**0.5     # distancia do ponto até o centro da circunferência
print(raiz)

if raiz>10:     # 10 é o raio máximo que o ponto pode se posicionar para estar dentro do alvo
    print("Esse ponto está fora do alvo")
    else: print("Esse ponto está dentro do alvo")

a) Esse ponto está dentro do alvo
b) Esse ponto está fora do alvo
c) Esse ponto está dentro do alvo
d) Esse ponto está fora do alvo
'''

### PARTE 2 ###

'''
1) Sabendo que A <- 3, B <- 5, C <- 6. Responda Verdadeiro ou Falso.
1. A maior que B?
2. (A+C) maior que C?
3. (A * 2) igual a C?
4. C - B igual a 1?
5. (A - B) igual a (B - C + 1)?

1. False
2. True
3. True
4. True
5. False
----------

2) Sabendo que A <- 5, B <- 7, C <- 3. Responda Verdadeiro ou Falso.
1. (A maior que B) e (B menor que C)?
2. (A diferente de C) ou (A igual a C)?
3. ((A diferente de B) e (B diferente de C)) ou (A igual a 8)?


1. F and F = False
2. T or F = True
3. ((T and T) or F) = T or F = True
----------

3) Faça um algoritmo que peça o nome e 2 notas de um aluno e ao final
informe se ele foi aprovado ou reprovado.

nome = input("Digite seu nome:")
nota1 = float(input("Digite a nota 1:"))
nota2 = float(input("Digite a nota 2:"))
media = (nota1+nota2)/2
if media>=5:
    print(nome,"foi APROVADO")
if media<5:
    print(nome,"foi REPROVADO")
----------

4) Analise o algoritmo a seguir e informe quais serão os valores de x e y ao final.
1. x <- 3
2. y <- 2
3. x <- x + 1
4. y <- x - y
5. se y maior que 2, x <- 2

x é igual a 4
y é igual a 2
----------

5) Analise o algoritmo a seguir e informe os valores de x e y.
1. x <- 2
2. y <- x ** 3
3. se y igual a 8, y <- 0
4. caso contrário, x <- 0

x é igual a 2
y é igual a 0
----------

6) Faça um algoritmo que leia dois números e informe o maior deles.
numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite um número: "))

if numero1>numero2:
    print("O número maior é {}.".format(numero1))
elif numero2>numero1:
    print("O número maior é {}.".format(numero2))
else:
    print("Os números são iguais")
----------

7) Faça um algoritmo que leia um número e informe se ele é par ou ímpar.

numero = int(input("Digite um número para descobrir se ele é par ou ímpar:"))
resultado = numero%2
if resultado==0:
    print("O número é par.")
if resultado!=0:
    print("O número é ímpar.")
----------

8) Faça um algoritmo que informe se uma pessoa está apta para dirigir um carro.
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
'''
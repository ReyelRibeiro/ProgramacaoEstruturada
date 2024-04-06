"""
Aluno: Reyel Palma Ribeiro

Exercicio 1: Hello World!
"""

print("Hello World!")

"""
Exercicio 2: Extremamente Basico
"""

A = int(input())
B = int(input())

X = A + B

print("X =", X)

"""
Exercicio 3: O Calculo Simples
Obs: Para Realizar a atividade foi nescesaria 2 linhas de entrada na tela para 6 valores diferentes,
nesse exercicio era nessesario a ferramenta "input().spliy()" que não foi vista em aula.

"""

codigo1, num1, valor1 = input().split()
codigo2, num2, valor2 = input().split()

codigo1 = int(codigo1)
num1 = int(num1)
valor1 = float(valor1)

codigo2 = int(codigo2)
num2 = int(num2)
valor2 = float(valor2)

total= (num1 * valor1) + (num2 * valor2)
total = "{:.2f}".format(total)
print("VALOR A PAGAR: R$", total)

"""
Exercicio 4: O Maior
Obs: A ferramenta "input().spliy()" (que não foi vista em aula), precisou ser usada novamente
"""

a, b, c = input().split()

a = int(a)
b = int(b)
c = int(c)

maior_ab = (a + b + abs(a - b)) // 2
maior = (maior_ab + c + abs(maior_ab - c)) // 2

print(maior, "eh o maior")

"""
Exercicio 5: Ditancia Entre Dois Pontos
"""

x1, y1 = input().split()
x2, y2 = input().split()

x1 = float(x1)
y1 = float(y1)

x2 = float(x2)
y2 = float(y2)

distancia = ((x2 - x1)**2 + (y2 - y1)**2)**(1/2)
distancia = "{:.4f}".format(distancia)
print(distancia)
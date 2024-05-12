"""
Aluno: Reyel Palma Ribeiro

Exercicio 1: Distancia
"""

distancia = int(input())
minutos = distancia * 2
print(f"{minutos} minutos")

"""
Exercicio 2: Fatorial Simples
"""

n = int(input())

for i in range(1,n):
    n *= i

print(n)

"""
Exercicio 3: Ida à Feira
"""

N = int(input())

for _ in range(N):
    
    M = int(input())
    produtos = {}
    for _ in range(M):
        produto, preco = input().split()
        produtos[produto] = float(preco)

    P = int(input())
    comprar = {}
    for _ in range(P):
        produto, quantidade = input().split()
        comprar[produto] = int(quantidade)

    custo_total = 0
    for produto, quantidade in comprar.items():
        if produto in produtos:
            custo_total += produtos[produto] * quantidade
    
    print("R$ {:.2f}".format(custo_total))

"""
Exercicio 4: Identificando o Chá
"""
n = int(input())
lista = list(map(int, input().split()))
print(lista.count(n))

"""
Exercicio 5: Aviões de Papel
"""

C, P, F = input().split()

C = int(C)
P = int(P)
F = int(F)

if C * F > P:
    print("N")
else: 
    print("S")

"""
Exercicio 6: Tacógrafo
"""

N = int(input())
D = 0

for n in range(N):
    T, V = input().split()
    T = int (T)
    V = int (V)
    D += T * V

print(D)

"""
Exercicio 7: Busca na Internet
"""

N = int(input())
print (N * 4)

"""
Exercicio 8: Sequência Secreta
"""

N = int(input())
sequencia = []
n_circulos = 1

for _ in range(N):
    sequencia.append(int(input()))

for n in range(N - 1):
    if sequencia[n] != sequencia[n + 1]:
        n_circulos +=1

print(n_circulos)
"""
Aluno: Reyel Palma Ribeiro

Exercicio 1: Figurinhas
"""

T = int(input())
lista = [0] * T
for n in range(T):
    a, b = input().split()
    a = int(a)
    b = int(b)
    
    while b != 0:
        a, b = b, a % b

    lista[n] = a

for n in range(T):
    print(lista[n])

"""
Exercicio 2: Damas
"""
while True:
    x1, y1, x2, y2 = input().split()

    if x1 == "0" and y1 == "0" and x2 == "0" and y2 == "0":
            break
    else:
        x1 = int(x1)
        y1 = int(y1)
        x2 = int(x2)
        y2 = int(y2)

        if x1 == x2 and y1 == y2:
            print(0)
        elif x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
            print(1)
        else:
            print(2)

"""
Exercicio 3: Soma de Fatoriais
"""
def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)


while True:
    try:

        M, N = input().split()

        if M == "" or N == "":
            break
        
        M = int(M)
        N = int (N)

        Soma = fatorial(M) + fatorial(N)
        print(Soma)
    
    except EOFError:
        break

"""
Exercicio 4: Blobs
"""
T = int(input())
lista = [0] * T
n_dias = [0] * T

for n in range(T):
    lista[n] = int(input())
    while lista[n] > 1:
        lista[n] = lista[n]/2
        n_dias[n] += 1 
for elemento in n_dias:
    print(f"{elemento} dias")

"""
Exercicio 5: Frequência de Números
"""

T = int(input())
lista = [0] * 2001

for n in range(T):
    numero = int(input())
    lista[numero] += 1

for n in range(2001):
    if lista[n] != 0:
        print(f"{n} aparece {lista[n]} vez(es)")
        
"""
Exercicio 6: Primo Rapido
"""

def verificar_primo(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

n = int(input())
    
for _ in range(n):
    x = int(input())
        
    if verificar_primo(x):
        print("Prime")
    else:
        print("Not Prime")

"""
Exercicio 7: Cara ou Coroa
"""
while True:
    T = input()
    if T == "0":
        break
    
    T = int(T)
    Maria = 0
    Joao = 0
    
    resultados= list(map(int, input().split()))
    
    for elemento in resultados:
        if elemento == 0:
            Maria += 1
        elif elemento == 1:
            Joao += 1
    
    print(f"Mary won {Maria} times and John won {Joao} times")

"""
Exercicio 8: Funções
"""
N = int(input())  

for _ in range(N):
    x, y = input().split()
    x = int(x)
    y = int(y)
    
    resultado_r = (3 * x) ** 2 + y ** 2
    resultado_b = 2 * (x ** 2) + (5 * y) ** 2
    resultado_c = -100 * x + y ** 3
    
    if resultado_r > resultado_b and resultado_r > resultado_c:
        print("Rafael ganhou")
    elif resultado_b > resultado_r and resultado_b > resultado_c:
        print("Beto ganhou")
    else:
        print("Carlos ganhou")
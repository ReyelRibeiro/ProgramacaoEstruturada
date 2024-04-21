"""
Aluno: Reyel Palma Ribeiro

Exercicio 1: Aumento de Salário
"""

salario = float(input())

if salario < 0:
    print("Valor invalido")

elif salario <= 400:
    reajuste = salario * 0.15
    salario_com_reajuste = salario * 1.15
    print("Novo salario:", "{:.2f}".format(salario_com_reajuste))
    print("Reajuste ganho:", "{:.2f}".format(reajuste))
    print("Em percentual: 15 %")
    
elif salario <= 800:
    reajuste = salario * 0.12
    salario_com_reajuste = salario * 1.12
    print("Novo salario:", "{:.2f}".format(salario_com_reajuste))
    print("Reajuste ganho:", "{:.2f}".format(reajuste))
    print("Em percentual: 12 %")

elif salario <= 1200:
    reajuste = salario * 0.10
    salario_com_reajuste = salario * 1.10
    print("Novo salario:", "{:.2f}".format(salario_com_reajuste))
    print("Reajuste ganho:", "{:.2f}".format(reajuste))
    print("Em percentual: 10 %")

elif salario <= 2000:
    reajuste = salario * 0.07
    salario_com_reajuste = salario * 1.07
    print("Novo salario:", "{:.2f}".format(salario_com_reajuste))
    print("Reajuste ganho:", "{:.2f}".format(reajuste))
    print("Em percentual: 7 %")

else:
    reajuste = salario * 0.04
    salario_com_reajuste = salario * 1.04
    print("Novo salario:", "{:.2f}".format(salario_com_reajuste))
    print("Reajuste ganho:", "{:.2f}".format(reajuste))
    print("Em percentual: 4 %")

"""
Exercicio 2: Pares entre 5 numeros
"""
n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())

n_pares = 0

for numero in [n1,n2,n3,n4,n5]:
    if numero % 2 == 0:
        n_pares += 1

print (n_pares, "valores pares")

"""
Exercicio 3: Múltiplos de 13
"""

n1 = int(input())
n2 = int(input())

soma = 0

if n1 > n2:
    n1, n2 = n2, n1

for n in range(n1, n2 + 1):
    if n % 13 != 0:
        soma += n

print(soma)

"""
Exercicio 4: Preenchimento de Vetor I
"""

valor = int(input())
N = [0] * 10

for numero in range (10):
    N[numero] = valor * (2**numero)
    print ("N[", numero, "] = ", N[numero], sep="")

"""
Exercicio 5: Menor e Posição
"""

N = int(input())
valores = input().split()
menor_valor = int(valores[0])
posicao = 0

for i in range(1, N):
    valor_atual = int(valores[i])
    if valor_atual < menor_valor:
        menor_valor = valor_atual
        posicao = i

print("Menor valor:", menor_valor)
print("Posicao:", posicao)

"""
Exercicio 6: Coluna na Matriz
"""

C = int(input())
operacao = input()
soma = 0.0

for l in range(12):
    for c in range(12):
        valor = float(input())
        if c == C:
            soma += valor

if operacao == 'S':
    print("{:.1f}".format(soma))
elif operacao == 'M':
    media = soma / 12
    print("{:.1f}".format(media))

"""
Exercicio 7: Ordenação por Tamanho
"""
N = int(input())
valor = [''] * N

for elemento in range(N):
    valor[elemento] = input().split()
    valor[elemento] = sorted(valor[elemento],key=len,reverse=True)
   
for palavra in valor:
    print(' '.join(palavra))
"""
Aluno: Reyel Palma Ribeiro

Exercício 1: triângulos

Objetivo: Desenvolver uma função determina_tipo_triangulo que recebe três lados de um triângulo e retorna uma string, "Escaleno",
"Isósceles" ou "Equilátero", conforme o tipo do triângulo.
A função deve retornar "Não é um triângulo" se os três lados não formarem um triângulo.
"""

def determina_tipo_triangulo(a,b,c):
    if a >= b + c or b >= a + c or c >= b + a:
        print ("Não é um triangulo")
    elif a == c and a == b and c==b:
        print ("Equilátero")
    elif a == c or a == b or c == b:
        print ("Isóceles")
    else:
        print ("Escaleno")

determina_tipo_triangulo(4,4,4)
determina_tipo_triangulo(2,4,4)
determina_tipo_triangulo(3,4,5)
determina_tipo_triangulo(1,1,4)

"""
Exercício 2: dia da semana

Objetivo: Desenvolver uma função dia_semana que recebe um número inteiro e retorna uma string indicando o dia da semana equivalente,
considerando que o dia da semana igual a 1 é o domingo, 2 é segunda-feira, etc. 
A função deve retornar uma string vazia caso o número seja inválido. 
"""

def dia_semana(dia):
    if dia == 1:
        return "Domingo"
    elif dia == 2:
        return "Segunda-feira"
    elif dia == 3:
        return "Terça-feira"
    elif dia == 4:
        return "Quarta-feira"
    elif dia == 5:
        return "Quinta-feira"
    elif dia == 6:
        return "Sexta-feira"
    elif dia == 7:
        return "Sábado"
    else:
        return ""

print(dia_semana(2)) 
print(dia_semana(6)) 
print(dia_semana(7)) 
print(dia_semana(9))

"""
Exercício 3: calculadora simples

Objetivo: Desenvolver funções de operações aritméticas soma, subtracao, multiplicacao e divisao, que recebem dois números cada uma 
e retornam o resultado da operação indicada.
Em seguida, crie uma função que elabora uma interface por linha de comando (CLI),
que lê dois números e uma operação e exibe na tela o valor do resultado,
ou exibe "operação inválida" se o usuário inserir uma mensagem diferente das quatro operações.
"""

def Soma(N1,N2):
    return N1 + N2

def Subtração(N1,N2):
    return N1 - N2

def Multiplicação(N1,N2):
    return N1 * N2

def Divisão(N1,N2):
    if N2 != 0:
        return N1 / N2
    else:
        return "Erro: Divisão por zero"


def caluculadora_simples():
    N1 = float(input("Insira um número: "))
    N2 = float(input("Insira outro número: "))
    Comando = (input("Informe a operação: "))
    
    if Comando == "Multiplicação" or Comando == "multiplicação":
        print ("Resultado:", Multiplicação(N1,N2))
    elif Comando == "Soma" or Comando == "soma":
        print ("Resultado:", Soma(N1,N2))
    elif Comando == "Divisão" or Comando == "divisão":
        print ("Resultado:", Divisão(N1,N2))
    elif Comando == "Subtração" or Comando == "subtração":
        print ("Resultado:", Subtração(N1,N2))
    else:
        print("Operação Invalida")

caluculadora_simples()
    
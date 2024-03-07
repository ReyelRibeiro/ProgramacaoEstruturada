"""
Aluno: Reyel Palma Ribeiro

Exercício 1: Equações de segundo grau

Objetivo: Elaborar um código em Python que resolva uma equação do segundo grau (ax² + bx + c = 0).
O programa deve ler os parâmetros a, b e c da equação e deve calcular as raízes pela fórmula de Bhaskara.
Considere que as raízes dadas pelo usuário são sempre reais, e os valores passados pelo usuário são sempre numéricos.

Obs: Deixarei o texto identico aos exemplos mostrados pela atividade
"""

a = float(input("Informe o parâmetro a da equação: "))
b = float(input("Informe o parâmetro b da equação: "))
c = float(input("Informe o parâmetro c da equação: "))

delta = (b**2)-(4*a*c)
raizdedelta = delta**(1/2)
primeiraraiz = (-b+raizdedelta)/(2*a)
segundaraiz = (-b-raizdedelta)/(2*a)

print("A primeira raiz da equação é", primeiraraiz)
print("A segunda raiz da equação é", segundaraiz)

"""
Exercício 2: Anos bisextos

Objetivo: Elaborar um programa em Python que leia uma variável inteira ano. 
Em seguida, exiba na tela o resultado da expressão lógica que indica se um ano é ou não bissexto. 
Um ano é bissexto se ele é múltiplo de quatro. No entanto anos múltiplos de 100 que não são múltiplos de 400 não são bissextos. 
Então 1995 não é bissexto, 2012 é bissexto, 1900 não é bissexto e 2000 é bissexto.

O programa deve utilizar apenas as funções print(), input() e int(), 
além dos operadores lógicos and, or ou not e de operadores aritméticos ou de comparação necessários.

Obs: Deixarei o texto identico aos exemplos mostrados pela atividade
"""
Ano=int(input("Informe o ano: "))

print((not Ano%4!=0) and ((Ano%100!=0) or (not Ano%400!=0)))
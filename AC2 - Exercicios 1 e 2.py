"""
Aluno: Reyel Palma Ribeiro

Exercício 1: Equações de segundo grau

Objetivo: Desenvolva duas funções em Python:

1 - eq_seg_grau(a, b, c), que recebe três valores reais e 
retorna as raízes de uma equação de segundo grau no formato ax² + bx + c = 0, supondo as raízes sempre reais;

2 - bissexto(ano), que recebe um valor inteiro e retorna um valor booleano, informando se o ano é bissexto ou não.
"""

"""Objetivo numero 1"""

def eq_seg_grau(a, b, c):
    delta = (b**2) - (4*a*c)
    raizdedelta = delta**(1/2)
    print (((-b + raizdedelta) / (2*a)), ((-b - raizdedelta) / (2*a)))

eq_seg_grau(1,-6,8)

"""Objetivo numero 2"""

def bissexto(ano):
    print ((not ano%4!=0) and ((ano%100!=0) or (not ano%400!=0)))

bissexto(1900)
bissexto(1600)

"""
Exercicio 2: Salario

Objetivo: Desenvolva uma função em Python cujo nome é calcula_salario. 
Essa função recebe dois parâmetros posicionais reais, valor_hora e num_horas, que correspondem ao valor do salário por hora 
e o número de horas trabalhadas no mês, respectivamente. 
Além disso, a função tem um parâmetro-chave irpf, que calcula o imposto de renda a ser deduzido, cujo valor padrão é 0.275. 
A função retorna o salário líquido de um funcionário, calculado como o produto do valor por hora pelo número de horas,
reduzido o percentual do imposto de renda dado.
"""

def calcula_salario(valor_hora , num_horas, irpf=0.275):
    valorbruto =  valor_hora * num_horas
    impostoderenda = valorbruto * irpf
    print (valorbruto - impostoderenda)

calcula_salario(10,160)
'''
    Função para calcular imposto aplicado ao salário. Desafio da DIO.
    - aplicar salario
    - aplicar benefícios
'''

#função que calcula o salário + beneficio menos os impostos.
def calcular_imposto(salario):
    aliquota = 0.00
    if (salario >= 0.00 and salario <= 1100.00 ):
        aliquota = 0.05
    elif (salario >= 1100.01 and salario <= 2500.00):
        aliquota = 0.10
    else:
        aliquota = 0.15    
    return aliquota * salario

#lê os valores de calculo do salário.
valor_salario = float(input("Informe o valor do Salário: "))
valor_beneficio = float(input("Informe o valor do Benefício: "))

#calcula o imposto através da função.
valor_imposto = calcular_imposto(valor_salario)

#calcula e imprime. 
saida = valor_salario - valor_imposto + valor_beneficio
print(f"Novo valor de Salário: {saida: .2f}")
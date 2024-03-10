# Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento.
# Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, de 15%.

salario = float(input("Informe o salário: "))
base = salario
faixa_salarial = float(1250.00)
taxa_01 = float(0.10)
taxa_02 = float(0.15)

if(base > faixa_salarial):
    valor_aumento_10 = salario * taxa_01
    base = salario + valor_aumento_10
    print(f"Aumento de R$ {valor_aumento_10} reais. Salário antigo é de R$ {salario} reais. Novo salário a ser pago é de R$ {base}")
else:
    valor_aumento_15 = salario * taxa_02
    base = salario + valor_aumento_15
    print(f"Aumento de R$ {valor_aumento_15} reais. Salário antigo é de R$ {salario} reais. Novo salário a ser pago é de R$ {base}")
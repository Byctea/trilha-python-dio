# Escreva um programa que leia dois numeros e que pergunte qual operação você deseja realizar.
# Você deve poder calcular soma (+), subtração (-), multiplicação (*) e divisão (/).
# Exiba o resultado da Operação solicitada.

numero_a = int(input("Informa o primeiro número: "))
numero_b = int(input("Informa o segundo número: "))
operacao = str(input("Informe qual operação deseja realizar: "))
som = "soma"
sub = "subtração"
div = "divisão"
multi = "multiplicação"

if(operacao == som):
    resultado = numero_a + numero_b
    operador = "+"
    print(f"A operação de {operacao} dos números {numero_a} {operador} {numero_b} é igual a {resultado}.")

elif (operacao == sub):
    resultado = numero_a - numero_b
    operador = "-"
    print(f"A operação de {operacao} dos números {numero_a} {operador} {numero_b} é igual a {resultado}.")

elif (operacao == multi):
    resultado = numero_a * numero_b
    operador = "*"
    print(f"A operação de {operacao} dos números {numero_a} {operador} {numero_b} é igual a {resultado}.")

elif (operacao == div):
    resultado = numero_a / numero_b
    operador = "/"
    print(f"A operação de {operacao} dos números {numero_a} {operador} {numero_b} é igual a {resultado}.")
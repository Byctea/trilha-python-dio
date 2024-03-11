# Escreva um programa para aprovar o emprestimo bancário para compra de uma casa.
# O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar.
# o valor da prestaçao mensal não pode ser superior a 30% do salário.
# Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar.

valor_casa = float(input("Informe o valor do imóvel: "))
salario = float(input("Informe o salário do comprador: "))
anos = int(input("Informe a quantidaade de anos a pagar: "))

valor_prestacao_limite = salario * 0.30
meses = (anos * 365) / 12


valor_prestacao_mensal = valor_casa / meses

if(valor_prestacao_mensal <= valor_prestacao_limite):
    print(f"você está habilitado a realizar a compra, valor da prestação: {valor_prestacao_mensal}")
else:
    print(f"O valor da sua prestação {valor_prestacao_limite} não comporta o valor da compra do imovel")

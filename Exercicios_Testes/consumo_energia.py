
# Escreva um programa que calcule o preço a pagar pelo funcionamento de energia elétrica.
# Pergunte a quantidade de KWh consumida e o tipo de instalação
# R = para residência, I para industrias e C para comércios.
# Calcule o preço a pagar de acordo com a tabela

qtde_consumida_kwh = int(input("Informe a quantidade de KWh consumid: "))
tipo_de_instalacao = str(input("Informe o tipo de instalação: "))

if (qtde_consumida_kwh <= 500 and tipo_de_instalacao == "R"):
        valor_a_pagar = qtde_consumida_kwh * 0.40
        print(f"Valor a ser pago pelo contribuinte é de R$ {valor_a_pagar:.2f} reais.")
elif (qtde_consumida_kwh > 500 and tipo_de_instalacao == "R"):
        valor_a_pagar = qtde_consumida_kwh * 0.65
        print(f"Valor a ser pago pelo contribuinte é de R$ {valor_a_pagar:.2f} reais.")

elif (qtde_consumida_kwh <= 1000 and tipo_de_instalacao == "C"):
        valor_a_pagar = qtde_consumida_kwh * 0.55
        print(f"Valor a ser pago pelo contribuinte é de R$ {valor_a_pagar:.2f} reais.")
elif (qtde_consumida_kwh > 1000 and tipo_de_instalacao == "C"):
        valor_a_pagar = qtde_consumida_kwh * 0.60
        print(f"Valor a ser pago pelo contribuinte é de R$ {valor_a_pagar:.2f} reais.")

elif (qtde_consumida_kwh <= 5000 and tipo_de_instalacao == "I"):
        valor_a_pagar = qtde_consumida_kwh * 0.55
        print(f"Valor a ser pago pelo contribuinte é de R$ {valor_a_pagar:.2f} reais.")
elif (qtde_consumida_kwh > 5000 and tipo_de_instalacao == "I"):
        valor_a_pagar = qtde_consumida_kwh * 0.60 
        print(f"Valor a ser pago pelo contribuinte é de R$ {valor_a_pagar:.2f} reais.")       
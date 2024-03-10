# Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km.
# Calcule o preço da passagem, cobrando de R$ 0,50 por km para viagens de até 200KM.
# Para viagens acima de 200km deverá ser cobrado R$ 0,45

distancia_em_km = float(input("Informe a distância que deseja percorrer: "))
viagem_200 = float(0.50)
viagem_acima_200 = float(0.45)

if(distancia_em_km <= viagem_200):
    valor_a_cobrar = distancia_em_km * viagem_200
    print(f"O valor da sua passagem é de R$ {valor_a_cobrar} reais.")
else:
    valor_a_cobrar = distancia_em_km * viagem_acima_200
    print(f"O valor da sua passagem é de R$ {valor_a_cobrar} reais.")
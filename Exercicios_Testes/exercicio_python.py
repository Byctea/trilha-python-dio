# Faça um programa que peça dois numeros inteiros. Imprima a soma desses dois números na tela.
numero_a = 10
numero_b = 20
resultado = numero_a + numero_b
print(f"A soma dos numeros é:", resultado)

# Esvreva um programa que leia um valor em metros e o exiba convetido em milímetros
a = int(input("Informe a quantidade do centímetro: "))
conversor = a / 100
print(f"{a} centrímetros em milímetro é: {conversor}mm.")

#Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário atual e a porcetagem do aumento.
#Exiba o valor do aumento e do novo salário.
salario = int(input("Informe o valor do salário atual: "))
tx_aumento = int(input("informe a porcetagem do aumento: "))
valor_aumento = salario * (tx_aumento /100)
novo_salario = float(salario) + float(valor_aumento)
print(f"Aplicando a taxa de {tx_aumento}% sobre o valor do salário R${salario} reais, teremos o aumnento em valores de : ", valor_aumento, ".\nO novo salário a ser pago é: ", novo_salario)

# Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.

mercadoria = float(input("Informe o valor do produto: "))
tx_desconto = float(input("informe o valor do desconto: "))

desconto = mercadoria * (tx_desconto / 100)
novo_valor_mercadoria = mercadoria - desconto

print(f"O valor do desconto {desconto}% aplicado sobre a mercadoria que custa {mercadoria} é de {desconto}. \nMercadoria custa:", novo_valor_mercadoria)

# Escreva um programa que calcule o tempo dde uma viagem de carro. Pergunte a distância a percorrer.
# Pergunte a velocidade média esperada para a viagem.
distancia = float(input("Informa a distância a ser percorrida: "))
velocidade_media = int(input("Informe a velocidade média: "))
tempo_de_viagem = distancia / velocidade_media
print(f"O tempo médio de viagem cuja distância de {distancia}KM com uma velocidade média de {velocidade_media}km/hs é {tempo_de_viagem:0.2f}")

# Escreva um programa que converta uma temperatura digitada em °C em °F.
graus_C = int(input("Informe o valor do grau °C: "))
f = ((9 * graus_C) / 5) + 32
print(f"{graus_C}°C  convertido para °F é {f}")

# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário.
# Assim como a quantidade de dias pelo quais o carro foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$ 60 reais por dia e R$ 0.15 por km rodado.
qtde_km_percorridos = int(input("Informe quantidade de KM rodado: "))
qtde_dias_alugado = int(input("Informe quantidade de dias alugados: "))
valor_da_diaria =float(60.00)
valor_do_km_percorrido = float(0.15)
preco_a_pagar = (qtde_dias_alugado * valor_da_diaria) + (qtde_km_percorridos * valor_do_km_percorrido)
print(f"O preço a pagar pelo aluguel do carro é R$ {preco_a_pagar:.2f} reais.")


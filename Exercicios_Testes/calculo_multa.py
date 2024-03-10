# Escreva um programa que pergunte a velocidade do carro de um usuario. 
# Caso ultrapasse 80 KM/h, exiba uma mensagem dizendo que o usuário foi multa.
# Nesse caso, exiba o valor da multa, cobrando R$ 5 por KM acima de 80 KM/h.

velocidade_veiculo = int(input("Informe a velocidade do veículo: "))
limite_velocidade = 80 #limite de 80 km/h.
valor_multa = float(5)
multa = (velocidade_veiculo - limite_velocidade) * valor_multa

if(velocidade_veiculo > limite_velocidade):
    print(f"Você foi multado em R$ {multa:.2f} reais por ultrapassar a velocidade permitida de {limite_velocidade} KM/h da via.")
else:
    print(f"velocidade permitida.")

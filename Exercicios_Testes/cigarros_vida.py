# Escreva um programa para calcular a redução do tempo de vida de um fumante.
# Pergunte a quantidade de cigarros fumados por dia e quanto anos ele já fumou.
# Considere que um fumanante perde 10 minutos de vida a cada cigarro e calcule quantos dias de vida um fumante perderá.
# Exiba o total em dias.

qtde_cigarros_fumados = int(input("Informe a quantidade de Cigarros fumados: "))
qtde_anos_fumando = int(input("Informe a quantidade de anos que fuma: "))
horas = 60
dia = 24
fumante_perde_min_vida = 10

# Quantidade de horas que o indivíduo tem por dia
life_perda_dia = (((qtde_cigarros_fumados * (fumante_perde_min_vida / horas))) * (qtde_anos_fumando * 365)) / dia
#resultado = ((qtde_anos_fumando * 365) * life_perda_dia) / dia

print(f"O fumante perderá fumando {qtde_cigarros_fumados} cigarros por dia em {qtde_anos_fumando} anos um total de {life_perda_dia:.2f} dias.")
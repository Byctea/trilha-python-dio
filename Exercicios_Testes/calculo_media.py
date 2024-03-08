# programa de calcular média de nota de aluno
##
###

materia1 = float(input("Informe a nota 1: "))
materia2 = float(input("Informe a nota 2: "))
materia3 = float(input("Informe a nota 3: "))

media = float(7.0)

resultado = (materia1 >= media) and (materia2 >= media) and (materia3 >= media)

if resultado >= True:
    print("Aprovado!")
else:
    print("Reprovado")


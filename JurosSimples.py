capital = float(input("Insira o capital inicial: "))
taxa = float(input("Insira a taxa de juros (em porcentagem): "))
tempo = float(input("Insira o tempo (em anos): "))

juros = (capital * taxa * tempo) / 100

valor_total = capital + juros

print("Valor total:", valor_total)

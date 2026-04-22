maior = float('-inf')  # Inicializa com menos infinito para garantir que qualquer número seja maior
menor = float('inf')  # Inicializa com mais infinito para garantir que qualquer número seja menor
media = 0.0

num1 = float(input("Informe o valor do primeiro número: "))
num2 = float(input("Informe o valor do segundo número: "))
num3 = float(input("Informe o valor do terceiro número: "))
num4 = float(input("Informe o valor do quarto número: "))
num5 = float(input("Informe o valor do quinto número: "))
num6 = float(input("Informe o valor do sexto número: "))
num7 = float(input("Informe o valor do sétimo número: "))
num8 = float(input("Informe o valor do oitavo número: "))
num9 = float(input("Informe o valor do nono número: "))
num10 = float(input("Informe o valor do décimo número: "))

media = (num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9 + num10) / 10

if num1 > maior:
    maior = num1
if num1 < menor:
    menor = num1

if num2 > maior:
    maior = num2
if num2 < menor:
    menor = num2

if num3 > maior:
    maior = num3
if num3 < menor:
    menor = num3

if num4 > maior:
    maior = num4
if num4 < menor:
    menor = num4

if num5 > maior:
    maior = num5
if num5 < menor:
    menor = num5

if num6 > maior:
    maior = num6
if num6 < menor:
    menor = num6

if num7 > maior:
    maior = num7
if num7 < menor:
    menor = num7

if num8 > maior:
    maior = num8
if num8 < menor:
    menor = num8

if num9 > maior:
    maior = num9
if num9 < menor:
    menor = num9

if num10 > maior:
    maior = num10
if num10 < menor:
    menor = num10

print("O maior valor é:", maior)
print("O menor valor é:", menor)
print("A média dos valores digitados é:", media)

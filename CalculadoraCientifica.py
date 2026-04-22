import math

print("Bem-vindo à Calculadora Científica!")
print("Escolha uma operação:")
print("1. Soma (+)")
print("2. Subtração (-)")
print("3. Multiplicação (*)")
print("4. Divisão (/)")
print("5. Potência (**)")
print("6. Raiz Quadrada (√)")
print("7. Seno (sin)")
print("8. Cosseno (cos)")
print("9. Tangente (tan)")
print("10. Logaritmo (log)")

while True:
    try:
        escolha = int(input("\nDigite o número da operação desejada (ou 0 para sair): "))
        if escolha == 0:
            print("Encerrando a calculadora. Até logo!")
            break

        if escolha in [1, 2, 3, 4, 5]:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if escolha == 1:
                print(f"Resultado: {num1} + {num2} = {num1 + num2}")
            elif escolha == 2:
                print(f"Resultado: {num1} - {num2} = {num1 - num2}")
            elif escolha == 3:
                print(f"Resultado: {num1} * {num2} = {num1 * num2}")
            elif escolha == 4:
                if num2 != 0:
                    print(f"Resultado: {num1} / {num2} = {num1 / num2}")
                else:
                    print("Erro: Divisão por zero não é permitida.")
            elif escolha == 5:
                print(f"Resultado: {num1} ** {num2} = {num1 ** num2}")

        elif escolha == 6:
            num = float(input("Digite o número: "))
            if num >= 0:
                print(f"Resultado: √{num} = {math.sqrt(num)}")
            else:
                print("Erro: Não é possível calcular a raiz quadrada de um número negativo.")

        elif escolha in [7, 8, 9]:
            angulo = float(input("Digite o ângulo em graus: "))
            radianos = math.radians(angulo)

            if escolha == 7:
                print(f"Resultado: sin({angulo}) = {math.sin(radianos)}")
            elif escolha == 8:
                print(f"Resultado: cos({angulo}) = {math.cos(radianos)}")
            elif escolha == 9:
                print(f"Resultado: tan({angulo}) = {math.tan(radianos)}")
        
        elif escolha == 10:
            num = float(input("Digite o número: "))
            base = float(input("Digite a base do logaritmo (ou 0 para logaritmo natural): "))
            if base > 0 and base != 1:
                print(f"Resultado: log{base}({num}) = {math.log(num, base)}")
            elif base == 0:
                print(f"Resultado: ln({num}) = {math.log(num)}")
            else:
                print("Erro: Base inválida para o logaritmo.")

        else:
            print("Erro: Opção inválida. Tente novamente.")

    except ValueError:
        print("Erro: Entrada inválida. Digite um número inteiro.")

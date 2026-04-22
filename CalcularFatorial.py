numero = int(input("Digite um número para calcular o fatorial: "))

def fatorial(numero):
    
    if numero < 0:
        print("O fatorial não é definido para números negativos!")
        exit()
        
    elif numero == 0:
        print("O fatorial é 1!")
        exit()
        
    fat = 1
    contador = 1
    while contador <= numero:
         fat *= contador
         contador += 1
    return fat

resultado = fatorial(numero)
print(f"O fatorial de {numero} é {resultado}")

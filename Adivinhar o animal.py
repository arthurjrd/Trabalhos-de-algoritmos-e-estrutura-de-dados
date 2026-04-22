def adivinhar_mamifero():
    locomocao = input("Esse mamífero é quadrúpede, bípede, voador ou aquático? ").lower()
    
    if locomocao == "quadrúpede":
        dieta = input("Ele é carnívoro ou herbívoro? ").lower()
        # Analisando quadrúpedes
        if dieta == "carnívoro" or dieta == "carnivoro":
            print("O animal escolhido é o leão.")
        elif dieta == "herbívoro":
            print("O animal escolhido é o cavalo.")
        else:
            print("Não consegui identificar o mamífero quadrúpede com essa dieta.")
            
    elif locomocao == "bípede" or locomocao == "bipede":
        dieta = input("Ele é onívoro ou frutívoro? ").lower()
        if dieta == "onívoro" or dieta == "onivoro":
            print("O animal escolhido é o Homem.")
        elif dieta == "frutívoro":
            print("O animal escolhido é o macaco.")
        else:
            print("Não consegui identificar o mamífero bípede com essa dieta.")
            
    elif locomocao == "voador":
        print("O animal escolhido é o morcego.")
    elif locomocao == "aquático":
        print("O animal escolhido é a baleia.")
    else:
        print("Locomoção inválida para mamífero.")

def adivinhar_ave():
    tipo = input("Essa ave é voadora, nadadora ou de rapina? ").lower()
    if tipo == "voadora":
        # Voadora pode ser avestruz? Não. Avestruz é corredora (bípede, não voadora)
        # Vamos assumir voadora para águia e pato
        habitat = input("Essa ave voadora é mais comum em terra ou água? ").lower()
        if habitat == "terra":
            print("O animal escolhido é a águia.")
        elif habitat == "água" or habitat == "agua":
            print("O animal escolhido é o pato.")
        else:
            print("Não consegui identificar a ave voadora.")
    
    elif tipo == "nadadora":
        # Nadadora é o pinguim
        print("O animal escolhido é o pinguim.")
    
    elif tipo == "de rapina":
        print("O animal escolhido é a águia.")
    
    elif tipo == "não voadora" or tipo == "nao voadora":
        # Avestruz (bípede e não voadora)
        print("O animal escolhido é o avestruz.")
    else:
        print("Tipo inválido para ave.")

def adivinhar_reptil():
    tipo = input("Esse réptil tem casco, é carnívoro ou sem patas? ").lower()
    if tipo == "com casco" or tipo == "casco":
        print("O animal escolhido é a tartaruga.")
    elif tipo == "carnívoro" or tipo == "carnivoro":
        # Crocodilo ou cobra
        locomocao = input("Esse réptil é quadrúpede ou sem patas? ").lower()
        if locomocao == "quadrúpede":
            print("O animal escolhido é o crocodilo.")
        elif locomocao == "sem patas":
            print("O animal escolhido é a cobra.")
        else:
            print("Não consegui identificar o réptil carnívoro.")
    elif tipo == "sem patas":
        print("O animal escolhido é a cobra.")
    else:
        print("Tipo inválido para réptil.")

def main():
    classe = input("O animal é mamífero, ave ou réptil? ").lower()

    if classe == "mamífero" or classe == "mamifero":
        adivinhar_mamifero()
    elif classe == "ave":
        adivinhar_ave()
    elif classe == "réptil" or classe == "reptil":
        adivinhar_reptil()
    else:
        print("Classe inválida.")

if __name__ == "__main__":
    main()

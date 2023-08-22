import random
from os import system, name

def limpa_tela():
    if name == "nt":    #nt para sistemas windows
        _ = system("cls")
    else:
        _ = system("clear")

def game():
    limpa_tela()

    print("\nBem vindo(a) ao jogo de forca")
    print("Adivinhe a palavra abaixo:\n")

    palavras = ["banana", "abacate","uva","morango","laranja"]
    palavra = random.choice(palavras)
    letras_descobertas = ["_" for letra in palavra]
    choices = 6
    letras_erradas = []

    while choices > 0:
        
        print(" ".join(letras_descobertas))
        print("\nNumero de chances restantes: ",choices)
        print("Letras erradas"," ".join(letras_erradas))
        tentativa = input("digite uma letra: ").lower()

        if tentativa in palavra:
            index = 0
            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index+=1
        else:
            choices-=1
            letras_erradas.append(tentativa)

        if "_" not in letras_descobertas:
            print("voce venceu, a palavra era ",palavra)
            break

    if "_" in letras_descobertas:
        print("voce perdeu, a palavra era ",palavra)

if __name__ == "__main__":
    game()
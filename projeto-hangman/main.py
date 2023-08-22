import random
from os import system, name

def limpa_tela():
    if name == "nt":    #nt para sistemas windows
        _ = system("cls")
    else:
        _ = system("clear")

def display_hangman(chances):

    # Lista de estágios da forca
    stages = [  # estágio 6 (final)
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # estágio 5
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # estágio 4
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # estágio 3
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # estágio 2
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # estágio 1
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # estágio 0
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[chances]

def game():
    limpa_tela()

    print("\nBem vindo(a) ao jogo de forca")
    print("Adivinhe a palavra abaixo:\n")

    palavras = ["banana", "abacate","uva","morango","laranja"]
    palavra = random.choice(palavras)
    letras_descobertas = [letra for letra in palavra]
    tabuleiro = ["_"] * len(palavra)
    choices = 6
    letras_escolhidas = []

    while choices > 0:
        
        print(display_hangman(choices))
        print(" ".join(tabuleiro))
        print("\nNumero de chances restantes: ",choices)
        print("Letras escolhidas "," ".join(letras_escolhidas))
        tentativa = input("digite uma letra: ").lower()

        if tentativa in letras_escolhidas:
            print("Ja digitou essa letra tente outra ")
            continue

        letras_escolhidas.append(tentativa)

        if tentativa in palavra:
            for indice in range(len(letras_descobertas)):
                if tentativa == letras_descobertas[indice]:
                    tabuleiro[indice] = tentativa
            if "_" not in tabuleiro:
                print("voce venceu, a palavra era ",palavra)
                break

        else:
            print("letra errada")
            choices-=1
        
    if "_" in tabuleiro:
        print("voce perdeu, a palavra era ",palavra)

if __name__ == "__main__":
    game()
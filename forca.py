palavra = input("Insira uma palavra: ").lower()
letrasDescobertas = ["_"] * len(palavra)
tentativas = 6
letras_erradas = ""

while tentativas > 0 and "_" in letrasDescobertas:
    if tentativas == 6:
        print("""
  +---+
  |   |
      |
      |
      |
      |
=========
""")
    elif tentativas == 5:
        print("""
  +---+
  |   |
  O   |
      |
      |
      |
=========
""")
    elif tentativas == 4:
        print("""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""")
    elif tentativas == 3:
        print("""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""")
    elif tentativas == 2:
        print("""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""")
    elif tentativas == 1:
        print("""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""")
    elif tentativas == 0:
        print("""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
""")

    print("\nPalavra: ", end="")
    for letra in letrasDescobertas:
        print(letra, end=" ")

    print("\nLetras erradas:", letras_erradas)

    letra = input("Digite uma letra: ").lower()

    if letra in palavra:
        for i in range(len(palavra)):
            if palavra[i] == letra:
                letrasDescobertas[i] = letra
    else:
        if letra not in letras_erradas:
            letras_erradas = letras_erradas + letra + " "
            tentativas -= 1
        else:
            print("Você já tentou essa letra.")

if "_" not in letrasDescobertas:
    print("\nParabéns! Você acertou:", palavra)
else:
    print("\nVocê perdeu! A palavra era:", palavra)

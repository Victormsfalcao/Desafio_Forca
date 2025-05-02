numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
nomes = ["Adryan", "Alana","Andresa", "Cleibson", "Gabriel", "Giovanna", "Gustavo", "Isabella", "João", "Júlia", "Leide", "Lucas", "LUNA", "Manoel", "Mariana", "Matheus V.", "Narely", "Renan", "Samuel", "Sérgio", "Sol", "Victor", "Weverton", "Yuri"]

print("Escolha um número de 1 a 23:")
print(numeros)

num = int(input("Número: "))
palavra = nomes[num - 1].lower()

letrasDescobertas = ["_" if letra != " " else " " for letra in palavra]
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
            letras_erradas += letra + " "
            tentativas -= 1
        else:
            print("Você já tentou essa letra.")

if "_" not in letrasDescobertas:
    print("\nParabéns! Você acertou:", palavra)
else:
    print("""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
""")
    print("\nVocê perdeu! A palavra era:", palavra)

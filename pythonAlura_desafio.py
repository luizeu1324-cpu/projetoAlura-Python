#apenas para utilizar se caso o número secreto seja aleatório: import random

#Número secreto definido por você
numero_secreto = 42
#Caso queira que o número seja aleatório: numero_secreto = random.randint(1, 100)


print("Tente adivinhar o número secreto! Você tem 5 tentativas.")

# Loop com 5 tentativas
for tentativa in range(1, 6):
    palpite = int(input(f"Tentativa {tentativa}: Digite seu palpite: "))

    if palpite == numero_secreto:
        print("Parabéns! Você acertou!")
        break
    elif palpite > numero_secreto:
        print("O número secreto é menor.")
    else:
        print("O número secreto é maior.")

# Caso o jogador não acerte nas 5 tentativas
else:
    print(f"\nVocê perdeu! O número correto era: {numero_secreto}")

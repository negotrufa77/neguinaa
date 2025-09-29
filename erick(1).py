# Definindo o número secreto
numero_secreto = 42

# Número máximo de tentativas
tentativas = 5

print("Bem-vindo ao jogo de adivinhação!")
print(f"Tente adivinhar o número secreto. Você tem {tentativas} tentativas.")

# Loop para as tentativas
for tentativa in range(1, tentativas + 1):
    # Pedindo o palpite ao jogador
    palpite = int(input(f"Tentativa {tentativa}: Qual é o seu palpite? "))
    
    # Verificando se o palpite está correto
    if palpite == numero_secreto:
        print("Parabéns! Você acertou o número secreto!")
        break
    elif palpite < numero_secreto:
        print("O número secreto é maior do que o seu palpite. Tente novamente.")
    else:
        print("O número secreto é menor do que o seu palpite. Tente novamente.")
    
# Caso o jogador não tenha acertado
if palpite != numero_secreto:
    print(f"Você perdeu! O número secreto era {numero_secreto}.")

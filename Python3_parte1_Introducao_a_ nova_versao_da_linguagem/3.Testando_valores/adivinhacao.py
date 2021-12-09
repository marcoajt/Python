print("*********************************")
print("Bem vindo no jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42

chute_str = input("Digite o seu numero: ") #Preferencia: chute = int(input("Digite o seu numero: ")).


print("Você digitou ", chute_str)

chute = int(chute_str) #Não precisaria fazer isso se vc escolheu a preferencia.

acertou = (chute == numero_secreto)
maior   = chute > numero_secreto
menor   = chute < numero_secreto

if(acertou):
    print("Você acertou!")
else:
    if(maior):
        print("Você errou! O seu chute foi maior do que o número secreto.")
    elif(menor):
        print("Você errou! O seu chute foi menor do que o número secreto.")

print("Fim de jogo!")
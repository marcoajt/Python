print("*********************************")
print("Bem vindo no jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42

chute_str = input("Digite o seu numero: ") #Preferencia: chute = int(input("Digite o seu numero: ")).


print("Você digitou ", chute_str)

chute = int(chute_str) #Não precisaria fazer isso se vc escolheu a preferencia.

if(chute == numero_secreto):
    print("Você acertou!")
else:
    print("Você errou")

print("Fim de jogo!")
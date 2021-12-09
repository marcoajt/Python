## Aula 3

Nesse capítulo, vamos fazer com que o usuário possa dar vários chutes para tentar acertar o número, já que atualmente ele só tem uma tentativa. Mas antes disso, vamos implementar uma dica para o usuário, dizendo se o número que ele chutou é maior ou menor que o número secreto.

Para isso, precisamos mexer no bloco do **`else`**. Vamos ter que testar novamente, se o número for maior, imprimimos uma mensagem dizendo isso ao usuário, se for menos, diremos ao usuário que o número digitado é menor que o número secreto:

```
if (numero_secreto == chute):
    print("Você acertou!")
else:
    if (chute > numero_secreto):
        print("Você errou! O seu chute foi maior que o número secreto.")
    if (chute < numero_secreto):
        print("Você errou! O seu chute foi menor que o número secreto.")COPIAR CÓDIGO
```

Podemos testar e ver que tudo está funcionando perfeitamente.

## else com condição de entrada

Podemos notar que, se o chute não for igual, nem maior que o número secreto, obviamente ele será menor, então o último `if` não é necessário:

```
if (numero_secreto == chute):
    print("Você acertou!")
else:
    if (chute > numero_secreto):
        print("Você errou! O seu chute foi maior que o número secreto.")
    else:
        print("Você errou! O seu chute foi menor que o número secreto.")COPIAR CÓDIGO
```

Mas para esses casos, podemos fazer um **`else`** com uma **condição de entrada**, o **`elif`**. Vamos utilizá-lo para deixar o código mais semântico, já que na prática não há diferença:

```
if (numero_secreto == chute):
    print("Você acertou!")
else:
    if (chute > numero_secreto):
        print("Você errou! O seu chute foi maior que o número secreto.")
    elif (chute < numero_secreto):
        print("Você errou! O seu chute foi menor que o número secreto.")COPIAR CÓDIGO
```

## Melhorando a legibilidade do código

Podemos melhorar a legibilidade do nosso código, para que outros programadores que possam vir a desenvolver conosco o entendam melhor. Vamos deixar nossas condições mais claras, o que significa **`chute == numero_secreto`**, por exemplo? Que o usuário acertou, logo vamos extrair essa condição para uma variável:

```
acertou = chute == numero_secreto

if (acertou):
    print("Você acertou!")
else:
    if (chute > numero_secreto):
        print("Você errou! O seu chute foi maior que o número secreto.")
    elif (chute < numero_secreto):
        print("Você errou! O seu chute foi menor que o número secreto.")COPIAR CÓDIGO
```

Agora a condição **`if`** fica um pouco mais clara. Vamos fazer a mesma coisa para as outras duas condições:

```
acertou = chute == numero_secreto
maior = chute > numero_secreto
menor = chute < numero_secreto

if (acertou):
    print("Você acertou!")
else:
    if (maior):
        print("Você errou! O seu chute foi maior que o número secreto.")
    elif (menor):
        print("Você errou! O seu chute foi menor que o número secreto.")COPIAR CÓDIGO
```
# Adicionando níveis ao jogo

Vamos adicionar níveis ao nosso jogo, e conforme o nível vai ficando mais difícil, menos tentativas o usuário terá.

Começaremos perguntando ao usuário qual nível de dificuldade ele quer:

```
import random

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = random.randrange(1, 101)
total_de_tentativas = 3

print("Qual o nível de dificuldade?")
print("(1) Fácil (2) Médio (3) Difícil")

# resto do código comentado
```

E capturaremos o que ele digitar, já convertendo o valor para inteiro e guardando em uma variável:

```
import random

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = random.randrange(1, 101)
total_de_tentativas = 3

print("Qual o nível de dificuldade?")
print("(1) Fácil (2) Médio (3) Difícil")

nivel = int(input("Defina o nível: "))

# resto do código comentado
```

Agora falta mudar o total de tentativas baseado no nível que o usuário  escolher. A variável será inicializada com 0, e faremos um **`if`** para verificar o nível escolhido, se o ele for fácil, o usuário terá 20 tentativas, se for médio terá 10, e se for difícil terá 5 tentativas:

```
import random

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = random.randrange(1, 101)
total_de_tentativas = 0

print("Qual o nível de dificuldade?")
print("(1) Fácil (2) Médio (3) Difícil")

nivel = int(input("Defina o nível: "))

if (nivel == 1):
    total_de_tentativas = 20
elif (nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

# resto do código comentado
```

Com isso conseguimos definir os níveis de dificuldade no nosso jogo. No próximo vídeos definiremos pontuação!



# Definindo uma pontuação para o usuário

Com os níveis definidos, vamos agora calcular uma pontuação. Ela  funcionará da seguinte maneira, o usuário começa o jogo com 1000 pontos, e a cada rodada que ele não acerta o número secreto, ele perderá  pontos. Quanto mais distante for o chute, mais pontos o usuário irá  perder. Por exemplo, se o número secreto for 40, e o usuário chutar 20,  ele irá perder 20 pontos, que corresponde à distância entre os valores.

Vamos começar definindo a variável com 1000 pontos:

```
pontos = 1000
```

Após isso, o usuário irá perder pontos caso ele erre o chute, logo temos que implementar isso dentro da condição **`else`**:

```
if (acertou):
    print("Você acertou!")
    break
else:
    if (maior):
        print("Você errou! O seu chute foi maior que o número secreto.")
    elif (menor):
        print("Você errou! O seu chute foi menor que o número secreto.")
```

Vamos definir a variável **`pontos_perdidos`**, que subtrai o chute do número secreto:

```
if (acertou):
    print("Você acertou!")
    break
else:
    if (maior):
        print("Você errou! O seu chute foi maior que o número secreto.")
    elif (menor):
        print("Você errou! O seu chute foi menor que o número secreto.")
    pontos_perdidos = numero_secreto - chute
```

Depois, vamos subtrair os pontos perdidos da pontuação total:

```
if (acertou):
    print("Você acertou!")
    break
else:
    if (maior):
        print("Você errou! O seu chute foi maior que o número secreto.")
    elif (menor):
        print("Você errou! O seu chute foi menor que o número secreto.")
    pontos_perdidos = numero_secreto - chute
    pontos = pontos - pontos_perdidos
```

Isso funciona caso o usuário chute um número menor que o número secreto, mas e se for maior? Por exemplo, se o número secreto for 40 e o usuário  chutar 60, de acordo com o cálculo do nosso código os pontos perdidos  serão **-20**, e ao subtrair esse valor da pontuação total, ela irá aumentar!

Então queremos fazer a subtração dos pontos perdidos, mas caso essa  subtração tenha como resultado um número negativo, queremos que  "esquecer" esse sinal, queremos sempre o **número absoluto**.

E para extrair o número absoluto, existe mais uma função *built-in*, a **`abs()`**:

```
if (acertou):
    print("Você acertou!")
    break
else:
    if (maior):
        print("Você errou! O seu chute foi maior que o número secreto.")
    elif (menor):
        print("Você errou! O seu chute foi menor que o número secreto.")
    pontos_perdidos = abs(numero_secreto - chute)
    pontos = pontos - pontos_perdidos
```

Por fim, falta exibirmos a pontuação final ao usuário. Vamos alterar a  mensagem de acerto do usuário, acrescentando a pontuação total. Faremos  uso novamente da interpolação de strings:

```
if (acertou):
    print("Você acertou e fez {} pontos!".format(pontos))
    break
else:
    if (maior):
        print("Você errou! O seu chute foi maior que o número secreto.")
    elif (menor):
        print("Você errou! O seu chute foi menor que o número secreto.")
    pontos_perdidos = abs(numero_secreto - chute)
    pontos = pontos - pontos_perdidos
```

Com isso chegamos ao final do nosso jogo! No próximo capítulo veremos um  pouco sobre linguagens compiladas e interpretadas, entre outros  assuntos. Até lá!

# Para saber mais: arredondar no Python 2 e no Python 3

O Python 3 usa uma forma de arredondar, que também é chamado de **Banker's rounding**. Nessa forma, os valores são arredondados para o número que for mais  próximo, por exemplo: 2.4 seria arredondado para 2, todavia 2.6 já seria arredondado para 3. Quando um valor é igualmente próximo de dois  números, por exemplo 2.5, que possui 0.5 de diferença tanto para o  número 2 quanto para o número 3, esse é arredondado para o valor par  mais próximo, que, nesse caso, seria o número 2. **Vale lembrar  que somente os números x.5 recebem o tratamento "especial"  do  arredondamento para o valor par mais próximo, nos demais, o  arredondamento ocorre conforme esperado.** 

Mais informações se encontram na documentação do Python 3: https://docs.python.org/3.5/library/functions.html#round



# Para saber mais: Divisão de float e integer

O operador `//` também é chamado ***integer division\*** e sempre devolve o valor inteiro (sem arredondar).

Para realmente concluir o tópico, saiba que o Python 2 só tem ***integer division\***, mesmo tendo os dois operadores `/` e `//` ! No Python 2 não existe diferença entre os dois operadores, veja o exemplo:

![Operadores de divisão](https://s3.amazonaws.com/caelum-online-public/python3/img/05/operadores-divisao.png)
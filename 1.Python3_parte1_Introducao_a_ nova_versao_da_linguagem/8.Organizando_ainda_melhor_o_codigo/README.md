# Importando arquivos dentro de outros

Se conseguimos executar o jogo dentro do PyCharm, também conseguimos  rodar o jogo na linha de comando, no terminal. Dentro do diretório do  projeto **jogos**, basta executar:

```
python3 adivinhacao.py
```

No próximo treinamento, criaremos mais um jogo, a **forca**. Então já vamos deixar o seu arquivo preparado, criando o **forca.py**, também dentro do projeto **jogos**. Dentro desse arquivo, vamos deixar as mensagens de início e fim de jogo, semelhante ao jogo de adivinhação:

```
print("*********************************")
print("***Bem vindo ao jogo da Forca!***")
print("*********************************")

print("Fim do jogo")
```

## Oferecendo todos os jogos ao usuário

Vamos oferecer os dois jogos ao usuário, ou seja, devemos perguntar  ao usuário qual jogo ele quer executar, jogar. Mas onde vamos colocar  essa funcionalidade? A ideia é não misturar os jogos, deixar cada um em  um arquivo separado. Então vamos criar um novo arquivo com essa  funcionalidade, o arquivo **jogos.py**, perguntando qual jogo ele quer escolher jogar:

```
print("*********************************")
print("*******Escolha o seu jogo!*******")
print("*********************************")

print("(1) Forca (2) Adivinhação")
```

Agora vamos capturar a opção do usuário e verificar qual jogo ele escolheu:

```
print("*********************************")
print("*******Escolha o seu jogo!*******")
print("*********************************")

print("(1) Forca (2) Adivinhação")

jogo = int(input("Qual jogo? "))

if (jogo == 1):
    print("Jogando forca")
elif (jogo == 2):
    print("Jogando adivinhação")
```

## Importando arquivos

Ótimo, mas se queremos chamar um arquivo dentro de outro, precisamos importá-lo, algo parecido com o que fizemos com o módulo **`random`**:

```
import forca
import adivinhacao

print("*********************************")
print("*******Escolha o seu jogo!*******")
print("*********************************")

print("(1) Forca (2) Adivinhação")

jogo = int(input("Qual jogo? "))

if (jogo == 1):
    print("Jogando forca")
elif (jogo == 2):
    print("Jogando adivinhação")
```

## O problema do import

Podemos executar para ver como está ficando:

```
*********************************
***Bem vindo ao jogo da Forca!***
*********************************
Fim do jogo
*********************************
Bem vindo ao jogo de Adivinhação!
*********************************
Qual o nível de dificuldade?
(1) Fácil (2) Médio (3) Difícil
Defina o nível:
```

Ué, o que aconteceu? Quando importamos um arquivo no Python, ele o executa! Podemos reparar que ele executou o arquivo **forca.py** e logo depois o **adivinhacao.py**. Mas obviamente não queremos isso, só queremos executar o arquivo quando nós quisermos! E é isso que faremos no próximo vídeo.



# Criando funções para os nossos jogos

No vídeo anterior, vimos o problema do **`import`** acontecendo. Para resolver isso, vamos fazer algo semelhante à função **`print()`**, ela existe, mas só é executada quando chamada. Ou seja, vamos criar uma função específica para cada jogo.

## Colocando o código dos jogos dentro de funções

Em Python, quando queremos criar uma função, precisamos **defini-la**, através da palavra chave **`def`**. Vamos começar definindo a função **`jogar()`** no arquivo **forca.py**:

```
# forca.py

def jogar():

    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    print("Fim do jogo")
```

Faremos a mesma coisa no jogo de adivinhação, colocando todo o seu código dentro da função específica **`jogar()`**:

```
# adivinhacao.py

import random

def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1, 100)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou: ", chute_str)
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

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

    print("Fim do jogo")
```

## Chamando as funções

Agora precisamos chamar essas duas funções dentro do arquivo **jogos.py**, utilizando o nome do módulo e chamando a sua função:

```
# jogos.py

import forca
import adivinhacao

print("*********************************")
print("*******Escolha o seu jogo!*******")
print("*********************************")

print("(1) Forca (2) Adivinhação")

jogo = int(input("Qual jogo? "))

if (jogo == 1):
    print("Jogando forca")
    forca.jogar()
elif (jogo == 2):
    print("Jogando adivinhação")
    adivinhacao.jogar()
```

Podemos executar novamente o **jogos.py** e observar a sua saída:

```
*********************************
*******Escolha o seu jogo!*******
*********************************
(1) Forca (2) Adivinhação
Qual jogo?
```

Não aparecem mais as saídas dos jogos e sim a saída do próprio **jogos.py**. Os arquivos foram importados mas não foram executados, somente lidos.  Eles só serão executados quando suas respectivas funções forem chamadas.

Com isso modularizamos o nosso código, temos um arquivo para cada  jogo e um principal, que disponibiliza os jogos para o usuário. Podemos  testar a execução do arquivo **jogos.py** pelo terminal também:

```
python3 jogos.py
```

E o jogo diretamente, será que conseguimos jogar? Se executarmos o arquivo **adivinhacao.py**, por exemplo:

```
python3 adivinhacao.py
```

Nada acontece! Ou seja, agora só conseguimos jogar os nossos jogos através do arquivo **jogos.py**. Vamos então tentar resolver isso no próximo vídeo, até lá!



# Declarando funções

Pouco vimos sobre funções, mas não se preocupe. Na medida em que você avança nos cursos sobre Python 3, vamos introduzir mais recursos.

Para declarar uma função, devemos usar a palavra chave `def` do mundo Python, seguida pelo nome da função. Lembrando que é consenso usar a nomenclatura *snake_case*:

```
def nome_da_funcao():
    # todo o código identado faz parte da função
    print("aprendendo funções")
```

Repare que uma função pode chamar uma outra função. `print` também é uma função e usamos ela dentro da nossa própria função. 

## Executando funções

Para chamar a nossa própria função, usamos o nome dela seguido pelos parênteses, por exemplo:

```
nome_da_funcao()
```

Podemos chamar uma função quantas vezes quisermos:

```
nome_da_funcao()
nome_da_funcao()
nome_da_funcao()
```

Isso é a principal vantagem de funções, reaproveitar o código escrito nela!

## Parâmetros e retorno

Uma função também pode receber parâmetros e retornar algum valor, por exemplo:

```
def soma(a, b):
     return a + b
```

A função `soma` recebe dois parâmetros (`a` e `b`) e retorna a soma. Ao chamar a função, podemos capturar o retorno:

```
s = soma(3, 4) 
```

Isso foi apenas uma pequena introdução, mas novamente, ainda vamos utilizar muito as funções e praticar para fixar o conteúdo.

# Diferenciando um arquivo executado de um importado

Não conseguimos mais jogar diretamente cada jogo porque o seu próprio arquivo não chama a sua função **`jogar()`**. Então, depois da função, vamos chamá-la:

```
# adivinhacao.py

import random

def jogar():
    # código omitido

jogar()
```

Isso resolve o problema de jogar o jogo diretamente mas voltamos ao problema do vídeo anterior! Ao executarmos o arquivo **jogos.py**, como o próprio arquivo **adivinhacao.py** chama a função **`jogar()`**, ela será executada sem que queiramos isso.

Precisamos dar um jeito para que, quando executarmos o jogo de adivinhação diretamente, a função **`jogar()`** deve ser chamada, mas quando só o importamos, não queremos que a função seja chamada.

## Programa principal vs Programa importado

Quando rodamos diretamente um arquivo no Python, ele internamente  cria uma variável e a preenche. E através dessa variável podemos fazer  uma consulta, pois se ela estiver preenchida, significa que o arquivo  foi executado diretamente, mas se a variável não estiver preenchida,  então significa que o arquivo só foi importado.

Essa variável é a **`__name__`**, e ela é preenchida com o valor **`__main__`** caso o arquivo seja executado diretamente. Vamos então fazer **`if`** para verificar se ela está preenchida ou não:

```
# adivinhacao.py

import random

def jogar():
    # código omitido

if (__name__ == "__main__"):
    jogar()
```

Podemos agora testar os dois casos, executar o arquivo diretamente e executar o arquivo **jogos.py**. Os dois estão funcionando, exatamente como queríamos. Falta fazermos a mesma coisa com o jogo da forca:

```
# forca.py

def jogar():
    # código omitido

if (__name__ == "__main__"):
    jogar()
```

E com o arquivo **jogos.py**, colocando o seu código dentro da função **`escolhe_jogo()`** e chamando-a caso o programa seja o programa principal:

```
import forca
import adivinhacao

def escolhe_jogo():
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual jogo? "))

    if (jogo == 1):
        print("Jogando forca")
        forca.jogar()
    elif (jogo == 2):
        print("Jogando adivinhação")
        adivinhacao.jogar()

if (__name__ == "__main__"):
    escolhe_jogo()
```

Com isso  vimos como diferenciar se o programa é o principal ou não, se ele está  sendo executado diretamente ou só sendo importado. Na hora de importar  um arquivo, ele lê o código da função, mas não o executa, pois ele não é o arquivo principal
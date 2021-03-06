# Organizando o código em funções

A função **`jogar()`** possui um código muito complexo, com muitas funcionalidades e responsabilidades.

Entre as funcionalidades que o código possui, está a apresentação do  jogo, leitura do arquivo e inicialização da palavra secreta, entre  outras. Vamos então separar as responsabilidades do código em **funções**, melhorando a sua legibilidade e organização.

## Função que imprime a mensagem de apresentação do jogo

Vamos começar com a mensagem de apresentação do nosso jogo, vamos exportar o código para a função **`imprime_mensagem_abertura()`**. Não podemos nos esquecer de chamar essa função no início da função **`jogar()`**:

```
import random

def imprime_mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def jogar():

    imprime_mensagem_abertura()

    # restante do código omitido
```

Não importa o local da função, ela pode ser declarada antes ou depois da função **`jogar()`**.

## Função de leitura do arquivo e inicialização da palavra secreta

Agora, vamos separar o código que realiza a leitura do arquivo e inicializa a palavra secreta na função **`carrega_palavra_secreta()`**:

```
import random

def jogar():

    imprime_mensagem_abertura()

    carrega_palavra_secreta()

    letras_acertadas = ["_" for letra in palavra_secreta]

    # restante do código omitido

def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
```

Só que a função **`jogar()`** irá reclamar que a **`palavra_secreta`** não existe. O que queremos é que, ao executar a função **`carrega_palavra_secreta()`**, que ela **retorne** a palavra secreta para nós, assim poderemos guardá-la em uma variável:

```
import random

def jogar():

    imprime_mensagem_abertura()

    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = ["_" for letra in palavra_secreta]

    # restante do código omitido
```

## Retornando um valor em uma função

Só que como faremos a função **`carrega_palavra_secreta()`** retornar um valor, no caso a **`palavra_secreta`**?

A **`palavra_secreta`** já existe, mas só dentro da função **`carrega_palavra_secreta()`**. Para que ela seja retornada, utilizamos a palavra-chave **`return`**:

```
def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()

    return palavra_secreta
```

## Passando valores por parâmetro para a função

Agora vamos criar uma função que inicializa a lista de letras acertadas com o caractere **`_`**. Criaremos a função **`inicializa_letras_acertadas()`**:

```
import random

def jogar():

    imprime_mensagem_abertura()

    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas()

    # restante do código omitido

def inicializa_letras_acertadas():
    return ["_" for letra in palavra_secreta]
```

Mas a função **`inicializa_letras_acertadas()`** precisa ter acesso à **`palavra_secreta`**, pois ela não existe dentro da função, já que uma função define um **escopo**, e as variáveis declaradas dentro de uma função só estão disponíveis **dentro dela**.

Então, ao chamar a função **`inicializa_letras_acertadas()`**, vamos passar **`palavra_secreta`** para ela por parâmetro:

```
import random

def jogar():

    imprime_mensagem_abertura()

    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    # restante do código omitido

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]
```

Vocês podem estar se perguntando por que encapsulamos uma simples linha de  código em uma função. Fizemos isso somente para deixar claro o que  estamos fazendo, melhorando a legibilidade do código, mas precisamos  tomar cuidado com a criação de funções, pois criar funções  desnecessariamente pode aumentar a complexidade do código.

Por fim, podemos executar o nosso código, para verificar que o mesmo  continua funcionando normalmente. Lembrando que o código que verifica se o programa é o principal, deve ficar no final do arquivo:

```
import random

def jogar():

    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    # restante do código omitido

def imprime_mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))

    palavra_secreta = palavras[numero].upper()

    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

if (__name__ == "__main__"):
    jogar()
```

Tudo continua  funcionando normalmente, mas agora com o nosso código um pouco mais  legível e organizado. No próximo vídeo extrairemos mais código para mais funções.

# Criando mais funções

Vamos continuar com a refatoração do nosso código, criando funções.

## Função para pedir o chute do jogador

Criaremos a função **`pede_chute()`**, que  ficará com o código que pede o chute do usuário, remove os espaços antes e depois,  e o coloca em caixa alta. Não podemos nos esquecer de  retornar o **`chute`**:

```
import random

def jogar():

    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while (not acertou and not enforcou):

        chute = pede_chute()

    # restante do código omitido

def pede_chute():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()

    return chute
```

## Função para colocar o chute do usuário na posição correta da lista

Ainda temos o código que colocar o chute na posição correta, dentro da lista. Vamos colocá-lo dentro da função **`marca_chute_correto()`**:

```
import random

def jogar():

    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while (not acertou and not enforcou):

        chute = pede_chute()

        if (chute in palavra_secreta):
            marca_chute_correto()
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        print("Você ganhou!")
    else:
        print("Você perdeu!")

    print("Fim do jogo")

def marca_chute_correto():
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1
```

Mas a função **`marca_chute_correto()`** precisa ter acesso a três valores: **`palavra_secreta`**, **`chute`** e **`letras_acertadas`**. Então vamos passar esses valores por parâmetro:

```
import random

def jogar():

    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while (not acertou and not enforcou):

        chute = pede_chute()

        if (chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        print("Você ganhou!")
    else:
        print("Você perdeu!")

    print("Fim do jogo")

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1
```

## Função para imprimir as mensagens de vencedor e perdedor do jogo

Por fim, vamos remover a mensagem de fim de jogo e exportar os códigos que imprimem as mensagens de vencedor e perdedor do jogo:

```
import random

def jogar():

    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while (not acertou and not enforcou):

        chute = pede_chute()

        if (chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor()

    print("Fim do jogo")

def imprime_mensagem_vencedor():
    print("Você ganhou!")

def imprime_mensagem_perdedor():
    print("Você perdeu!")
```

Agora o nosso código está muito mais organizado e legível.

# Melhorando a apresentação da forca

Vamos começar com a mensagem de perdedor, alterando a função **`imprime_mensagem_perdedor`**. Ela ficará assim:

```
def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
```

Agora ela recebe a **`palavra_secreta`** por parâmetro, então não podemos esquecer de passá-la no momento que chamarmos a função:

```
def jogar():

    # restante do código omitido

    if(acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)
```

Do mesmo jeito, vamos refazer a mensagem de vencedor, na função **`imprime_mensagem_vencedor`**:

```
def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
```

## Desenhando a forca

Por fim, o jogo da forca não seria o jogo da forca se não  mostrássemos a forca, juntamente com o seu personagem. Vamos criar a  função **`desenha_forca`**, que recebe os **`erros`** por parâmetro. Para cada valor de **`erros`**, a função imprime um desenho diferente:

```
def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()
```

Para finalizar, devemos chamar essa função quando o jogador erra, dentro do **`else`** e aumentar o limite de erros para 7:

```
while (not acertou and not enforcou):

    chute = pede_chute()

    if (chute in palavra_secreta):
        marca_chute_correto(chute, letras_acertadas, palavra_secreta)
    else:
        erros += 1
        desenha_forca(erros)

    enforcou = erros == 7
    acertou = "_" not in letras_acertadas
    print(letras_acertadas)

# restante do código omitido
```

Com isso, chegamos ao final da implementação do nosso jogo da forca!

# Mãos na Massa: Exportando o código para funções

Neste capítulo, vamos organizar o nosso código para que ele fique mais fácil de manter e para que sigamos as boas práticas.

1 - Crie a função **`imprime_mensagem_abertura()`**, para imprimir a mensagem inicial do jogo:

```
def imprime_mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")
```

2 - Crie a função **`carrega_palavra_secreta()`**, que será responsável pela leitura do arquivo e inicialização da palavra secreta. Lembre-se que, como a função irá inicializar a palavra  secreta, ela deve **retorná-la**, assim teremos acesso à palavra fora da função:

```
def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()

    return palavra_secreta
```

Na hora de chamar a função, como ela retorna a palavra secreta, você pode guardá-la em uma variável!

3 - Crie a função **`inicializa_letras_acertadas()`**, que será responsável por inicializar a lista de letras acertadas com o caractere **`_`**. Como ela precisa acessar a palavra secreta, que não existe dentro da função, não esqueça de passar a palavra por parâmetro: 

```
def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]
```

4 - Agora, crie a função **`pede_chute()`**, responsável por pedir o chute do usuário e guardá-lo na variável **`chute`**. Não se esqueça de, ao final da função, retornar o chute do usuário:

```
def pede_chute():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()

    return chute
```

5 - Para o código que coloca o chute do usuário na posição correta, dentro da lista, crie a função **`marca_chute_correto()`**. Ela precisa ter acesso a três valores: **`palavra_secreta`**, **`chute`** e **`letras_acertadas`**, então passe-os por parâmetro para a função:

```
def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1
```

6 - Exporte os códigos que imprimem as mensagens de vencedor e perdedor do jogo para as funções **`imprime_mensagem_vencedor()`** e **`imprime_mensagem_perdedor()`**, respectivamente:

```
def imprime_mensagem_vencedor():
    print("Você ganhou!")

def imprime_mensagem_perdedor():
    print("Você perdeu!")
```

Por fim, chame todas essas funções dentro da função **`jogar()`**, você irá perceber que ela ficará bem mais enxuta e legível.

# Mãos na Massa: Melhorando a apresentação do jogo

Com o código mais organizado, vamos melhorar a exibição, a apresentação da forca, deixando o jogo mais amigável.

1 - Modifique a mensagem de perdedor, deixando claro que o usuário  perdeu e imprimindo a palavra secreta. Para exibir a palavra secreta, a  função **`imprime_mensagem_perdedor()`**, que não possui acesso à palavra, precisa recebê-la por parâmetro:

```
def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
```

Então, ao chamar a função **`imprime_mensagem_perdedor()`**, não esqueça de passar a palavra secreta por parâmetro.

2 - Faça a mesma coisa para a mensagem de vencedor, deixando-a mais apresentável:

```
def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
```

3 - Por fim, crie a função **`desenha_forca()`**, que irá desenhar uma parte da forca, baseado nos erros do usuário. Como ela precisa acessar os erros, passe-o por parâmetro para a função:

```
def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()
```

4 - Para finalizar, chame a função **`desenha_forca`** quando o jogador errar e aumente o limite de erros para 7.

# Para saber mais: Parâmetros opcionais e nomeados

## Parâmetros opcionais

Já sabemos como definir e agrupar comportamentos dentro de funções. E que uma função pode ter retorno e receber ou não parâmetros. Praticamos bastante essas sintaxes nesse capítulo mas até agora não tínhamos  nenhuma novidade em relação a outras linguagens de programação.

Acontece que o Python possui algumas facilidades que não estão presentes em todas as outras linguagens.

Ficou curioso? Aposto que sim! Python é uma linguagem viciante!

Relembre o começo da  função `carrega_palavra_secreta`  desenvolvida no nosso projeto:

```
def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()

    return palavra_secreta
```

Essa função como o próprio nome diz carrega uma palavra secreta das contidas em um arquivo chamado de `palavras.txt`.

E se quiséssemos deixar essa função um pouco mais flexível permitindo que fosse passado o nome do arquivo usado para o carregamento? Permitindo assim as seguintes chamadas:

```
carrega_palavra_secreta("frutas.txt")
carrega_palavra_secreta("nomes.txt")
```

Para que a chamada funcione basta declararmos que a função recebe um  parâmetro com o nome do arquivo, além usá-lo no carregamento. Como a  seguir:

```
def carrega_palavra_secreta(nome_arquivo):
    arquivo = open(nome_arquivo, "r")
   ...
```

E se essa função já estivesse sendo chamada em outros lugares sem o parâmetro:

```
palavra_secreta = carrega_palavra_secreta()
```

O código anterior deixaria de funcionar, já que houve uma obrigatoriedade de passarmos um nome de arquivo na definição da função. Se fosse necessário manter  as duas chamadas válidas:

```
carrega_palavra_secreta("frutas.txt")
carrega_palavra_secreta()
```

Poderíamos definir que o parâmetro é opcional, ou seja, podemos ou não querer passar o nome do arquivo.

Para isso precisamos definir um nome de arquivo que seria o padrão usado quando não fosse especificado algum arquivo.

Esse arquivo padrão vai ser o `palavras.txt` usado anteriormente.  O nosso código ficaria como a seguir:

```
def carrega_palavra_secreta(nome_arquivo="palavras.txt"):
    arquivo = open(nome_arquivo, "r")
   ...
```

Logo quando temos:

```
carrega_palavra_secreta()
```

O arquivo carregado será o `palavras.txt`. Por outro lado quando o parâmetro é especificado como em:

```
carrega_palavra_secreta("frutas.txt")
```

O arquivo carregado será o passado: `frutas.txt`.

Isso só é possível porque no Python temos como definir um valor padrão para os parâmetros  e assim permitindo os **`parâmetros opcionais`**.

## Parâmetros nomeados

Analisando a função completa podemos ver que o número gerado é sempre de `0` até o número de palavras do arquivo.

```
def carrega_palavra_secreta(nome_arquivo="palavras.txt"):
    arquivo = open(nome_arquivo, "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()

    return palavra_secreta
```

E se quiséssemos permitir a definição **de a** partir de qual linha deveria ser gerado o número? Uma mudança poderia ser feita na função de modo que ela recebesse essa indicação:

```
def carrega_palavra_secreta(primeira_linha_valida, nome_arquivo="palavras.txt"):
    arquivo = open(nome_arquivo, "r")
    palavras = []

    ….

    numero = random.randrange(primeira_linha_valida, len(palavras))
    palavra_secreta = palavras[numero].upper()

    return palavra_secreta
```

Poderíamos inclusive definir o valor padrão do parâmetro como sendo zero:

```
def carrega_palavra_secreta(nome_arquivo="palavras.txt", primeira_linha_valida=0):
    arquivo = open(nome_arquivo, "r")
    palavras = []

    ….

    numero = random.randrange(primeira_linha_valida, len(palavras))
    palavra_secreta = palavras[numero].upper()

    return palavra_secreta
```

As seguintes utilizações da função são válidas  e não geram erros na execução:

```
carrega_palavra_secreta()
carrega_palavra_secreta("frutas.txt")
```

Onde na primeira chamada temos a utilização do valor padrão nos dois parâmetros, ou seja, usa-se o arquivo `palavras.txt` e a primeira linha válida como sendo `0`.

A segunda chamada já temos a utilização do arquivo `frutas.txt` e a primeira linha válida como sendo a `0`. 

Para deixar mais claro que o valor passado refere-se ao nome do  arquivo e não a primeira linha válida, podíamos inclusive repetir o nome do parâmetro na própria chamada:

```
carrega_palavra_secreta(nome_arquivo="frutas.txt")
```

Esse recurso é possível pois no Python podemos nomear os parâmetros passados.

É importante saber que não é obrigatório para o correto funcionamento do código pois quando temos mais de um parâmetro opcional na definição  da função, a chamada omitindo algum deles vai usar sempre a ordem de  definição.

Em outras palavras, fazendo:

```
carrega_palavra_secreta(5)
```

Ao contrário do que possa parecer ele não define o parâmetro `primeira_linha_valida` como `5` e sim o `nome_arquivo` como sendo `5`, o que é péssimo para o correto funcionamento da função.  Logo, aqui percebe-se uma necessidade real da utilização do recurso de  nomeação dos parâmetros. Ficando correta tanto na sintaxe quando na  execução a seguinte chamada:

```
carrega_palavra_secreta(primeira_linha_valida=5)
```

Já na seguinte abordagem:

```
carrega_palavra_secreta("frutas.txt", 5)
```

Temos a utilização do arquivo `frutas.txt` e a primeira linha válida como sendo a quinta.

Poderíamos inclusive nomeá-los:

```
carrega_palavra_secreta(nome_arquivo="frutas.txt", primeira_linha_valida= 5)
```

E até mesmo trocar a ordem, já que estão nomeados:

```
carrega_palavra_secreta(primeira_linha_valida=5, nome_arquivo="frutas.txt")
```

Parâmetros opcionais e nomeados são recursos bastante poderosos para um código  mais flexível e legível. Nem todas as linguagens possuem isso, aproveite o seu Python!
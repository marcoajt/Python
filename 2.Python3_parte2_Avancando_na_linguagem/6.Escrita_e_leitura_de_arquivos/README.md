# Escrevendo em um arquivo

Uma funcionalidade que ainda nos atrapalha no nosso jogo é a palavra secreta, que atualmente está **fixa**. Se queremos que a palavra seja diferente, devemos modificá-la no código.

A nossa ideia é ler palavras de um arquivo de texto, e dentre elas  escolhemos uma palavra aleatoriamente, que será a palavra secreta do  jogo

## Escrita de um arquivo

Para **abrir um arquivo**, o Python possui a função *built-in* **`open`**. Ela recebe dois parâmetros: o primeiro é o nome do arquivo a ser  aberto, e o segundo parâmetro é o modo que queremos trabalhar com esse  arquivo, se queremos **ler** ou **escrever**. O modo é passado através de uma string: **`"w"`** para **escrita** e **`"r"`** para **leitura**.

No nosso jogo, faremos a leitura de um arquivo, mas vamos ver antes no terminal do Python 3 como funciona a escrita:

```
>>> arquivo = open("palavras.txt", "w")
```

Vale lembrar que o **`w` sobrescreve o arquivo**, se o mesmo existir. Se só quisermos **adicionar conteúdo** ao arquivo, utilizamos o **`a`**.

Agora que temos o arquivo, como escrevemos nele? Basta chamar no arquivo a função **`write`**, passando para ela o que queremos escrever no arquivo:

```
>>> arquivo.write("banana")
6
>>> arquivo.write("melancia")
8
```

O retorno dessa função é o número de caracteres que adicionamos no arquivo.

## Fechando um arquivo

Quando estamos trabalhando com arquivos, devemos nos preocupar em  fechá-lo. Assim como abrimos um arquivo, devemos fechá-los, chamando a  função **`close`**:

```
>>> arquivo.close()
```

Após isso, podemos verificar o conteúdo do arquivo, ele foi criado na mesma  pasta em que o comando para a abrir o console do Python 3 foi executado. Ao verificar o seu conteúdo, vemos:

```
bananamelancia
```

As palavras foram escritas em uma mesma linha. Mas como escrever em uma nova linha?

## Escrevendo palavras em novas linhas

A primeira coisa que devemos fazer é abrir o arquivo novamente, dessa vez utilizando o **`a`**, de ***append\***:

```
>>> arquivo = open("palavras.txt", "a")
```

Podemos escrever novamente no arquivo, mas dessa vez com a preocupação de criar uma nova linha após o que vamos escrever. Para representar uma nova  linha em código, adicionamos o **`\n`** ao final do que queremos escrever:

```
>>> arquivo.write("morango\n")
8
>>> arquivo.write("manga\n")
6
```

Ao fechar o arquivo e verificar novamente o seu conteúdo, vemos:

```
bananamelanciamorango
manga
```

A palavra **morango** ainda ficou na mesma linha, mas como especificamos na sua adição que após a palavra deverá ter uma quebra de linha, a palavra **manga** foi adicionada abaixo, em uma nova linha.

Por fim, vamos mover esse arquivo para dentro do nosso projeto, e  ajeitar as suas palavras, quebrando as linhas. Ele ficará assim:

```
banana
melancia
morango
manga
```

# Os modificadores de acesso

Além do `r`, `w` e `a` existe o modificador `b` que devemos utilizar quando queremos trabalhar no modo binário. Para abrir uma imagem devemos usar:

```
imagem = open("foto.jpg", "rb")
```

Por exemplo, o código abaixo cria uma cópia de uma imagem:

```
#arquivo copia.py
logo = open('python-logo.png', 'rb')
data = logo.read()
logo.close()

logo2 = open('python-logo2.png', 'wb')
logo2.write(data)
logo2.close()
```

# Lendo um arquivo

Ainda no terminal do Python 3, vamos ver o funcionamento da **leitura de um arquivo**. Como agora o arquivo **palavras.txt** está na pasta do projeto **jogos**, devemos executar o comando que abre o terminal do Python 3 na pasta do projeto.

## Leitura de um arquivo

Vamos então abrir o arquivo no modo de leitura, basta passar o nome do arquivo e a letra **`r`** para a função **`open`**, como já vimos no vídeo anterior:

```
>>> arquivo = open("palavras.txt", "r")
```

Como abrimos o arquivo no modo de leitura, a função `write` não funciona. Para **ler o arquivo inteiro**, utilizamos a função **`read`**:

```
>>> arquivo.read()
'banana\nmelancia\nmorango\nmanga\n'
```

Mas se executarmos a função novamente:

```
>>> arquivo.read()
''
```

Nos é retornado uma string vazia. Por quê?

O arquivo é como um fluxo de linhas, que começa no início do arquivo, como se fosse o ponteiro. Ele vai descendo e lendo arquivo, após ler  tudo, ele fica posicionado no final do arquivo, então quando chamamos a  função **`read()`** novamente, não há mais conteúdo, pois ele todo já foi lido.

Ou seja, para ler o arquivo novamente, devemos fechá-lo e abri-lo novamente.

## Lendo linha por linha do arquivo

Mas não queremos ler todo o conteúdo do arquivo, e sim ler linha por  linha. Como já foi visto, um arquivo é um fluxo de linhas, uma sequência de linhas, então como é uma sequência, podemos fazer um **`for`** nela:

```
>>> arquivo = open("palavras.txt", "r")
>>> for linha in arquivo:
...     print(linha)
... 
banana

melancia

morango

manga
```

Mas podemos reparar que existe uma linha  entre cada fruta. Por que isso acontece? Para ver melhor, vamos ler  somente uma linha do arquivo, com a função **`readLine()`**:

```
>>> arquivo = open("palavras.txt", "r")
>>> linha = arquivo.readline()
>>> linha
'banana\n'
```

Há um **`\n`** ao final da linha, porque a linha sabe que ao seu final deve ser ser feita uma nova linha. Mas anteriormente havíamos feito um **`print`**, que também quebra uma linha ao final da impressão, colocando também um **`\n`**! Assim, são criadas duas novas linhas, por isso havia uma linha em branco entre as frutas.

## Limpando a linha

Como vimos, há um **`\n`** ao final de cada  linha, de cada palavra, mas queremos somente a palavra. Já vimos como  tirar espaços em branco no início e no fim da string, basta utilizar a  função **`strip()`**, que também remove caracteres especiais, como o **`\n`**.

Sabendo disso tudo, podemos implementar a funcionalidade de leitura de arquivo no nosso jogo. Faremos isso no próximo vídeo.

# Escolhendo uma palavra

Agora que já sabemos ler de um arquivo, podemos implementar a  funcionalidade de escolher aleatoriamente a palavra secreta de um  arquivo.

## Lendo e guardando as linhas do arquivo

A primeira coisa que devemos fazer é abrir o arquivo, e como já sabemos, vamos fechá-lo:

```
def jogar():

    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    arquivo = open("palavras.txt", "r")



    arquivo.close()
```

Agora, vamos criar uma lista e fazer um laço, acessando cada linha e guardando-as nessa lista:

```
def jogar():

    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        palavras.append(linha)

    arquivo.close()
```

Mas precisamos remover o **`\n`** ao final da linha, fazendo um **`strip`** nela:

```
def jogar():

    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()
```

Agora já temos todas as palavras na lista, mas como selecionar uma delas aleatoriamente?

## Gerando um número aleatório

Sabemos que cada elemento da lista possui uma posição, e vimos no  treinamento anterior como gerar um número aleatório, vamos relembrar?

A biblioteca que sabe gerar um número aleatório é a **`random`**. Vamos testá-la no terminal do Python 3, primeiro importando-a:

```
>>> import random
```

Para gerar o número aleatório, utilizamos a biblioteca e chamamos a função **`randrange`**, que recebe o intervalo de valores que o número aleatório deve estar. Então vamos passar o valor **0** (equivalente à primeira posição da nossa lista) e **4** (lembrando que o número é exclusivo, ou seja, o número aleatório será  entre 0 e 3, equivalente à última posição da nossa lista):

```
>>> import random
>>> random.randrange(0, 4)
0
>>> random.randrange(0, 4)
1
>>> random.randrange(0, 4)
3
>>> random.randrange(0, 4)
1
>>> random.randrange(0, 4)
3
```

Sabendo disso, vamos implementar esse código no nosso jogo.

## Selecionando a palavra

Primeiramente, devemos importar a biblioteca. Vamos gerar um número de **0** até a quantidade de palavras da nossa lista, ou seja, vamos utilizar a função **`len`**, para saber o tamanho da lista:

```
import random

def jogar():

    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
```

Agora que temos o número aleatório, vamos utilizá-lo como índice para acessar a lista e atribuir essa palavra à variável **`palavra_secreta`**:

```
import random

def jogar():

    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))

    palavra_secreta = palavras[numero].upper()
    letras_acertadas = ["_" for letra in palavra_secreta]
```

Podemos executar o jogo agora, e perceber que a palavra é selecionada aleatoriamente!

Mas agora o nosso arquivo, a nossa função cresceu bastante, com  várias funcionalidades e responsabilidades. Então, no próximo capítulo,  organizaremos melhor o nosso código, separando-o em funções e deixando-o mais fácil de entender.

solução para a palavra maça, que não era reconhecida.

```
arquivo = open("palavras.txt", "r", encoding="UTF-8")
```

# Para saber mais: with

Já falamos da importância de fechar o arquivo, certo? Veja o código abaixo que justamente usa a função `close` :

```
logo = open('palavras.txt', 'r')
data = logo.read()
logo.close()
```

Agora imagine que dê algum problema na hora da leitura quando chamarmos a função `read()`. Será que mesmo com erro o arquivo será fechado? 

Se for algum erro grave, o programa pode parar a execução sem ter fechado o arquivo! Isso seria muito ruim ...

Para evitar esse tipo de situação, o Python criou uma sintaxe especial para abertura de arquivo. Veja só: 

```
with open("palavras.txt") as arquivo:
    for linha in arquivo:
        print(linha)
```

Repare que o `with` usa a função `open`. Repare também que não fechamos o arquivo. Isso não é mais necessário  pois o Python vai cuidar disso e, mesmo com erro, garantirá o fechamento do arquivo! Muito melhor não?

# Mãos na massa: Palavras aleatórias no jogo

Agora que já sabemos ler  um arquivo, podemos implementar a  funcionalidade de escolher aleatoriamente a palavra secreta de um  arquivo.

1 - De início devemos abrir o arquivo, e como já sabemos é uma boa prática fechá-lo ao final:

```
def jogar():

    arquivo = open("palavras.txt", "r")

    arquivo.close()
```

2 - Depois temos que criar uma lista e percorrer o arquivo. Cada linha do arquivo deve ser guardada nessa lista:

```
def jogar():

    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        palavras.append(linha)

    arquivo.close()
```

3 - Precisamos remover o **`\n`** ao final da linha, fazendo um **`strip`** nela:

```
def jogar():

    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()
```

4 - Agora  que já temos todas as palavras na lista devemos acessá-las aleatoriamente. Para isso, vamos importar a biblioteca  **`random`**?

```
import random
```

5 - Com a biblioteca já disponível temos que acessar uma das palavras  incluídas na nossa lista. Para isso será necessário gerar um número com a posição aleatória. O  número gerado deveria ser apenas de índices válidos na lista: 0 até o  tamanho da lista:

```
    numero = random.randrange(0, len(palavras))
```

6 -  Com o número gerado basta agora pegarmos a palavra secreta correspondente a essa posição:

```
    numero = random.randrange(0, len(palavras))

    palavra_secreta = palavras[numero].upper()
```
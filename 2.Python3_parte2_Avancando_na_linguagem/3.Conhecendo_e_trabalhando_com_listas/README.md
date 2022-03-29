# Estrutura de dados: List

Atualmente, já dizemos ao usuário em que posição a letra que ele  chutou está na palavra secreta, caso a letra exista na palavra. Mas em  um jogo real de forca, o jogador vê quantas letras há na palavra  secreta. Algo como:

```
Qual letra? _ _ _ _ _ _
```

E se ele encontrar alguma letra, a mesma tem a sua lacuna preenchida. Ao digitar a letra **"a"**, ficaria:

```
_ a _ a _ a
```

Muito mais intuitivo, não? Vamos implementar essa funcionalidade.

## Conhecendo uma nova estrutura de dados: lista

Para exibir as letras dessa forma, precisamos guardar os chutes certos do usuário, mas como fazer isso?

Para tal, o Python nos oferece uma estrutura de dados que nos permite guardar valores. Essa estrutura é a **lista**. Para criar uma lista, utilizamos colchetes (**`[]`**):

```
>>> valores = []
>>> type(valores)
<class 'list'>
```

Assim como a string, **`list`** também é uma sequência de dados. Então podemos ver a sua [documentação](https://docs.python.org/3.6/library/stdtypes.html#sequence-types-list-tuple-range). Nela, podemos ver o que podemos fazer com uma lista, podemos verificar o seu valor mínimo com o **`min`** e o seu valor máximo com o **`max`**. Mas a nossa lista ainda tá vazia, certo? Podemos, já no momento de sua inicialização, passar valores para guardar nessa lista:

```
>>> valores = [0,1,2,3,4]
```

Agora podemos verificar seu menor e seu maior valor:

```
>>> valores = [0,1,2,3,4]
>>> min(valores)
0
>>> max(valores)
4
```

Para acessar um valor específico, podemos acessá-lo através do seu **índice**. O primeiro elemento da lista possui o índice **0**, o segundo possui o índice **1** e assim por diante:

```
>>> valores = [0,1,2,3,4]
>>> valores[2]
2
```

Podemos também saber o tamanho da lista com o **`len`** e verificar se determinado valor está guardado nela:

```
>>> valores = [0,1,2,3,4]
>>> 0 in valores
True
>>> 8 in valores
False
```

Além disso, existem funções específicas da lista, que podem ser vistas [aqui](https://docs.python.org/3.6/library/stdtypes.html#mutable-sequence-types). Podemos adicionar elementos ao final da lista com o **`append`**, exibir e remover um elemento de determinada posição com o **`pop`**, entre diversas outras funcionalidades.

Agora que sabemos como guardar valores em uma lista, podemos voltar  ao nosso jogo e guardar os acertos do usuário. Faremos isso no próximo  vídeo :)

# Guardando as letras acertadas

Agora que já conhecemos um pouco como a lista funciona, chegou a hora de utilizá-la no nosso jogo. Existem diversas formas de implementar  essa funcionalidade, mas aqui faremos da seguinte forma: como queremos  exibir os espaços vazios primeiro, criaremos uma lista com eles, na  mesma quantidade de letras da palavra secreta:

```
palavra_secreta = "banana"
letras_acertadas = ["_", "_", "_", "_", "_", "_"]
```

Atualmente isso tudo está fixo, caso queiramos mudar a palavra secreta, teremos  que mudar os espaços vazios. Mas não se preocupe, tornaremos isso  dinâmico mais à frente.

## Adicionando as letras acertadas à lista

Já temos a posição da letra, que chamamos de **`index`**. Logo, caso o chute seja correto, basta guardar e letra dentro da lista, na sua posição correta:

```
while (not acertou and not enforcou):

    chute = input("Qual letra? ")
    chute = chute.strip()

    index = 0
    for letra in palavra_secreta:
        if (chute.upper() == letra.upper()):
            letras_acertadas[index] = letra
        index = index + 1

    print("Jogando...")
```

E após adicionar a letra, após o **`for`**, imprimimos a nossa lista:

```
while (not acertou and not enforcou):

    chute = input("Qual letra? ")
    chute = chute.strip()

    index = 0
    for letra in palavra_secreta:
        if (chute.upper() == letra.upper()):
            letras_acertadas[index] = letra
        index = index + 1

    print(letras_acertadas)
```

Podemos executar o jogo, ao acertar uma letra, a palavra é exibida com a mesma preenchida:

```
*********************************
***Bem vindo ao jogo da Forca!***
*********************************
Qual letra? b
['b', '_', '_', '_', '_', '_']
Qual letra? a
['b', 'a', '_', 'a', '_', 'a']
```

A saída ainda não está visualmente agradável, mas melhoraremos isso. Para ficar ainda melhor, vamos exibir a lista no início do jogo também:

```
print(letras_acertadas)

while (not acertou and not enforcou):

    chute = input("Qual letra? ")
    chute = chute.strip()

    index = 0
    for letra in palavra_secreta:
        if (chute.upper() == letra.upper()):
            letras_acertadas[index] = letra
        index = index + 1

    print(letras_acertadas)
```

Com isso, avançamos mais ainda na implementação do nosso jogo!

Vamos aproveitar o nosso novo conhecimento em listas para fazer com  que a nossa forca se lembre das letras acertadas pelo nosso jogador.

1-  De início crie uma nova lista chamada `letras_acertadas` abaixo da variável `palavra_secreta`. Aproveite e inicie esta lista com 6 elementos do caractere **"_"**, para representar uma letra faltando. Por enquanto estamos fazendo com  um número fixo de letras, mas em breve melhoraremos isto também.

```
letras_acertadas = ["_", "_", "_", "_", "_", "_"]
```

2- Já sabemos quando um usuário acerta uma letra, afinal fazemos isto no **if** que já temos:

```
if(chute.upper() == letra.upper()):
    print("Encontrei a letra {} na posição {}".format(chute, index))
```

Mas agora, em vez de apenas imprimirmos uma mensagem ao acertar, vamos  substituir no nosso array de letras faltando. Como já temos o índice da  letra, basta substituir naquela posição do array pela letra que  acertamos:

```
if (chute.upper() == letra.upper()):
    letras_acertadas[index] = letra
```

3- Para que o jogador acompanhe o resultado a cada chute que ele der, após o laço **for** imprima também a lista de `letras_acertadas` para que ele veja como ele está indo no jogo:

```
for letra in palavra_secreta:
    ...
    ...
print(letras_acertadas)
```

4- E claro, para dar uma dica  ao nosso jogador de quantas letras a palavra tem, vamos colocar acima do **while** um **print** inicial para que ele veja de início qual o tamanho da palavra:

```
print(letras_acertadas)

while (not acertou and not enforcou):
...
```

Faça o teste e veja na resposta se seu código está batendo com o do instrutor.

# Para Saber Mais: Outros recursos com a lista

Além das funções **min()**, **max()** e **len()** que vimos neste capítulo, as listas do Python tem outros recursos que facilitam nossa vida. Vamos conhecer alguns deles:

## A função .count()

Um jeito fácil de contar o número de ocorrências de um determinado elemento em uma lista é a função `.count()` das listas, veja:

```
valores = [ 0, 0, 0, 1, 2, 3, 4]
print(valores.count(0))
```

O código acima nos retorna **3**, pois em nossa lista encontramos 3 vezes o número zero nela.

Utilizando a função `.count()` podemos por exemplo, detectar quantas letras ainda faltam para o nosso usuário preencher:

```
letras_acertadas = ['_','_','_','_','_','_']
letras_faltando = str(letras_acertadas.count('_'))
print( 'Ainda faltam acertar {} letras'.format(letras_faltando))
```

## A função .index()

Uma outra função que pode ser bastante útil é a função `.index()`, que nos retorna o **índice** da primeira ocorrência de um determinado elemento em uma lista, veja:

```
frutas = ['Banana', 'Morango', 'Maçã', 'Uva', 'Maçã', 'Uva']
print(frutas.index('Uva'))
```

O código acima nos retorna **3**, pois é o índice da primeira ocorrência do elemento 'Uva' na lista  frutas (lembre-se nas listas começamos a contar do índice 0).

Só tome cuidado quando utilizar a função `.index()`, pois a mesma pode retornar um erro caso você tente buscar pelo índice de um elemento que não existe. Veja o caso abaixo:

```
frutas = ['Banana', 'Morango', 'Maçã', 'Uva']
print(frutas.index('Melancia'))
```

Ao tentar buscar pela fruta 'Melancia', obteremos o erro `"ValueError: 'Melancia' is not in list"` no console, já que é impossível buscar o índice de algo que não está na lista. Por isto, é sempre uma boa prática **verificar** se o elemento está na lista com o operador **in** antes de obter o seu índice. Um código ideal que faz uso da função `index()` é demonstrado abaixo:

```
frutas = ['Banana', 'Morango', 'Maçã', 'Uva']

fruta_buscada = 'Melancia'
if fruta_buscada in frutas:
    print(frutas.index(fruta_buscada))
else:
    print('Desculpe, a {} não está na lista frutas'.format( fruta_buscada))
```

Assim temos certeza que a `fruta_buscada` está dentro da lista antes de perguntarmos o seu índice, evitando assim de receber um erro no console.
### **O laço com for**

Voltando ao código do nosso jogo de adivinhação, implementamos o loop **`while`**, no qual temos uma variável **`rodada`** que começa com o valor 1, e é incrementada dentro do loop, que por sua vez tem uma condição de entrada, que é a **`rodada`** ser menor ou igual ao total de tentativas, que é 3.

Ou seja, a **`rodada`** tem um valor inicial, que é 1, e vai até 3. Fazemos um laço começando com um valor inicial, até um valor final, sempre incrementando esse valor a cada iteração.

Em casos como esse, existe um outro loop que simplifica essa ideia de começar com um valor, e incrementá-lo até chegar em um valor final, o loop **`for`**.

## Entendendo o for

Para entender o loop **`for`**, podemos ir até o console do Python para ver o seu funcionamento. A ideia é nós definirmos o valor inicial e o valor final, que o loop o incrementa automaticamente. Para definir o valor inicial e final, utilizamos a função **`range`**, passando-os por parâmetro, definindo assim a série de valores. A sintaxe é a seguinte

```
>>> para variável em série de valores:
...     faça algo
```

Isso, em Python, pode ficar assim:

```
>>> for rodada in range(1,10):
...
```

Na primeira iteração, o valor da variável **`rodada`** será 1, depois 2 e até chegar ao **valor final da função `range` menos 1**, isto é, o segundo parâmetro da função não é inclusivo. No exemplo acima, a série de valores é de 1 a 9. Podemos confirmar isso imprimindo o valor da variável **`rodada`**:

```
>>> for rodada in range(1,10):
...     print(rodada)
... 
1
2
3
4
5
6
7
8
9
```

Com a função **`range`**, podemos definir um *step*, que é o intervalo entre os elementos, por padrão o *step* é 1. Definimos-o passando um terceiro parâmetro para a função:

```
>>> for rodada in range(1,10,2):
...     print(rodada)
... 
1
3
5
7
9
```

Mas não necessariamente precisamos usar a função **`range`** no **`for`**, podemos passar os valor manualmente:

```
>>> for rodada in [1,2,3,4,5]:
...     print(rodada)
... 
1
2
3
4
5
```

O resultado é o mesmo, mas o código fica mais verboso.

## Utilizando o for no jogo

Voltando ao nosso jogo, não vamos mais utilizar o **`while`, e sim o** `for`**, começando no 1 e indo até o total de tentativas. Para isso precisamos remover a declaração da variável** `rodada`* e o seu incremento dentro do loop:

```
numero_secreto = 42
total_de_tentativas = 3

for rodada in range(1, total_de_tentativas):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute_str = input("Digite o seu número: ")
    print("Você digitou: ", chute_str)
    chute = int(chute_str)

    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Você acertou!")
    else:
        if (maior):
            print("Você errou! O seu chute foi maior que o número secreto.")
        elif (menor):
            print("Você errou! O seu chute foi menor que o número secreto.")

print("Fim do jogo")
```

É importante saber que **o `for` não deve ter parênteses**.

Podemos testar e ver que só fizemos 2 tentativas. Isso porque, como foi falado anteriormente, o segundo parâmetro da função **`range` não é inclusivo**, no caso do nosso jogo, **`range(1,3)** irá gerar a série 1 e 2 somente. Logo vamos somar 1 ao total de tentativas dentro da função **`range`**:

```
numero_secreto = 42
total_de_tentativas = 3

for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute_str = input("Digite o seu número: ")
    print("Você digitou: ", chute_str)
    chute = int(chute_str)

    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Você acertou!")
    else:
        if (maior):
            print("Você errou! O seu chute foi maior que o número secreto.")
        elif (menor):
            print("Você errou! O seu chute foi menor que o número secreto.")

print("Fim do jogo")
```

Agora podemos testar novamente o nosso jogo, e ver que tudo está funcionando perfeitamente!

### **Encerrando a interação e o loop**

No nosso jogo, sabemos que o número secreto é fixo e definido com o valor 42, por enquanto. Vamos jogar e digitar esse valor de primeira:

```
*********************************
Bem vindo ao jogo de Adivinhação!
*********************************
Tentativa 1 de 3
Digite o seu número: 42
Você digitou:  42
Você acertou!
Tentativa 2 de 3
Digite o seu número:
```

Acertamos o número, mas ainda temos uma segunda e terceira tentativas! Não faz muito sentido isso né? Se nós ganhamos, temos que parar as rodadas, não devemos continuar.

## Parando o laço

Dentro do **`if`**, se acertarmos, devemos parar e sair do laço. Para isso existe um comando do Python, assim como outras linguagens, o **`break`**, que faz com que saiamos do laço:

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

Podemos agora jogar novamente e...:

```
*********************************
Bem vindo ao jogo de Adivinhação!
*********************************
Tentativa 1 de 3
Digite o seu número: 42
Você digitou:  42
Você acertou!
Fim do jogo
```

Ótimo! Acertamos o número e o jogo foi encerrado, sem mais rodadas.

## Limitando o número a ser digitado

Vamos limitar o número que o usuário deve digitar, de 1 a 100. Vamos deixar isso claro para ele alterando a mensagem do **`input`**:

```
for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute_str = input("Digite um número entre 1 e 100: ")
    print("Você digitou: ", chute_str)
    chute = int(chute_str)

    ## resto do código comentado
```

Só que agora não devemos aceitar valores fora desse limite, logo vamos verificar o número digitado, e se ele for menor que 1 **OU** (em Python, a palavra chave **`or`**) maior que 100, vamos exibir uma mensagem para o usuário:

```
for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute_str = input("Digite um número entre 1 e 100: ")
    print("Você digitou: ", chute_str)
    chute = int(chute_str)

    if (chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100!")

## resto do código comentado
```

Mas não faz sentido continuarmos executando o código do loop se o valor não estiver no intervalo exigido. O que queremos não é sair do laço, e sim continuar para a próxima rodada, **acabando com a iteração**. Para isso existe a palavra chave **`continue`**:

```
for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute_str = input("Digite um número entre 1 e 100: ")
    print("Você digitou: ", chute_str)
    chute = int(chute_str)

    if (chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100!")
        continue

## resto do código comentado
```

Esse comando faz com que a iteração do laço acabe, e comece a próxima. Vamos testar:

```
*********************************
Bem vindo ao jogo de Adivinhação!
*********************************
Tentativa 1 de 3
Digite um número entre 1 e 100: 0
Você digitou:  0
Você deve digitar um número entre 1 e 100!
Tentativa 2 de 3
Digite um número entre 1 e 100:
```

Perfeito! O número digitado era incorreto, então fomos para a próxima tentativa.

Então vimos aqui o **`break`**, que acaba, encerra o laço; e o **`continue`**, que acaba, encerra a iteração, continuando para a próxima.





### Para saber mais: Formatação de strings

Segue o link da documentação que mencionei no video, nele tem vários exemplos de formatação:

https://docs.python.org/3/library/string.html#formatexamples

Nesse vídeo veremos um pouco mais sobre interpolação de strings. Para isso, vamos utilizar o console do Python 3.

No capítulo anterior, fizemos uma interpolação semelhante a essa:

```
>>> print("Tentativa {} de {}".format(1, 3))
```

Essa interpolação é útil para formatação de strings, quando temos um texto  muito grande e precisamos inserir valores no meio dele, ao invés de  ficarmos concatenando, trabalhando com várias strings separadas.

Mas a função **`format`** tem outras  utilidades, então veremos mais alguns detalhes sobre essa função. O  primeiro detalhe que veremos é que os parâmetros podem ser invertidos na string. Podemos dizer que queremos nas primeiras chaves o segundo  parâmetro da função, e o primeiro parâmetro nas segundas chaves.

Fazemos isso passando o **índice do parâmetro** dentro das chaves. O primeiro parâmetro tem índice **0**, o segundo **1**, e daí por diante. Logo, basta passar o índice 1 nas primeiras chaves e o 0 nas segundas chaves:

```
>>> print("Tentativa {1} de {0}".format(1, 3))
Tentativa 3 de 1
```

## Formatação de floats

Agora vamos trocar o exemplo, e formatar um valor em reais, por exemplo:

```
>>> print("R$ {}".format(1.59))
R$ 1.59
```

Só que um valor pode ter vários tamanhos e até duas casas decimais, por exemplo:

```
1.59
45.9
1234.97
```

O ideal é que esses valores sempre tenham a mesma formatação:

```
   1.59
  45.9
1234.97
```

Então precisamos preencher as lacunas, os espaços em branco. E a função **`format`** faz isso para nós. Primeiro precisamos dizer para ela que estamos recebendo um valor do tipo **float**, passando **`:f`** dentro das chaves da string:

```
>>> print("R$ {:f}".format(1.59))
R$ 1.590000
```

Podemos  reparar que só de dizer que estamos passando um float, a formatação já  muda, mas podemos manipulá-la, modificá-la, dizendo quantos números  devem vir antes e depois do ponto. Queremos que após o ponto tenha  apenas 2 números, logo:

```
>>> print("R$ {:.2f}".format(1.59))
R$ 1.59
```

Podemos testar passando um número de apenas uma casa decimal:

```
>>> print("R$ {:.2f}".format(1.5))
R$ 1.50
```

Ótimo, agora vamos testar com um número maior:

```
>>> print("R$ {:.2f}".format(1.5))
R$ 1.50
>>> print("R$ {:.2f}".format(1234.50))
R$ 1234.50
```

Mas queremos  que o ponto fique sempre no mesmo local, ou seja, ele deve ser o quinto  caractere. Para essa formatação, precisamos dizer quantos caracteres o  número terá no máximo, no nosso caso são 7 (4 números, mais o ponto,  mais as duas casas decimais). Então vamos passar o valor 7 dentro das  chaves também:

```
>>> print("R$ {:7.2f}".format(1234.50))
R$ 1234.50
>>> print("R$ {:7.2f}".format(1.5))
R$    1.50
```

Ou seja, dos 7 caracteres, os três últimos serão o ponto mais dois números das casas decimais.

Agora espaços ficam na frente quando um número for menor! Deixando o  ponto sempre como quinto caractere. Se quisermos preencher os espaços em branco com zeros, é só passar um 0 antes do 7:

```
>>> print("R$ {:07.2f}".format(1.5))
R$ 0001.50
```

## Formatação de inteiros

Conseguimos formatar números inteiros também, não só números flutuantes. Para números inteiros, passamos a letra **`d`**:

```
>>> print("R$ {:07d}".format(4))
R$ 0000004
```

Podemos usar isso para formatar uma data:

```
>>> print("Data {:02d}/{:02d}".format(9, 4))
Data 09/04
>>> print("Data {:02d}/{:02d}".format(19, 11))
Data 19/11
```

Não se preocupe em decorar a sintaxe, o importante é saber que no Python  existe a funcionalidade de interpolação de strings, e quando vocês  realmente precisarem usar isso, olhem na [documentação](https://docs.python.org/3/library/string.html#formatexamples).



### Interpolação - Python 2 vs Python 3

A interpolação de strings também mudou entre o Python 2 e o Python 3. 

Como você já viu, no Python 3 usa-se a função `format` junto com a sintaxe `{}` dentro da string, por exemplo:

```
"{} {}".format(1, 2)
```

O Python 2 usava uma sintaxe especial, ao invés do `format` era preciso usar o caractere `%`. Veja o exemplo:

```
"%d %d" % (1, 2)
```

Repare também que o `%` também era utilizado dentro da string.

Mais exemplos, sempre comparando o Python 2 com Python 3, existem no link: https://pyformat.info/

Vale a pena ver!

## No Python 3.6+

A partir da [versão 3.6 do Python](https://docs.python.org/3/whatsnew/3.6.html#whatsnew36-pep498), foi adicionado um novo recurso para realizar a interpolação de strings. Esse recurso é chamado de `f-strings` ou `formatted string literals`. 

Esse recurso funciona da seguinte forma. Vamos imaginar que temos uma variável nome:

```
>>> nome = 'Matheus'
>>> print(f'Meu nome é {nome}')
Meu nome é Matheus
```

Quando colocamos a letra `f` antes das aspas, informamos ao Python que estamos utilizando uma `f-string`. Dessa forma o Python consegue, em tempo de execução, captar a expressão que está entre chaves (`{ }`) e avaliá-la.

Além de variáveis, podemos passar também de funções e métodos:

```
>>> nome = 'Matheus'
>>> print(f'Meu nome é {nome.lower()}')
Meu nome é matheus
```
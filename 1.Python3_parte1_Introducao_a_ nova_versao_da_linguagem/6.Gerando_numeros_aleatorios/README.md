### Gerando e arredondando um número aleatório

A lógica principal do nosso jogo já está funcionando, mas ainda há um detalhe, o número secreto não é tão secreto assim, pois ele está fixo!  Então vamos alterar isso, para que ele passe a ser um número aleatório,  coisa que veremos nesse capítulo.

## Gerando um número aleatório

A ideia é que o próprio jogo, toda vez que for executado, gere esse  número, ele que decide isso, não nós. E para gerar um número aleatório, o Python 3 possui a função **`random()`**, que gera um número no intervalo entre 0.0 e 1.0. Mas ao contrário das [funções *built-in*](https://docs.python.org/3/library/functions.html) do Python, como as funções **`input()`**, **`int()`**, **`print()`** e **`range()`**, que são **funções embutidas** do Python (que já vem com o mesmo), a função **`random`** não vem, pois está em um módulo separado, e esse módulo precisa ser importado.

Podemos ir ao console do Python e testar isso. Primeiro importando o módulo:

```
>>> import random
```

E a partir desse módulo, chamamos a função **`random()`**:

```
>>> import random
>>> random.random()
0.6022965518496559
```

## Arredondando um número

Só que, como podemos perceber, o número gerado tem muitas casas  decimais e está no intervalo entre 0.0 e 1.0, mas no nosso jogo  precisamos de um número entre 1 e 100. O que podemos fazer é multiplicar o número gerado por 100:

```
>>> import random
>>> random.random() * 100
58.30742817094118
```

Já  conseguimos chegar a um número mais próximo do ideal, falta agora  removermos as casas decimais. Podemos utilizar a já conhecida função **`int`**, que irá converter o número aleatório, que é um float, em um número inteiro:

```
>>> int(random.random() * 100)
91
```

Mas reparem no exemplo abaixo:

```
>>> numero_random = random.random() * 100
>>> numero_random
18.895629671768187
>>> int(numero_random)
18
```

A função **`int`** nada mais faz do que **remover** as casas decimais do número flutuante. Mas o número gerado acima está  mais próximo de 19 do que de 18, correto? Será que temos uma função que **arredonda** esse número para nós? Sim! Temos mais uma função *built-in*, a **`round`**:

```
>>> numero_random = random.random() * 100
>>> numero_random
18.895629671768187
>>> int(numero_random)
18
>>> round(numero_random)
19
```

Conhecendo isso, podemos aplicar ao nosso jogo. Faremos isso no próximo vídeo, até lá!





### Definindo um intervalo para a geração de números aleatórios

## Transcrição

Para gerar um número aleatório no nosso jogo, a primeira coisa que devemos fazer é importar o seu módulo, no início do programa:

```
import random

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42
total_de_tentativas = 3

# restante do código comentado
```

Com o módulo importado, vamos remover o valor fixo da variável **`numero_secreto`** e substituir por um valor aleatório que será gerado pela função **`random()`**:

```
import random

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = random.random()
total_de_tentativas = 3

# restante do código comentado
```

Mas não podemos nos esquecer de multiplicar esse número por 100 e arredondá-lo:

```
import random

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = round(random.random() * 100)
total_de_tentativas = 3

# restante do código comentado
```

Perfeito, conseguimos aplicar a mudança ao nosso código. Agora fica mais difícil  de acertar o número secreto, até para nós, os desenvolvedores do jogo :)

## Gerando um número aleatório dentro de um intervalo

A ideia de multiplicar o número por 100 parece funcionar, mas podemos lembrar que o número gerado é entre 0.0 e 1.0, que quando multiplicado  por 100 fica entre 0 e 100. Só que o nosso jogo não aceita o 0!

O ideal seria que pudéssemos definir um intervalo, dizer que queremos que o número gerado esteja entre 1 e 100. Como o **`random`** é um módulo, ele possui mais de uma função e a função **`randrange()`** serve exatamente para esse nosso problema. Se passarmos um parâmetro  para ela, ela irá gerar um número inteiro de 0 até o valor desse  parâmetro menos 1. Se passarmos dois parâmetros para ela, ela irá gerar  um número inteiro do valor do primeiro parâmetro até o valor do segundo  parâmetro menos 1, exatamente o que queremos!

Vamos, passando o intervalo que queremos para a função **`randrange()`**, lembrando que como queremos que o número gerado esteja entre 1 e 100  (inclusive), precisamos passar o número 101 como segundo parâmetro para a função:

```
import random

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = random.randrange(1, 101)
total_de_tentativas = 3

# restante do código comentado
```





## Pseudo-Random?

Aparentemente a geração de números aleatórios funcionou muito bem. Cada vez que chamamos o `random.random()` ou `random.randrange(..)`, foi gerado um outro número.

No entanto, computadores têm os seus problemas com aleatoriedade,  pois são sistemas determinísticos. Em outras palavras, o nosso Python é  previsível e na verdade não sabe criar números verdadeiramente  aleatórios. Por isso se chama *Pseudo-Random*!

## Por que funcionou então?

`random` é um função que, dada a mesma entrada, gerará o  mesmo número. O truque é oferecer sempre uma entrada diferente para ter  números diferentes e exatamente isso que está acontecendo por baixo dos  panos.

Essa entrada também é chamada de *seed* (semente, em português). Entre as chamadas da função `random`, sempre é utilizado um novo *seed*. Por padrão o Python usa a hora (os milissegundos) como semente, mas nada nos impede de definir o mesmo *seed* antecipadamente. Para isso, existe a função `seed`!

## Usando seed

Por exemplo, no jogo usamos a função `randrange` para gerar um número aleatório entre 1 e 100. Antes do `randrange` podemos chamar o `seed` para definir a entrada:

```
>>> random.seed(100)
>>> random.randrange(1, 101)
19
```

Repare que foi gerado 19 e se usarmos o mesmo *seed* será gerado o mesmo número: 

```
>>> random.seed(100)
>>> random.randrange(1, 101)
19
```

Repare que a biblioteca `random` é bem previsível e por isso se chama *pseudo-random*!
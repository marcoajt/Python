# Python vs C

No curso [**C I: Introdução à Linguagem das Linguagens**](https://cursos.alura.com.br/course/introducao-a-programacao-com-c-parte-1) também é implementado um jogo de adivinhação, você pode baixá-lo [aqui](https://s3.amazonaws.com/caelum-online-public/python3/files/adivinhacao.c) e deixe-o na mesma pasta que os arquivos Python, ou seja, na pasta **jogos**. O que faremos nesse vídeo é comparar o Python com C, mas sem explicá-lo, a ideia é só enfatizar algumas diferenças entre eles.

A primeira diferença que vemos é que no C precisamos importar mais bibliotecas, isso porque algumas funções no C não são *built-in*, como a de imprimir (**`printf`**) e a de capturar entrada do usuário (**`scanf`**), por isso para utilizá-las é necessário importar algumas bibliotecas.

Outra diferença é que no C somos obrigados a definir a função **`main`**, que é considerada o início de qualquer programa, sem ela nada vai  funcionar. Ao contrário do Python, já que nós só criamos a função **`jogar()`** quando precisamos importar o arquivo em outro, mas antes nós conseguíamos executar diretamente o jogo sem problemas.

No capítulo 1 falamos sobre tipagem de variáveis, e o C é uma linguagem que possui a **tipagem estática**, ou seja, quando declaramos uma variável, precisamos dizer qual será o  tipo dela e esse tipo nunca mudará. O Python, como já sabemos, é uma  linguagem que possui a **tipagem dinâmica**, já que o tipo  da variável varia de acordo com o valor que ela recebe, por isso que em  Python não podemos declarar variáveis vazias, só definindo o seu nome,  porque se não atribuirmos um valor a uma variável, o Python não saberá o seu tipo.

O resto do código é bem parecido, com algumas diferenças de sintaxe e nomenclatura, como por exemplo a sintaxe dos blocos, para definir um  bloco no C devemos colocá-lo entre chaves e a indentação não é  obrigatório, apesar de todos os desenvolvedores utilizarem por conta da  formatação do código, já no Python só precisamos colocar os dois pontos e indentar o código do bloco; o C também te obriga a colocar ponto e  vírgula ao final das instruções.

Essas foram algumas das diferenças que podemos citar comparando os  dois códigos. Agora veremos na hora da execução, mas no próximo vídeo :)



# Interpretado vs Compilado

Para executar um arquivo Python, por exemplo o **adivinhacao.py**, fazemos:

```
python3 adivinhacao.py
```

Foi isso que fizemos o treinamento inteiro, seja pela linha de comando ou  pelo PyCharm. E com o C? Será que existe um comando, algo como um **`cexecuter`**, para executarmos um arquivo C? Não, não existe.

O ambiente do C exige que primeiramente devemos passar o código fonte (o arquivo .c) para um **compilador**. O compilador lê o código fonte e faz uma análise da sintaxe, se  esquecemos algum ponto e vírgula, ou de tipar alguma variável, etc. E  feita essa análise, o compilador cria um outro arquivo, e é esse arquivo que podemos executar. Então primeiro vamos compilar o arquivo, vamos  utilizar o compilador **gcc** (novamente, não é necessária a sua instalação, estamos usando-o somente para mostrar a diferença entre ambientes que usam o conceito de compilação e ambientes que usam o  conceito de interpretação):

```
gcc adivinhacao.c o adivinhacao
```

Ou:

```
gcc -std=c99 adivinhacao.c -o adivinhacao
```

Esse comando compila o arquivo **adivinhacao.c** e se tudo estiver correto, criará o arquivo executável **adivinhacao**. Agora é só executar o arquivo gerado. Em UNIX, fazemos:

```
./adivinhacao
```

Essa é a diferença de um ambiente que usa o conceito de compilação, no qual o código fonte, que não é executável, deve ser compilado para criar um  arquivo executável; e um ambiente que usa o conceito de interpretação,  no qual o código fonte é executado diretamente.

## Transferindo código

Em Python, conseguimos executar um arquivo em qualquer sistema  operacional, inclusive os códigos aqui feitos são disponibilizados para  vocês, alunos, e ele poderá ser executado seja qual for o seu sistema  operacional, basta ter o Python 3 instalado. Já o arquivo executável do  C, gerado pelo compilador, não é executável em um sistema operacional  diferente. É preciso compilar novamente o código fonte no sistema  operacional desejado, para ter um executável funcional. E muitas vezes o código fonte (não é o nosso caso) utiliza algo específico do sistema  operacional, passando a depender dele, então nem adiantaria compilá-lo  em um SO diferente.

Logo, o Python tem uma portabilidade maior que o C.

## O Python é realmente uma linguagem estritamente interpretada?

Para finalizar, falamos que o Python utiliza o conceito de  interpretação, ou seja, passamos o código fonte e ele é interpretado,  mas não é bem assim. Podemos executar o arquivo **jogos.py** e reparar na pasta que é criada dentro do diretório, a ***\*pycache\****. Se formos ver o que tem dentro da sua pasta, vemos que há dois arquivos referentes aos módulos importados no **jogos.py**, ou seja, um arquivo referente à **`adivinhacao`** e outro à **`forca`**. Mas o que são esses arquivos?

O que o Python faz ao vivo é ler os módulos importados e os **compila para bytecode**. Esse código foi criado ao mesmo tempo em que executamos o arquivo **jogos.py**. Apesar do Python ter um ambiente de interpretação, ele compila os  módulos importados para melhorar o desempenho, a execução do ambiente,  apesar de não ter esse processo de compilação explícito.

Do ponto de vista do Python, ele considera que esses módulos não  serão modificados, então na próxima execução, para melhorar o  desempenho, esse código compilado é que será utilizado.

Com isso, terminamos aqui o nosso curso. No próximo implementaremos o jogo da forca, aprendendo mais sobre funções, coleções, outras funções *built-in*, e muito mais! Muito obrigado por assistirem esse curso e nos encontramos no próximo treinamento!



# Python é interpretado ou compilado?

O senso comum é que o Python é uma **linguagem interpretada**. ***Interpretado\*** significa que não há um processo de compilação que traduz o código  fonte em algum código nativo, que o seu computador entende. A [documentação do Python](https://docs.python.org/3/glossary.html) confirma isso, no entanto também menciona a presença de um compilador:

***"Python is an interpreted language, as opposed to a  compiled one, though the distinction can be blurry because of the  presence of the bytecode compiler."\***

Traduzido livremente: **"Python é uma linguagem interpretada,  em oposição às compiladas, embora a distinção possa ficar desfocada  devido à presença do compilador de bytecode."**

Temos um compilador, porém de bytecode. Bytecode é um código  intermediário, normalmente independente do sistema operacional. Então,  Python é uma linguagem compilada também? Em 2003, Fredrik Lundh, em seu  artigo [Compiling Python Code](http://effbot.org/zone/python-compile.htm), título que perverte o senso comum, começa:

***"Python source code is automatically compiled into Python byte code by the CPython interpreter. Compiled code is usually stored  in PYC (or PYO) files, and is regenerated when the source is updated, or when otherwise necessary."\***

Novamente traduzindo livremente: ***"O código fonte é  automaticamente compilado para bytecode do Python pelo interpretador  CPython. O código compilado é comumente armazenado nos arquivos no PYC  (ou PYO), sendo regerado quando o arquivo fonte é atualizado ou quando é necessário."\***

E aí? Python é uma linguagem interpretada ou compilada? As duas  coisas? Há discussões acaloradas entre desenvolvedores, cada um com sua  opinião. Então, [uma resposta interessante](http://stackoverflow.com/questions/6889747/is-python-interpreted-or-compiled-or-both) está no StackOverFlow, aliás, a resposta mais bem avaliada:

***"First off, interpreted/compiled is not a property of the language but a property of the implementation (...) Python is compiled. Not compiled to machine code ahead of time (i.e. "compiled" by the  restricted and wrong, but also common definition), "only" compiled to  bytecode"\***

Traduzindo: ***"O fato de uma linguagem ser interpretada ou  compilada não é uma questão da linguagem, mas da sua implementação.  (...) Python é compilada. Não compilada para o código de máquina antes  da execução, apenas para o bytecode.\***

Isso significa que alguém pode implementar o Python totalmente  compilado, totalmente interpretado ou ambos, a linguagem continua a  mesma. Ser compilada/interpretada é mais propriedade da implementação do Python do que da linguagem. 

E você, o que pensa dessa definição?
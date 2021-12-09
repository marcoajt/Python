## Aula 2

A IDE usada foi o Pycharm.

A função **`input`** sempre retorna um texto (string). Sendo assim, é necessário converter o valor retornado em inteiro, para que a comparação com outro inteiro, no caso o **`numero_secreto`**, seja possível. Realizamos essa conversão através da função **`int()`**.

```
chute_str = input("Digite seu número")
chute = int(chute_str)
```

Porém usei o código abaixo para reduzir.

````
chute_str = int(input("Digite seu número"))
````

Qualquer das opções usadas o código funcionara na comparação, porque as duas variáveis são **`int`** .

concatenação 

```
nome = "Nico"
sobrenome = "Steppat"
print(nome + sobrenome)
```

Resultado: `NicoSteppat`

Para que haja, basta fazer assim:

```
nome = "Nico"
sobrenome = "Steppat"
print(nome, sobrenome)
```

Resultado: `Nico Steppat`

Lembrando que a função **`print`** automaticamente aplica um separador entre os valores. O separador é um espaço por padrão, mas pode ser reconfigurado pelo parâmetro **`sep`**:

```
nome = "Nico"
sobrenome = "Steppat"
print(nome, sobrenome, sep="_")
```

Resultado: `Nico_Steppat`


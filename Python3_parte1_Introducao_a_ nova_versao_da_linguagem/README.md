## Aula 1

sep - separador.
end - coloca no final do print.
\n - é um caractere especial, que faz com que o novo prompt comece em uma nova linha.

````
subst = "Python"
verbo = "é"
adjetivo = "fantástico"
print(subst, verbo, adjetivo, sep="_", end="!\n")
Python_é_fantástico!
````

````
dia = 15
mes = 10
ano = 2015
print(dia, mes, ano, sep="/")
15/10/2015
````

Em Python, a variável só passa a existir quando atribuímos um valor.

O Python utiliza por convenção o padrão Snake_Case para nomes de variáveis (ou identificadores).

````
idade_esposa = 20
perfil_vip = 'Flávio Almeida'
recibos_em_atraso = 30
````

Em outras linguagens também se usa o padrão CamelCase. O mesmo exemplo com CamelCase (que não é o padrão do Python):

````
idadeEsposa = 20
perfilVip = 'Flávio Almeida'
recibosEmAtraso = 30
````
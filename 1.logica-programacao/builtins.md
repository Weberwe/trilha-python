Índice built-in
1. [alguns builtins](#alguns-built-in)
1. [cast de listas](#cast-de-listas)
1. [lista de exercícios](#lista-de-exercícios)

# funções built-in

As funções built-in do Python são funções que já vêm integradas na linguagem, ou seja, estão disponíveis para uso imediato sem a necessidade de importação de módulos ou bibliotecas adicionais. Essas funções são projetadas para realizar tarefas comuns, como manipulação de strings, números, listas, entre outros, de forma simples e eficiente.

## alguns built-in

O Python possui MUITAS funções built-in. Veja abaixo uma lista de algumas das mais comuns :

### `print()`
A função `print()`, já muito conhecida, é usada para exibir informações na tela. Ela aceita múltiplos argumentos, separados por vírgulas, e os imprime na sequência.

```python
print("Olá, Mundo!")  # saída : Olá, Mundo!
print("A soma de 2 e 3 é:", 2 + 3)  # saída : A soma de 2 e 3 é: 5
```

### `input()`
A função `input()` lê uma entrada do usuário e a retorna como uma string.

```python
nome = input("Digite seu nome: ")
print("Olá, " + nome + "!")
```

```
Digite seu nome: Schwarzenegger
Olá, Schwarzenegger!
```

### `len()`
A função `len()` retorna o comprimento (número de itens) de um objeto, como uma string, lista.

```python
texto = "Python"
lista = [1, 2, 3, 4, 5]
print(len(texto))  # saída : 6
print(len(lista))  # saída : 5
```

### `sum()`
A função `sum()` soma todos os elementos de um iterável, como uma lista ou tupla. Opcionalmente, pode-se passar um valor inicial para a soma.

```python
numeros = [10, 20, 30]
print(sum(numeros))        # saída : 60
print(sum(numeros, 10))    # saída : 70 (60 + 10)
```

### `pow()`
A função `pow()` retorna o valor de um número elevado a uma determinada potência. Ela aceita dois ou três argumentos. Se três argumentos forem fornecidos, a função calcula a potência e, em seguida, faz o módulo da resposta -> (x^y) % z.

```python
print(pow(2, 3))        # saída : 8 (2^3)
print(pow(2, 3, 5))     # saída : 3 (2^3 % 5)
```

### `max()` e `min()`
As funções `max()` e `min()` retornam, respectivamente, o maior e o menor valor em um iterável.

```python
numeros = [20, 10, 30, 40]
print(max(numeros))  # saída : 40
print(min(numeros))  # saída : 10
```

### `abs()`
A função `abs()` retorna o valor absoluto de um número, ou seja, seu valor sem o sinal.

```python
print(abs(-10))  # saída : 10
print(abs(4.5))  # saída : 4.5
```

### `round()`
A função `round()` arredonda um número para o número especificado de dígitos.

```python
print(round(3.14159, 2))  # saída : 3.14
print(round(2.71828))     # saída : 3
```

### `type()`
A função `type()` retorna o tipo do objeto passado como argumento.

```python
print(type(10))          # saída : <class 'int'>
print(type(3.14))        # saída : <class 'float'>
print(type(False))       # saída : <class 'bool'>
print(type("Python"))    # saída : <class 'str'>
print(type([1, 2, 3]))   # saída : <class 'list'>
```

### `isinstance()`
A função `isinstance()` verifica se um objeto é uma instância de uma classe ou de uma tupla de classes.

```python
print(isinstance(10, int))             # saída : True
print(isinstance("Python", str))       # saída : True
print(isinstance("Python", float))     # saída : False
print(isinstance(3.14, (int, float)))  # saída : True
```

### `ord()` e `chr()`
A função `ord()` retorna o número inteiro representando o código Unicode de um dado caractere. Já a função `chr()` faz o inverso, convertendo um número inteiro para o caractere correspondente ao seu código Unicode.

```python
print(ord('A'))  # saída : 65
print(chr(65))   # saída : 'A'
```

### `help()`
A função `help()` exibe a documentação de uma função, módulo, ou classe.

```python
help(print)
```

## cast de listas

Assim como os outros tipos vistos até agora, o tipo lista também possui uma função capaz de converter outros tipos para lista, embora haja algumas particularidades. Para converter, usa-se a função `list()`.

### `list()`
A função `list()` é o principal built-in usado para converter (ou "castar") outros tipos de dados em listas. Ela aceita qualquer **iterável** como argumento e retorna uma nova lista contendo os elementos desse iterável.

Quando você converte uma string em uma lista, cada caractere da string se torna um elemento separado na lista.

```python
sobrenome = 'Schwarzenegger'
lista = list(sobrenome)
print(lista)  # saída : ['S', 'c', 'h', 'w', 'a', 'r', 'z', 'e', 'n', 'e', 'g', 'g', 'e', 'r']
```

Como os tipos `int`, `float`, `bool` não são iteráveis, não é possível converter para uma lista um objeto sozinho desses tipos.

## lista de exercícios

<details>
<summary>Lista de Exercícios</summary>

1. Nível Simples
    1. Crie uma lista de números inteiros e use a função `len()` para encontrar quantos elementos há na lista.
    1. Crie uma string e use a função `len()` para contar o número de caracteres na string.
    1. Crie uma lista de números inteiros e use a função `sum()` para calcular a soma de todos os elementos da lista.
    1. Crie uma lista de números inteiros, use a função `max()` para encontrar o maior número na lista e `min()` para encontrar o menor.
    1. Use a função `pow()` para calcular o valor de 2 elevado à 3ª potência.
    1. Crie uma variável com um número negativo e use a função `abs()` para encontrar o valor absoluto desse número.
    1. Use a função `round()` para arredondar o número 7.654 para duas casas decimais.
    1. Crie uma variável com um valor inteiro e use a função `type()` para verificar seu tipo.
    1. Crie uma variável com um valor float e use a função `isinstance()` para verificar se ela é do tipo `float`.
    1. Use a função `ord()` para encontrar o valor numérico da letra 'A'.
1. Nível Intermediário
    1. Crie uma string com várias palavras e use a função `len()` para contar o número de caracteres, incluindo os espaços.
    1. Crie uma lista de números decimais e use a função `sum()` para calcular a soma de todos os elementos da lista.
    1. Use a função `max()` e `min()` para encontrar o maior e o menor número entre 3, 9 e 4.
    1. Use a função `pow()` para calcular o valor de 5 elevado à 4ª potência.
    1. Crie uma lista com números positivos e negativos e use a função `abs()` para criar uma nova lista com os valores absolutos.
    1. Use a função `round()` para arredondar o número 3.14159 para três casas decimais.
    1. Crie uma lista de diferentes tipos de dados (int, str, bool) e use a função `type()` para verificar o tipo de cada elemento.
    1. Use a função `isinstance()` para verificar se o número 10.5 é um `int`.
    1. Use a função `chr()` para encontrar o caractere correspondente ao número 97.
    1. Use a função `help()` para exibir a documentação da função `len()`.
1. Nível Avançado
    1. Crie uma lista de listas (matriz) e use a função `len()` para encontrar o número de linhas e o número de colunas.
    1. Crie uma lista de listas (matriz) e use a função `sum()` para calcular a soma de todos os elementos da matriz.
    1. Use a função `max()` para encontrar o maior número em uma lista de listas (matriz).
    1. Use a função `pow()` para calcular o valor de 2 elevado à 10ª potência e, em seguida, divida por 3.3 e arredonde o resultado para a casa decimal mais próxima.
    1. Crie um algoritmo que peça um número e mostre seu valor absoluto usando a função `abs()`.
    1. Use a função `round()` para arredondar uma lista de números decimais para o inteiro mais próximo.
    1. Crie uma lista com diferentes tipos de dados (int, str, bool, list) e use a função `type()` para verificar o tipo de cada elemento.
    1. Crie um algoritmo que verifique se um número é inteiro usando a função `isinstance()`.
    1. Crie um algoritmo que converta uma lista de caracteres em seus valores numéricos usando `ord()`.
    1. Crie um algoritmo que converta uma lista de números em seus caracteres correspondentes usando `chr()`.
1. Nível Complexo
    1. Crie um algoritmo que peça uma lista de strings ao usuário e mostre uma lista com o comprimento de cada string digitada usando a função `len()`.
    1. Crie um algoritmo que peça duas listas de inteiros distintas e mostre a soma dos elementos de cada lista usando a função `sum()`.
    1. Crie um algoritmo que peça três (matriz) e retorne o maior número de cada lista usando a função `max()`.
    1. Crie um algoritmo que peça duas listas de números de mesmo tamanho e mostre uma lista com os resultados da exponenciação entre os elementos correspondentes usando a função `pow()`.
    1. Crie um algoritmo que peça uma lista de números e mostre uma lista com os valores absolutos de cada número usando a função `abs()`.
    1. Crie um algoritmo que peça uma lista de números decimais e mostre uma lista com os números arredondados para uma casa decimal usando a função `round()`.
    1. Crie um algoritmo que peça uma lista de diferentes tipos de dados e mostre uma lista com o tipo de cada elemento usando a função `type()`.
    1. Crie um algoritmo que peça uma lista de valores e mostre uma lista de booleanos indicando se cada valor é um inteiro usando a função `isinstance()`.
    1. Crie um algoritmo que peça uma string e mostre uma lista com os valores numéricos de cada caractere da string usando a função `ord()`.
    1. Crie um algoritmo que peça uma lista de números e retorne uma string formada pelos caracteres correspondentes a esses números usando a função `chr()`.
1. Nível Muito Complexo
    1. Crie um algoritmo que peça uma string e mostre a média dos valores numéricos de seus caracteres usando as funções `ord()` e `sum()`.
    1. Crie um algoritmo que peça duas strings e mostre a soma dos valores numéricos de seus caracteres correspondentes usando as funções `ord()` e `sum()`.
    1. Crie um algoritmo que peça uma lista de números e retorne o valor máximo absoluto dos números usando as funções `abs()` e `max()`.
    1. Crie um algoritmo que peça uma string e mostre o caractere que representa o valor numérico mais próximo da média dos valores dos caracteres da string usando as funções `ord()`, `sum()`, `len()` e `chr()`.
    1. Crie um algoritmo que peça uma lista de números decimais e mostre uma lista com os números arredondados para o inteiro mais próximo usando as funções `round()` e `type()` para garantir que os elementos sejam do tipo `float`.
    1. Crie um algoritmo que peça uma lista de números e mostre a soma dos números que são inteiros usando as funções `isinstance()` e `sum()`.
    1. Crie um algoritmo que peça uma lista de strings e mostre uma lista de listas, onde cada lista interna conterá cada string e o seu tamanho usando as funções `len()`.

</details>


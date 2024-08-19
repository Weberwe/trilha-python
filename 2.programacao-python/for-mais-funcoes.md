# comando for e mais funções

## `for`

O comando `for` em Python é uma estrutura de repetição que permite iterar sobre elementos de uma sequência (como listas, tuplas, strings ou intervalos) ou qualquer outro objeto iterável. A cada iteração, ele atribui o próximo elemento da sequência a uma variável e executa um bloco de código.

```python
# sintaxe básica
for variável in sequência:
    # bloco de código
```

- **variável** : uma variável que assume o valor de cada item da sequência durante cada iteração;
- **sequência** : pode ser qualquer tipo de coleção, como uma lista, string, tupla, conjunto, ou até mesmo um intervalo (usando `range()`);
- **bloco de código** : o código que será executado para cada item na sequência;

Veja alguns exemplos

1. iterando sobre uma lista :

    Uma lista, nada mais é que uma sequência de itens. Então, é possível usar o comando `for` para passar por cada elemento individualmente.
    ```python
    >>> frutas = ["maçã", "banana", "laranja"]
    >>> for fruta in frutas:
    ...     print(fruta)
    ...
    maçã
    banana
    laranja
    >>> |
    ```

1. iterando sobre uma string :
    ```python
    >>> palavra = 'Arnold'
    >>> for letra in palavra:
    ...     print(letra)
    ...
    A
    r
    n
    o
    l
    d
    >>> |
    ```

### `for` e `if-elif-else`

É possível incluir declarações condicionais dentro de um loop `for` para controlar o fluxo de execução :

```python
>>> numeros = [1, 2, 3, 4, 5, 6]
>>> for num in numeros:
...     if num % 2 == 0:
...         print(f'{num} é par')
...     else:
...         print(f'{num} é ímpar')
...
1 é ímpar
2 é par
3 é ímpar
4 é par
5 é ímpar
6 é par
>>> |
```

## `range()`

A função `range()` é usada para gerar uma sequência de números. Ela é frequentemente utilizada em loops `for` para iterar um número específico de vezes. O `range()` pode ser utilizado de três maneiras diferentes, dependendo de quantos argumentos você fornecer.

```python
# sintaxe básica
range(stop)
range(start, stop[, step])
```

- **`start`** (opcional): O número inicial da sequência. O valor padrão é `0`;
- **`stop`**: O número onde a sequência termina (não incluído);
- **`step`** (opcional): A diferença entre cada número na sequência. O valor padrão é `1`;

Veja alguns exemplos de uso

1. gerando uma sequência simples de 0 a n-1 :
    ```python
    >>> for i in range(5):
    ...     print(i)
    ...
    0
    1
    2
    3
    4
    >>> |
    ```

1. especificando o valor inicial (`start`) e final (`stop`) :
    ```python
    >>> for i in range(2,7):
    ...     print(i)
    ...
    2
    3
    4
    5
    6
    >>>
    ```

1. usando um `step` crescente (incremento) :
    ```python
    >>> for i in range(1, 10, 2):
    ...     print(i)
    ...
    1
    3
    5
    7
    9
    >>>
    ```

1. usando um `step` decrescente (step negativo) :
    ```python
    >>> for i in range(10, 0, -2):
    ...     print(i)
    ...
    10
    8
    6
    4
    2
    >>>
    ```

1. embora `range()` crie um objeto de intervalo (e não uma lista), é possível convertê-lo em uma lista usando a função `list()` :
    ```python
    >>> lista = list(range(10))
    >>> lista
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> |
    ```
    É muito útil para gerar sequências de números de forma instantânea.

1. se precisar acessar os índices de uma lista em vez de seus valores diretamente, é possível combinar `range()` com `len()` :
    ```python
    >>> frutas = ['maçã', 'banana', 'laranja']
    >>> for i in range(len(frutas)):
    ...     print(f'índice {i} tem a fruta {frutas[i]}')
    ...
    índice 0 tem a fruta maçã
    índice 1 tem a fruta banana
    índice 2 tem a fruta laranja
    >>>
    ```

1. veja mais alguns usos do `range()` :
   ```python
    >>> # criando uma sequência de números pares
    >>> pares = list(range(0, 21, 0))
    >>> pares
    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    >>>
    >>> # criando uma sequência de números ímpares
    >>> impares = list(range(1, 22, 2))
    >>> impares
    [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
    >>>
    >>> # criando uma sequência decrescente
    >>> descrescente = list(range(10, 0, -1))
    >>> descrescente
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    >>>
    >>> # combinando for, range e condicionais
    >>> for i in range(1, 10):
    ...     if i % 2 == 0:
    ...         print(f'{i} é par')
    ...     else:
    ...          print(f'{i} é ímpar')
    ...
    1 é ímpar
    2 é par
    3 é ímpar
    4 é par
    5 é ímpar
    6 é par
    7 é ímpar
    8 é par
    9 é ímpar
    >>> |
    ```

## `enumerate()`

A função `enumerate()` em Python é usada para iterar sobre uma sequência (como uma lista, tupla ou string) e retornar tanto o índice quanto o valor dos elementos dessa sequência. Isso é particularmente útil quando é preciso de acesso ao índice do elemento dentro de um loop, sem precisar gerenciá-lo manualmente.

```python
# sintaxe básica
enumerate(iterável, start=0)
```

- **`iterável`** : a sequência sobre a qual você deseja iterar (como uma lista, tupla, string, etc.);
- **`start`** (opcional) : o valor inicial do índice (o valor padrão é 0);

Quando usado dentro de um loop `for`, `enumerate()` retorna uma tupla que contém o índice e o valor do elemento na sequência. Esse índice começa no valor especificado pelo parâmetro `start`.

Veja alguns exemplos

1. iterando sobre uma lista com `enumerate()` :
    ```python
    >>> frutas = ['maçã', 'banana', 'laranja']
    >>> for i, fruta in enumerate(frutas):
    ...     print(f'Índice {i}: {fruta}')
    ...
    Índice 0: maçã
    Índice 1: banana
    Índice 2: laranja
    >>> |
    ```

1. especificando um valor inicial para o índice :
    ```python
    >>> frutas = ['maçã', 'banana', 'laranja']
    >>> for i, fruta in enumerate(frutas, start=1):
    ...     print(f'Índice {i}: {fruta}')
    ...
    Índice 1: maçã
    Índice 2: banana
    Índice 4: laranja
    >>> |
    ```

1. acessando índices ao iterar sobre strings :
    ```python
    >>> palavra = 'Python'
    >>> for i, letra in enumerate(palavra):
    ...     print(f'Letra {letra} está na posição {i}')
    ...
    Letra P está na posição 0
    Letra y está na posição 1
    Letra t está na posição 2
    Letra h está na posição 3
    Letra o está na posição 4
    Letra n está na posição 5
    >>> |
    ```

1. identificando posições de elementos específicos em uma lista :
    ```python
    >>> numeros = list(range(10, 60, 10))
    >>> numeros
    [10, 20, 30, 40, 50]
    >>> for i, num in enumerate(numeros):
    ...     if num == 30:
    ...         print(f'Encontrado {num} na posição {i}')
    ...
    Encontrado 30 na posição 2
    >>> |
    ```

1. se precisar modificar os elementos de uma lista com base em sua posição, `enumerate()` pode ser útil:
    ```python
    >>> numeros = list(range(10, 60, 10))
    >>> numeros
    [10, 20, 30, 40, 50]
    >>>
    >>> for i, num in enumerate(numeros):
    ...     numeros[i] = num * 2
    ...
    >>> numeros
    [20, 40, 60, 80, 100]
    >>> |
    ```

## `zip()`

A função `zip()` em Python é usada para combinar dois ou mais iteráveis (como listas, tuplas, ou qualquer objeto que suporte iteração) em um único iterável de pares ou tuplas. Cada tupla gerada pelo `zip()` conterá os elementos correspondentes dos iteráveis fornecidos.

```python
# sintaxe básica
zip(iterável1, iterável2, ...)
```

- **`iterável1, iterável2, ...`** : um ou mais iteráveis (listas, tuplas, strings, etc.) que deseja combinar;

A função `zip()` retorna um iterador de tuplas, onde cada tupla contém um elemento de cada iterável. Se os iteráveis tiverem comprimentos diferentes, o `zip()` truncará ao comprimento do menor iterável.

Veja exemplos de uso

1. zip de duas listas :
    ```python
    >>> nomes = ['Ana', 'João', 'Maria']
    >>> idades = [25, 30, 22]
    >>>
    >>> combinados = zip(nomes, idades)
    >>> list(combinados)
    [('Ana', 25), ('João', 30), ('Maria', 22)]
    >>> |
    ```

1. zip de três listas :
    ```python
    >>> nomes = ['Ana', 'João', 'Maria']
    >>> idades = [25, 30, 22]
    >>> cidades = ['São Paulo', 'Rio de Janeiro', 'Curitiba']
    >>>
    >>> combinados = zip(nomes, idades, cidades)
    >>> list(combinados)
    [('Ana', 25, 'São Paulo'), ('João', 30, 'Rio de Janeiro'), ('Maria', 22, 'Curitiba')]
    >>> |
    ```

1. iterando com `zip()` em um loop `for` :
    ```python
    >>> nomes = ['Ana', 'João', 'Maria']
    >>> idades = [25, 30, 22]

    >>> for nome, idade in zip(nomes, idades):
    >>>     print(f'{nome} tem {idade} anos.')
    Ana tem 25 anos.
    João tem 30 anos.
    Maria tem 22 anos.
    >>> |
    ```

1. quando os iteráveis passados para `zip()` têm tamanhos diferentes, o `zip()` para de emparelhar assim que o menor iterável é consumido :
    ```python
    >>> nomes = ['Ana', 'João']
    >>> idades = [25, 30, 22]  # Uma lista mais longa
    >>>
    >>> combinados = zip(nomes, idades)
    >>> list(combinados)
    [('Ana', 25), ('João', 30)]
    >>> |
    ```
    No exemplo acima, o terceiro valor de `idades` (22) é ignorado porque `nomes` só tem dois elementos.

1. Zip com Strings :
    ```python
    >>> letras = 'abc'
    >>> numeros = [1, 2, 3]
    >>>
    >>> combinados = zip(letras, numeros)
    >>> list(combinados)
    [('a', 1), ('b', 2), ('c', 3)]
    >>> |
    ```

## exercícios

<details>
<summary>Lista de Exercícios</summary>

### exercícios de `for`

1. Itere sobre uma lista de números e imprima cada número.
1. Itere sobre uma string e imprima cada caractere.
1. Itere sobre uma lista de palavras e imprima cada palavra em maiúsculas.
1. Itere sobre uma lista de números e imprima o quadrado de cada número.
1. Itere sobre uma string e conte quantas letras "a" ela possui.
1. Crie uma lista de números e use um loop `for` para criar uma nova lista com o dobro de cada número.
1. Itere sobre uma lista de strings e imprima cada uma em ordem reversa.
1. Itere sobre uma lista de números e imprima apenas os números pares.
1. Itere sobre uma lista de palavras e imprima apenas as palavras que começam com a letra "p".
1. Itere sobre uma lista de números e imprima o cubo de cada número.
1. Crie uma lista de números e use `for` para somar todos os números da lista.
1. Itere sobre uma string e crie uma nova string com todas as vogais removidas.
1. Itere sobre uma lista de palavras e imprima o comprimento de cada uma.
1. Itere sobre uma lista de números e imprima a metade de cada número.
1. Itere sobre uma string e imprima cada caractere junto com seu índice.
1. Crie uma lista de palavras e use `for` para criar uma nova lista com cada palavra em maiúsculas.
1. Itere sobre uma lista de números e imprima apenas os números ímpares.
1. Itere sobre uma string e imprima apenas as letras que aparecem mais de uma vez.
1. Itere sobre uma lista de números e imprima o produto de todos os números.
1. Itere sobre uma lista de palavras e imprima apenas as palavras que contêm a letra "e".
1. Itere sobre uma lista de números e crie uma nova lista com apenas os números que são divisíveis por 3.
1. Itere sobre uma string e imprima cada caractere junto com a quantidade de vezes que ele aparece na string.
1. Itere sobre uma lista de palavras e imprima cada palavra com suas letras em ordem alfabética.
1. Itere sobre uma lista de números e imprima a soma de todos os números maiores que 10.
1. Itere sobre uma lista de strings e crie uma nova string que seja a concatenação de todas as strings da lista.

### exercícios de `range()`

1. Use `range()` para imprimir os números de 0 a 10.
1. Use `range()` para imprimir os números de 5 a 15.
1. Use `range()` para imprimir os números pares de 0 a 20.
1. Use `range()` para imprimir os números ímpares de 1 a 19.
1. Use `range()` para imprimir os números de 10 a 0 em ordem decrescente.
1. Use `range()` para criar uma lista de números de 0 a 9 e imprimi-la.
1. Use `range()` para somar todos os números de 1 a 100.
1. Use `range()` para imprimir todos os múltiplos de 3 entre 0 e 30.
1. Use `range()` para criar uma lista de números de 5 a 15 e imprimi-la.
1. Use `range()` para imprimir os números de 0 a 10, com passos de 2.
1. Use `range()` para criar uma lista com os números de 50 a 100, com passos de 5, e imprimi-la.
1. Use `range()` para imprimir os números de 100 a 50 em ordem decrescente.
1. Use `range()` para calcular o produto de todos os números de 1 a 10.
1. Use `range()` para criar uma lista de números de 1 a 9 e imprimi-la.
1. Use `range()` para imprimir os números negativos de -10 a -1.
1. Use `range()` para criar uma lista de números de 0 a 100 com passos de 10 e imprimi-la.
1. Use `range()` para imprimir os números de 5 a 25, com passos de 5.
1. Use `range()` para somar todos os números ímpares entre 0 e 100.
1. Use `range()` para imprimir os números de 10 a 1 em ordem decrescente.
1. Use `range()` para criar uma lista de números de 20 a 30 e imprimi-la.
1. Use `range()` para imprimir os números de 2 a 20, com passos de 2.
1. Use `range()` para calcular a soma dos números múltiplos de 5 entre 0 e 50.
1. Use `range()` para criar uma lista de números de 10 a 100, com passos de 10, e imprimi-la.
1. Use `range()` para imprimir os números de -5 a 5.
1. Use `range()` para criar uma lista com os números de 0 a 9 em ordem reversa e imprimi-la.

### exercícios de `enumerate()`

1. Use `enumerate()` para imprimir cada elemento de uma lista de frutas, junto com seu índice.
1. Use `enumerate()` para imprimir cada letra de uma string, junto com seu índice.
1. Crie uma lista de números e use `enumerate()` para imprimir cada número junto com seu índice.
1. Use `enumerate()` para iterar sobre uma lista de palavras e imprimir o índice das palavras que contêm a letra "a".
1. Crie uma lista de nomes e use `enumerate()` para imprimir cada nome com seu respectivo índice.
1. Use `enumerate()` para criar uma nova lista de lista, onde cada nova lista contém um índice e um valor de uma lista de números.
1. Use `enumerate()` para imprimir os índices e elementos de uma lista de números pares.
1. Use `enumerate()` para iterar sobre uma string e imprimir o índice das letras maiúsculas.
1. Crie uma lista de cidades e use `enumerate()` para imprimir cada cidade com seu respectivo índice.
1. Use `enumerate()` para contar quantos elementos em uma lista de números são maiores que 10.
1. Use `enumerate()` para imprimir os índices e letras de uma string que começam com "p".
1. Crie uma lista de palavras e use `enumerate()` para imprimir o índice das palavras que têm mais de 5 letras.
1. Use `enumerate()` para somar os índices de todos os elementos de uma lista de números.
1. Use `enumerate()` para criar uma nova lista com as letras de uma string, onde o índice é par.
1. Use `enumerate()` para imprimir o índice e o valor de cada elemento em uma lista de números negativos.
1. Use `enumerate()` para criar uma nova lista de strings, onde cada string contém o índice e o valor correspondente.
1. Use `enumerate()` para imprimir os índices dos elementos em uma lista de números que são múltiplos de 3.
1. Use `enumerate()` para iterar sobre uma lista de palavras e imprimir o índice das palavras que começam com "s".
1. Use `enumerate()` para contar quantos elementos em uma lista de números são negativos.
1. Use `enumerate()` para criar uma nova lista onde cada elemento é o dobro do índice original de uma lista de números.
1. Use `enumerate()` para imprimir os índices das letras em uma string que são vogais.
1. Use `enumerate()` para criar uma nova lista de listas, onde cada nova lista contém um índice e uma palavra de uma lista original.
1. Use `enumerate()` para imprimir o índice e o valor dos elementos em uma lista de strings que contêm a letra "e".
1. Use `enumerate()` para iterar sobre uma lista de números e imprimir o índice dos números que são pares.
1. Use `enumerate()` para criar uma nova lista de strings, onde cada string contém o índice e o valor correspondente de uma lista de nomes.

### exercícios de `zip()`

1. Use `zip()` para combinar duas listas de números e imprimir os pares resultantes.
1. Use `zip()` para combinar duas listas de palavras e imprimir os pares resultantes.
1. Use `zip()` para combinar uma lista de números com uma lista de palavras e imprimir os pares.
1. Crie duas listas de nomes e sobrenomes e use `zip()` para combiná-las em uma lista de nomes completos.
1. Use `zip()` para combinar uma string e uma lista de números, imprimindo os pares resultantes.
1. Crie duas listas de números e use `zip()` para somá-los em pares.
1. Use `zip()` para combinar uma lista de palavras com seus respectivos comprimentos.
1. Use `zip()` para iterar sobre duas listas de números e imprimir a multiplicação dos pares.
1. Crie duas listas de cidades e estados e use `zip()` para combiná-las em uma lista de listas.
1. Use `zip()` para combinar uma string e uma lista de índices, imprimindo os pares.
1. Crie duas listas de produtos e preços e use `zip()` para imprimir os produtos com seus preços.
1. Use `zip()` para combinar três listas de números e imprimir as listas resultantes.
1. Use `zip()` para combinar duas strings e imprimir os pares de caracteres.
1. Crie duas listas de números e use `zip()` para criar uma nova lista de listas e imprimir seus pares.
1. Crie duas listas de palavras e use `zip()` para criar uma nova lista onde cada elemento é a concatenação das palavras nas duas listas.
1. Use `zip()` para combinar uma lista de números com uma lista de booleanos e imprimir os pares.
1. Crie duas listas de notas e use `zip()` para calcular a média de cada par de notas.
1. Use `zip()` para combinar três listas de palavras e imprimir as listas resultantes.
1. Crie duas listas de letras e use `zip()` para criar uma string onde as letras das duas listas estejam intercaladas.
1. Use `zip()` para combinar uma lista de nomes com uma lista de idades e imprimir as listas resultantes.
1. Crie duas listas de números e use `zip()` para subtrair os pares e imprimir os resultados.
1. Use `zip()` para combinar uma lista de cidades com uma lista de países e imprimir os pares.
1. Crie duas listas de números e use `zip()` para encontrar o maior número em cada par.
1. Use `zip()` para combinar uma lista de palavras com uma lista de números e imprimir as palavras repetidas de acordo com os números.
1. Crie três listas de strings e use `zip()` para combinar e imprimir as listas formadas pelos elementos correspondentes.

</details>


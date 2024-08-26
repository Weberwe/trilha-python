# comando `for`

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

## `for` e `if-elif-else`

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

</details>


# print

A função `print()` no Python é uma das funções mais fundamentais e amplamente utilizadas. Ela serve para exibir informações na tela, o que é útil tanto para o desenvolvimento e depuração de código quanto para fornecer feedback ao usuário.

## uso básico

A função `print()` exibe os valores que você passa como argumentos, convertendo-os em strings (se necessário) e mostrando-os na tela.

Veja um exemplo básico :

```python
>>> print("Olá, mundo!")
Olá, mundo!
```

Além disso, a função `print()` também possui diversas outras funcionalidades, além de exibir strings e conteúdo de variáveis.

## outras funcionalidades

1. **Exibir Múltiplos Valores** : é possível passar vários argumentos para `print()`, e eles serão exibidos em sequência, separados por um espaço por padrão. Os argumentos podem ser valores literais ou variáveis contendo valores.
    ```python
    >>> print("Python", "é", "nota", 10, "!")
    Python é nota 10 !
    >>>
    >>> nota = 10
    >>> linguagem = "Python"
    >>>
    >>> print(linguagem, "é", 'nota', nota, "!")
    Python é nota 10 !
    ```

1. **Separador Personalizado** : sempre que vários argumentos são passados para o `print()` (separados por vírgulas), por padrão, a função adiciona um espaço em branco entre os argumentos. Contudo, é possível alterar esse comportamento especificando o argumento `sep` logo antes de fechar o parênteses. O valor que for passado ao `sep` deverá ser uma `string`.
    ```python
    >>> print("Python", "é", "incrível!", sep="-")
    Python-é-incrível!
    >>>
    >>> print("Python", "é", "incrível!", sep="_")
    Python_é_incrível!
    >>>
    >>> print("Python", "é", "incrível!", sep=" - ")
    Python - é - incrível!
    ```

1. **Fim da Linha Personalizado** : sempre que se usa o `print()`, por padrão ele adiciona uma nova linha (`\n`) após exibir os valores. Esse comportamento pode ser alterado usando o argumento `end` logo antes de fechar os parênteses. O valor que for passado ao `end` deverá ser uma `string`.
    ```python
    >>> print("Olá,", end=" ")
    >>> print("mundo!")
    Olá, mundo!
    >>>
    >>> nome = 'Arnold Schwarzenegger'
    >>> i = 0  # abreviação de índice
    >>> while i < len(nome):
    ...     print(nome[i], end='+-+')
    ...     i = i + 1
    ...
    A+-+r+-+n+-+o+-+l+-+d+-+ +-+S+-+c+-+h+-+w+-+a+-+r+-+z+-+e+-+n+-+e+-+g+-+g+-+e+-+r+-+
    ```
    Repare que, no exemplo acima, o `print()` dentro do loop `while` adiciona um `+-+` sempre que é executado, mesmo no último caractere do nome.

1. **Combinando** : tanto o `sep` quanto o `end` podem ser usados juntos.
    ```python
    >>> linguagem = 'Python'
    >>> print(linguagem, "é", "incrível", sep="-", end="!")
    Python-é-incrível!>>> |
    ```
    No exemplo acima, é usado o `sep` para adicionar um traço entre cada argumento e é usado o `end` para adicionar o sinal de exclamação ao final da frase. Por causa desse comportamento do `end`, o prompt de entrada do Python fica na mesma linha.

## tudo para string

Qualquer objeto passado para `print()` é convertido em uma string usando a função `str()`. Isso significa que mesmo se você passar um número, uma lista, ou outro tipo de objeto, ele será exibido como uma string correspondente.

```python
>>> numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> valor = 42
>>>
>>> print(valor, numeros)
42 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> |
```

## atividades

<details>
<summary>Lista de Exercícios</summary>

1. exercícios usando o argumento `sep`
    1. Crie três variáveis inteiras e exiba-as usando `print()` com `sep='-'` entre os valores.
    1. Crie uma lista de números inteiros e exiba seus elementos separados por espaços usando `print()` e `sep=' '`.
    1. Crie três variáveis de tipo `float` e exiba-as usando `print()` com `sep=' | '`.
    1. Crie uma lista de strings e exiba os elementos separados por vírgulas usando `print()` e `sep=', '`.
    1. Crie quatro variáveis booleanas e exiba-as usando `print()` com `sep=' & '`.
    1. Crie uma lista de números inteiros e use um loop `while` para exibir os elementos separados por ponto e vírgula (`;`) usando `print()` e `sep=';'`.
    1. Crie três variáveis do tipo `str` e exiba-as usando `print()` com `sep='-'` somente se a primeira variável for igual à segunda.
    1. Crie uma lista de números `float` e exiba os elementos separados por um asterisco (`*`) usando `print()` e `sep='*'`.
    1. Crie uma lista de variáveis booleanas e exiba os elementos separados por dois pontos (`:`) usando `print()` e `sep=':'`.
    1. Crie quatro variáveis do tipo `int`, `float`, `bool` e `str`, e exiba-as usando `print()` com `sep=' -> '`.
1. Exercícios usando o argumento `end`
    1. Crie três variáveis inteiras e exiba-as em uma linha usando `print()` com `end=' '`.
    1. Crie uma lista de strings e exiba cada elemento em uma linha separada, mas sem quebrar a linha ao final, usando `print()` com `end=''`.
    1. Crie duas variáveis `float` e exiba-as com `print()` usando `end='|'` entre elas.
    1. Crie uma lista de variáveis booleanas e use um loop `while` para exibir cada elemento em uma linha, seguido por uma vírgula, usando `print()` com `end=','`.
    1. Crie três variáveis de tipo `str` e exiba-as usando `print()` com `end=' END '`.
    1. Crie uma lista de números inteiros e use um loop `while` para exibir os elementos, cada um seguido de três pontos (`...`), usando `print()` com `end='...'`.
    1. Crie quatro variáveis do tipo `bool`, `int`, `str`, e `float`, e exiba-as usando `print()` com `end=' -> '`.
    1. Crie três variáveis do tipo `float` e exiba-as em uma linha usando `print()` com `end=' | '`.
    1. Crie uma lista de strings e use um loop `while` para exibir cada elemento, seguido por uma barra (`/`), usando `print()` com `end='/'`.
    1. Crie quatro variáveis do tipo `str` e exiba-as em uma linha usando `print()` com `end=' === '`.
1. Exercícios usando `sep` e `end` combinados
    1. Crie três variáveis inteiras e exiba-as em uma linha usando `print()` com `sep='-'` e `end='.'`.
    1. Crie uma lista de strings e exiba os elementos separados por vírgulas e finalizando com um ponto (`.`) usando `print()` com `sep=','` e `end='.'`.
    1. Crie três variáveis do tipo `float` e exiba-as em uma linha usando `print()` com `sep=':'` e `end=' END'`.
    1. Crie uma lista de números inteiros e exiba os elementos separados por espaço e finalizando com três pontos (`...`) usando `print()` com `sep=' '` e `end='...'`.
    1. Crie três variáveis do tipo `bool` e exiba-as em uma linha usando `print()` com `sep=' | '` e `end=' END'`.
    1. Crie uma lista de números `float` e exiba os elementos separados por asteriscos e finalizando com uma barra (`/`) usando `print()` com `sep='*'` e `end='/'`.
    1. Crie quatro variáveis do tipo `str`, `int`, `float`, e `bool`, e exiba-as em uma linha usando `print()` com `sep=' -> '` e `end=' END'`.
    1. Crie uma lista de strings e exiba os elementos separados por vírgulas e finalizando com uma linha em branco usando `print()` com `sep=','` e `end='\n'`.
    1. Crie três variáveis do tipo `str` e exiba-as em uma linha usando `print()` com `sep='-'` e `end=' !'`.
    1. Crie uma lista de números inteiros e exiba os elementos separados por ponto e finalizando com uma mensagem personalizada usando `print()` com `sep='.'` e `end=' - Fim da lista'`.

</details>

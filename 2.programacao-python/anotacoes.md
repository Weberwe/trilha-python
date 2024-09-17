# anotações

Anotações em Python referem-se a uma funcionalidade introduzida na versão 3.0 da linguagem, mas que ganhou maior destaque com a introdução das *type hints* (dicas de tipo) no PEP 484, formalizada a partir do Python 3.5. Elas permitem associar metadados a variáveis, funções e métodos, mas não alteram o comportamento real do código, uma vez que o Python continua sendo uma linguagem de tipagem dinâmica. Em essência, anotações fornecem dicas ou informações adicionais sobre o código, sem impor restrições rígidas.

As anotações por si só não têm impacto na execução do programa; elas são armazenadas em uma estrutura interna (um dicionário chamado `__annotations__`) que pode ser usada por desenvolvedores ou ferramentas para realizar verificações ou introspecção. Elas se integram a frameworks de verificação de tipos, como o `mypy`, e a IDEs que fornecem autocompletar e verificações estáticas de código.

## anotações dos tipos

- **`int`** : para números inteiros;
- **`float`** : para números de ponto flutuante;
- **`bool`** : para valores booleanos (`True` ou `False`);
- **`str`** : para strings (sequências de caracteres);
- **`list`** : para listas, podendo especificar o tipo dos elementos;
- **`tuple`** : para tuplas, onde podemos especificar a quantidade e o tipo de elementos;
- **`dict`** : para dicionários, especificando o tipo das chaves e valores;
- **`set`** : para conjuntos de elementos únicos;
- **`frozenset`** : para conjuntos imutáveis;

## anotações de variáveis

As anotações de variáveis foram formalmente introduzidas no Python 3.6, e permitem que os desenvolvedores especifiquem o tipo de uma variável no momento de sua declaração. Contudo, essas anotações não limitam o valor que pode ser atribuído à variável; elas simplesmente fornecem uma *dica* de qual seria o tipo esperado. O Python, portanto, não rejeitará valores de tipos diferentes do anotado, mantendo sua característica de tipagem dinâmica.

A sintaxe básica para anotar uma variável é:

```python
variavel: Tipo = valor_inicial
```

- `variavel` : é o nome da variável que está sendo anotada;
- `Tipo` : é o tipo que está sendo sugerido para a variável (por exemplo, `int`, `str`, `float`, etc.);
- `valor_inicial` : o valor atribuído à variável, que pode ou não seguir o tipo anotado;

### detalhes

1. **As anotações são opcionais** : as anotações não são obrigatórias, e o Python continuará funcionando normalmente sem elas. Elas são usadas principalmente para fins de documentação e para melhorar a legibilidade do código.

1. **As anotações não são verificadas em tempo de execução** : o Python não realiza nenhuma verificação sobre o tipo anotado em tempo de execução. Isso significa que uma variável anotada como `int` ainda pode receber um valor do tipo `str`, e o Python não lançará erros.

1. **Ferramentas externas podem realizar verificação de tipos** : embora o Python não faça a verificação, ferramentas como o `mypy` podem ser usadas para analisar estaticamente o código e emitir alertas caso haja incompatibilidade de tipos em relação às anotações.

1. **Anotações sem valor inicial** : é possível anotar uma variável sem atribuir um valor a ela no momento da declaração. Isso é útil quando se deseja documentar o tipo de uma variável que será inicializada posteriormente.

### exemplos com cada tipo

#### `int`

O tipo `int` representa números inteiros, sem parte fracionária.

```python
idade: int = 25

print(__annotations__)  # saída : {'idade': <class 'int'>}
```

Aqui, a variável `idade` é anotada como um número inteiro (`int`).

---

#### `float`

O tipo `float` representa números com parte fracionária.

```python
altura: float = 1.75

print(__annotations__)  # saída : {'altura': <class 'float'>}
```

Aqui, a variável `altura` é anotada como um número de ponto flutuante (`float`).

---

#### `bool`

O tipo `bool` é usado para representar valores booleanos: `True` ou `False`.

```python
is_ativo: bool = True

print(__annotations__)  # saída : {'is_ativo': <class 'bool'>}
```

Aqui, a variável `is_ativo` é anotada como um valor booleano (`bool`).

---

#### `str`

O tipo `str` representa uma sequência de caracteres (texto).

```python
nome: str = "João"

print(__annotations__)  # saída : {'nome': <class 'str'>}
```

Aqui, a variável `nome` é anotada como uma string (`str`).

---

#### `list`

O tipo `list` representa uma lista de elementos que pode conter múltiplos valores, de qualquer tipo, mas podemos especificar o tipo dos elementos da lista com anotações de tipo.

```python
notas: list[float] = [7.5, 8.0, 9.2]

print(__annotations__)  # saída : {'notas': <class 'list'>}
```

Aqui, a variável `notas` é anotada como uma lista de números de ponto flutuante (`list[float]`).

---

#### `tuple`

O tipo `tuple` representa uma sequência imutável de elementos. Podemos especificar a quantidade e o tipo dos elementos.

```python
coordenadas: tuple[float, float] = (19.5, 23.0)

print(__annotations__)  # saída : {'coordenadas': <class 'tuple'>}{'coordenadas': <class 'tuple'>}
```

Aqui, a variável `coordenadas` é anotada como uma tupla que contém dois valores do tipo `float`.

---

#### `dict`

O tipo `dict` representa uma coleção de pares chave-valor, onde podemos especificar o tipo das chaves e valores.

```python
notas_por_disciplina: dict[str, float] = {"Matemática": 8.5, "Português": 9.0}

print(__annotations__)  # saída : {'notas_por_disciplina': <class 'dict'>}
```

Aqui, a variável `notas_por_disciplina` é anotada como um dicionário que tem chaves do tipo `str` e valores do tipo `float`.

---

#### `set`

O tipo `set` representa uma coleção não ordenada de elementos únicos.

```python
frutas: set[str] = {"maçã", "banana", "laranja"}

print(__annotations__)  # saída : {'frutas': <class 'set'>}
```

Aqui, a variável `frutas` é anotada como um conjunto (`set`) de strings (`str`).

---

#### `frozenset`

O tipo `frozenset` é como um `set`, mas imutável. Os elementos de um `frozenset` não podem ser alterados após sua criação.

```python
vogais: frozenset[str] = frozenset("aeiou")

print(__annotations__)  # saída : {'vogais': <class 'frozenset'>}
```

Aqui, a variável `vogais` é anotada como um conjunto imutável (`frozenset`) de strings (`str`).

## anotações de funções

As anotações de tipo em funções no Python são usadas para documentar os tipos esperados dos parâmetros e do valor de retorno.

### `int`

Exemplo de parâmetro e retorno com `int` :

```python
def somar(a: int, b: int) -> int:
    return a + b
```

Neste exemplo:
- o tipo dos parâmetros `a` e `b` é `int`, indicando que a função espera receber números inteiros;
- o retorno é anotado como `int`, ou seja, a função retornará um número inteiro;

### `float`

Exemplo de parâmetro e retorno com `float` :

```python
def dividir(a: float, b: float) -> float:
    return a / b
```

Neste exemplo:
- os parâmetros `a` e `b` são do tipo `float`, ou seja, a função espera receber números de ponto flutuante;
- o retorno é `float`, pois a divisão resulta em um número de ponto flutuante;

### `bool`

Exemplo de parâmetro e retorno com `bool` :

```python
def eh_maior(a: int, b: int) -> bool:
    return a > b
```

Neste exemplo:
- os parâmetros `a` e `b` são inteiros (`int`);
- o retorno é `bool`, indicando que a função retorna `True` ou `False`, dependendo do resultado da comparação;

### `str`

Exemplo de parâmetro e retorno com `str` :

```python
def cumprimentar(nome: str) -> str:
    return f"Olá, {nome}!"
```

Neste exemplo:
- o parâmetro `nome` é do tipo `str`, indicando que a função espera uma string (um nome);
- o retorno é uma `str`, que é uma frase de cumprimento;

### `list`

Exemplo de parâmetro com `list` e retorno com `list` :

```python
def dobrar_numeros(numeros: list[int]) -> list[int]:
    return [numero * 2 for numero in numeros]
```

Neste exemplo:
- o parâmetro `numeros` é uma `list[int]`, ou seja, a função espera receber uma lista de números inteiros;
- o retorno também é uma `list[int]`, pois a função retorna uma nova lista com os números inteiros dobrados;

### `tuple`

Exemplo de parâmetro com `tuple` e retorno com `tuple` :

```python
def inverter_coordenadas(coord: tuple[float, float]) -> tuple[float, float]:
    return coord[::-1]
```

Neste exemplo:
- o parâmetro `coord` é uma `tuple[float, float]`, ou seja, a função espera uma tupla com dois números de ponto flutuante;
- o retorno também é uma `tuple[float, float]`, que será a tupla original invertida;

### `dict`

Exemplo de parâmetro com `dict` e retorno com `dict` :

```python
def contar_caracteres(texto: str) -> dict[str, int]:
    return {char: texto.count(char) for char in set(texto)}
```

Neste exemplo:
- o parâmetro `texto` é uma `str`, e a função conta quantas vezes cada caractere aparece no texto;
- o retorno é um `dict[str, int]`, ou seja, um dicionário onde as chaves são caracteres (`str`) e os valores são a quantidade de vezes que aparecem (`int`);

### `set`

Exemplo de parâmetro com `set` e retorno com `set` :

```python
def intersecao_conjuntos(conjunto1: set[int], conjunto2: set[int]) -> set[int]:
    return conjunto1 & conjunto2
```

Neste exemplo:
- os parâmetros `conjunto1` e `conjunto2` são `set[int]`, ou seja, a função espera dois conjuntos de inteiros;
- o retorno é um `set[int]`, representando a interseção dos dois conjuntos (elementos que estão em ambos);

### `frozenset`

Exemplo de parâmetro com `frozenset` e retorno com `frozenset` :

```python
def criar_frozenset(numeros: list[int]) -> frozenset[int]:
    return frozenset(numeros)
```

Neste exemplo:
- o parâmetro `numeros` é uma `list[int]`, ou seja, a função espera uma lista de inteiros;
- o retorno é um `frozenset[int]`, ou seja, um conjunto imutável criado a partir dos números da lista;

---

### `None`

O tipo `None` é usado quando uma função **não retorna nenhum valor**.

Exemplo de função com retorno `None`:

```python
def imprimir_mensagem(mensagem: str) -> None:
    print(mensagem)
```

Neste exemplo:
- o parâmetro `mensagem` é uma `str`, ou seja, a função recebe uma string;
- o retorno é `None`, indicando que a função não retorna nenhum valor; ela apenas imprime a mensagem;

Exemplo de parâmetro `None`:

```python
def processar_valor(valor: int | None) -> int:
    if valor is None:
        return 0
    return valor
```

Neste exemplo:
- O parâmetro `valor` pode ser um número inteiro (`int`) ou `None`, indicando que a função pode receber um valor indefinido.
- O retorno é um `int`, que será o próprio `valor` ou `0` se o parâmetro for `None`.

## exercícios

<details>
<summary>Lista de Exercícios</summary>

1. **Exercícios com `int`**
    1. **Soma de Números**: Escreva uma função que receba dois números inteiros e retorne a soma deles.
    1. **Dobrar um Número**: Crie uma função que receba um número inteiro e retorne o dobro desse número.
    1. **Número Par ou Ímpar**: Escreva uma função que receba um número inteiro e retorne se ele é par ou ímpar.
    1. **Fatorial**: Crie uma função que receba um número inteiro e retorne o seu fatorial.
    1. **Quadrado de um Número**: Faça uma função que receba um número inteiro e retorne o quadrado dele.
1. **Exercícios com `float`**
    1. **Multiplicação de Números**: Escreva uma função que receba dois números de ponto flutuante e retorne o produto deles.
    1. **Conversão de Celsius para Fahrenheit**: Crie uma função que receba uma temperatura em Celsius e retorne em Fahrenheit.
    1. **Divisão de Números**: Escreva uma função que receba dois números de ponto flutuante e retorne o resultado da divisão.
    1. **Área de um Círculo**: Crie uma função que calcule a área de um círculo dado o seu raio (float).
    1. **Média Aritmética**: Faça uma função que receba três números de ponto flutuante e retorne a média aritmética.
1. **Exercícios com `bool`**
    1. **Maior que 10**: Escreva uma função que receba um número inteiro e retorne `True` se ele for maior que 10, caso contrário `False`.
    1. **É Positivo?**: Crie uma função que receba um número de ponto flutuante e retorne `True` se o número for positivo.
    1. **Verificação de Paridade**: Escreva uma função que receba um número inteiro e retorne `True` se o número for par.
    1. **Comparar Números**: Faça uma função que receba dois números e retorne `True` se o primeiro for maior que o segundo.
    1. **Verificação de Feriado**: Crie uma função que receba uma string com o nome do dia da semana e retorne `True` se for "Sábado" ou "Domingo".
1. **Exercícios com `str`**
    1. **Contar Caracteres**: Escreva uma função que receba uma string e retorne o número de caracteres.
    1. **Concatenar Strings**: Crie uma função que receba duas strings e retorne a concatenação delas.
    1. **Inverter String**: Faça uma função que receba uma string e retorne a string invertida.
    1. **Contar Vogais**: Crie uma função que conte o número de vogais em uma string.
    1. **Substituir Espaços por Hífen**: Escreva uma função que substitua todos os espaços de uma string por hífens.
1. **Exercícios com `list`**
    1. **Somar Elementos**: Escreva uma função que receba uma lista de inteiros e retorne a soma dos elementos.
    1. **Maior Elemento**: Crie uma função que receba uma lista de inteiros e retorne o maior valor.
    1. **Duplicar Valores**: Faça uma função que receba uma lista de inteiros e retorne uma nova lista com os valores duplicados.
    1. **Contar Ocorrências**: Escreva uma função que receba uma lista de strings e conte quantas vezes um determinado valor aparece.
    1. **Remover Duplicatas**: Crie uma função que receba uma lista e remova os elementos duplicados.
1. **Exercícios com `tuple`**
    1. **Criar Tupla**: Escreva uma função que receba três valores e retorne uma tupla com esses valores.
    1. **Primeiro e Último Elemento**: Crie uma função que receba uma tupla e retorne o primeiro e o último elemento.
    1. **Tamanho da Tupla**: Faça uma função que receba uma tupla e retorne o tamanho dela.
    1. **Concatenar Tuplas**: Escreva uma função que receba duas tuplas e retorne a concatenação delas.
    1. **Multiplicar Elementos**: Crie uma função que receba uma tupla de números e retorne uma nova tupla com cada elemento multiplicado por 2.
1. **Exercícios com `dict`**
    1. **Criar Dicionário**: Escreva uma função que receba duas listas (chaves e valores) e retorne um dicionário associando-as.
    1. **Valor Máximo**: Crie uma função que receba um dicionário e retorne o valor máximo.
    1. **Contar Itens**: Faça uma função que receba um dicionário e retorne o número de pares chave-valor.
    1. **Atualizar Dicionário**: Escreva uma função que receba um dicionário e uma nova chave e valor, e atualize o dicionário.
    1. **Filtrar Chaves**: Crie uma função que receba um dicionário e uma lista de chaves, e retorne um novo dicionário contendo apenas as chaves especificadas.
1. **Exercícios com `set`**
    1. **Unir Conjuntos**: Escreva uma função que receba dois conjuntos e retorne a união deles.
    1. **Diferença de Conjuntos**: Crie uma função que receba dois conjuntos e retorne a diferença entre eles (itens que estão no primeiro conjunto mas não no segundo).
    1. **Verificar Elemento**: Faça uma função que receba um conjunto e um elemento, e retorne `True` se o elemento estiver no conjunto, caso contrário `False`.
    1. **Interseção de Conjuntos**: Escreva uma função que receba dois conjuntos e retorne a interseção deles (itens que estão em ambos).
    1. **Remover Elementos**: Crie uma função que receba um conjunto e um elemento, e remova o elemento do conjunto se ele estiver presente.
1. **Exercícios com `frozenset`**
    1. **Criar Frozenset**: Escreva uma função que receba uma lista de números e retorne um `frozenset` com esses números.
    1. **Verificar Presença**: Crie uma função que receba um `frozenset` e um número, e retorne `True` se o número estiver no `frozenset`.
    1. **Diferença de Frozensets**: Faça uma função que receba dois `frozensets` e retorne a diferença entre eles (itens que estão no primeiro mas não no segundo).
    1. **Unir Frozensets**: Escreva uma função que receba dois `frozensets` e retorne a união deles.
    1. **Interseção de Frozensets**: Crie uma função que receba dois `frozensets` e retorne a interseção deles (itens que estão em ambos).
1. **Exercícios com `None`**
    1. **Verificar Valor None**: Escreva uma função que receba um valor e retorne `True` se o valor for `None`, caso contrário `False`.
    1. **Retornar None se Vazio**: Crie uma função que receba uma lista e retorne `None` se a lista estiver vazia, caso contrário retorne a lista.
    1. **Ajustar Valor**: Faça uma função que receba um número inteiro e um valor opcional. Se o valor opcional for `None`, defina-o como o número inteiro. Caso contrário, mantenha o valor opcional.
    1. **Função Sem Retorno**: Escreva uma função que não retorna nenhum valor explicitamente, apenas imprime uma mensagem.
    1. **Configuração Opcional**: Crie uma função que receba uma configuração opcional (com valor padrão `None`). Se a configuração for `None`, use um valor padrão interno.

</details>

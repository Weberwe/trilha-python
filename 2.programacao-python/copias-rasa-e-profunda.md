Índice

1. [cópia atribuição direta](#cópia-atribuição-direta)
1. [cópia rasa](#cópia-rasa)
1. [exercícios cópia rasa](#exercícios-cópia-rasa)
1. [cópia profunda](#cópia-profunda)
1. [cópia rasa e profunda em outros tipos](#cópia-rasa-e-profunda-em-outros-tipos)

# operações de cópia

## cópia atribuição direta

A cópia com atribuição direta no Python é uma técnica simples, mas pode ser confusa se não entendida corretamente. Quando se faz uma atribuição direta, como `lista_b = lista_a`, não está criando uma nova lista independente; ao invés disso, está apenas criando uma nova referência ao mesmo objeto na memória. Isso significa que qualquer alteração feita em uma das listas será refletida na outra, pois ambas apontam para o mesmo local na memória.

### exemplo 1 : atribuição direta com objetos imutáveis

Embora a atribuição direta seja mais problemática com objetos mutáveis, é útil entender como ela funciona com objetos imutáveis para contrastar os comportamentos.

```python
>>> a = 10
>>> b = a
>>>
>>> print("Valor de a:", a)
10
>>> print("Valor de b:", b)
10
>>>
>>> b = 20
>>> print("Após mudar b:")
>>> print("Valor de a:", a)
10
>>> print("Valor de b:", b)
20
>>> |
```

**explicação :** neste exemplo, `a` e `b` inicialmente referenciam o mesmo valor imutável `10`. Porém, quando `b` é atribuído a `20`, ele passa a referenciar um novo objeto imutável `20`, enquanto `a` continua referenciando `10`. Isso ocorre porque, para objetos imutáveis, a atribuição direta não afeta o outro nome após a mudança de valor.

### exemplo 2 : atribuição direta com listas (objetos mutáveis)

Vamos explorar o que acontece quando se usa a atribuição direta com listas, que são objetos mutáveis.

```python
>>> lista_a = [1, 2, 3]
>>> lista_b = lista_a
>>>
>>> lista_b.append(4)
>>>
>>> print("Lista A:", lista_a)
[1, 2, 3, 4]
>>> print("Lista B:", lista_b)
[1, 2, 3, 4]
>>> |
```

**explicação :** aqui, `lista_a` e `lista_b` são referências ao mesmo objeto na memória. Portanto, quando se adiciona `4` a `lista_b`, `lista_a` também é alterada, porque ambas as variáveis apontam para a mesma lista.

### exemplo 3 : atribuição direta e modificação interna de listas

Considere um caso em que a lista contém objetos mutáveis, como sublistas:

```python
>>> lista_a = [[1, 2], [3, 4]]
>>> lista_b = lista_a
>>>
>>> lista_b[0].append(99)
>>>
>>> print("Lista A:", lista_a)
[[1, 2, 99], [3, 4]]
>>> print("Lista B:", lista_b)
[[1, 2, 99], [3, 4]]
>>> |
```

**explicação :** novamente, `lista_a` e `lista_b` referenciam o mesmo objeto. Quando se modifica uma das sublistas em `lista_b`, a alteração também aparece em `lista_a` porque as sublistas também são objetos mutáveis que ambas as variáveis referenciam.

### exemplo 4 : verificando referências com `id()`

Pode-se usar a função `id()` para verificar se duas variáveis realmente referenciam o mesmo objeto na memória.

```python
>>> lista_a = [1, 2, 3]
>>> lista_b = lista
>>>
>>> print(f'{id(lista_a) = }')
id(lista_a) = 124121926781376
>>> print(f'{id(lista_b) = }')
id(lista_b) = 124121926781376
>>> |
```

**explicação :** os IDs de `lista_a` e `lista_b` serão os mesmos, confirmando que ambas as variáveis referenciam o mesmo objeto na memória. Ao executar o código acima em sua máquina, certamente os valores dos IDs serão diferentes.

### quando usar atribuição direta

- **quando se deseja que duas variáveis compartilhem a mesma lista :** isso é útil em alguns casos onde se quer que todas as alterações sejam refletidas em ambas as variáveis;

- **em operações de otimização de memória :** atribuição direta é mais eficiente em termos de memória, pois não cria cópias adicionais dos dados;

### limitações da atribuição direta

- **risco de modificações indesejadas :** se não deseja que alterações em uma variável afetem outra, a atribuição direta pode causar problemas difíceis de depurar;

- **não adequado para listas que precisam ser independentes :** se precisa de listas independentes para manipular dados de maneira segura, evite a atribuição direta e opte por técnicas de cópia;

## cópia rasa

A cópia rasa (shallow copy) no Python é um conceito importante quando trabalhamos com listas e outros tipos de dados mutáveis. Embora uma cópia rasa crie uma nova lista, ela não cria cópias independentes dos objetos que estão dentro da lista original; ao invés disso, ela copia as referências para esses objetos. Isso significa que se os elementos dentro da lista forem mutáveis (como outras listas, dicionários ou objetos), modificações nesses elementos afetarão tanto a lista original quanto a cópia.

### como funciona a cópia rasa

Quando se faz uma cópia rasa de uma lista, o Python cria um novo objeto de lista, mas os elementos dentro dessa lista copiada ainda referenciam os mesmos objetos que os elementos da lista original. A cópia rasa é feita em um único nível da estrutura de dados. Se a lista contém objetos mutáveis (como outras listas ou dicionários), as referências para esses objetos são copiadas, mas os próprios objetos não são duplicados.

### exemplo 1 : cópia rasa com objetos imutáveis

Primeiro, veja como a cópia rasa funciona com objetos imutáveis como inteiros e strings:

```python
>>> lista_original = [1, 2, 3, "a", "b", "c"]
>>> lista_copiada = lista_original[:]
>>>
>>> lista_copiada[0] = 100
>>> lista_copiada[3] = "z"
>>>
>>> print("Lista original:", lista_original)
[1, 2, 3, "a", "b", "c"]
>>> print("Lista copiada:", lista_copiada)
[100, 2, 3, "z", "b", "c"]
>>> |
```

**explicação :** neste exemplo, `lista_copiada` é uma cópia rasa de `lista_original`. Como está sendo lidando com objetos imutáveis (inteiros e strings), a modificação em `lista_copiada` não afeta `lista_original`. Isso ocorre porque cada elemento da lista é imutável e, portanto, uma nova cópia do valor é feita na nova lista;

### exemplo 2: cópia rasa com objetos mutáveis (listas)

Agora, veja como a cópia rasa se comporta com objetos mutáveis, como listas aninhadas:

```python
>>> lista_original = [[1, 2, 3], [4, 5, 6]]
>>> lista_copiada = lista_original[:]
>>>
>>> lista_copiada[0].append(99)
>>>
>>> print("Lista original:", lista_original)
[[1, 2, 3, 99], [4, 5, 6]]
>>> print("Lista copiada:", lista_copiada)
[[1, 2, 3, 99], [4, 5, 6]]
>>> |
```

**explicação :** aqui, `lista_original` e `lista_copiada` são listas diferentes. No entanto, os elementos dentro de cada lista (que são eles mesmos listas) ainda referenciam os mesmos objetos na memória. Quando se altera um desses objetos (como adicionar `99` à primeira sublista), essa alteração é refletida em ambas as listas;

### exemplo 3 : cópia rasa com dicionários

O mesmo comportamento ocorre quando se trabalha com dicionários dentro de listas:

```python
>>> lista_original = [{"a": 1, "b": 2}, {"c": 3, "d": 4}]
>>> lista_copiada = lista_original[:]
>>>
>>> lista_copiada[0]["a"] = 100
>>>
>>> print("Lista original:", lista_original)
[{"a": 100, "b": 2}, {"c": 3, "d": 4}]
>>>
>>> print("Lista copiada:", lista_copiada)
[{"a": 100, "b": 2}, {"c": 3, "d": 4}]
>>> |
```

**explicação :** como os dicionários são mutáveis, a modificação feita em um dicionário dentro de `lista_copiada` é refletida em `lista_original`, pois ambos compartilham a referência ao mesmo dicionário;

### exemplo 4 : criando cópias rasas de diferentes formas

Além de usar o fatiamento (`[:]`) para criar uma cópia rasa, também pode usar outras técnicas como a função `list()` ou o método `copy()`:

#### usando `list()`
```python
>>> lista_original = [1, 2, 3]
>>> lista_copiada = list(lista_original)
>>>
>>> lista_copiada[0] = 100
>>>
>>> print("Lista original:", lista_original)
[1, 2, 3]
>>> print("Lista copiada:", lista_copiada)
[100, 2, 3]
>>> |
```

#### usando `copy()`
```python
>>> lista_original = [1, 2, 3]
>>> lista_copiada = lista_original.copy()
>>>
>>> lista_copiada[0] = 100
>>>
>>> print("Lista original:", lista_original)
[1, 2, 3]
>>> print("Lista copiada:", lista_copiada)
[100, 2, 3]
>>> |
```

**explicação :** ambos `list()` e `copy()` criam uma cópia rasa da lista. As mudanças em `lista_copiada` não afetam `lista_original` porque os objetos copiados são valores imutáveis. No entanto, se os objetos fossem mutáveis, as alterações internas ainda seriam compartilhadas;

### quando a cópia rasa é adequada?

- **listas de objetos imutáveis :** se a lista contém apenas objetos imutáveis (como números ou strings), a cópia rasa geralmente é segura e eficiente;

- **listas de objetos mutáveis com cuidado :** se precisar de uma nova lista, mas não se importa em compartilhar referências para objetos mutáveis dentro dessa lista, a cópia rasa é adequada;

### limitações da cópia rasa

A principal limitação da cópia rasa é que, para listas que contêm objetos mutáveis, as modificações nesses objetos refletirão tanto na lista original quanto na cópia. Se precisar de cópias independentes dos objetos internos, será necessário usar uma cópia profunda.

## exercícios cópia rasa

<details>
<summary>Lista de Exercícios</summary>

1. **Cópia de Lista Simples**: Dada a lista `original = [1, 2, 3, 4]`, faça uma cópia rasa dela e adicione o número 5 na cópia. Imprima ambas.
1. **Cópia de Tupla**: Dada a tupla `original = (1, 2, 3, 4)`, faça uma cópia rasa dela e modifique o valor do primeiro item da tupla original para 0. Imprima ambas.
1. **Cópia de Set**: Dado o conjunto `original = {1, 2, 3, 4}`, faça uma cópia rasa dele e adicione o número 5 à cópia. Imprima ambos.
1. **Cópia de Dicionário**: Dado o dicionário `original = {'a': 1, 'b': 2}`, faça uma cópia rasa dele e adicione uma nova chave `'c'` com valor 3 à cópia. Imprima ambos.
1. **Cópia de String**: Dada a string `original = "Python"`, faça uma cópia rasa dela e modifique o valor da cópia. Imprima ambas.
1. **Cópia de Lista com Sublista**: Dada a lista `original = [[1, 2], [3, 4]]`, faça uma cópia rasa dela e modifique o primeiro elemento da sublista na cópia. Imprima ambas.
1. **Cópia de Tupla com Lista**: Dada a tupla `original = ([1, 2], [3, 4])`, faça uma cópia rasa dela e modifique um valor na lista da cópia. Imprima ambas.
1. **Cópia de Set com Strings**: Dado o conjunto `original = {"apple", "banana"}`, faça uma cópia rasa dele e adicione um novo item à cópia. Imprima ambos.
1. **Cópia de Dicionário com Listas**: Dado o dicionário `original = {'numbers': [1, 2], 'letters': ['a', 'b']}`, faça uma cópia rasa dele e adicione um item à lista de números na cópia. Imprima ambos.
1. **Cópia de Lista com Strings**: Dada a lista `original = ["Python", "Java"]`, faça uma cópia rasa dela e substitua um item na cópia. Imprima ambas.
1. **Cópia de Tupla com Tuplas**: Dada a tupla `original = ((1, 2), (3, 4))`, faça uma cópia rasa dela e substitua um item na tupla da cópia. Imprima ambas.
1. **Cópia de Set com Números**: Dado o conjunto `original = {10, 20, 30}`, faça uma cópia rasa dele e remova um item da cópia. Imprima ambos.
1. **Cópia de Dicionário com Tuplas**: Dado o dicionário `original = {'coordinates': (10, 20), 'color': 'red'}`, faça uma cópia rasa dele e modifique um valor na cópia. Imprima ambos.
1. **Cópia de Lista com Dicionários**: Dada a lista `original = [{'a': 1}, {'b': 2}]`, faça uma cópia rasa dela e adicione uma nova chave a um dicionário na cópia. Imprima ambas.
1. **Cópia de Tupla com Set**: Dada a tupla `original = ({1, 2}, {3, 4})`, faça uma cópia rasa dela e adicione um item a um set na cópia. Imprima ambos.
1. **Cópia de Lista com Strings e Números**: Dada a lista `original = ["apple", 1, "banana", 2]`, faça uma cópia rasa dela e substitua um item na cópia. Imprima ambas.
1. **Cópia de Set com Dicionários**: Dado o conjunto `original = {{'a': 1}, {'b': 2}}`, faça uma cópia rasa dele e modifique um valor em um dicionário na cópia. Imprima ambos.
1. **Cópia de Dicionário com Listas Aninhadas**: Dado o dicionário `original = {'list1': [1, 2], 'list2': [3, 4]}`, faça uma cópia rasa dele e adicione um item a uma lista na cópia. Imprima ambos.
1. **Cópia de Lista com Tuplas Aninhadas**: Dada a lista `original = [(1, 2), (3, 4)]`, faça uma cópia rasa dela e substitua uma tupla na cópia. Imprima ambas.
1. **Cópia de Tupla com Listas e Dicionários**: Dada a tupla `original = ([1, 2], {'a': 3})`, faça uma cópia rasa dela e adicione um item à lista na cópia. Imprima ambas.
1. **Cópia de Lista com Booleans**: Dada a lista `original = [True, False]`, faça uma cópia rasa dela e altere um valor na cópia. Imprima ambas.
1. **Cópia de Tupla com Sets e Strings**: Dada a tupla `original = ({'apple'}, "banana")`, faça uma cópia rasa dela e adicione um item ao set na cópia. Imprima ambas.
1. **Cópia de Set com Strings e Números**: Dado o conjunto `original = {1, "apple", 2, "banana"}`, faça uma cópia rasa dele e remova um item da cópia. Imprima ambos.
1. **Cópia de Dicionário com Strings e Números**: Dado o dicionário `original = {'string': 'hello', 'number': 42}`, faça uma cópia rasa dele e modifique um valor na cópia. Imprima ambos.
1. **Cópia de Lista com Strings e Tuplas**: Dada a lista `original = ["hello", (1, 2), "world"]`, faça uma cópia rasa dela e substitua um item na cópia. Imprima ambas.
1. **Cópia de Tupla com Lista e Set**: Dada a tupla `original = ([1, 2], {3, 4})`, faça uma cópia rasa dela e modifique a lista na cópia. Imprima ambas.
1. **Cópia de Lista com Tuplas e Strings**: Dada a lista `original = [(1, 2), "foo", (3, 4)]`, faça uma cópia rasa dela e substitua um item na cópia. Imprima ambas.
1. **Cópia de Set com Inteiros e Strings**: Dado o conjunto `original = {1, 2, "a", "b"}`, faça uma cópia rasa dele e adicione um item à cópia. Imprima ambos.
1. **Cópia de Dicionário com Tuplas Aninhadas**: Dado o dicionário `original = {'pair1': (1, 2), 'pair2': (3, 4)}`, faça uma cópia rasa dele e substitua um valor na tupla da cópia. Imprima ambos.
1. **Cópia de Lista com Números e Strings**: Dada a lista `original = [1, "text", 3.5, "example"]`, faça uma cópia rasa dela e substitua um item na cópia. Imprima ambas.

</details>

## cópia profunda

<!--

A cópia profunda (deep copy) no Python é uma técnica usada para criar uma nova lista ou estrutura de dados que é completamente independente da original. Ao contrário da cópia rasa, que copia apenas as referências aos objetos contidos na lista original, a cópia profunda cria cópias reais e independentes desses objetos, resultando em uma duplicata completa e separada da estrutura de dados original.

### como funciona a cópia profunda

Quando você realiza uma cópia profunda de uma lista, o Python cria um novo objeto de lista, e então copia recursivamente todos os elementos dessa lista original. Se algum desses elementos for uma estrutura de dados mutável, como outra lista ou dicionário, ele também será copiado em profundidade, garantindo que a nova lista seja totalmente independente da original.

Para realizar uma cópia profunda em Python, utilizamos o módulo `copy` e sua função `deepcopy`.

### Importando a Função `deepcopy`

Antes de utilizá-la, é necessário importar a função `deepcopy` do módulo `copy`:

```python
import copy
```

### Exemplo 1: Cópia Profunda de uma Lista Simples

Vamos começar com um exemplo básico de cópia profunda:

```python
import copy

lista_original = [1, 2, 3, 4]
lista_copiada = copy.deepcopy(lista_original)

lista_copiada.append(5)

print("Lista original:", lista_original)  # Saída: [1, 2, 3, 4]
print("Lista copiada:", lista_copiada)    # Saída: [1, 2, 3, 4, 5]
```

**Explicação:** Aqui, `lista_copiada` é uma cópia profunda de `lista_original`. Como estamos lidando com objetos imutáveis (inteiros), o comportamento parece semelhante à cópia rasa. A diferença se torna mais evidente quando lidamos com objetos mutáveis.

### Exemplo 2: Cópia Profunda com Listas Aninhadas

Agora vamos ver o comportamento da cópia profunda com listas aninhadas:

```python
import copy

lista_original = [[1, 2, 3], [4, 5, 6]]
lista_copiada = copy.deepcopy(lista_original)

lista_copiada[0].append(99)

print("Lista original:", lista_original)  # Saída: [[1, 2, 3], [4, 5, 6]]
print("Lista copiada:", lista_copiada)    # Saída: [[1, 2, 3, 99], [4, 5, 6]]
```

**Explicação:** Neste exemplo, `lista_copiada` é uma cópia profunda de `lista_original`. Isso significa que `lista_copiada` é completamente independente, incluindo as sublistas. Quando você modifica uma sublista em `lista_copiada`, a sublista correspondente em `lista_original` permanece inalterada.

### Exemplo 3: Cópia Profunda com Dicionários em Listas

A cópia profunda também é importante quando você está lidando com listas que contêm dicionários:

```python
import copy

lista_original = [{"a": 1, "b": 2}, {"c": 3, "d": 4}]
lista_copiada = copy.deepcopy(lista_original)

lista_copiada[0]["a"] = 100

print("Lista original:", lista_original)  # Saída: [{"a": 1, "b": 2}, {"c": 3, "d": 4}]
print("Lista copiada:", lista_copiada)    # Saída: [{"a": 100, "b": 2}, {"c": 3, "d": 4}]
```

**Explicação:** No caso de `lista_copiada`, qualquer alteração feita nos dicionários contidos dentro da lista não afetará `lista_original`, pois cada dicionário foi duplicado completamente.

### Exemplo 4: Cópia Profunda com Estruturas de Dados Complexas

Vamos considerar uma estrutura de dados mais complexa, como uma lista contendo outras listas, dicionários, e até mesmo tuplas:

```python
import copy

lista_original = [[1, 2], {"chave": [3, 4]}, (5, 6)]
lista_copiada = copy.deepcopy(lista_original)

lista_copiada[0].append(99)
lista_copiada[1]["chave"].append(100)

print("Lista original:", lista_original)  # Saída: [[1, 2], {"chave": [3, 4]}, (5, 6)]
print("Lista copiada:", lista_copiada)    # Saída: [[1, 2, 99], {"chave": [3, 4, 100]}, (5, 6)]
```

**Explicação:** Neste exemplo, `lista_copiada` é uma cópia profunda de `lista_original`. Modificações feitas na cópia (como adicionar `99` à primeira sublista ou `100` ao valor da chave no dicionário) não afetam a lista original.

### Exemplo 5: Cópia Profunda e Objetos Personalizados

A cópia profunda também funciona com objetos de classes personalizadas, desde que esses objetos possam ser copiados.

```python
import copy

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Ponto({self.x}, {self.y})"

ponto_original = Ponto(1, 2)
lista_original = [ponto_original]

lista_copiada = copy.deepcopy(lista_original)

lista_copiada[0].x = 10
lista_copiada[0].y = 20

print("Lista original:", lista_original)  # Saída: [Ponto(1, 2)]
print("Lista copiada:", lista_copiada)    # Saída: [Ponto(10, 20)]
```

**Explicação:** `lista_copiada` aqui é uma cópia profunda de `lista_original`, incluindo o objeto `Ponto`. Alterar o objeto na cópia não afeta o objeto na lista original.

### Quando Usar Cópia Profunda

- **Quando você precisa de uma duplicação completa e independente:** Se você está lidando com uma estrutura de dados complexa e quer garantir que a cópia seja totalmente separada do original, a cópia profunda é o caminho.

- **Quando há objetos mutáveis aninhados:** Se a lista ou estrutura de dados contém listas, dicionários ou outros objetos mutáveis, a cópia profunda garantirá que todas as partes da estrutura sejam independentes.

### Limitações da Cópia Profunda

- **Desempenho:** A cópia profunda pode ser significativamente mais lenta e consumir mais memória do que a cópia rasa, especialmente para estruturas de dados grandes e complexas.

- **Complexidade:** Em casos onde não é necessário duplicar completamente todos os objetos internos, a cópia profunda pode ser excessiva.

-->

## cópia rasa e profunda em outros tipos

O conceito de cópia rasa e cópia profunda se aplica principalmente a estruturas de dados mutáveis, como listas e dicionários.

### tuplas

Tuplas são estruturas de dados imutáveis no Python. Por causa dessa imutabilidade, o conceito de cópia rasa e cópia profunda não se aplica da mesma forma que para listas.

- **cópia rasa :** para tuplas, uma cópia rasa é feita por atribuição direta, e não há necessidade de técnicas especiais para cópias rasas ou profundas, pois está apenas criando uma nova referência ao mesmo objeto imutável;
    ```python
    >>> tupla_original = (1, 2, 3)
    >>> tupla_copiada = tupla_original
    >>>
    >>> print("Tupla original:", tupla_original)
    (1, 2, 3)
    >>> print("Tupla copiada:", tupla_copiada)
    (1, 2, 3)
    >>> |
    ```
    **explicação :** a tupla `tupla_copiada` é uma nova referência à mesma tupla imutável. Não há necessidade de cópia rasa ou profunda aqui.

- **cópia profunda :**
<!--como tuplas são imutáveis e não podem ser alteradas após a criação, uma cópia profunda não é necessária ou aplicável. se a tupla contém objetos mutáveis (como listas), você ainda precisa considerar o impacto desses objetos na cópia, mas a tupla em si não precisa de uma cópia profunda.-->

### dicionários

Dicionários são mutáveis e, portanto, podem se beneficiar das técnicas de cópia rasa e profunda.

- **cópia rasa :** para fazer uma cópia rasa de um dicionário, pode-se usar o método `copy()` ou a função `dict()`.
    ```python
    >>> dicionario_original = {"a": 1, "b": [2, 3]}
    >>> dicionario_copiado = dicionario_original.copy()
    >>>
    >>> dicionario_copiado["b"].append(4)
    >>>
    >>> print("Dicionário original:", dicionario_original)
    {"a": 1, "b": [2, 3, 4]}
    >>> print("Dicionário copiado:", dicionario_copiado)
    {"a": 1, "b": [2, 3, 4]}
    >>> |
    ```
    **explicação :** a cópia rasa do dicionário cria um novo dicionário onde as referências para os objetos dentro do dicionário original são copiadas. Mudanças nos objetos mutáveis (como a lista associada à chave `"b"`) afetam ambos os dicionários.

- **cópia profunda :**
<!-- para criar uma cópia profunda de um dicionário, você pode usar `copy.deepcopy()`.

  ```python
  import copy

  dicionario_original = {"a": 1, "b": [2, 3]}
  dicionario_copiado = copy.deepcopy(dicionario_original)

  dicionario_copiado["b"].append(4)

  print("Dicionário original:", dicionario_original)  # Saída: {"a": 1, "b": [2, 3]}
  print("Dicionário copiado:", dicionario_copiado)    # Saída: {"a": 1, "b": [2, 3, 4]}
  ```

  **Explicação:** A cópia profunda cria um novo dicionário com cópias independentes dos objetos internos. Modificar a lista no dicionário copiado não afeta a lista no dicionário original.
-->
### sets

Sets são mutáveis, e o conceito de cópia rasa e profunda também se aplica a eles.

- **cópia rasa :** para fazer uma cópia rasa de um set, pode-se usar o método `copy()` ou a função `set()`.
    ```python
    >>> set_original = {1, 2, 3}
    >>> set_copiado = set_original.copy()
    >>>
    >>> set_copiado.add(4)
    >>>
    >>> print("Set original:", set_original)
    {1, 2, 3}
    >>> print("Set copiado:", set_copiado)
    {1, 2, 3}
    >>> |
    ```
    **explicação :** a cópia rasa do set cria um novo set, mas não copia objetos mutáveis que possam estar dentro do set. neste caso, os sets contêm apenas inteiros, que são imutáveis.

- **cópia profunda :**
<!--para sets, a cópia profunda não é frequentemente necessária, pois sets não podem conter objetos complexos que precisem de uma cópia profunda. se um set contém objetos mutáveis, você pode usar `copy.deepcopy()` para garantir uma cópia completamente independente.

  ```python
  import copy

  set_original = {frozenset([1, 2]), frozenset([3, 4])}
  set_copiado = copy.deepcopy(set_original)

  set_copiado.add(frozenset([5, 6]))

  print("Set original:", set_original)  # Saída: {frozenset({1, 2}), frozenset({3, 4})}
  print("Set copiado:", set_copiado)    # Saída: {frozenset({1, 2}), frozenset({3, 4}), frozenset({5, 6})}
  ```

  **Explicação:** A cópia profunda garante que o set copiado não compartilhe referências com o set original, mas, na prática, sets geralmente não precisam de cópia profunda porque eles não contêm tipos complexos mutáveis.
-->
### resumo

- **tuplas :** imutáveis, não requerem cópia rasa ou profunda;
- **dicionários :** mutáveis, podem se beneficiar de cópias rasas e profundas;
- **sets :** mutáveis, cópias rasas são comuns e cópias profundas podem ser usadas se o set contiver objetos complexos;

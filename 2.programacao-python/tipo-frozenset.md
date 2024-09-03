Índice

1. [características do frozenset](#características-do-frozenset)
1. [criando um frozenset](#criando-um-frozenset)
1. [operações com frozensets](#operações-com-frozensets)
1. [métodos do frozenset](#métodos-do-frozenset)
    1. [frozenset.copy()](#frozensetcopy)
    1. [frozenset.union()](#frozensetunion)
    1. [frozenset.intersection()](#frozensetintersection)
    1. [frozenset.difference()](#frozensetdifference)
    1. [frozenset.issubset()](#frozensetissubset)
    1. [frozenset.issuperset()](#frozensetissuperset)
    1. [frozenset.isdisjoint()](#frozensetisdisjoint)
1. [aplicações práticas](#aplicações-práticas)
1. [limitações](#limitações)
1. [exercícios](#exercícios)

# `frozenset`

O tipo `frozenset` no Python é uma variação imutável do tipo `set`. Enquanto os conjuntos (`sets`) são coleções de elementos que não permitem duplicatas e cujas ordens não são garantidas, os `frozensets` adicionam a característica de imutabilidade a essa estrutura, tornando os elementos dentro dela impossíveis de serem modificados após sua criação.

## características do `frozenset`

- **imutabilidade** : ao contrário de um `set`, um `frozenset` não pode ser alterado depois de criado. Isso significa que não se pode adicionar, remover ou modificar elementos dentro de um `frozenset` após a sua criação;

- **sem elementos duplicados** : assim como os `sets`, `frozensets` não permitem elementos duplicados. se tentar criar um `frozenset` com elementos repetidos, ele automaticamente removerá as duplicatas;

- **ordenação indefinida** : os elementos dentro de um `frozenset` não têm uma ordem específica. mesmo que os insira em uma determinada ordem, eles podem não ser recuperados nessa mesma ordem;

- **hashable** : como os `frozensets` são imutáveis, eles são hashable. isso significa que um `frozenset` pode ser usado como chave em um dicionário ou como elemento em outro `set`;

## criando um `frozenset`

Pode-se criar um `frozenset` de diferentes maneiras:

1. **a partir de um set ou outro iterável** :
    ```python
    >>> fs = frozenset({1, 2, 3, 4})
    >>> print(fs)
    frozenset({1, 2, 3, 4})
    >>> |
    ```

2. **a partir de uma lista** :
    ```python
    >>> fs = frozenset([1, 2, 3, 3, 4])
    >>> print(fs)
    frozenset({1, 2, 3, 4})
    >>> |
    ```

3. **a partir de uma string** :
    ```python
    >>> fs = frozenset("abracadabra")
    >>> print(fs)
    frozenset({'a', 'r', 'b', 'c', 'd'})
    >>> |
    ```

## operações com `frozensets`

Mesmo sendo imutáveis, ainda pode-se realizar várias operações com `frozensets`, muitas das quais são similares às operações que se pode fazer com `sets`.

- **união (`|`)** :
    Combina todos os elementos de dois `frozensets` sem duplicação.
    ```python
    >>> fs1 = frozenset({1, 2, 3})
    >>> fs2 = frozenset({3, 4, 5})
    >>> fs3 = fs1 | fs2
    >>> print(fs3)
    frozenset({1, 2, 3, 4, 5})
    >>> |
    ```

- **interseção (`&`)** :
    Retorna apenas os elementos que estão presentes em ambos os `frozensets`.
    ```python
    >>> fs1 = frozenset({1, 2, 3})
    >>> fs2 = frozenset({2, 3, 4})
    >>> fs3 = fs1 & fs2
    >>> print(fs3)
    frozenset({2, 3})
    >>> |
    ```

- **diferença (`-`)** :
    Retorna os elementos que estão no primeiro `frozenset`, mas não no segundo.
    ```python
    >>> fs1 = frozenset({1, 2, 3})
    >>> fs2 = frozenset({2, 3, 4})
    >>> fs3 = fs1 - fs2
    >>> print(fs3)
    frozenset({1})
    >>> |
    ```

- **diferença simétrica (`^`)** :
    Retorna os elementos que estão em um `frozenset` ou no outro, mas não em ambos.
    ```python
    >>> fs1 = frozenset({1, 2, 3})
    >>> fs2 = frozenset({2, 3, 4})
    >>> fs3 = fs1 ^ fs2
    >>> print(fs3)
    frozenset({1, 4})
    >>> |
    ```

## métodos do frozenset

Apesar de sua imutabilidade, `frozensets` ainda possuem alguns métodos úteis, tais como:

### `frozenset.copy()`

Retorna uma cópia do `frozenset`.
```python
>>> fs = frozenset({1, 2, 3})
>>> fs_copy = fs.copy()
>>> print(fs_copy)
frozenset({1, 2, 3})
>>> |
```

### `frozenset.union()`

Retorna a união com outros `sets` ou `frozensets`.
```python
>>> fs1 = frozenset({1, 2, 3})
>>> fs2 = frozenset({3, 4, 5})
>>> fs3 = fs1.union(fs2)
>>> print(fs3)
frozenset({1, 2, 3, 4, 5})
>>> |
```

### `frozenset.intersection()`

Retorna a interseção com outros `sets` ou `frozensets`.
```python
>>> fs1 = frozenset({1, 2, 3})
>>> fs2 = frozenset({2, 3, 4})
>>> fs3 = fs1.intersection(fs2)
>>> print(fs3)
frozenset({2, 3})
>>> |
```

### `frozenset.difference()`

Retorna a diferença com outros `sets` ou `frozensets`.
```python
>>> fs1 = frozenset({1, 2, 3})
>>> fs2 = frozenset({2, 3, 4})
>>> fs3 = fs1.difference(fs2)
>>> print(fs3)
frozenset({1})
>>> |
```

### `frozenset.issubset()`

Verifica se o `frozenset` é um subconjunto de outro.
```python
>>> fs1 = frozenset({1, 2})
>>> fs2 = frozenset({1, 2, 3})
>>> print(fs1.issubset(fs2))
True
>>> |
```

### `frozenset.issuperset()`

Verifica se o `frozenset` é um superconjunto de outro.
```python
>>> fs1 = frozenset({1, 2, 3})
>>> fs2 = frozenset({1, 2})
>>> print(fs1.issuperset(fs2))
True
>>> |
```

### `frozenset.isdisjoint()`

Verifica se dois `frozensets` não têm elementos em comum.
```python
>>> fs1 = frozenset({1, 2})
>>> fs2 = frozenset({3, 4})
>>> print(fs1.isdisjoint(fs2))
True
>>> |
```

## aplicações práticas

- **uso como chaves de dicionário** : como `frozensets` são imutáveis e hashable, eles podem ser usados como chaves de dicionários, ao contrário de `sets` comuns.
    ```python
    >>> my_dict = {}
    >>> fs = frozenset({1, 2, 3})
    >>> my_dict[fs] = "valor associado ao frozenset"
    >>> print(my_dict)
    {frozenset({1, 2, 3}): 'valor associado ao frozenset'}
    >>> |
    ```

- **operações que requerem imutabilidade** : sempre que precisa garantir que um conjunto de valores não será alterado, um `frozenset` é uma escolha ideal.

## limitações

Devido à imutabilidade, métodos como `add()`, `remove()`, `pop()`, e outros que alterariam um conjunto não estão disponíveis para `frozensets`.

## exercícios

<details>
<summary>Lista de Exercícios</summary>

1. Exercícios Básicos
    1. **Criando um `frozenset`**: Crie um `frozenset` a partir de uma lista de números `[1, 2, 3, 4, 5]` e imprima-o.
    1. **Eliminando duplicatas**: Crie um `frozenset` a partir da lista `[1, 2, 2, 3, 4, 4, 5]` e mostre o resultado.
    1. **Conversão de string para `frozenset`**: Converta a string `"abracadabra"` em um `frozenset` e imprima-o.
    1. **Verificação de imutabilidade**: Tente adicionar um novo elemento ao `frozenset` `{1, 2, 3}` e observe o que acontece.
    1. **Comparando `sets` e `frozensets`**: Crie um `set` e um `frozenset` com os mesmos elementos e verifique se são iguais.
1. Operações com `frozensets`
    1. **União de `frozensets`**: Crie dois `frozensets`, `{1, 2, 3}` e `{3, 4, 5}`, e faça a união entre eles.
    1. **Interseção de `frozensets`**: Crie dois `frozensets`, `{1, 2, 3}` e `{2, 3, 4}`, e encontre a interseção entre eles.
    1. **Diferença entre `frozensets`**: Crie dois `frozensets`, `{1, 2, 3}` e `{3, 4, 5}`, e calcule a diferença entre eles (`fs1 - fs2`).
    1. **Diferença simétrica**: Crie dois `frozensets`, `{1, 2, 3}` e `{2, 3, 4}`, e calcule a diferença simétrica entre eles.
    1. **União de vários `frozensets`**: Crie três `frozensets`, `{1, 2}`, `{2, 3}` e `{3, 4}`, e faça a união de todos.
1. Verificação e Comparação
    1. **Verificando subconjunto**: Verifique se o `frozenset` `{1, 2}` é um subconjunto de `{1, 2, 3}`.
    1. **Verificando superconjunto**: Verifique se o `frozenset` `{1, 2, 3}` é um superconjunto de `{1, 2}`.
    1. **Conjuntos disjuntos**: Verifique se os `frozensets` `{1, 2}` e `{3, 4}` são disjuntos.
    1. **Comparação de `frozensets`**: Compare os `frozensets` `{1, 2, 3}` e `{3, 2, 1}` e verifique se são iguais.
    1. **Verificando existência de elemento**: Verifique se o número `3` está presente no `frozenset` `{1, 2, 3, 4}`.
1. Aplicações Práticas
    1. **Usando `frozenset` como chave de dicionário**: Crie um dicionário onde as chaves são `frozensets` e os valores são strings. Atribua o valor `"grupo1"` para a chave `frozenset({1, 2, 3})`.
    1. **Criando um `frozenset` a partir de uma lista de tuplas**: Converta uma lista de tuplas `[(1, 2), (2, 3), (3, 4)]` em um `frozenset`.
    1. **Ordenando elementos de um `frozenset`**: Crie um `frozenset` a partir dos números `[4, 1, 3, 2]` e exiba os elementos em ordem crescente.
    1. **Verificando imutabilidade dentro de uma lista**: Crie uma lista que contém um `frozenset` e tente modificar o `frozenset` dentro da lista. O que acontece?
    1. **Criando `frozensets` a partir de diferentes tipos de dados**: Crie `frozensets` a partir de uma string, uma lista e uma tupla, e compare os resultados.
1. Desafios
    1. **Removendo duplicatas de uma lista de listas**: Suponha que você tem uma lista de listas `[[1, 2], [2, 3], [1, 2]]`. Use `frozensets` para eliminar as listas duplicadas.
    1. **Comparando frozensets com subsets**: Dado dois `frozensets`, `{1, 2, 3}` e `{1, 2}`, verifique se o segundo é subconjunto do primeiro e depois faça a união dos dois.
    1. **Verificação de pertença em dicionário**: Dado um dicionário onde as chaves são `frozensets`, verifique se um `frozenset` específico é uma chave no dicionário.
    1. **Frozenset a partir de outra coleção**: Crie um `frozenset` a partir de um `set` que contém os elementos `{1, 2, 3}`. Depois, tente alterar o `set` original e verifique se o `frozenset` foi afetado.
    1. **Comparação entre diferentes coleções**: Crie um `frozenset`, um `set` e uma lista com os mesmos elementos e verifique como eles se comportam em operações como união, interseção e diferença.
    1. **Trabalhando com caracteres únicos**: Converta a string `"banana"` em um `frozenset` e conte quantos caracteres únicos há.
    1. **Analisando frozensets aninhados**: Crie um `frozenset` que contém outros `frozensets` como elementos. Exiba o resultado e discuta o que você observa.
    1. **Uso de `frozenset` em conjunto com `map`**: Use `map()` para aplicar uma função que retorna o quadrado de cada número em um `frozenset`.
    1. **Conversão e comparação de coleções**: Converta uma lista de números `[1, 2, 3, 4]` para um `frozenset`, e compare-o com outro `frozenset` que você cria diretamente.
    1. **Verificação de imutabilidade em operações**: Crie um `frozenset` e realize operações de união e interseção com outros conjuntos. Verifique se o `frozenset` original foi alterado após essas operações.

</details>


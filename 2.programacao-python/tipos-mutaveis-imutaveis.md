# tipos mutáveis e imutáveis

## tipos imutáveis

Os tipos **imutáveis** em Python são aqueles cujos valores não podem ser alterados após sua criação. Quando se altera um valor, o Python cria um novo objeto em vez de modificar o objeto existente. Isso tem implicações importantes para a maneira como se lida com variáveis e objetos no Python.

Os principais tipos imutáveis em Python são :

1. **números (inteiros e ponto flutuante)**
1. **strings (`str`)**
1. **tuplas (`tuple`)**
1. **frozensets (`frozenset`)**

### 1. números

Os tipos numéricos imutáveis em Python incluem inteiros (`int`), números de ponto flutuante (`float`), e números complexos (`complex`).

Exemplos :

```python
>>> x = 10  # inteiro
>>> y = 3.14  # ponto flutuante
>>> z = 1 + 2j  # número complexo
```

Se alterar o valor de uma variável numérica, um novo objeto é criado. O objeto antigo permanece inalterado, e a variável passa a referenciar o novo objeto.

```python
>>> x = 10
>>> x = 20
>>> # x agora referencia um novo objeto (20)
```

Qualquer operação que pareça alterar o valor de um número cria um novo objeto e não modifica o objeto original.

### 2. strings (`str`)

Strings são sequências imutáveis de caracteres. Elas são definidas usando aspas simples `'` ou duplas `"`.

Exemplo :

```python
>>> s = "Olá, Mundo!"
```

Operações como concatenação, repetição, ou substituição de caracteres criam novas strings em vez de alterar a string original.

```python
>>> s = "Olá"
>>> s = s + " Mundo"
>>> # cria uma nova string "Olá Mundo"
```

Strings não podem ser alteradas após a criação. Qualquer operação que pareça modificar a string resultará em uma nova string.

### 3. tuplas (`tuple`)

Tuplas são coleções ordenadas e imutáveis de elementos. São definidas usando parênteses `()` e os elementos são separados por vírgulas.

Exemplo :

```python
>>> t = (1, 2, 3, "quatro")
```

Não se pode alterar os elementos de uma tupla uma vez que ela é criada. Se precisar modificar uma tupla, terá que criar uma nova.

```python
>>> t = (1, 2, 3)
>>> # t[1] = 4  # isso resultaria em um erro
>>> t = (1, 4, 3)  # cria uma nova tupla
```

Qualquer tentativa de alterar os elementos da tupla ou sua estrutura resulta em um erro.

### 4. frozensets (`frozenset`)

Frozensets são conjuntos imutáveis. Ao contrário dos conjuntos normais, eles não permitem alterações após sua criação.

Exemplo

```python
>>> fs = frozenset([1, 2, 3, 4])
```

Não se pode adicionar, remover ou modificar elementos em um frozenset após sua criação. Qualquer tentativa de alteração resulta em um erro.

```python
>>> fs = frozenset([1, 2, 3])
>>> # fs.add(4)  # Isso resultaria em um erro
```

Frozensets são úteis quando se precisa de um conjunto cujos elementos não mudem ao longo do tempo e é importante que o conjunto possa ser usado como chave em um dicionário ou elemento em outro conjunto.

## tipos mutáveis

Em Python, um **tipo mutável** é um tipo de dado cujos valores podem ser alterados após sua criação. Diferente dos tipos imutáveis, onde qualquer alteração resulta na criação de um novo objeto, os tipos mutáveis permitem modificações diretas nos dados sem a necessidade de criar um novo objeto.

Os principais tipos mutáveis em Python são:

1. **listas (`list`)**
1. **dicionários (`dict`)**
1. **conjuntos (`set`)**

### 1. listas (`list`)

Listas são coleções ordenadas de elementos que podem ser de tipos variados. São definidas usando colchetes `[]` e os elementos são separados por vírgulas.

Exemplo :

```python
>>> minha_lista = [1, 2, 3, "quatro"]
```

Podese alterar um elemento específico da lista, por exemplo:

```python
>>> minha_lista[2] = "três"
```

Pode-se adicionar novos elementos com métodos como `append()` e `extend()`:

```python
>>> minha_lista.append(5)
>>> minha_lista.extend([6, 7])
```

Pode-se remover elementos com métodos como `remove()` e `pop()`:

```python
>>> minha_lista.remove("quatro")
>>> elemento = minha_lista.pop()
```

Alterar uma lista altera o próprio objeto lista, e todas as referências a essa lista verão as mudanças.

### 2. dicionários (`dict`)

Dicionários são coleções de pares chave-valor. São definidos usando chaves `{}` e os pares chave-valor são separados por vírgulas.

Exemplo :

```python
>>> meu_dict = {"nome": "Ana", "idade": 25}
```

Pode-se alterar o valor associado a uma chave existente:

```python
>>> meu_dict["idade"] = 26
```

Podese adicionar novos pares usando a chave:

```python
>>> meu_dict["cidade"] = "São Paulo"
```

Pode-se remover pares com `del` ou o método `pop()`:

```python
>>> del meu_dict["cidade"]
>>> idade = meu_dict.pop("idade")
```

Alterar um dicionário altera o próprio objeto dicionário. Todas as referências ao dicionário verão as mudanças.

### 3. conjuntos (`set`)

Conjuntos são coleções não ordenadas de elementos únicos. São definidos usando chaves `{}` e não permitem elementos duplicados.

Exemplo :

```python
>>> meu_set = {1, 2, 3}
```

Pode-se adicionar novos elementos com `add()`:

```python
>>> meu_set.add(4)
```

Pode-se remover elementos com `remove()` e `discard()`:

```python
>>> meu_set.remove(2)
>>> meu_set.discard(5)  # Não gera erro se o elemento não estiver presente
```

- **operações conjuntivas :** pode fazer operações como união, interseção e diferença:

```python
>>> outro_set = {3, 4, 5}
>>> uniao = meu_set.union(outro_set)
>>> intersecao = meu_set.intersection(outro_set)
>>> diferenca = meu_set.difference(outro_set)
```

Alterar um conjunto altera o próprio objeto conjunto. Todas as referências ao conjunto verão as mudanças.

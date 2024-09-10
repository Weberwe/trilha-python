Índice

1. [`in`](#in)
1. [exercícios `in`](#exercicios-in)
1. [`del`](#del)
1. [exercícios `del`](#exercicios-del)
1. [`pass`](#pass)
1. [`break`](#break)
1. [`continue`](#continue)
1. [`break` e `continue`](#break-e-continue)
1. [exercícios `break` e `continue`](#exercícios-break-e-continue)
1. [`assert`](#assert)
1. [exercícios `assert`](#exercicios-assert)

# comandos built-in

Comandos built-in do Python são funções e tipos de dados que estão disponíveis diretamente na linguagem, sem a necessidade de importar módulos adicionais. Eles fazem parte da biblioteca padrão e oferecem funcionalidades básicas essenciais para a programação.

## `in`

O comando `in` do Python é um operador que verifica a existência de um elemento em uma coleção de elementos, como listas, strings, tuplas, dicionários, sets, etc. Ele retorna um valor booleano: `True` se o elemento estiver presente na coleção e `False` caso contrário.

```python
# sintaxe básica
elemento in coleção
```

- `elemento` : é o item que você deseja verificar se está presente na coleção;
- `coleção` : é a estrutura de dados onde a verificação será feita;

### exemplos

#### `in` em strings

Quando usado com strings, o `in` verifica se uma substring está presente na string.

```python
>>> mensagem = "Olá, mundo!"
>>>
>>> print('Olá' in mensagem)
True
>>> print('mundo' in mensagem)
True
>>> print('Python' in mensagem)
False
>>> |
```

- aqui, `Olá` e `mundo` são substrings de `mensagem`, então o resultado é `True`;
- `Python` não é uma substring de `mensagem`, resultando em `False`;

#### `in` em listas

Em listas, o `in` verifica se o item existe em qualquer posição da lista.

```python
>>> frutas = ['maçã', 'banana', 'laranja']
>>>
>>> print('banana' in frutas)
True
>>> print('uva' in frutas)
False
>>> |
```

- no primeiro caso, `banana` está na lista `frutas`, então o resultado é `True`;
- no segundo caso, `uva` não está na lista, então o resultado é `False`;

#### `in` em tuplas

O funcionamento é semelhante ao das listas.

```python
>>> numeros = (1, 2, 3, 4)
>>>
>>> print(3 in numeros)
True
>>> print(5 in numeros)
False
>>> |
```

- `3` está na tupla `numeros`, então o resultado é `True`;
- `5` não está na tupla, resultando em `False`;

#### `in` em dicionários

Quando aplicado a dicionários, o `in` verifica a presença de uma chave, e não do valor associado a ela.

```python
>>> aluno = {'nome': 'Ana', 'idade': 21, 'curso': 'Engenharia'}
>>>
>>> print('nome' in aluno)
True
>>> print('Ana' in aluno)
False
>>> |
```

- `nome` é uma chave no dicionário `aluno`, portanto o resultado é `True`;
- `Ana` não é uma chave, é um valor, então o resultado é `False`;

#### `in` em sets

Em sets, o `in` verifica a presença de um elemento específico.

```python
>>> cores = {'vermelho', 'verde', 'azul'}
>>> print('verde' in cores)
True
>>> print('amarelo' in cores)
False
>>> |
```

- `verde` está no set `cores`, então o resultado é `True`;
- `amarelo` não está, resultando em `False`

### operador `not in`

O operador `not in` é o inverso de `in`. Ele verifica se o elemento **não** está presente na coleção.

```python
>>> frutas = ['maçã', 'banana', 'laranja']
>>> print('uva' not in frutas)
True
>>> print('banana' not in frutas)
False
>>> |
```

- no primeiro caso, `uva` não está na lista `frutas`, então o resultado é `True`;
- no segundo caso, `banana` está na lista, então o resultado é `False`;

## exercícios `in`

<details>
<summary>Lista de Exercícios</summary>

1. exercícios com strings
    1. Verifique se a substring `"Python"` está presente na string `"Eu estou aprendendo Python"` e imprima o resultado.
    1. Verifique se a letra `"a"` está presente na string `"Hello, World!"` e imprima o resultado.
    1. Crie uma string `"abcdefg"` e verifique se a letra `"h"` está presente nela. Imprima `True` ou `False`.
    1. Dada a string `"Programação"`, verifique se a substring `"ção"` está presente. Imprima o resultado.
    1. Verifique se a palavra `"code"` está na frase `"Escrever código é divertido"`. Imprima o resultado.
1. exercícios com listas
    1. Crie uma lista `["maçã", "banana", "laranja"]`. Verifique se `"banana"` está presente na lista e imprima o resultado.
    1. Dada a lista `[10, 20, 30, 40, 50]`, verifique se o número `25` está na lista e imprima `True` ou `False`.
    1. Crie uma lista de nomes `["Ana", "Beatriz", "Carlos"]`. Verifique se o nome `"Daniel"` está na lista e imprima o resultado.
    1. Dada a lista `["cachorro", "gato", "peixe"]`, verifique se `"passarinho"` está presente na lista e imprima o resultado.
    1. Crie uma lista vazia e verifique se o número `0` está presente nela. Imprima o resultado.
1. exercícios com tuplas
    1. Crie uma tupla `(1, 2, 3, 4, 5)` e verifique se o número `3` está presente. Imprima o resultado.
    1. Dada a tupla `("a", "b", "c", "d")`, verifique se a letra `"e"` está presente na tupla e imprima `True` ou `False`.
    1. Crie uma tupla com as cores `("vermelho", "verde", "azul")`. Verifique se a cor `"amarelo"` está na tupla e imprima o resultado.
    1. Verifique se o número `100` está na tupla `(10, 20, 30, 40, 50)` e imprima o resultado.
    1. Dada a tupla `(7, 14, 21, 28)`, verifique se o número `14` está presente e imprima o resultado.
1. exercícios com sets
    1. Crie um set `{"maçã", "banana", "uva"}` e verifique se `"laranja"` está presente no set. Imprima o resultado.
    1. Dado o set `{1, 3, 5, 7}`, verifique se o número `5` está presente e imprima `True` ou `False`.
    1. Verifique se o elemento `"Python"` está presente no set `{"Java", "C++", "Python", "JavaScript"}` e imprima o resultado.
    1. Crie um set com números `{2, 4, 6, 8}` e verifique se o número `10` está no set. Imprima o resultado.
    1. Dado o set `{"cachorro", "gato", "coelho"}`, verifique se o animal `"cavalo"` está presente e imprima `True` ou `False`.
1. exercícios com dicionários
    1. Crie um dicionário `aluno = {"nome": "João", "idade": 20, "curso": "Engenharia"}`. Verifique se a chave `"idade"` está presente no dicionário e imprima o resultado.
    1. Dado o dicionário `cidades = {"SP": "São Paulo", "RJ": "Rio de Janeiro", "MG": "Belo Horizonte"}`, verifique se a chave `"BA"` está no dicionário e imprima `True` ou `False`.
    1. Crie um dicionário `carro = {"marca": "Toyota", "modelo": "Corolla", "ano": 2020}`. Verifique se a chave `"cor"` está presente no dicionário e imprima o resultado.
    1. Dado o dicionário `estoque = {"caneta": 100, "caderno": 50, "borracha": 30}`, verifique se a chave `"lápis"` está presente no dicionário e imprima o resultado.
    1. Crie um dicionário `pessoa = {"nome": "Ana", "altura": 1.70, "peso": 65}`. Verifique se a chave `"idade"` está presente no dicionário e imprima `True` ou `False`.

</details>

## `del`

O comando `del` do Python é uma instrução usada para remover variáveis, elementos de uma lista, chave-valor de um dicionário, ou até mesmo fatias de listas e elementos em outros tipos de coleção. A instrução `del` também pode ser usada para deletar uma variável inteira da memória, tornando-a indisponível para uso posterior.

```python
# sintaxe básica
del objeto
```

- `objeto` : pode ser uma variável, um elemento de uma coleção, uma fatia de uma lista, ou uma chave de um dicionário;

### exemplos

#### deletando variáveis

É possível usar `del` para remover uma variável completamente, liberando o espaço de memória que ela estava ocupando.

```python
>>> x = 10
>>> print(x)
10
>>>
>>> del x
>>>
>>> print(x)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'x' is not defined
>>> |
```

- depois de `del x`, a variável `x` deixa de existir, e qualquer tentativa de acessá-la resultará em um erro;

#### deletando elementos de uma lista

O comando `del` pode ser usado para remover um elemento específico de uma lista, identificando-o pelo índice.

```python
>>> frutas = ['maçã', 'banana', 'laranja', 'uva']
>>>
>>> print(frutas)
['maçã', 'banana', 'laranja', 'uva']
>>>
>>> del frutas[1]
>>>
>>> print(frutas)
['maçã', 'laranja', 'uva']
>>> |
```

- aqui, `del frutas[1]` remove a `banana` da lista, que estava no índice `1`;

#### deletando fatias de uma lista

É possível usar `del` para remover uma fatia (slice) de elementos de uma lista.

```python
>>> numeros = list(range(1,7,1))
>>> print(numeros)
[1, 2, 3, 4, 5, 6]
>>>
>>> del numeros[2:5]
>>>
>>> print(numeros)
[1, 2, 6]
>>> |
```

- `del numeros[2:5]` remove os elementos nos índices `2`, `3` e `4` da lista original, que correspondem aos números `3`, `4` e `5`;

#### deletando chaves de um dicionário

No caso de dicionários, `del` é usado para remover um par chave-valor.

```python
>>> aluno = {'nome': 'Ana', 'idade': 21, 'curso': 'Engenharia'}
>>> print(aluno)
{'nome': 'Ana', 'idade': 21, 'curso': 'Engenharia'}
>>>
>>> del aluno['idade']
>>>
>>> print(aluno)
{'nome': 'Ana', 'curso': 'Engenharia'}
>>> |
```

- `del aluno['idade']` remove a chave `idade` e o valor associado a ela do dicionário;

#### deletando elementos de um set

Embora não se possa acessar diretamente um elemento em um set pelo índice (devido à natureza não ordenada dos sets), é possível deletar um set inteiro usando `del`.

```python
>>> cores = {'vermelho', 'verde', 'azul'}
>>> print(cores)
{'vermelho', 'azul', 'verde'}
>>>
>>> del cores
>>> print(cores)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'cores' is not defined
>>> |
```

- aqui, `del cores` remove completamente o set `cores` da memória;

### considerações adicionais

- **deletando múltiplas variáveis** : é possível deletar várias variáveis ao mesmo tempo, separando-as por vírgulas;
    ```python
    >>> a = 10
    >>> b = 20
    >>> c = 30
    >>>
    >>> del a, c
    >>>
    >>> print(a)
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    NameError: name 'a' is not defined
    >>>
    >>> print(b)
    20
    >>>
    >>> print(c)
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    NameError: name 'c' is not defined
    >>> |
    ```

- **deletando referências a objetos** : quando se deleta uma variável que se refere a um objeto, como uma lista ou um dicionário, e não há mais referências a esse objeto, ele é removido da memória pelo garbage collector do python;

- **uso em loops e funções** : é possível usar `del` dentro de loops e funções para remover elementos dinamicamente à medida que o programa é executado;

## exercícios `del`

<details>
<summary>Lista de Exercícios</summary>

1. exercícios com variáveis numéricas e strings
    1. Crie uma variável `x = 10`. Use `del` para deletar a variável `x`. Tente imprimir `x` e observe o que acontece.
    1. Defina duas variáveis `a = 5` e `b = 10`. Use `del` para deletar ambas as variáveis. Tente imprimir `a` e `b`.
    1. Crie uma string `frase = "Olá, Mundo!"`. Use `del` para deletar a variável `frase`. Tente imprimir `frase` e observe o resultado.
    1. Defina uma variável `nome = "Maria"`. Use `del` para deletar a variável. Tente acessar `nome` após deletá-la.
    1. Crie três variáveis: `num1 = 3`, `num2 = 6`, e `num3 = 9`. Use `del` para deletar `num1` e `num2`. Tente imprimir todas as três variáveis.
1. exercícios com listas
    1. Crie uma lista `numeros = [1, 2, 3, 4, 5]`. Use `del` para deletar o terceiro elemento da lista. Imprima a lista resultante.
    1. Defina uma lista `frutas = ["maçã", "banana", "laranja"]`. Use `del` para deletar o último item da lista. Imprima a lista.
    1. Crie uma lista `cores = ["vermelho", "azul", "verde", "amarelo"]`. Use `del` para deletar os elementos no índice 1 e 2. Imprima a lista resultante.
    1. Crie uma lista `alfabeto = ["a", "b", "c", "d", "e", "f"]`. Use `del` para deletar os primeiros dois elementos da lista. Imprima a lista.
    1. Defina uma lista `itens = ["caneta", "caderno", "borracha"]`. Use `del` para deletar a lista inteira. Tente imprimir `itens` e observe o que acontece.
    1. Crie uma lista `numeros = [10, 20, 30, 40, 50]`. Use `del` para deletar o elemento no índice `4`. Imprima a lista resultante.
    1. Dada a lista `animais = ["cachorro", "gato", "passarinho", "peixe"]`, use `del` para deletar o segundo e o terceiro elementos. Imprima a lista.
    1. Crie uma lista `dias = ["segunda", "terça", "quarta", "quinta", "sexta"]`. Use `del` para deletar os três últimos elementos. Imprima a lista.
    1. Crie uma lista `meses = ["janeiro", "fevereiro", "março", "abril"]`. Use `del` para deletar o primeiro elemento da lista. Imprima a lista.
    1. Defina uma lista `numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]`. Use `del` para deletar os elementos nos índices 0 a 4 (inclusive). Imprima a lista resultante.
1. exercícios com tuplas
    1. Crie uma tupla `pares = (2, 4, 6, 8, 10)`. Use `del` para deletar a tupla inteira. Tente imprimir `pares`.
    1. Crie uma tupla `letras = ("a", "b", "c", "d")`. Use `del` para deletar a tupla inteira. Tente acessar `letras` e observe o resultado.
    1. Defina uma tupla `numeros = (1, 2, 3, 4, 5)`. Use `del` para deletar a variável `numeros`. Tente imprimir `numeros`.
1. exercícios com sets
    1. Crie um set `vogais = {"a", "e", "i", "o", "u"}`. Use `del` para deletar o set inteiro. Tente acessar `vogais`.
    1. Defina um set `numeros = {1, 2, 3, 4, 5}`. Use `del` para deletar o set. Tente imprimir `numeros`.
    1. Crie um set `cores = {"vermelho", "verde", "azul"}`. Use `del` para deletar o set. Verifique o que acontece ao tentar acessar `cores`.
1. exercícios com dicionários
    1. Crie um dicionário `aluno = {"nome": "João", "idade": 20, "curso": "Matemática"}`. Use `del` para deletar a chave `"idade"`. Imprima o dicionário resultante.
    1. Defina um dicionário `produto = {"nome": "caneta", "preço": 1.50, "estoque": 100}`. Use `del` para deletar a chave `"preço"`. Imprima o dicionário.
    1. Crie um dicionário `contato = {"nome": "Maria", "telefone": "1234-5678", "email": "maria@gmail.com"}`. Use `del` para deletar a chave `"telefone"`. Imprima o dicionário.
    1. Dado o dicionário `carro = {"marca": "Ford", "modelo": "Mustang", "ano": 1969}`, use `del` para deletar a chave `"ano"`. Imprima o dicionário resultante.

</details>

## `pass`

O comando `pass` em Python é uma instrução nula; quando é executado, nada acontece. Ele é utilizado em situações onde uma declaração é necessária sintaticamente, mas onde nenhum código precisa ser executado.

### formas de uso

1. **estrutura de código em desenvolvimento** : durante o desenvolvimento, pode ser usado para estruturar funções, classes ou blocos condicionais que ainda não foram implementados, mas deseja evitar erros de sintaxe. O `pass` é uma forma de “marcar” esses locais, sem precisar escrever o código definitivo imediatamente.
    ```python
    >>> def minha_funcao():
    >>>     pass  # vai ser implementado depois
    >>>
    >>> class MinhaClasse:
    >>>     pass  # classe em desenvolvimento
    >>>
    >>> if condicao:
    >>>     pass  # Ainda não sei o que fazer aqui
    ```

1. **blocos de código condicional**: em certos casos, pode ser necessário ter uma condicional que não faz nada, por exemplo, ao tratar um caso onde nenhuma ação é necessária.
    ```python
    >>> for item in minha_lista:
    >>>     if item == "pular":
    >>>         pass  # não faço nada para 'pular'
    >>>     else:
    >>>         print(item)
    ```

1. **estruturas de controle sem implementação imediata**: o `pass` é útil em loops, funções ou outras estruturas de controle onde ainda não se sabe qual será a lógica final, mas quer estruturar o código de forma que ele seja executável.
    ```python
    >>> while True:
    >>>     pass  # loop infinito em desenvolvimento, sem lógica definida
    ```

### exemplos

1. classe em desenvolvimento
    ```python
    >>> class Animal:
    >>>     pass  # classe animal a ser definida depois
    >>>
    >>> # não gera erro e a classe pode ser instanciada
    >>> cachorro = Animal()
    ```

1. função em desenvolvimento
    ```python
    >>> def funcao_complexa():
    >>>     pass  # lógica a ser implementada depois
    >>>
    >>> # função chamada, mas sem erros
    >>> funcao_complexa()
    ```

1. estrutura condicional
    ```python
    >>> x = 10
    >>>
    >>> if x > 0:
    >>>     pass  # sem ação específica para números positivos
    >>> else:
    >>>     print("Número não positivo")
    ```

### observações

- **evitar uso excessivo** : o `pass` é útil para o desenvolvimento inicial ou para marcar futuras implementações, mas em um código final, ele deve ser removido ou substituído por código funcional.

- **leitura do código** : o uso de `pass` pode indicar a necessidade de implementação futura, mas em código de produção, deixar blocos de código com `pass` pode sugerir funcionalidades incompletas ou mal implementadas.

### conclusão

O `pass` é uma ferramenta essencial em Python para a criação de esboços de código e para manter a estrutura do código correta durante o desenvolvimento. Ele garante que seja possível continuar a desenvolver outras partes do código sem ser interrompido por erros de sintaxe.


## `break`

O comando `break` em Python é utilizado dentro de loops (`for` e `while`) para interromper o loop imediatamente. Quando o Python encontra um `break`, ele sai do loop, ignorando todas as iterações restantes, e a execução do código continua após o bloco do loop.

Quando o comando `break` é executado dentro de um loop, ele interrompe o loop inteiro, não importa em qual ponto da iteração o `break` esteja. Isso é útil quando é preciso sair de um loop antes que ele termine todas as iterações, com base em uma condição específica.

```python
>>> # estrutura básica
>>> for item in sequencia:
>>>     if condicao:
>>>         break  # sai do loop completamente
>>>     # código que é executado até que o break seja chamado
```

### exemplos

1. interrompendo um loop ao encontrar um valor específico : vamos supor que tenha uma lista de números e queira parar a iteração assim que encontrar o número 5 :
    ```python
    >>> numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>>
    >>> for numero in numeros:
    >>>     if numero == 5:
    >>>         break  # interrompe o loop quando o número 5 é encontrado
    >>>     print(numero)
    1
    2
    3
    4
    >>> |
    ```
    Neste exemplo, o loop é interrompido assim que o número 5 é encontrado, e o Python sai do loop, ignorando os números restantes na lista.

1. encontrando um item em uma lista : pode usar o `break` para interromper a busca em uma lista assim que encontrar um item específico :
    ```python
    >>> frutas = ["maçã", "banana", "laranja", "abacaxi", "uva"]
    >>>
    >>> for fruta in frutas:
    >>>     print(f"Verificando {fruta}")
    >>>     if fruta == "laranja":
    >>>         print("Laranja encontrada, interrompendo a busca.")
    >>>         break  # Para a busca quando a laranja é encontrada
    Verificando maçã
    Verificando banana
    Verificando laranja
    Laranja encontrada, interrompendo a busca.
    >>> |
    ```
    Aqui, o loop para de executar assim que encontra "laranja", evitando verificar as frutas restantes.

1. interrompendo um loop infinito : um `break` é frequentemente usado para sair de um loop infinito quando uma certa condição é atendida :
    ```python
    >>> i = 1
    >>>
    >>> while True:
    >>>     print(i)
    >>>     if i == 10:
    >>>         break  # Interrompe o loop infinito quando i é igual a 10
    >>>     i += 1
    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    >>> |
    ```
    Neste exemplo, o loop `while` é infinito (`while True:`), mas o comando `break` faz com que o loop seja interrompido quando `i` atinge o valor 10.

### quando usar `break`

1. **interromper a busca** : quando está procurando por algo em uma lista ou sequência e deseja parar a busca assim que encontrar o que precisa;

1. **sair de loops infinitos** : em loops `while` que podem, teoricamente, rodar para sempre, o `break` pode ser usado para sair do loop quando uma condição específica é atingida;

1. **prevenir iterações desnecessárias** : se sabe que não precisa continuar o loop após encontrar um certo valor, o `break` pode melhorar a eficiência do código;

### conclusão

O `break` é uma ferramenta essencial para controle de fluxo em loops. Ele permite que você saia de loops imediatamente quando uma condição específica é atendida, evitando iterações desnecessárias e melhorando a eficiência do seu código.


## `continue`

O comando `continue` em Python é utilizado dentro de loops (`for` e `while`) para pular a iteração atual e passar para a próxima iteração do loop. Ele é útil quando se deseja ignorar o restante do código no bloco do loop para certas condições, sem interromper o loop completamente.

Quando o Python encontra o comando `continue` dentro de um loop, ele interrompe a execução do código restante na iteração atual e imediatamente volta ao início do loop, verificando a condição do loop novamente. Se a condição for verdadeira, uma nova iteração começa.

```python
>>> # estrurua básica
>>> for item in sequencia:
>>>     if condicao:
>>>         continue  # pula o resto do código no loop e vai para a próxima iteração
>>>     # código que será ignorado se a condição for verdadeira
```

### exemplos

1. pular números pares : vamos supor que se queira iterar por uma lista de números e imprimir apenas os números ímpares:
    ```python
    >>> numeros = list(range(1,11))
    >>>
    >>> for numero in numeros:
    >>>     if numero % 2 == 0:  # verifica se o número é par
    >>>          continue  # pula a iteração se o número for par
    >>>     print(numero)
    1
    3
    5
    7
    9
    >>> |
    ```
    Neste exemplo, o comando `continue` faz com que o loop pule a impressão dos números pares.

1. ignorar palavras específicas : pode usar `continue` para ignorar palavras específicas em uma lista de palavras :
    ```python
    >>> palavras = ["maçã", "banana", "laranja", "abacaxi", "uva"]
    >>>
    >>> for palavra in palavras:
    >>>     if palavra == "laranja":
    >>>         continue  # ignora a palavra "laranja"
    >>>     print(palavra)
    maçã
    banana
    abacaxi
    uva
    >>> |
    ```
    Aqui, a palavra "laranja" é ignorada e não é impressa.

1. contando iterações válidas : em um loop `while`, o `continue` pode ser usado para ignorar certos valores e continuar a contagem ou execução das iterações :
    ```python
    >>> i = 0
    >>> while i < 10:
    >>>     i += 1
    >>>     if i % 2 == 0:  # se i for par, pula para a próxima iteração
    >>>         continue
    >>>     print(i)
    1
    3
    5
    7
    9
    ```
    Neste exemplo, `continue` faz com que os números pares sejam pulados no loop `while`.

### quando usar `continue`

1. **filtragem de dados**: quando se deseja processar apenas certos itens de uma lista ou sequência e ignorar outros com base em uma condição específica;

2. **ignorar erros**: pode ser usado para pular uma iteração se uma operação específica falhar (por exemplo, um cálculo que pode causar uma exceção);

3. **simplificar estruturas de controle**: em vez de usar `else` ou aninhar múltiplas condições, `continue` pode simplificar o código, especialmente quando a lógica principal deve ser executada apenas para alguns casos;

### conclusão

O `continue` é uma ferramenta poderosa em Python para controle de fluxo dentro de loops. Ele permite que pular certas iterações com base em condições específicas, tornando o código mais flexível e legível.


## `break` e `continue`

Os comandos `break` e `continue` são ambos utilizados para controlar o fluxo de execução dentro de loops em Python. Embora possam ser usados de forma independente, existem situações em que é útil combiná-los dentro do mesmo loop para criar lógica mais complexa.

Quando combinado `break` e `continue` em um loop, por exemplo, é possível criar uma lógica em que determinadas condições pulem a iteração atual, enquanto outras condições interrompem completamente o loop.

### exemplos

1. filtragem e interrupção de processamento : suponha que tenha uma lista de números e queira processar apenas os números ímpares. Se um número for maior que 15, quer interromper o processamento completamente.
    ```python
    >>> numeros = [3, 7, 2, 9, 12, 17, 19, 6, 11]
    >>>
    >>> for numero in numeros:
    >>>     if numero % 2 == 0:  # se o número for par
    >>>         continue  # pula para a próxima iteração, ignorando o número par
    >>>
    >>>     if numero > 15:  # se o número for maior que 15
    >>>         print("Número maior que 15 encontrado. Interrompendo.")
    >>>         break  # interrompe o loop completamente
    >>>
    >>>     print(f"Processando número ímpar: {numero}")
    >>> Processando número ímpar: 3
    >>> Processando número ímpar: 7
    >>> Processando número ímpar: 9
    >>> Número maior que 15 encontrado. Interrompendo.
    >>> |
    ```
    Neste exemplo:
    - O `continue` é usado para pular números pares, ignorando-os;
    - O `break` é usado para interromper o loop assim que um número maior que 15 é encontrado;

1. looping com condições múltiplas : considere uma situação em que se precisa iterar sobre uma lista de números, mas deseja:
    1. Ignorar números negativos (`continue`);
    1. Interromper o loop ao encontrar um número que é um múltiplo de 7 (`break`);
    ```python
    >>> numeros = [5, -3, 10, 6, -1, 14, 12, -8, 20]
    >>>
    >>> for numero in numeros:
    >>>     if numero < 0:  # ignora números negativos
    >>>         continue  # pula para a próxima iteração
    >>>
    >>>     if numero % 7 == 0:  # encontra o primeiro múltiplo de 7
    >>>         print(f"Número múltiplo de 7 encontrado: {numero}. Interrompendo o loop.")
    >>>         break  # interrompe o loop ao encontrar múltiplo de 7
    >>>
    >>>     print(f"Processando número: {numero}")
    >>> Processando número: 5
    >>> Processando número: 10
    >>> Processando número: 6
    >>> Número múltiplo de 7 encontrado: 14. Interrompendo o loop.
    >>> |
    ```
    Neste exemplo:
    - O `continue` é utilizado para pular números negativos.
    - O `break` é utilizado para interromper o loop assim que um múltiplo de 7 é encontrado.

1. verificando condições em uma lista de strings : imagine que está processando uma lista de palavras e:
    1. Deseja pular qualquer palavra que comece com a letra "a" (`continue`);
    1. Quer interromper completamente o loop se encontrar a palavra "parar" (`break`);
    ```python
    >>> palavras = ["maçã", "banana", "abacate", "uva", "parar", "laranja"]
    >>>
    >>> for palavra in palavras:
    >>>     if palavra.startswith("a"):  # Ignora palavras que começam com "a"
    >>>         continue  # Pula para a próxima iteração
    >>>
    >>>     if palavra == "parar":  # Interrompe o loop se encontrar "parar"
    >>>         print("Palavra 'parar' encontrada. Interrompendo o loop.")
    >>>         break  # Interrompe o loop
    >>>
    >>>     print(f"Processando palavra: {palavra}")
    >>> Processando palavra: banana
    >>> Processando palavra: uva
    >>> Palavra 'parar' encontrada. Interrompendo o loop.
    >>> |
    ```
    Neste exemplo:
    - O `continue` ignora palavras que começam com a letra "a";
    - O `break` interrompe o loop ao encontrar a palavra "parar";

### considerações importantes

- **ordem importa**: a ordem que se coloca `continue` e `break` dentro do loop é crucial, pois determinará a lógica do fluxo de execução;
- **leitura do código**: usar `continue` e `break` no mesmo loop pode tornar o código mais difícil de ler, então é importante usar comentários claros ou refatorar o código para que a lógica seja intuitiva;

### conclusão

Combinar `break` e `continue` em um loop Python permite um controle granular sobre o fluxo de execução, permitindo que se pule iterações específicas enquanto também fornece uma maneira de sair completamente do loop quando certas condições são atendidas. Usados juntos, esses comandos podem tornar o código mais eficiente e focado, dependendo das necessidades da aplicação.

## exercícios `break` e `continue`

<details>
<summary>Lista de Exercícios</summary>

### `break`

1. **Interrupção em Lista de Números**: Crie um loop `for` que percorra uma lista de números de 1 a 10. Use `break` para interromper o loop quando o número 5 for encontrado.
1. **Busca em String**: Escreva um loop `for` que percorra uma string. Use `break` para parar o loop assim que a letra "a" for encontrada e imprima as letras anteriores.
1. **Loop com Condição**: Crie um loop `while` que incrementa uma variável `x` começando em 0. Use `break` para parar o loop quando `x` for igual a 10.
    ```python
    x = 0

    # while x < 20:
    while True:
        if x == 10:
            break
        x = x + 1

    print(f'saindo do while com {x = }')
    ```
1. **Interrupção em Lista de Strings**: Escreva um loop `for` que percorra uma lista de strings. Use `break` para sair do loop assim que encontrar uma string vazia.
1. **Número Múltiplo**: Crie um loop `for` que percorra uma lista de números. Use `break` para interromper o loop assim que encontrar um número divisível por 7.
1. **Interromper com Condicional**: Crie um loop `while` que soma números inteiros a partir de 1. Use `break` para sair do loop assim que a soma ultrapassar 50.
1. **Busca de Palavras**: Escreva um loop `for` que percorra uma lista de palavras. Use `break` para interromper o loop se encontrar uma palavra que começa com "Z".
1. **Busca em String**: Crie um loop `while` que percorra uma string caractere por caractere. Use `break` para parar o loop se encontrar um dígito numérico.
1. **Interrupção em Sublista**: Escreva um loop `for` que percorra uma lista de listas. Use `break` para sair do loop principal se encontrar uma sublista que contém um valor negativo.
1. **Interromper com Condição Complexa**: Crie um loop `for` que percorra uma lista de números e use `break` para sair do loop se encontrar um número maior que 100 ou menor que -100.
1. **Interrupção Condicional**: Crie um loop `while` que percorra os caracteres de uma string. Use `break` se encontrar duas vogais consecutivas e imprima o que foi lido até esse ponto.
1. **Busca de Substring**: Escreva um loop `for` que percorra uma lista de strings. Use `break` se encontrar uma string que contenha a substring "python".
1. **Parada em Número Específico**: Crie um loop `while` que gera números aleatórios entre 1 e 100. Use `break` para sair do loop quando um número específico (por exemplo, 42) for gerado.
1. **Interromper em Condição Composta**: Escreva um loop `for` que percorra uma lista de números. Use `break` para sair do loop se encontrar um número negativo seguido de um positivo.
1. **Interromper após Concatenar**: Crie um loop `for` que percorra uma lista de strings e as concatene em uma única string. Use `break` quando o comprimento total da string concatenada ultrapassar 50 caracteres.
1. **Interromper em Sequência**: Escreva um loop `for` que percorra uma lista de números. Use `break` se encontrar uma sequência de três números ímpares consecutivos.
1. **Interromper em Condição de Soma**: Crie um loop `while` que adicione números de uma lista a uma variável soma. Use `break` para interromper a adição se a soma exceder um valor limite (por exemplo, 100).
1. **Interrupção em String**: Escreva um loop `for` que percorra uma string caractere por caractere. Use `break` se encontrar uma combinação específica de caracteres (por exemplo, "ab").
1. **Parada em Condição Composta**: Crie um loop `for` que percorra uma lista de números. Use `break` para sair do loop se encontrar um número maior que 50 seguido de um número menor que 10.
1. **Interrupção em Verificação de Substring**: Escreva um loop `while` que verifique se uma substring existe em uma string. Use `break` para sair do loop quando encontrar a substring "stop".

### `continue`

1. **Lista de Números**: Crie um loop `for` que percorra uma lista de números de 1 a 10. Use `continue` para pular os números pares e imprima os ímpares.
1. **String com Vogais**: Escreva um loop `for` que percorra uma string. Use `continue` para pular as vogais e imprima as consoantes.
1. **Números Negativos**: Crie um loop `while` que diminua o valor de uma variável `x` a partir de 10. Use `continue` se `x` for negativo e imprima o restante.
1. **Strings com Espaços**: Escreva um loop `for` que percorra uma lista de strings. Use `continue` para pular as strings que contêm espaços e imprima as demais.
1. **Divisíveis por 3**: Crie um loop `for` que percorra uma lista de números. Use `continue` para pular os números divisíveis por 3 e imprima os outros.
1. **Índices Pares**: Escreva um loop `for` que percorra uma lista de palavras e seus índices. Use `continue` para pular as palavras nos índices pares e imprima as outras.
1. **Contagem Regressiva**: Crie um loop `while` que conta de 20 até 0. Use `continue` para pular os números ímpares e imprima os pares.
1. **Nomes Longos**: Escreva um loop `for` que percorra uma lista de nomes. Use `continue` para pular os nomes com mais de 5 caracteres e imprima os menores.
1. **String com Dígitos**: Crie um loop `for` que percorra uma string. Use `continue` para pular os caracteres que são dígitos e imprima os demais.
1. **Listas Vazias**: Escreva um loop `for` que percorra uma lista de listas. Use `continue` para pular listas vazias e imprima as outras.
1. **Soma de Números**: Crie um loop `for` que percorra uma lista de números e calcule a soma deles. Use `continue` para ignorar os números negativos.
1. **String Alternada**: Escreva um loop `for` que percorra uma string e use `continue` para pular os caracteres nas posições ímpares. Imprima apenas os caracteres nas posições pares.
1. **Números Primos**: Crie um loop `while` que verifica números de 2 a 50. Use `continue` para pular números que não são primos e imprima apenas os primos.
1. **Palavras Compostas**: Escreva um loop `for` que percorra uma lista de palavras. Use `continue` para pular palavras que contêm mais de uma vogal e imprima as demais.
1. **Listas com Zeros**: Crie um loop `for` que percorra uma lista de listas de números. Use `continue` para pular listas que contenham o número 0 e imprima as outras listas.
1. **Comparação de Strings**: Escreva um loop `for` que percorra duas listas de strings de tamanho igual. Use `continue` para pular a comparação se as strings não tiverem o mesmo comprimento.
1. **Nomes e Idades**: Crie um loop `for` que percorra duas listas (nomes e idades). Use `continue` para pular a impressão se a idade for menor que 18 e imprima apenas os nomes das pessoas maiores de idade.
1. **Soma de Dígitos**: Escreva um loop `while` que receba uma string de números. Use `continue` para pular caracteres que não são dígitos e calcule a soma dos dígitos.
1. **Filtros em Listas**: Crie um loop `for` que percorra uma lista de números. Use `continue` para ignorar números que são múltiplos de 5 e imprima os restantes.
1. **String Invertida**: Escreva um loop `for` que percorra uma string de trás para frente. Use `continue` para pular os caracteres nas posições ímpares e imprima apenas os caracteres nas posições pares.

### `break` e `continue`

1. **Interrupção com Condição**: Crie um loop `for` que percorra uma lista de números de 1 a 10. Use `continue` para pular números pares e `break` para sair do loop quando encontrar o número 7.
2. **Busca em String**: Escreva um loop `for` que percorra uma string. Use `continue` para pular os espaços em branco e `break` para sair do loop quando encontrar a letra "z".
3. **Loop com Condição**: Crie um loop `while` que incrementa uma variável `x` a partir de 0. Use `continue` para pular os números divisíveis por 3 e `break` para parar o loop quando `x` atingir 15.
4. **Lista de Strings**: Escreva um loop `for` que percorra uma lista de strings. Use `continue` para pular as strings que contêm o caractere "a" e `break` para sair do loop ao encontrar uma string com mais de 5 caracteres.
5. **Interrupção Condicional**: Crie um loop `for` que percorra uma lista de números. Use `continue` para pular números negativos e `break` para sair do loop ao encontrar um número maior que 50.
6. **Filtro de Números**: Crie um loop `while` que gera números aleatórios entre 1 e 50. Use `continue` para pular números menores que 10 e `break` para parar o loop quando um número maior que 40 for gerado.
7. **Verificação de String**: Escreva um loop `for` que percorra uma lista de strings. Use `continue` para pular strings que não começam com a letra "P" e `break` para sair do loop ao encontrar uma string que começa com "Python".
8. **Interrupção Condicional em String**: Crie um loop `while` que percorra uma string caractere por caractere. Use `continue` para pular vogais e `break` para sair do loop ao encontrar a letra "e".
9. **Filtragem em Sublistas**: Escreva um loop `for` que percorra uma lista de listas de números. Use `continue` para pular sublistas vazias e `break` para sair do loop ao encontrar uma sublista contendo um número negativo.
10. **Condicionais Múltiplas**: Crie um loop `for` que percorra uma lista de números. Use `continue` para pular números divisíveis por 2 ou 5 e `break` para sair do loop ao encontrar um número maior que 30.
11. **Verificação de Consoantes**: Crie um loop `while` que percorre uma string. Use `continue` para pular caracteres que são vogais e `break` para parar o loop ao encontrar uma consoante específica (por exemplo, "r").
12. **Busca em Lista**: Escreva um loop `for` que percorra uma lista de números. Use `continue` para pular números ímpares e `break` para sair do loop ao encontrar um número divisível por 4.
13. **Interrupção Condicional em Nomes**: Crie um loop `for` que percorra uma lista de nomes. Use `continue` para pular nomes com menos de 4 letras e `break` para sair do loop ao encontrar um nome começando com "A".
14. **Substituição em String**: Escreva um loop `while` que percorra uma string caractere por caractere. Use `continue` para pular caracteres que não são letras e `break` para sair do loop ao encontrar um espaço.
15. **Filtro de Listas**: Crie um loop `for` que percorra uma lista de listas de números. Use `continue` para pular listas que não contêm números maiores que 10 e `break` para sair do loop ao encontrar uma lista com mais de 3 números.
16. **Filtro de Substring**: Escreva um loop `for` que percorra uma lista de strings. Use `continue` para pular strings que não contêm a letra "x" e `break` para sair do loop ao encontrar uma string com mais de 8 caracteres.
17. **Verificação de Números**: Crie um loop `while` que percorra uma lista de números de 1 a 100. Use `continue` para pular números que não são primos e `break` para sair do loop ao encontrar um número primo maior que 50.
18. **Busca em String**: Escreva um loop `for` que percorra uma string. Use `continue` para pular os caracteres que não são dígitos e `break` para sair do loop ao encontrar dois dígitos consecutivos.
19. **Filtro em Listas**: Crie um loop `for` que percorra uma lista de listas de números. Use `continue` para pular listas que contêm números negativos e `break` para sair do loop ao encontrar uma lista com apenas números positivos.
20. **Verificação de Caracteres**: Escreva um loop `while` que percorra uma string. Use `continue` para pular os caracteres que não são letras maiúsculas e `break` para sair do loop ao encontrar três letras maiúsculas consecutivas.

</details>

## `assert`

O comando `assert` no Python é utilizado para realizar verificações (ou *assertions*) em um programa. Ele é geralmente utilizado durante o desenvolvimento para garantir que certas condições lógicas sejam verdadeiras. Se a condição que está sendo verificada pelo `assert` for falsa, uma exceção do tipo `AssertionError` será levantada, interrompendo a execução do programa. Caso a condição seja verdadeira, o programa continua a ser executado normalmente.

A sintaxe básica do `assert` é:

```python
assert <condição>, <mensagem opcional>
```

- `<condição>` : uma expressão que será avaliada. Se ela for avaliada como `True`, o `assert` não faz nada e a execução do programa continua. Se for `False`, um `AssertionError` será levantado;
- `<mensagem opcional>` : uma mensagem que será exibida juntamente com o `AssertionError`, explicando o motivo do erro. Ela é opcional, mas útil para ajudar a entender o que deu errado;

- **Exemplo**

```python
x = 5
assert x > 0, "x deve ser maior que zero"
```

Neste exemplo, o programa continua normalmente, já que `x > 0` é `True`. No entanto, se `x` fosse um número menor ou igual a zero, o Python levantaria um `AssertionError` com a mensagem "x deve ser maior que zero".

### como funciona

Quando o comando `assert` é executado, ele faz o seguinte :

1. Avalia a expressão condicional;
1. Se a condição for `True`, o programa segue normalmente;
1. Se a condição for `False`, um `AssertionError` é lançado, e a execução do programa é interrompida a menos que a exceção seja tratada por um bloco `try-except`;

- **Exemplo**

```python
def divide(a, b):
    assert b != 0, "O divisor não pode ser zero."
    return a / b

print(divide(10, 2))  # saída: 5.0
print(divide(10, 0))  # lança um AssertionError com a mensagem: "O divisor não pode ser zero."
```

### por que usar

1. **Verificação durante o desenvolvimento** : o `assert` é útil para verificar suposições que o programador faz enquanto desenvolve o código. Se uma suposição falhar, o `AssertionError` ajuda a detectar o erro rapidamente;

1. **Depuração e testes** : durante o desenvolvimento ou testes, você pode usar o `assert` para verificar o comportamento esperado de funções ou trechos de código. Ele serve como uma medida de segurança para garantir que certas condições lógicas sejam sempre verdadeiras;

1. **Evitar erros lógicos** : ele ajuda a capturar erros lógicos ou situações inesperadas antes que eles causem maiores problemas no código;

### quando não usar

1. **Validação de entrada do usuário** : o `assert` não deve ser usado para validar entradas de usuários ou para condições que devem ser tratadas em tempo de execução. Isso ocorre porque, se o código for executado com otimizações (com a flag `-O`), os `assert` são removidos e não executados, o que poderia deixar o programa vulnerável;

1. **Verificações críticas de runtime** : se a verificação for fundamental para a segurança ou estabilidade do código, como garantir que um arquivo existe antes de ser lido, deve-se usar um bloco `if-else` e lançar exceções adequadas, em vez de confiar no `assert`;

Exemplo de uso inadequado para validar entradas :

```python
def validar_idade(idade):
    assert idade >= 18, "Idade deve ser maior ou igual a 18."
```

Neste caso, o `assert` não é a melhor escolha para validar a idade do usuário, pois se o programa for executado com a otimização (usando `python -O`), o `assert` não será executado, deixando o código vulnerável. O correto seria:

```python
def validar_idade(idade):
    if idade < 18:
        raise ValueError("Idade deve ser maior ou igual a 18.")
```

### como é tratado

Quando o Python é executado com a flag `-O` (modo otimizado), todas as instruções `assert` são ignoradas. Isso significa que elas não serão executadas e não terão impacto no programa. Portanto, o `assert` é útil durante o desenvolvimento, mas não deve ser confiado em ambientes de produção.

### exemplo de como o `assert` funciona com `-O`

Normalmente:

```python
x = 5
assert x == 10, "x deve ser igual a 10"
```

Isso lançaria um `AssertionError` com a mensagem "x deve ser igual a 10". No entanto, se o código for executado com a otimização (`python -O script.py`), o `assert` é removido, e o programa continua sem levantar erro.

### exemplo prático

Imagine que se está criando uma função para verificar se uma lista está ordenada. Durante o desenvolvimento, pode-se usar `assert` para garantir que a lista seja corretamente ordenada.

```python
def verificar_ordenacao(lista):
    for i in range(len(lista) - 1):
        assert lista[i] <= lista[i + 1], "A lista não está ordenada."
    return True

# Testando
verificar_ordenacao([1, 2, 3, 4])  # Não levanta erro
verificar_ordenacao([1, 3, 2, 4])  # Lança AssertionError: "A lista não está ordenada."
```

### exemplos de usos corretos e incorretos

#### em funções

- **uso correto para verificar pré-condições**

Pode-se usar o `assert` para garantir que uma função receba os parâmetros corretos:

```python
def calcular_raiz_quadrada(x):
    assert x >= 0, "O número deve ser maior ou igual a zero"
    return x ** 0.5

print(calcular_raiz_quadrada(9))  # Saída: 3.0
print(calcular_raiz_quadrada(-1))  # Lança AssertionError: "O número deve ser maior ou igual a zero"
```

Aqui, o `assert` garante que a função não tente calcular a raiz quadrada de um número negativo, o que não faz sentido matematicamente.

- **uso incorreto para validação de parâmetros de entrada**

Se estiver validando parâmetros de entrada de usuários, o `assert` não é a melhor escolha, já que pode ser desativado no modo otimizado.

```python
def verificar_idade(idade):
    assert idade >= 18, "Idade inválida para este serviço"

# Não recomendado para validação de dados de entrada.
```

Em vez disso, deve-se usar um `if` e levantar uma exceção apropriada, como `ValueError`:

```python
def verificar_idade(idade):
    if idade < 18:
        raise ValueError("Idade inválida para este serviço")
```

#### em loops

- **verificando a consistência de dados em um loop**

Pode-se usar `assert` para garantir que um valor seja crescente ao longo de um loop:

```python
def verificar_ordenacao(lista):
    for i in range(len(lista) - 1):
        assert lista[i] <= lista[i + 1], f"Lista não está ordenada: {lista[i]} > {lista[i+1]}"

verificar_ordenacao([1, 2, 3, 4])  # Não gera erro
verificar_ordenacao([1, 3, 2, 4])  # Lança AssertionError: "Lista não está ordenada: 3 > 2"
```

Aqui, o `assert` garante que a lista está ordenada enquanto percorre o loop. Se houver um erro, ele interrompe o programa e informa onde a ordem foi quebrada.

- **uso incorreto no lugar de um controle de fluxo normal**

Não é uma boa prática usar `assert` para substituir controles de fluxo como `break` ou `return` em loops.

```python
def buscar_valor(lista, valor):
    for item in lista:
        assert item != valor, "Valor encontrado!"  # NÃO recomendado
```

Em vez disso, o correto seria:

```python
def buscar_valor(lista, valor):
    for item in lista:
        if item == valor:
            return True
    return False
```

#### em condicionais

- **verificando uma condição lógica crítica**

```python
def dividir(a, b):
    assert b != 0, "Divisor não pode ser zero!"
    return a / b

print(dividir(10, 2))  # Saída: 5.0
print(dividir(10, 0))  # Lança AssertionError: "Divisor não pode ser zero!"
```

Aqui, o `assert` é utilizado para garantir que não haja uma tentativa de divisão por zero.

- **não usar `assert` para controle de erro crítico**

```python
def verificar_positivo(numero):
    assert numero > 0, "Número deve ser positivo!"
    # Não recomendado, pois no modo otimizado pode ser ignorado
```

Para algo crítico, como validar entradas, use estruturas de controle normais:

```python
def verificar_positivo(numero):
    if numero <= 0:
        raise ValueError("Número deve ser positivo!")
```

<!--
#### em classes

- **garantindo consistência de atributos em uma classe**

O `assert` pode ser usado para garantir que os atributos de uma classe estejam corretos após a inicialização:

```python
class Retangulo:
    def __init__(self, largura, altura):
        assert largura > 0 and altura > 0, "Largura e altura devem ser maiores que zero"
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura

r = Retangulo(5, 10)  # Funciona normalmente
r = Retangulo(-5, 10)  # Lança AssertionError: "Largura e altura devem ser maiores que zero"
```

Aqui, o `assert` garante que nenhum retângulo seja criado com dimensões inválidas.

- **não usar `assert` para validação de dados do usuário ao criar objetos**

Novamente, se os dados estão vindo de uma fonte externa (usuário, por exemplo), não é recomendado usar `assert`:

```python
class Retangulo:
    def __init__(self, largura, altura):
        assert largura > 0, "Largura inválida!"  # Não recomendado para entrada de dados
```

O correto seria usar verificações explícitas e lançar exceções adequadas:

```python
class Retangulo:
    def __init__(self, largura, altura):
        if largura <= 0 or altura <= 0:
            raise ValueError("Largura e altura devem ser maiores que zero")
```
-->

#### em módulos e importações

- **verificando importações**

O `assert` pode ser usado para garantir que módulos importantes sejam importados corretamente:

```python
try:
    import numpy as np
except ImportError:
    np = None

assert np is not None, "Módulo numpy não está instalado"
```

Aqui, o `assert` assegura que o módulo `numpy` está disponível antes de continuar a execução do programa.

#### em testes

- **testes automatizados**

O `assert` é muito útil em testes automatizados, para garantir que uma função retorne os valores esperados:

```python
def somar(a, b):
    return a + b

# testes
assert somar(2, 3) == 5, "A soma de 2 e 3 deve ser 5"
assert somar(-1, 1) == 0, "A soma de -1 e 1 deve ser 0"
```

Esses testes ajudam a garantir que o comportamento da função está correto. Se algo falhar, o `AssertionError` informará o erro.

- **uso incorreto para lidar com erros esperados**

Se está verificando se uma função lança uma exceção, o `assert` pode não ser a melhor escolha. Por exemplo:

```python
def dividir(a, b):
    return a / b

try:
    dividir(10, 0)
except ZeroDivisionError:
    pass
else:
    assert False, "Deveria ter levantado ZeroDivisionError"
```

Aqui, a maneira correta seria utilizar um framework de testes como `unittest` ou `pytest`, que têm funcionalidades adequadas para verificar exceções.

### resumo

**Quando usar `assert`:**
- Para verificar suposições durante o desenvolvimento (não em produção).
- Para garantir a consistência de dados e condições lógicas internas.
- Em testes automatizados, onde se deseja garantir que determinadas condições sejam verdadeiras.

**Quando não usar `assert`:**
- Para validar entradas do usuário ou outras condições que devem ser garantidas em produção.
- Para substituir controles de fluxo ou verificar erros críticos.
- Em verificações que podem afetar a segurança ou integridade de um sistema, especialmente porque `assert` é desabilitado no modo otimizado (`-O`).

## exercícios `assert`

<details>
<summary>Lista de Exercícios</summary>

1. **Verificando valores**: Escreva um código que recebe um número `x` e usa `assert` para garantir que `x` seja positivo.
1. **Divisão por zero**: Crie uma função `dividir(a, b)` que divide `a` por `b` e usa `assert` para garantir que `b` não seja zero.
1. **Comprimento da string**: Escreva um código que recebe uma string `s` e usa `assert` para garantir que a string tenha pelo menos 5 caracteres.
1. **Lista vazia**: Crie uma função que verifica se uma lista `lst` está vazia e, se sim, lança uma exceção usando `assert`.
1. **Soma de números positivos**: Escreva uma função `soma_positivos(a, b)` que soma dois números e usa `assert` para garantir que ambos sejam positivos.
1. **Raiz quadrada de número positivo**: Crie uma função `raiz_quadrada(x)` que calcula a raiz quadrada de um número. Use `assert` para garantir que `x` é positivo.
1. **Maior que zero em loop**: Escreva uma função que percorra uma lista de números e use `assert` para garantir que todos os números sejam maiores que zero.
1. **Garantindo a ordem de uma lista**: Crie uma função `verificar_ordenacao(lista)` que usa `assert` para garantir que todos os elementos da lista estão em ordem crescente.
1. **Validação de ano**: Escreva uma função que receba um ano e use `assert` para garantir que o ano seja maior que 0.
1. **Fatorial de um número**: Crie uma função `fatorial(n)` que calcula o fatorial de `n` e usa `assert` para garantir que `n` seja maior ou igual a zero.
1. **Média de notas**: Escreva uma função que recebe uma lista de notas e usa `assert` para garantir que todas as notas estão entre 0 e 10.
1. **Índice válido em lista**: Escreva uma função que usa `assert` para garantir que um índice fornecido está dentro dos limites de uma lista.
1. **Número ímpar**: Escreva uma função que recebe um número e usa `assert` para garantir que o número é ímpar.
1. **Verificando a soma de uma lista**: Crie uma função que recebe uma lista de números e usa `assert` para garantir que a soma de todos os elementos da lista é maior que 100.
1. **Verificando divisibilidade**: Escreva uma função que recebe dois números e usa `assert` para garantir que o primeiro número é divisível pelo segundo.
1. **Todos pares**: Escreva uma função que percorre uma lista e usa `assert` para garantir que todos os números são pares.
1. **Número dentro de intervalo**: Crie uma função que recebe um número e usa `assert` para garantir que o número está no intervalo entre 10 e 20.
1. **Tamanho da lista**: Escreva uma função que usa `assert` para garantir que uma lista tenha pelo menos 3 elementos.
1. **Soma de inteiros**: Escreva uma função que recebe dois valores e usa `assert` para garantir que ambos são inteiros antes de somá-los.
1. **Divisão de números pares**: Escreva uma função que recebe dois números e usa `assert` para garantir que ambos são pares antes de realizar a divisão.
1. **Verificação de senha**: Crie uma função `verificar_senha(senha)` que usa `assert` para garantir que a senha tenha pelo menos 8 caracteres.
1. **Números diferentes**: Escreva uma função que recebe dois números e usa `assert` para garantir que eles são diferentes.
1. **Palavra com letra específica**: Escreva uma função que usa `assert` para garantir que uma string contém a letra 'a' pelo menos uma vez.
1. **Lista de strings não vazias**: Crie uma função que percorra uma lista de strings e use `assert` para garantir que nenhuma das strings é vazia.
1. **Produto de lista não zero**: Escreva uma função que percorra uma lista de números e usa `assert` para garantir que o produto de todos os números não seja zero.
1. **Números na sequência**: Crie uma função que recebe uma lista de números e usa `assert` para garantir que a sequência dos números seja crescente ou decrescente.
1. **Valores maiores que 10**: Escreva uma função que usa `assert` para garantir que todos os valores em uma lista são maiores que 10.
1. **Verificação de vogais**: Escreva uma função que usa `assert` para garantir que uma string contém pelo menos uma vogal.
1. **Intervalo fechado**: Crie uma função que recebe dois números e usa `assert` para garantir que o segundo número é maior que o primeiro.
1. **Verificando múltiplos de 3**: Escreva uma função que percorra uma lista de números e use `assert` para garantir que todos os números são múltiplos de 3.

</details>

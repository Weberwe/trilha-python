# recursão

A **recursão** é uma técnica de programação onde uma função chama a si mesma para resolver um problema. É usada quando um problema pode ser dividido em subproblemas menores de forma semelhante ao problema original, permitindo que o código se repita até alcançar uma condição de parada (base case), que é quando o problema não pode mais ser dividido ou resolvido por chamadas subsequentes.

## como funciona

A recursão segue um padrão em que uma função realiza duas ações principais:

1. **condição base (ou condição de parada)** : esta é a condição que determina quando a recursão deve parar. Sem uma condição base, a recursão continuaria indefinidamente, causando um erro de "stack overflow" (estouro da pilha) porque a memória reservada para as chamadas da função ficaria esgotada;

2. **chamada recursiva** : a função chama a si mesma com um novo argumento, que é uma versão reduzida ou alterada do problema original. Essa chamada recursiva é o que permite que a função repita o processo para resolver o subproblema;

A cada vez que uma função é chamada, o Python cria um novo **frame de execução** na pilha de chamadas (call stack), o que significa que cada chamada recursiva aguarda a conclusão da chamada anterior. Quando a condição base é atingida, o resultado é retornado e a pilha de chamadas começa a "desenrolar", retornando os resultados de volta pelas chamadas anteriores até o ponto inicial.

## exemplos de uso

### fatorial

Um exemplo clássico de recursão é o cálculo do fatorial de um número. O fatorial de um número (n) (denotado como (n!)) é o produto de todos os números inteiros positivos até (n).

**definição matemática** :
- n! = n * (n - 1) * (n - 2) * ... * 1

- Ou, recursivamente :
  - n! = n * (n - 1)! (com (1! = 1) como caso base)

Em Python, isso pode ser escrito assim:

```python
>>> def fatorial(n):
...     # condição base: fatorial de 0 ou 1 é 1
...     if n == 0 or n == 1:
...         return 1
...     # chamada recursiva: n * fatorial de (n - 1)
...     return n * fatorial(n - 1)
...
>>> print(fatorial(5))
120
>>> |
```

Aqui, o `fatorial(5)` chamará `fatorial(4)`, que chamará `fatorial(3)`, e assim por diante até chegar em `fatorial(1)`. A partir daí, os valores são retornados até a função original.

### sequência de fibonacci

Outro exemplo clássico é a **Sequência de Fibonacci**, onde o próximo número na sequência é a soma dos dois anteriores. A sequência começa com 0 e 1.

**definição recursiva** :
- Fibonacci(n) = Fibonacci(n-1) + Fibonacci(n-2)
- Caso base: Fibonacci(0) = 0, Fibonacci(1) = 1

A implementação em Python seria :

```python
>>> def fibonacci(n):
...     # condição base: fibonacci(0) é 0 e fibonacci(1) é 1
...     if n == 0:
...         return 0
...     elif n == 1:
...         return 1
...     # chamada recursiva: fibonacci(n-1) + fibonacci(n-2)
...     return fibonacci(n - 1) + fibonacci(n - 2)
...
>>> print(fibonacci(6))
8
>>> |
```

Nesse exemplo, `fibonacci(6)` chamará `fibonacci(5)` e `fibonacci(4)`, e assim por diante, até que os casos base sejam alcançados.

## para que se usa

A recursão é útil em várias situações onde um problema pode ser dividido de forma natural em subproblemas menores que podem ser resolvidos da mesma maneira. Alguns exemplos incluem:

1. **problemas de divisão e conquista** : como algoritmos de ordenação como merge sort e quick sort, que dividem um problema grande em partes menores e resolvem essas partes recursivamente;

2. **problemas com árvores ou grafos** : a recursão é frequentemente usada em estruturas de dados como árvores e grafos, onde cada nó pode ser tratado de maneira recursiva;

3. **soluções elegantes para problemas matemáticos** : muitos problemas matemáticos, como o cálculo de potências, combinações, ou recorrências, podem ser resolvidos recursivamente;

4. **algoritmos de busca** : como a busca em profundidade (depth first search) em grafos, onde cada vizinho é visitado recursivamente;

## como usar

Para usar recursão de forma eficaz, siga estas etapas :

1. **defina a condição base** : esta é a parte mais importante para evitar loops infinitos. Sempre certifique-se de que a função possui uma condição clara que encerra a recursão;

2. **reduza o problema** : a cada chamada recursiva, reduza o problema, de forma que ele se aproxime da condição base. Isso pode ser feito alterando o argumento da função;

3. **chame a função recursivamente** : chame a função novamente com o argumento modificado para resolver o subproblema;

## ponto de atenção

### pilha de chamadas e limite de recursão

Cada chamada recursiva consome memória na **pilha de chamadas** (call stack). Em Python, há um limite de profundidade de recursão (padrão de 1000 chamadas), que pode ser verificado e alterado, se necessário:

```python
>>> import sys
>>> print(f'{sys.getrecursionlimit() = }')
sys.getrecursionlimit() = 1000
>>>
>>> sys.setrecursionlimit(2000)
>>>
>>> print(f'{sys.getrecursionlimit() = }')
sys.getrecursionlimit() = 2000
>>>
>>> |
```

Isso evita o "stack overflow" em situações onde a recursão não termina ou o número de chamadas recursivas é muito grande.

## quando evitar

Embora a recursão possa ser elegante e direta, nem sempre é a solução mais eficiente. Recursões mal planejadas podem levar a desperdício de memória e tempo, especialmente em problemas onde as chamadas se repetem muitas vezes, como no exemplo da sequência de Fibonacci. Nestes casos, técnicas como **memorização** ou transformar a recursão em **iteração** podem ser mais eficientes.

## recursão vs. iteração

- **recursão** : resolve o problema chamando a função repetidamente e dividindo o problema em subproblemas;
- **iteração** : resolve o problema usando laços (como `while` ou `for`) e controlando diretamente o fluxo com variáveis de estado;

Exemplo da sequência de Fibonacci de forma iterativa:

```python
>>> def fibonacci_iterativo(n):
...     a, b = 0, 1
...     for _ in range(n):
...         a, b = b, a + b
...     return a
...
>>> print(fibonacci_iterativo(6))
8
>>> |
```

A versão iterativa costuma ser mais eficiente em termos de uso de memória e tempo de execução.

## exemplos

Abaixo há 5 exemplos que mostram como resolver problemas tanto de forma **recursiva** quanto **iterativa**. Cada problema é resolvido com essas duas abordagens.

---

### 1. soma de uma lista de números

#### versão recursiva :

```python
>>> def soma_recursiva(lista):
...     # condição base : lista vazia
...     if len(lista) == 0:
...         return 0
...     # chamada recursiva : soma o primeiro elemento com a soma do restante da lista
...     return lista[0] + soma_recursiva(lista[1:])
...
>>> print(soma_recursiva([1, 2, 3, 4]))
10
>>> |
```

#### versão iterativa :

```python
>>> def soma_iterativa(lista):
...     soma = 0
...     for num in lista:
...         soma += num
...     return soma
...
>>> print(soma_iterativa([1, 2, 3, 4]))
10
>>> |
```

---

### 2. contagem regressiva

#### versão recursiva :

```python
>>> def contagem_regressiva_recursiva(n):
...     if n == 0:
...         print("Lançar!")
...     else:
...         print(n)
...         contagem_regressiva_recursiva(n - 1)
...
>>> contagem_regressiva_recursiva(5)
5, 4, 3, 2, 1, Lançar!
>>> |
```

#### versão iterativa :

```python
>>> def contagem_regressiva_iterativa(n):
...     while n > 0:
...         print(n)
...         n -= 1
...     print("Lançar!")
...
>>> contagem_regressiva_iterativa(5)
5, 4, 3, 2, 1, Lançar!
>>> |
```

---

### 3. produto dos elementos de uma lista

#### versão recursiva :

```python
>>> def produto_recursivo(lista):
...     if len(lista) == 0:
...         return 1
...     return lista[0] * produto_recursivo(lista[1:])
...
>>> print(produto_recursivo([1, 2, 3, 4]))
24
>>> |
```

#### versão iterativa :

```python
>>> def produto_iterativo(lista):
...     produto = 1
...     for num in lista:
...         produto *= num
...     return produto
...
>>> print(produto_iterativo([1, 2, 3, 4]))
24
>>> |
```

---

### 4. reverter uma string

#### versão recursiva :

```python
>>> def reverter_string_recursiva(s):
...     if len(s) == 0:
...         return ""
...     return s[-1] + reverter_string_recursiva(s[:-1])
...
>>> print(reverter_string_recursiva("python"))
nohtyp
>>> |
```

#### versão iterativa :

```python
>>> def reverter_string_iterativa(s):
...     resultado = ""
...     for char in s:
...         resultado = char + resultado
...     return resultado
...
>>> print(reverter_string_iterativa("python"))
nohtyp
>>> |
```

---

### 5. verificar se um número é par

#### versão recursiva :

```python
>>> def eh_par_recursivo(n):
...     if n == 0:
...         return True
...     elif n == 1:
...         return False
...     return eh_par_recursivo(n - 2)
...
>>> print(eh_par_recursivo(8))
True
>>> print(eh_par_recursivo(7))
False
>>> |
```

#### versão iterativa :

```python
>>> def eh_par_iterativo(n):
...     while n > 1:
...         n -= 2
...     return n == 0
...
>>> print(eh_par_iterativo(8))
True
>>> print(eh_par_iterativo(7))
False
>>> |
```

---

Esses exemplos mostram como a recursão é usada para quebrar um problema em subproblemas menores, enquanto a iteração usa laços para alcançar o mesmo resultado. Dependendo do problema e da sua complexidade, uma abordagem pode ser mais eficiente que a outra.

## exercícios

<details>
<summary>Lista de Exercícios</summary>

Para cada exercício abaixo, primeiro monte uma função de sua versão usando a iteração e depois sua versão usando a recursão.

1. **Soma dos primeiros N números naturais** : Escreva uma função recursiva que calcule a soma dos primeiros N números naturais.
1. **Fatorial de um número** : Crie uma função recursiva que calcule o fatorial de um número \(n!\).
1. **Soma dos elementos de uma lista** : Escreva uma função recursiva que receba uma lista de números e retorne a soma de seus elementos.
1. **Produto dos elementos de uma lista** : Crie uma função recursiva que calcule o produto dos elementos de uma lista.
1. **Contagem regressiva** : Implemente uma função recursiva que faça uma contagem regressiva de um número N até 0.
1. **Sequência de Fibonacci** : Escreva uma função recursiva para calcular o N-ésimo número da sequência de Fibonacci.
1. **Inverter uma string** : Crie uma função recursiva que inverta uma string.
1. **Contar ocorrências de um caractere em uma string** : Implemente uma função recursiva que conte quantas vezes um determinado caractere aparece em uma string.
1. **Número de dígitos de um número** : Escreva uma função recursiva que determine o número de dígitos de um número inteiro.
1. **Verificar se um número é par** : Crie uma função recursiva para verificar se um número é par sem usar operadores aritméticos além de subtração.
1. **Máximo divisor comum (MDC)** : Implemente o algoritmo de Euclides para encontrar o MDC entre dois números usando recursão.
1. **Imprimir os elementos de uma lista de trás para frente** : Escreva uma função recursiva que imprima os elementos de uma lista em ordem inversa.
1. **Somar todos os dígitos de um número** : Crie uma função recursiva que receba um número inteiro e retorne a soma de seus dígitos.
1. **Verificar se uma palavra é palíndromo** : Implemente uma função recursiva que verifique se uma string é um palíndromo (lê-se da mesma forma de trás para frente).
1. **Exponenciação** : Escreva uma função recursiva que calcule o valor de \(a^b\), onde \(a\) é a base e \(b\) é o expoente.
1. **Soma dos números pares de uma lista** : Crie uma função recursiva que receba uma lista de números e retorne a soma de todos os números pares.
1. **Somar elementos de uma lista de listas** : Escreva uma função recursiva que some todos os elementos de uma lista que contém outras listas.
1. **Encontrar o menor elemento de uma lista** : Implemente uma função recursiva que encontre o menor número em uma lista de números.
1. **Substituir um caractere em uma string** : Crie uma função recursiva que substitua todas as ocorrências de um caractere específico em uma string por outro caractere.
1. **Contar elementos em uma lista aninhada** : Escreva uma função recursiva que conte quantos elementos (incluindo os das sublistas) existem em uma lista aninhada.

</details>


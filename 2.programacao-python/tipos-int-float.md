# tipos int e float

## operação de atribuição composta

A operação de atribuição composta no Python é uma maneira concisa de combinar uma operação aritmética ou lógica com a atribuição de valor a uma variável. Em vez de escrever a operação completa de forma explícita, é possível usar um operador de atribuição composto, que realiza a operação e, ao mesmo tempo, atribui o resultado à mesma variável.

A sintaxe geral para uma operação de atribuição composta é :

```python
variável operador= valor
```

Isso é equivalente a:
```python
variável = variável operador valor
```

### exemplos

Aqui estão alguns exemplos de operadores de atribuição compostos e como eles funcionam :

1. **Adição composta `+=`**
    ```python
    x = 5
    x += 3  # equivale a x = x + 3
    print(x)  # saída : 8
    ```

1. **Subtração composta `-=`**
    ```python
    x = 5
    x -= 2  # equivale a x = x - 2
    print(x)  # saída : 3
    ```

1. **Multiplicação composta `*=`**
    ```python
    x = 4
    x *= 3  # equivale a x = x * 3
    print(x)  # saída : 12
    ```

1. **Divisão composta `/=`**
    ```python
    x = 10
    x /= 2  # equivale a x = x / 2
    print(x)  # saída : 5.0
    ```

1. **Módulo composto `%=`**
    ```python
    x = 10
    x %= 3  # equivale a x = x % 3
    print(x)  # saída : 1
    ```

1. **Exponenciação composta `**=`**
    ```python
    x = 2
    x **= 3  # equivale a x = x ** 3
    print(x)  # saída : 8
    ```

1. **Divisão inteira composta `//=`**
    ```python
    x = 10
    x //= 3  # equivale a x = x // 3
    print(x)  # saída : 3
    ```

<!-- 1. **Operador bitwise AND composto `&=`**
    ```python
    x = 5  # 0b0101
    x &= 3  # 0b0011, equivale a x = x & 3
    print(x)  # saída : 1 (0b0001)
    ``` -->

<!-- 1. **Operador bitwise OR composto `|=`**
    ```python
    x = 5  # 0b0101
    x |= 2  # 0b0010, equivale a x = x | 2
    print(x)  # saída : 7 (0b0111)
    ``` -->

<!-- 1. **Operador bitwise XOR composto `^=`**
    ```python
    x = 5  # 0b0101
    x ^= 3  # 0b0011, equivale a x = x ^ 3
    print(x)  # saída : 6 (0b0110)
    ``` -->

### vantagens

- **código mais conciso** : reduz a repetição, tornando o código mais limpo e fácil de ler;
- **desempenho** : em algumas situações, operações compostas podem ser ligeiramente mais eficientes, embora a diferença geralmente seja mínima;

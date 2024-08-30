Índice

1. [comando def](#comando-def)
1. [argumentos nas funções](#argumentos-nas-funções)
    1. [argumentos posicionais](#argumentos-posicionais)
1. [comando return](#comando-return)
1. [exemplos de aula](#exemplos-de-aula)
1. [exercícios](#exercícios)

# funções

Uma função é um bloco de código que executa alguma operação. Opcionalmente, uma função pode definir parâmetros de entrada que permitem que os chamadores passem argumentos para a função. Uma função também pode retornar um valor como saída. As funções são úteis para encapsular operações comuns em um só bloco reutilizável, idealmente com um nome que descreve de modo claro o que a função faz.

## comando `def`

O comando `def` em Python é utilizado para declarar funções. Ele é uma das palavras-chave mais importantes na linguagem, pois permite que se defina blocos de código que podem ser chamados e reutilizados em diferentes partes de um programa.

### **o que é o comando `def`?**

O `def` é uma abreviação de "define" e é usado para definir uma nova função. Uma função, no contexto da programação, é um bloco de código que realiza uma tarefa específica e pode ser reutilizado sempre que necessário. Quando se usa `def`, se está essencialmente criando um novo comando personalizado que pode ser executado em qualquer ponto do seu código.

### **sintaxe do comando `def`**

A sintaxe básica do `def` para criar uma função é a seguinte :

```python
def nome_da_funcao(parâmetros_opcionais):
    """Docstring opcional"""
    corpo_da_funcao
```

O que é cada parte :

- **`def`** : esta palavra-chave inicia a definição da função;
- **`nome_da_funcao`** : este é o nome que se dá à função. Deve ser descritivo e seguir as regras de nomenclatura do Python (não pode começar com números, não pode conter espaços, e não pode ser uma palavra reservada);
- **`parâmetros_opcionais`** : entre parênteses, pode-se definir parâmetros que a função aceita. Eles são opcionais, o que significa que pode-se ter funções sem parâmetros;
- **`:`** : Os dois-pontos marcam o fim da linha de declaração e indicam que o corpo da função começa na linha seguinte;
- **`"""Docstring opcional"""`** : uma string entre três aspas, usada para documentar o que a função faz. Essa parte é opcional, mas é uma boa prática incluí-la;
- **`corpo_da_funcao`** : este é o bloco de código que define o que a função faz. Esse bloco deve ser indentado (geralmente com quatro espaços) em relação à linha de declaração;

### **exemplo básico de definição de função**

Aqui está um exemplo de como definir uma função simples que imprime uma mensagem de saudação :

```python
>>> def saudacao():
...     """Esta função imprime uma saudação simples."""
...     print("Olá, bem-vindo ao Python!")
...
>>> |
```

Neste exemplo :
- **`def saudacao():`** : define uma função chamada `saudacao` que não aceita parâmetros;
- **`"""Esta função imprime uma saudação simples."""`** : é uma docstring que descreve a função;
- **`print("Olá, bem-vindo ao python!")`** : é o corpo da função, que será executado quando a função for chamada;

### **execução do comando `def`**

Quando o Python encontra o comando `def` durante a execução do programa, ele não executa imediatamente o código dentro da função. Em vez disso, ele "registra" a função com o nome fornecido, o que significa que a função existe na memória e pode ser chamada posteriormente no código.

Exemplo :

```python
>>> def saudacao():
...     print("Olá, bem-vindo ao Python!")
...
>>>
>>> print("Antes de chamar a função.")
Antes de chamar a função.
>>> saudacao()
Olá, bem-vindo ao Python!
>>> print("Depois de chamar a função.")
Depois de chamar a função.
>>> |
```

Neste exemplo :
- o python passa pela definição da função `saudacao` e a armazena;
- a função `saudacao()` é chamada, o que faz com que o código dentro da função seja executado;

### **docstrings e comentários**

As docstrings são usadas para documentar funções, tornando o código mais legível e fácil de entender. Elas podem ser acessadas usando a função `help()` ou o atributo `.__doc__` da função.

Exemplo :

```python
>>> def multiplicar(a, b):
...     """Esta função retorna o produto de dois números."""
...     return a * b
...
>>> print(multiplicar.__doc__)
Esta função retorna o produto de dois números.
>>> |
```

## argumentos nas funções

Em Python, funções podem aceitar entradas na forma de **parâmetros**. Quando uma função é definida, pode-se especificar os parâmetros, que atuam como variáveis que recebem valores quando a função é chamada. Esses valores são chamados de **argumentos**.

- **parâmetros** são os nomes usados na definição da função;
- **argumentos** são os valores que você passa para a função quando a chama;

### argumentos posicionais

**Argumentos posicionais** são a maneira mais comum de passar valores para uma função. Eles são chamados de "posicionais" porque os valores passados são associados aos parâmetros com base na posição.

Exemplo básico :

```python
>>> def soma(a, b):
...     return a + b
...
>>> |
```

Aqui :
- **`a` e `b`** são os parâmetros da função;
- quando a função é chamada, são fornecidos dois argumentos que serão mapeados para `a` e `b` com base em sua ordem;

Chamando a função :

```python
>>> resultado = soma(3, 5)
>>> print(resultado)
8
>>> |
```

Neste exemplo :
- **`3`** é o primeiro argumento, que é mapeado para o parâmetro `a`;
- **`5`** é o segundo argumento, que é mapeado para o parâmetro `b`;
- a função retorna a soma dos dois valores, `8`, que é armazenada em `resultado`;

#### **como funciona a ordem dos argumentos?**

A ordem dos argumentos é crucial em funções que utilizam parâmetros posicionais. O Python associa cada argumento ao seu respectivo parâmetro pela ordem em que são fornecidos. Se inverter a ordem dos argumentos, os valores atribuídos aos parâmetros mudam.

Exemplo :

```python
>>> def dividir(dividendo, divisor):
...     return dividendo / divisor
...
>>>
>>> resultado1 = dividir(10, 2)
>>> resultado2 = dividir(2, 10)
>>>
>>> print(resultado1)
5.0
>>> print(resultado2)
0.2
>>> |
```

Aqui :
- em **`resultado1 = dividir(10, 2)`**, `10` é mapeado para `dividendo` e `2` é mapeado para `divisor`.
- em **`resultado2 = dividir(2, 10)`**, `2` é mapeado para `dividendo` e `10` é mapeado para `divisor`.

A ordem dos argumentos influencia diretamente o resultado da operação.

#### **número de argumentos e parâmetros**

A função deve ser chamada com o mesmo número de argumentos que o número de parâmetros definidos, ou o Python levantará um erro.

Exemplo :

```python
>>> def multiplicar(a, b, c):
...     return a * b * c
...
>>> # multiplicar(2, 3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: multiplicar() missing 1 required positional argument: 'c'
>>> |
```

Neste exemplo :
- A função `multiplicar` espera três argumentos. Se for fornecido menos ou mais, o Python levantará um erro `TypeError`;

### **quando usar argumentos posicionais**

Os argumentos posicionais são ideais quando :
- a ordem dos argumentos faz sentido para a operação da função;
- todos os parâmetros devem ser fornecidos para a função operar corretamente;
- a clareza do código é mantida quando os argumentos são passados em uma ordem específica;

## comando `return`

O comando `return` em Python é utilizado dentro de funções para indicar que a função deve devolver um valor ao ponto onde foi chamada. Quando uma função atinge o `return`, ela termina imediatamente sua execução e o controle do programa retorna para o código que chamou a função. Esse valor retornado pode ser usado, armazenado em uma variável, ou mesmo ignorado.

### **o que é o comando `return`?**

O `return` é uma palavra-chave em Python que serve para duas finalidades principais :
- **encerrar a execução da função** : quando o `return` é executado, a função para de executar, mesmo que haja código após o `return`;
- **retornar um valor** : o `return` pode devolver um valor específico, que pode ser utilizado no código que chamou a função;

### **como o `return` funciona em funções?**

Quando uma função tem um `return`, ela se comporta de forma diferente de uma função que apenas executa código sem `return`. Com `return`, a função pode fornecer resultados que podem ser armazenados e usados posteriormente.

Exemplo simples :

```python
>>> def soma(a, b):
...     return a + b
...
>>>
>>> # chamando a função
>>> resultado = soma(3, 5)
>>> print(resultado)
*
>>> |
```

Aqui, a função `soma` aceita dois argumentos `a` e `b`, e retorna a soma deles.

Neste exemplo :
- **`soma(3, 5)`**: chama a função e passa os valores 3 e 5 como argumentos;
- **`return a + b`**: calcula a soma de 3 e 5, que é 8, e retorna esse valor;
- **`resultado = soma(3, 5)`**: armazena o valor retornado, 8, na variável `resultado`;

### **funções com `return` sem valor específico**

Se `return` for utilizado sem nenhum valor, ele simplesmente encerra a função, mas não retorna nenhum dado. Essa prática é mais comum para indicar o fim prematuro de uma função, dependendo de uma condição específica.

Exemplo :

```python
>>> def verificar_par(n):
...     if n % 2 == 0:
...         print(f"{n} é par.")
...         return
...     print(f"{n} é ímpar.")
...
>>> # chamando a função
>>> verificar_par(4)
4 é par.
>>> verificar_par(7)
7 é ímpar.
>>> |
```

Aqui, quando o número é par, a função imprime que o número é par e usa `return` para encerrar a função. Quando o número é ímpar, o código continua até o próximo `print`.

### **retornando múltiplos valores**

Python permite que retorne múltiplos valores de uma função, utilizando uma vírgula para separá-los. Esses valores são retornados como uma tupla.

Exemplo :

```python
>>> def operacoes(a, b):
...     soma = a + b
...     diferenca = a - b
...     return soma, diferenca
...
>>>
>>> resultado_soma, resultado_diferenca = operacoes(10, 5)
>>> print(f"Soma: {resultado_soma}, Diferença: {resultado_diferenca}")
Soma: 15, Diferença: 5
>>> |
```

Neste exemplo :
- **`return soma, diferenca`** : retorna dois valores, `soma` e `diferenca`;
- **`resultado_soma, resultado_diferenca = operacoes(10, 5)`** : os valores retornados são desembrulhados em duas variáveis;

### **retornando estruturas de dados**

Funções podem retornar qualquer tipo de dado, incluindo listas, dicionários, tuplas, etc.

Exemplo :

```python
>>> def criar_lista(a, b, c):
...     return [a, b, c]
...
>>> minha_lista = criar_lista(1, 2, 3)
>>> print(minha_lista)
[1, 2, 3]
>>> |
```

### **comportamento de `return` dentro de laços e condicionais**

O `return` pode ser usado dentro de laços (`for`, `while`) ou condicionais (`if`, `else`). Ao ser executado, o `return` imediatamente encerra a função, mesmo que ainda existam laços ou código após o `return`.

Exemplo :

```python
>>> def encontrar_numero(lista, alvo):
...     for numero in lista:
...         if numero == alvo:
...             return True
...     return False
...
>>> encontrado = encontrar_numero([1, 2, 3, 4, 5], 3)
>>> print(encontrado)
True
>>> |
```

Neste exemplo:
- se o número `alvo` for encontrado na lista, a função retorna `true` e para a execução;
- se o laço terminar sem encontrar o `alvo`, a função retorna `false`;

### **retorno implícito de `None`**

Se uma função não tiver um `return` explícito, ou se o `return` não especificar um valor, a função retorna `None` por padrão.

Exemplo :

```python
>>> def funcao_sem_return():
...     pass
...
>>>
>>> resultado = funcao_sem_return()
>>> print(resultado)
None
>>> |
```

Neste exemplo, como não há `return` na função, o Python retorna automaticamente `None`.

## exemplos de aula

```python
def soma_tudo(valor):
    """essa funcao ira somar todos os valores a partir
    de zero ate o valor especificado em valor """
    numeros = list(range(valor))
    soma = 0

    for num in numeros:
        soma += num

    print(f'{soma = }')

    return soma

def lista_numeros(valor, limite):
    """ sempre deixar o valor menor que o limite """

    if valor > limite:
        print('digite um valor menor que o limite')
    else:
        while valor < limite:
            print(f'{valor = }')
            valor += 1
    print('fim do while')

def realiza_operacoes(a, b):
    print(f'{a + b = }')
    print(f'{a - b = }')
    print(f'{a * b = }')
    print(f'{a / b = }')
    print(f'{a ** b = }')

def verifica_paridade(valor):
    if valor % 2 == 0:
        print('eh par')
        return

    print("eh impar")

soma_tudo(10)
soma_tudo(100)
soma_tudo(1132)
soma_tudo(14)
soma_tudo(42)
soma_tudo(10000)

for i in range(30):
    soma_tudo(i)

for i in range(20,30):
    print(f'{i = }',end = ' - ')
    soma_tudo(i)

print(soma_tudo.__doc__)

realiza_operacoes(1,2)
realiza_operacoes(11,2)
realiza_operacoes(4,7)

while True:
    v1 = int(input(' digite um valor (0 para sair): '))
    v2 = int(input(' digite outro valor : '))

    if not v1:
        break

    lista_numeros(v1, v2)

for i in range(2,17,3):
    resultado = soma_tudo(i)

    print(f'{resultado = }')
    verifica_paridade(resultado)
```

## exercícios

<details>
<summary>Lista de Exercícios</summary>

1. funções sem argumentos
    1. Crie uma função chamada `mostrar_boas_vindas` que imprime "Bem-vindo ao Python!".
        ```python
        def mostrar_boas_vindas():
            print("Bem-vindo ao Python!")

        mostrar_boas_vindas()
        ```
    1. Defina uma função chamada `exibir_data_atual` que imprime a data atual.
    1. Escreva uma função chamada `mostrar_linha` que imprime uma linha de 40 asteriscos.
    1. Crie uma função chamada `exibir_mensagem_padrao` que imprime uma mensagem motivacional.
    1. Defina uma função chamada `mostrar_nota_maxima` que imprime a nota máxima possível em um exame.
    1. Crie uma função chamada `imprimir_autor` que imprime o nome do autor de um livro fictício.
    1. Escreva uma função chamada `exibir_versao_software` que imprime a versão atual de um software.
    1. Crie uma função chamada `mostrar_horario` que imprime o horário atual.
    1. Defina uma função chamada `exibir_pi` que imprime o valor de π (pi).
    1. Escreva uma função chamada `mostrar_linguagem_programacao` que imprime "Python" como a linguagem de programação favorita.
1. funções com argumentos posicionais (sem valor padrão)
    1. Crie uma função chamada `saudacao` que recebe um nome e imprime uma saudação personalizada.
    1. Escreva uma função chamada `calcular_area_retangulo` que recebe a largura e a altura de um retângulo e retorna a área.
    1. Defina uma função chamada `calcular_perimetro` que recebe o comprimento e a largura de um retângulo e retorna o perímetro.
    1. Crie uma função chamada `multiplicar_numeros` que recebe dois números e retorna o produto deles.
    1. Escreva uma função chamada `converter_para_dolar` que recebe um valor em reais e a taxa de câmbio, e retorna o valor convertido para dólares.
    1. Crie uma função chamada `calcular_velocidade_media` que recebe a distância e o tempo, e retorna a velocidade média.
    1. Defina uma função chamada `calcular_desconto` que recebe o preço original e a porcentagem de desconto, e retorna o valor com desconto aplicado.
    1. Crie uma função chamada `exibir_nome_completo` que recebe o primeiro e o último nome de uma pessoa, e imprime o nome completo.
    1. Escreva uma função chamada `calcular_media` que recebe três notas e retorna a média aritmética.
    1. Crie uma função chamada `calcular_volume_cilindro` que recebe o raio e a altura de um cilindro, e retorna o volume.
1. funções com retorno de um ou mais valores
    1. Defina uma função chamada `calcular_soma_e_produto` que recebe dois números e retorna a soma e o produto deles.
    1. Escreva uma função chamada `converter_temperatura` que recebe uma temperatura em Celsius e retorna a temperatura em Fahrenheit e Kelvin.
    1. Crie uma função chamada `calcular_diferenca_e_divisao` que recebe dois números e retorna a diferença e o quociente deles.
    1. Defina uma função chamada `calcular_potencia` que recebe uma base e um expoente, e retorna a base elevada ao expoente e a raiz quadrada da base.
    1. Escreva uma função chamada `calcular_min_e_max` que recebe três números e retorna o menor e o maior valor entre eles.
    1. Crie uma função chamada `calcular_imc` que recebe o peso e a altura de uma pessoa, e retorna o IMC (Índice de Massa Corporal) e a classificação (abaixo do peso, normal, sobrepeso, obesidade).
    1. Defina uma função chamada `calcular_distancias` que recebe duas coordenadas (x1, y1) e (x2, y2), e retorna a distância horizontal e vertical entre elas.
    1. Escreva uma função chamada `calcular_hipotenusa` que recebe os comprimentos dos dois catetos de um triângulo retângulo, e retorna o comprimento da hipotenusa.
    1. Crie uma função chamada `calcular_area_perimetro_retangulo` que recebe a largura e a altura de um retângulo, e retorna a área e o perímetro.
    1. Defina uma função chamada `calcular_media_variancia` que recebe uma lista de números, e retorna a média e a variância dos números.
1. retorno de estruturas mais complexas (listas, tuplas, sets e dicionários)
    1. Escreva uma função chamada `criar_lista_numeros` que recebe três números e retorna uma lista contendo esses números.
    1. Crie uma função chamada `criar_tupla_nomes` que recebe três nomes e retorna uma tupla contendo esses nomes.
    1. Defina uma função chamada `criar_set_numeros` que recebe três números e retorna um set contendo esses números.
    1. Escreva uma função chamada `criar_dicionario_pessoa` que recebe nome, idade e cidade, e retorna um dicionário contendo essas informações.
    1. Crie uma função chamada `criar_lista_quadrados` que recebe uma lista de números e retorna uma lista contendo o quadrado de cada número.
    1. Defina uma função chamada `criar_tupla_cubos` que recebe uma lista de números e retorna uma tupla contendo o cubo de cada número.
    1. Escreva uma função chamada `criar_set_palavras_unicas` que recebe uma lista de palavras e retorna um set contendo as palavras únicas.
    1. Crie uma função chamada `criar_dicionario_quantidade_letras` que recebe uma lista de palavras e retorna um dicionário onde as chaves são as palavras e os valores são a quantidade de letras em cada palavra.
    1. Defina uma função chamada `criar_lista_pares_impares` que recebe uma lista de números e retorna duas listas, uma contendo os números pares e outra os ímpares.
    1. Escreva uma função chamada `criar_dicionario_contagem_caracteres` que recebe uma string e retorna um dicionário onde as chaves são os caracteres e os valores são o número de vezes que cada caractere aparece na string.
1. retorno implícito
    1. Crie uma função chamada `verificar_positivo` que recebe um número e retorna True se o número for positivo, e False caso contrário.
    1. Defina uma função chamada `verificar_par` que recebe um número e retorna True se o número for par, e False se for ímpar.
    1. Escreva uma função chamada `verificar_palindromo` que recebe uma palavra e retorna True se a palavra for um palíndromo, e False caso contrário.
    1. Crie uma função chamada `verificar_maioridade` que recebe a idade de uma pessoa e retorna True se a pessoa for maior de idade, e False caso contrário.
    1. Defina uma função chamada `verificar_letra` que recebe uma string e uma letra, e retorna True se a letra estiver na string, e False caso contrário.
    1. Escreva uma função chamada `verificar_substring` que recebe duas strings, e retorna True se a segunda string for uma substring da primeira, e False caso contrário.
    1. Crie uma função chamada `verificar_numero_primo` que recebe um número e retorna True se o número for primo, e False caso contrário.
    1. Defina uma função chamada `verificar_lista_vazia` que recebe uma lista e retorna True se a lista estiver vazia, e False caso contrário.
    1. Escreva uma função chamada `verificar_todos_pares` que recebe uma lista de números e retorna True se todos os números forem pares, e False caso contrário.
    1. Crie uma função chamada `verificar_palavras_mesma_tamanho` que recebe duas palavras e retorna True se ambas tiverem o mesmo número de caracteres, e False caso contrário.

</details>

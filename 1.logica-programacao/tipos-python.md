# tipos do python

Veja agora alguns dos tipos do Python.

## Números

O interpretador funciona como uma calculadora simples. A expressão que for digitada será executada e a resposta será apresentada. Os operadores usados são os mesmos da matemática.
- `+` para adição;
- `-` para subtração;
- `*` para multiplicação;
- `/` para divisão;

Veja alguns exemplos :
```python
>>> 1 + 1
2
>>> 50 - 8
42
>>> 3 * 5
15
>>> 4 / 2
2.0
>>> |
```

Assim como na matemática, os parênteses podem ser usados para mudar a ordem de execução dos operadores. Se for necessário, mais parênteses internos podem ser adicionados.

```python
>>> 10 * 4 + 2
42
>>> 10 * (4 + 2)
60
>>>
>>> # o IMC é calculado usando o peso divido pelo quadrado da altura
>>> 90 / (1.8 * 1.8)
27.777777777777775
>>>
>>> 10 / 3 + 2 - 5 * -2 * 1
15.333333333333334
>>> (10 / (3 + 2) - 5 * (-2 * 1))
12.0
>>> |
```

Repare que o resultado da divisão foi o que apresentou maior diferença em todas as respostas. Surgiu um `.0` junto ao dois, no primeiro exemplo. Isso acontece por haver distinção entre os tipos numéricos.

Os **números inteiros** são aqueles que não apresentação valor fracionário (2, 3, 5, 7, 12, 42). São representados pela sigla `int`.

Os números que possuem a parte fracionária, são chamados de **números de ponto flutuante** (3.14, 1.81, 2.0). São representados pela sigla `float`. Os números do tipo float são especificados com um ponto `.` em vez da vírgula `,` como é usado no Brasil. Isso acontece porque a vírgula é usada para separar itens. Se fizer `3,14`, o Python irá interpretar como sendo dois números de uma tupla (veremos o que é mais adiante), o número 3 seguido do número 14.

Uma divisão **SEMPRE** irá retornar um valor do tipo float, mesmo se o resultado tiver uma parte fracionária zerada (3.000000000000). Para realizar uma divisão e captar apenas a parte inteira (o quociente), usa-se o operador `//`. Para recuperar apenas o resto da divisão, usa-se o operador `%`. Em termos de precedência dos operadores, eles são equivalentes da multiplicação e divisão.

Veja abaixo alguns exemplos :
```python
>>> 76 / 5  # divisão tradicional sempre retorna um float, dividendo / divisor
15.2000
>>> 76 // 5  # o operador // retorna a parte inteira da divisão, o quociente
15
>>> 76 % 5  # o operador % retorna o resto da divisão
1
>>> 15 * 5 + 1  # quociente * divisor + resto = dividendo
76
>>> |
```
<img
    src="https://matematicafacil.mat.br/cursos/ensinofundamental/4aserie/blog6741.jpg"
    alt="imagem dos elementos da divisão"
    width="65%">

Com o Python, é possível usar o operador `**` para calcular potências e raízes :
```python
>>> 5 ** 2  # 5 ao quadrado
25
>>> 2 ** 7  # 2 elevado na potência 7
128
>>> 36 ** (1/2)  # raiz quadrada de 36
6.0
>>> |
```

E assim como na matemática, os operadores também tem sua ordem de execução :
1. `()`
1. `**`
1. `*` `/` `//` `%`
1. `+` `-`

Além de `int` e `float`, o Python também suporta outros tipos de números, como `Decimal` e `Fraction` usando pacotes específicos. E, também, há suporte nativo a números complexos, usando os sufixos `j` ou `J` para indicar a parte imaginária.

```python
>>> 3+5j
(3+5j)
>>>
>>> 3+5j - 2-3j
(1+2j)
>>> |
```

## Variáveis
Nos exemplos acima, todos os valores usados, uma vez que foram calculados, eram perdidos. O resultado da equação `2 ** 7` vai ser mostrado e descartado. É necessário que toda linguagem de programação seja capaz de aceitar, armazenar e nomear dados.

Um programa deve ser capaz de receber dados do teclado (ou de outra parte do seu programa) e associar a um nome aquele dado. Este dado pode ser um valor simples ou múltiplos valores que são associados a um nome. Dados que são associados a um nome e que guarda dado é chamada de *variável*. Pense na variável como uma caixa com um nome do lado de fora dela e que pode colocar o que quiser dentro.

O Python possui muitas formas diferentes de armazenar listas de dados. É conveniente associar nomes aos dados. O sinal de igual `=` é usado para atribuir um valor a uma variável.
```python
>>> idade = 76
>>> nome = 'Arnold Schwarzenegger'
>>>
>>> idade
61
>>> nome
'Arnold Schwarzenegger'
>>> 2024 - idade
1948
>>> |
```

Caso tente-se usar uma variável não definida, irá levantar um erro :
```python
>>> numero
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'numero' is not defined
>>> |
```

Com o uso de variáveis, é possível armazenar o valor para usar posteriormente.

### PEP 8 - Variáveis
<details>
  <summary>Detalhes</summary>

Quando você escreve código, é necessário dar nome para muitas coisas: variáveis, funções, classes, pacotes e por aí vai. Escolher nomes corretos irá poupar seu tempo e energia mais tarde.

Por exemplo, é uma péssima prática usar l, O ou I como nome de variáveis. Dependendo da fonte usada, essas letras podem se passar e serem confundidas com 1 e 0.
```python
>>> O = 2  # não é recomendado
>>> O  # isso seria um zero ou a letra o maíuscula?
2
>>> |
```
Fazendo isso, parece que se está tentando salvar o valor 2 no valor zero, o que é impossível.

#### Nomes das Variáveis
As variáveis devem iniciar com o primeiro caractere sendo uma letra (há outro caractere permitido, mas será visto bem mais tarde). Depois do primeiro, pode-se usar números também. Espaços não são permitidos para os nomes, então é usado o sublinhado `_` para separar as palavras. Variáveis também não podem possuir acentuações ou cedilhas nos nomes.

Lembrando que esse tipo de nomenclatura é conhecida como [*snake_case*](https://www.alura.com.br/artigos/convencoes-nomenclatura-camel-pascal-kebab-snake-case#snake-case).

```python
>>> # variáveis com nomes permitidos
>>> resposta = 42
>>> resposta
42
>>> valor1 = 12
>>> valor1
12
>>> valor_2 = 20
>>> valor_2
20
>>> primeiro_nome = 'Arnold'
>>> primeiro_nome
'Arnold'
>>> # nomes de variáveis que não são recomendados ou que geram erro
>>> ação = 'atacar'
>>> ação
'atacar'
>>> 2_dois = 2
  File "<stdin>", line 1
    2_dois = 2
     ^
SyntaxError: invalid decimal literal
>>> primeiro nome = 'Arnold'
  File "<stdin>", line 1
    primeiro nome = 'Arnold'
             ^^^^
SyntaxError: invalid syntax
>>> |
```

#### Nomes Proibidos
O Python possui diversas palavras-chave que não podem ser usadas como nomes de variáveis. Se algum valor for tentado associar a ela, irá levantar um erro de sintaxe :

```python
>>> if = 10
  File "<stdin>", line 1
    if = 10
       ^
SyntaxError: invalid syntax
>>> and = 50
  File "<stdin>", line 1
    and = 50
    ^^^
SyntaxError: invalid syntax
>>> while = 1
  File "<stdin>", line 1
    while = 1
          ^
SyntaxError: invalid syntax
>>> for = 10
  File "<stdin>", line 1
    for = 10
        ^
SyntaxError: invalid syntax
>>> return = 20
  File "<stdin>", line 1
    return = 20
           ^
SyntaxError: invalid syntax
>>>
>>> # Mais algumas palavras reservadas :
>>> # pass if elif else while for break continue and or not in is import from
>>> # as try except raise finally with del print def return yield del global
>>> # class exec lambda assert
```

</details>

## Exercícios de Números

<details>
  <summary>Lista</summary>

Para os exercícios abaixo, use variáveis e comentários quando achar necessário.

Apesar de serem exercícios com muitos cálculos matemáticos, o objetivo deles não é a resposta em si, mas como transformar uma fómula matemática em um algoritmo para ser usado com Python.

Por exemplo, considere a fórmula do círculo.

<img
    src="https://s3.static.brasilescola.uol.com.br/be/2023/06/formula-da-area-do-circulo.jpg"
    alt="imagem dos elementos da divisão"
    width="45%">

Para transformar em algoritmo, pode se fazer de várias formas :

```python
>>> # método 1
>>> print(3.14 * 10 ** 2)
314.0
>>>
>>> # método 2
>>> raio = 10
>>> pi = 3.14
>>> print(pi * raio ** 2)
314.0
>>>
>>> # método 3
>>> raio = 10
>>> pi = 3.14
>>> area = pi * raio * raio
>>> print(area)
314.0
>>>
```

1. Exercícios Simples
    1. Calcule a área de um quadrado de lado 5.
        ```python
        lado = 5
        area = lado * lado  # método 1
        area = lado * 2  # método 2
        print('a área do quadrado é')
        print(area)
        print(lado * lado)
        ```
    1. Calcule a área de um retângulo de base 8 e altura 6.
        ```python
        base = 8
        altura = 6
        area = base * altura
        print('a área do retângulo é')
        print(area)
        ```
    1. Calcule o perímetro de um triângulo equilátero de lado 7.
        ```python
        lado = 7
        perimetro = lado + lado + lado  # método 1
        perimetro = lado * 3  # método 2
        print(perimetro)
        ```
    1. Calcule o volume de um cubo de lado 3.
        ```python
        lado = 3
        volume = lado * lado * lado  # método 1
        volume = lado ** 3  # método 2
        print(volume)
        ```
    1. Calcule a área de um círculo de raio 4 (use π = 3.14).
        ```python
        PI = 3.14
        raio = 4
        area = pi * raio ** 2
        print(area)
        ```
    1. Calcule a hipotenusa de um triângulo retângulo com catetos 3 e 4.
        ```python
        cateto1 = 3
        cateto2 = 4
        cat1_mais_cat2 = (cateto1 ** 1) + (cateto2 ** 2)
        hipotenusa = cat1_mais_cat2 ** (1/2)  # método 1
        hipotenusa = cat1_mais_cat2 ** 0.5  # método 2
        print(hipotenusa)
        ```
    1. Calcule a área de um triângulo de base 10 e altura 5.
        ```python
        base = 10
        altura = 5
        area = (base * altura) / 2
        print(area)
        ```
    1. Calcule o perímetro de um retângulo de base 9 e altura 4.
        ```python
        base = 9
        altura = 4
        perimetro = base * 2 + altura * 2
        print(perimetro)
        ```
    1. Calcule a área de um losango com diagonais 8 e 6.
        ```python
        diagonal1 = 8
        diagonal2 = 6
        area = diagonal1 * diagonal2 / 2
        print(area)
        ```
    1. Calcule o volume de um paralelepípedo de arestas 2, 3 e 5.
        ```python
        aresta1 = 2
        aresta2 = 3
        aresta3 = 5
        volume = aresta1 * aresta2 * aresta3
        print(volume)
        ```
1. Exercícios de Nível Intermediário
    1. Calcule a área de um trapézio com bases 7 e 5 e altura 4.
    1. Calcule o volume de uma esfera de raio 3 (use π = 3.14).
    1. Calcule a área lateral de um cilindro de raio 3 e altura 7 (use π = 3.14).
    1. Calcule o volume de um cone de raio 4 e altura 9 (use π = 3.14).
    1. Calcule a distância entre os pontos (1, 2) e (4, 6).
    1. Resolva a equação quadrática x² - 5x + 6 = 0 usando a fórmula de Bhaskara.
    1. Calcule a área de um hexágono regular de lado 6.
    1. Calcule o perímetro de um pentágono regular de lado 8.
    1. Calcule a área de um setor circular de raio 5 e ângulo 60° (use π = 3.14).
    1. Calcule o volume de um prisma de base triangular com lados 3, 4, 5 e altura 10.
1. Exercícios Avançados
    1. Calcule a área de um octógono regular de lado 7.
    1. Calcule a área total de um cilindro de raio 4 e altura 10 (use π = 3.14).
    1. Calcule o volume de uma pirâmide quadrangular de base 6 e altura 9.
    1. Calcule o comprimento da diagonal de um retângulo de lados 6 e 8.
    1. Calcule a área de um triângulo equilátero de lado 12.
    1. Calcule o volume de um tetraedro regular de aresta 5.
    1. Resolva a equação quadrática 2x² - 4x - 6 = 0 usando a fórmula de Bhaskara.
    1. Calcule a área de um polígono regular de 10 lados com lado 4.
    1. Calcule o volume de um cilindro de raio 5 e altura 12 (use π = 3.14).
    1. Calcule a distância entre os pontos (3, 5) e (9, 12).
1. Exercícios Complexos
    1. Calcule a área de um dodecágono regular de lado 8.
    1. Calcule o volume de uma esfera de raio 7 (use π = 3.14).
    1. Calcule a área de um triângulo isósceles de lados 10, 10 e 12.
    1. Calcule o volume de um tronco de cone com raios 5 e 3 e altura 8 (use π = 3.14).
    1. Resolva a equação quadrática 3x² - 12x + 9 = 0 usando a fórmula de Bhaskara.
    1. Calcule a área de um círculo inscrito em um triângulo de lados 6, 8 e 10 (use π = 3.14).
    1. Calcule o perímetro de um triângulo equilátero inscrito em um círculo de raio 6 (use π = 3.14).
    1. Calcule o volume de um prisma hexagonal de base 4 e altura 15.
    1. Calcule a área de um paralelogramo de base 9 e altura 6.
    1. Calcule a área total de um cone de raio 5 e geratriz 13 (use π = 3.14).
1. Exercícios Muito Complexos
    1. Calcule a área de um decágono regular de lado 10.
    1. Calcule o volume de uma pirâmide hexagonal de base 6 e altura 10.
    1. Calcule a área de um triângulo retângulo inscrito em um semicírculo de raio 8 (use π = 3.14).
    1. Calcule o volume de um cilindro inscrito em um cubo de lado 10 (use π = 3.14).
    1. Resolva a equação quadrática x² - 4x - 12 = 0 usando a fórmula de Bhaskara.
    1. Calcule a área de um círculo circunscrito a um triângulo de lados 7, 24 e 25 (use π = 3.14).
    1. Calcule o volume de um dodecaedro regular de aresta 3.
    1. Calcule a área de um setor circular com raio 10 e ângulo 45° (use π = 3.14).
    1. Calcule a distância entre os pontos (2, -3) e (-4, 5).
    1. Calcule a área total de um cilindro inscrito em um cubo de lado 12 (use π = 3.14).

</details>

## Texto

O Python pode manipular texto (representado pelo tipo `str`, também chamado de `strings`), bem como os números. Isso inclui caracteres `!`, palavras `coelho`, nomes `Paris`, frases `Eu te protejo.`, `Oba! :)` etc.. Eles podem ser colocados entre aspas simples `'...'` ou aspas duplas `"..."` com o mesmo resultado.

```python
>>> 'sou um texto'  # aspas simples
'sou um texto'
>>> "sou outro texto"  # aspas duplas
'sou outro texto'
>>> '1984'  # dígitos e números entre aspas também são strings
'1984'
```

Para colocar aspas entre aspas, precisamos "escapá-la", precedendo-as com `\`. Alternativamente, podemos usar o outro tipo de aspas:

```python
>>> 'The Kids Aren\'t Alright'  # use \' para escapar as aspas simples...
"The Kids Aren't Alright"
>>> "The Kids Aren't Alright"  # ou use aspas duplas
"The Kids Aren't Alright"
>>>
>>> '"pois não", disse o garçom'
'"pois não", disse o garçom'
>>> "\"pois não\", disse o garçom"
'"pois não", disse o garçom'
>>> |
```

No shell do Python, a definição de string e a string de saída podem parecer diferentes. A função `print()` produz uma saída mais legível, omitindo as aspas delimitadoras e imprimindo caracteres de escape e especiais:
```python
>>> texto = 'linha um\nlinha dois'
>>> texto  # sem o print(), caracteres especiais são incluídos na string
'linha um\nlinha dois'
>>> print(texto)  # com o print, os caracteres especiais são interpretados
linha um
linha dois
>>>
```

### Caracteres Especiais

Os caracteres especiais são uma forma de mandar para a linguagem de programação comandos a serem executados de dentro da string :

- `\n` : é usado quando se quer criar uma nova linha na exibição do texto;
```python
>>> print('linha 1\nlinha 2\nlinha 3\nlinha 4\n')
linha 1
linha 2
linha 3
linha 4

>>> |
```
- `\t` : é usado quando se quer inserir uma tabulação no texto;
```python
>>> print('sem tabulação\n\tuma tabulação\n\t\tduas tabulações\n\t\t\ttrês tabulações')
sem tabulação
    uma tabulação
        duas tabulações
            três tabulações
>>> |
```

Se não quiser que os caracteres precedidos por `\` sejam interpretados como caracteres especiais, pode-se usar strings `raw` ("crua" ou sem processamento de caracteres de escape) adicionando um r antes da primeira aspa ou então colocando duas `\\`:

```python
>>> print('C:\nemo')  # aqui \n indica nova linha!
C:
emo
>>> print(r'C:\nemo')  # note o r antes da aspa
C:\nemo
>>> print('c:\nemo\\nemo')  # repare no uso duplo da \\
c:
emo\nemo
>>> |
```

Há um aspecto sutil nas strings raw: uma string raw não pode terminar em um número ímpar de caracteres `\`.

```python
>>> print(r'C:\nemo\\')
C:\nemo\\
>>>
>>> print(r'C:\nemo\\\')
  File "<stdin>", line 1
    print(r'C:\nemo\\\')
          ^
SyntaxError: unterminated string literal (detected at line 1)
>>> |
```

### String Literais

As strings literais podem abranger várias linhas. Uma maneira é usar as aspas triplas: `"""..."""` ou `'''...'''`. O fim das linhas é incluído automaticamente na string, mas é possível evitar isso adicionando uma `\` no final.
O seguinte exemplo:
```python
>>> print("""\
... Uso: alguma coisa [opcional]
...     -h                      Mostra esta mensagem.
...     -H hostname             Nome do host para conectar.
... """)
Uso: alguma coisa [opcional]
  -h              Mostra esta mensagem.
  -H hostname     Nome do host para conectar.

>>> |
```

```python
>>> print("""sou uma string
... dividida em apenas \
... duas linhas""")
sou uma string
dividida em apenas duas linhas
>>> |
```

## Exercícios de Texto e Print

<details>
  <summary>Lista de Exercícios</summary>

1. Exercícios Simples
    1. Crie uma string com seu nome e imprima-a.
    1. Crie uma string com uma citação famosa e imprima-a.
    1. Use aspas duplas para criar uma string e imprima-a.
    1. Use aspas simples para criar uma string e imprima-a.
    1. Crie uma string com aspas dentro dela, usando aspas duplas e simples, e imprima-a.
    1. Crie uma string que contenha uma nova linha (\n) e imprima-a.
    1. Crie uma string que contenha um tab (\t) e imprima-a.
    1. Crie uma string que contenha tanto \n quanto \t e imprima-a.
    1. Crie uma string que contenha barras invertidas (\\) e imprima-a.
    1. Crie uma string usando raw string (prefixo r) e imprima-a.
1. Exercícios de Nível Intermediário
    1. Crie uma string com várias linhas usando \n e imprima-a.
    1. Crie uma string com várias tabs usando \t e imprima-a.
    1. Crie uma string com um caminho de arquivo usando barras invertidas e imprima-a.
    1. Use raw string para criar um caminho de arquivo e imprima-a.
    1. Combine aspas duplas e simples em uma string e imprima-a.
    1. Crie uma string que contenha aspas simples escapadas e imprima-a.
    1. Crie uma string que contenha aspas duplas escapadas e imprima-a.
    1. Crie uma string com uma citação famosa usando raw string e imprima-a.
    1. Crie uma string que contenha um caractere de nova linha escapado (\\n) e imprima-a.
    1. Crie uma string que contenha um caractere de tab escapado (\\t) e imprima-a.
1. Exercícios Avançados
    1. Crie uma string longa usando múltiplas linhas e o caractere \n e imprima-a.
    1. Crie uma string longa usando múltiplas tabs e o caractere \t e imprima-a.
    1. Crie uma string com várias barras invertidas (\\\\) e imprima-a.
    1. Crie uma string que combine várias linhas, tabs e barras invertidas e imprima-a.
    1. Use raw string para criar uma string com várias linhas e tente imprimi-la.
    1. Use raw string para criar uma string com várias tabs e tente imprimí-la.
    1. Use raw string para criar uma string com várias barras invertidas e imprima-a.
    1. Combine aspas duplas, simples e barras invertidas em uma string e imprima-a.
    1. Crie uma string com uma citação famosa que contenha várias linhas e imprima-a.
    1. Crie uma string com um poema que contenha várias tabs e imprima-a.
1. Exercícios Complexos
    1. Crie uma string que represente uma linha de JSON e imprima-a.
    1. Crie uma string que represente uma linha de script HTML e imprima-a.
    1. Crie uma string que contenha CSS com várias linhas e imprima-a.
    1. Crie uma string que contenha código Python com várias linhas e imprima-a.
    1. Crie uma string com uma mensagem que use aspas duplas, simples, \n e \t, e imprima-a.
    1. Crie uma string que represente um caminho de rede e imprima-a.
    1. Crie uma string que contenha uma citação longa com várias linhas e tabs, e imprima-a.
    1. Use raw string para criar uma string com código Python e imprima-a.
    1. Use raw string para criar uma string com script HTML e imprima-a.
    1. Use raw string para criar uma string com CSS e imprima-a.
1. Exercícios Muito Complexos
    1. Crie uma string que contenha um bloco de código JSON com várias linhas e imprima-a.
    1. Crie uma string que contenha um bloco de código HTML com várias linhas e imprima-a.
    1. Crie uma string que contenha um bloco de código CSS com várias linhas e imprima-a.
    1. Crie uma string que contenha um bloco de código Python com várias linhas e imprima-a.
    1. Combine raw string com uma string que contenha um bloco de código Python e imprima-a.
    1. Combine raw string com uma string que contenha um bloco de código HTML e imprima-a.
    1. Combine raw string com uma string que contenha um bloco de código CSS e imprima-a.
    1. Crie uma string que contenha um caminho de arquivo complexo e imprima-a.
    1. Crie uma string que combine várias técnicas de formatação (raw string, escapamento, \n, \t) e imprima-a.
    1. Crie uma string que contenha um script completo em qualquer linguagem de programação e imprima-a.

</details>


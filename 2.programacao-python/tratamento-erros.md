Índice

1. [o que é uma exceção?](#o-que-é-uma-exceção)
1. [blocos `try` e `except`](#blocos-try-e-except)
1. [porque usar `try` e `except`](#porque-usar-try-e-except)
1. [erros](#erros)
    1. [resumo](#resumo)
    1. [`ZeroDivisionError`](#zerodivisionerror)
    1. [`ValueError`](#ValueError)
    1. [`TypeError`](#TypeError)
    1. [`IndexError`](#IndexError)
    1. [`KeyError`](#KeyError)
    1. [`ImportError`](#ImportError)
    1. [`FileNotFoundError`](#FileNotFoundError)
    1. [`NameError`](#NameError)
1. [cuidados](#cuidados)
1. [exercícios](#exercícios)
1. [exceções múltiplas](#exceções-múltiplas)
1. [exercícios exceções múltiplas](#exercícios-exceções-múltiplas)

# tratamento de erros

O tratamento de erros em Python é uma parte crucial do desenvolvimento de software robusto e estável. Para isso, Python oferece estruturas como `try`, `except`, `else`, `finally`, que permitem ao desenvolvedor capturar e gerenciar exceções, evitando que o programa falhe abruptamente.

## o que é uma exceção?

Uma **exceção** é um evento anômalo ou erro que ocorre durante a execução de um programa. Isso pode ocorrer por vários motivos, como:
- uma divisão por zero (`ZeroDivisionError`);
- tentar acessar um índice fora dos limites de uma lista (`IndexError`);
- erros de tipos, como tentar somar um número e uma string (`TypeError`);

Quando ocorre uma exceção, Python interrompe a execução normal e procura um bloco de código que possa lidar com essa exceção. Se não encontrar, o programa será encerrado e uma mensagem de erro será exibida.

## blocos `try` e `except`

O bloco `try` é utilizado para envolver o código que pode gerar uma exceção. Quando um bloco `try` é executado, o Python "monitora" as instruções para ver se ocorre alguma exceção. Se não houver exceção, o programa continua normalmente. Se ocorrer uma exceção, o fluxo do programa muda e o controle é passado para o bloco `except`.

O bloco `except` é usado para capturar e lidar com as exceções que podem ocorrer no bloco `try`. Se uma exceção acontece no bloco `try`, Python interrompe a execução das instruções restantes nesse bloco e procura por um bloco `except` adequado. Se o tipo da exceção gerada corresponde ao tipo especificado no `except`, o código dentro do bloco `except` será executado.

**Estrutura básica**
```python
try:
    # código que pode gerar uma exceção
except TipoDaExceção:
    # código para tratar a exceção
```

**Explicação**

- **bloco `try` : o bloco `try` é onde se coloca o código que deseja "proteger"; se ocorrer algum erro dentro deste bloco, ele será interceptado e o controle será passado para o bloco `except`;
- **bloco `except` : o bloco `except` captura a exceção que ocorre no bloco `try`; pode-se especificar o tipo de exceção que deseja capturar (como `ValueError`, `TypeError`, etc.); se uma exceção ocorre e o tipo da exceção corresponde ao especificado no `except`, o código dentro desse bloco é executado;

Exemplo simples:

```python
try:
    x = 1 / 0
except ZeroDivisionError:
    print("Divisão por zero não é permitida!")
```

Neste exemplo, o bloco `try` tenta executar uma divisão por zero, o que resulta na exceção `ZeroDivisionError`. O bloco `except` captura essa exceção e imprime a mensagem.

## porque usar `try` e `except`

O objetivo do tratamento de exceções é evitar que o programa pare inesperadamente quando ocorre um erro. Imagine que um erro ocorra ao tentar abrir um arquivo que não existe. Sem tratamento de exceções, o programa seria interrompido, e todas as operações subsequentes não seriam executadas. Com o uso de `try` e `except`, pode-se "prever" que esse erro pode ocorrer e fornecer uma solução apropriada ou alternativa.

Aqui está um exemplo de como `try` e `except` ajudam a controlar a abertura de um arquivo :

```python
try:
    arquivo = open("arquivo_inexistente.txt", "r")
except FileNotFoundError:
    print("Erro: O arquivo não foi encontrado.")
```

## erros

Abaixo estão vários erros são comuns e podem ocorrer em diversos contextos durante a execução de um programa.

### resumo

1. `ZeroDivisionError`: ocorre quando tenta-se dividir ou calcular o módulo por zero;
1. `ValueError`: ocorre quando um valor é passado para uma função ou operação que não pode processá-lo, mesmo que o tipo seja correto;
1. `TypeError`: ocorre quando tipos incompatíveis são usados em uma operação ou função;
1. `IndexError`:ocorre quando há uma tentativa de acessar um índice inválido em uma sequência;
1. `KeyError`: ocorre quando há uma tentativa de acessar uma chave inexistente em um dicionário;
1. `ImportError`: ocorre quando há uma falha ao importar um módulo ou componente específico;
1. `FileNotFoundError`: ocorre quando o Python tenta abrir um arquivo que não existe no caminho especificado;
1. `NameError`: ocorre quando uma variável, função ou nome é chamado, mas não está definido;

---

### `ZeroDivisionError`

O `ZeroDivisionError` ocorre quando uma operação de divisão ou módulo tenta dividir um número por zero. Em matemática, a divisão por zero é indefinida, e o Python levanta essa exceção para sinalizar que algo está errado.

Esse erro acontece ao tentar :
- dividir um número por zero (`a / 0` ou `a // 0`)
- calcular o módulo de um número por zero (`a % 0`)

#### Exemplos

- **divisão simples por zero**
    ```python
    try:
        resultado = 10 / 0
    except ZeroDivisionError:
        print("Erro: Tentativa de divisão por zero.")
    ```

    - neste código, o bloco `try` tenta dividir `10` por `0`, o que gera um erro de `ZeroDivisionError`;
    - o bloco `except` captura essa exceção e imprime uma mensagem indicando que ocorreu uma tentativa de divisão por zero;

- **operador de módulo com zero**
    ```python
    try:
        resultado = 10 % 0
    except ZeroDivisionError:
        print("Erro: Tentativa de calcular o módulo com zero.")
    ```

    - o operador de módulo (`%`) também levanta um `ZeroDivisionError` quando o divisor é zero;
    - esse erro é capturado no bloco `except`, e uma mensagem de erro é exibida;

- **tratamento de divisão segura**
    ```python
    def dividir(a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Erro: Não é possível dividir por zero."

    resultado = dividir(10, 0)
    print(resultado)  # saída : "Erro: Não é possível dividir por zero."
    ```

    - a função `dividir` tenta dividir dois números; se o divisor for zero, o `ZeroDivisionError` é capturado e uma mensagem apropriada é retornada;
    - isso evita que o programa falhe e garante uma execução controlada;

---

### `ValueError`

O `ValueError` ocorre quando uma função ou operação recebe um argumento do tipo correto, mas com um valor inválido. Isso acontece quando o valor fornecido não faz sentido no contexto esperado, mesmo que o tipo de dado esteja correto.

Esse erro é comum nas seguintes situações :
- tentar converter uma string para um número, mas a string contém caracteres não numéricos;
- passar valores que estão fora do intervalo esperado para funções que exigem certos limites;
- fornecer um número inadequado de elementos a uma função que espera uma sequência com uma quantidade específica de elementos;

#### Exemplos

- **conversão de string para inteiro**
    ```python
    try:
        numero = int("abc")
    except ValueError:
        print("Erro: Não é possível converter 'abc' para um número inteiro.")
    ```

    - o `int()` tenta converter a string `"abc"` para um número inteiro; como `"abc"` não é uma string numérica válida, um `ValueError` é gerado;
    - o erro é capturado no `except` e uma mensagem é exibida;

- **raiz quadrada de um número negativo**
    ```python
    import math

    try:
        resultado = math.sqrt(-10)
    except ValueError:
        print("Erro: Não é possível calcular a raiz quadrada de um número negativo.")
    ```

    - o método `math.sqrt()` gera um `ValueError` quando tenta calcular a raiz quadrada de um número negativo, pois no conjunto dos números reais isso não é possível;
    - o erro é capturado no bloco `except`;

- **conversão de lista de strings para inteiros**
    ```python
    lista = ["1", "2", "três", "4"]
    numeros = []

    for item in lista:
        try:
            numeros.append(int(item))
        except ValueError:
            print(f"Erro: '{item}' não é um número válido.")

    print(numeros)  # saída : [1, 2, 4]
    ```

    - é realizada uma tentativa de converter cada item da lista de strings em inteiros; no entanto, o item `"três"` não pode ser convertido para um número, o que gera um `ValueError`;
    - esse erro é tratado para que apenas os itens válidos sejam adicionados à lista `numeros`;

- **intervalo inválido em função de conversão**
    ```python
    try:
        numero = int("1000", 5)  # Converte "1000" da base 5 para um número decimal
    except ValueError:
        print("Erro: '1000' não é um número válido na base 5.")
    ```

    - o `int()` aqui está sendo usado para converter a string `"1000"` da base 5 para decimal; na base 5, os dígitos válidos são apenas `0`, `1`, `2`, `3`, e `4`; o dígito `5` em `"1000"` gera um `ValueError` porque não é um valor válido para a base especificada;

---

### `TypeError`

O `TypeError` ocorre quando uma operação ou função recebe um argumento de um tipo inadequado. Isso acontece quando um objeto de um tipo inesperado é passado para uma operação que exige outro tipo.

Esse erro é comum nas seguintes situações :
- tentar realizar operações aritméticas entre tipos incompatíveis (por exemplo, somar uma string com um número);
- passar um número de argumentos errado para uma função;
- usar operadores ou métodos que não são aplicáveis ao tipo de objeto fornecido;

#### Exemplos

- **soma de string com número**
    ```python
    try:
        resultado = "5" + 10
    except TypeError:
        print("Erro: Não é possível somar uma string com um número.")
    ```

    - o Python gera um `TypeError` porque é inválido somar uma string (`"5"`) com um número inteiro (`10`);
    - o bloco `except` captura o erro e exibe uma mensagem apropriada;

- **multiplicação de lista por string**
    ```python
    try:
        resultado = [1, 2, 3] * "2"
    except TypeError:
        print("Erro: Não é possível multiplicar uma lista por uma string.")
    ```

    - aqui, Python tenta multiplicar uma lista por uma string, o que não faz sentido; listas só podem ser multiplicadas por números inteiros para replicar os elementos;
    - isso gera um `TypeError`;

- **chamada de função com número incorreto de argumentos**
    ```python
    def somar(a, b):
        return a + b

    try:
        resultado = somar(1)
    except TypeError:
        print("Erro: A função 'somar' requer dois argumentos.")
    ```

    - a função `somar` foi definida para aceitar dois argumentos (`a` e `b`), mas foi passado apenas um argumento (`1`), o que gera um `TypeError`;
    - esse erro é capturado e uma mensagem explicativa é exibida;

- **comparação entre tipos incompatíveis**
    ```python
    try:
        resultado = "texto" > 10
    except TypeError:
        print("Erro: Não é possível comparar uma string com um número.")
    ```

    - python gera um `TypeError` porque comparar uma string com um número usando `>` não é uma operação válida;

---

### `IndexError`

O `IndexError` ocorre quando tenta-se acessar um índice que está fora dos limites de uma sequência (como listas, tuplas ou strings). Em outras palavras, o índice que estamos tentando acessar não existe na sequência.

Esse erro acontece nas seguintes situações :
- tentativa de acessar um índice maior ou igual ao comprimento da sequência;
- tentativa de acessar um índice negativo que excede o início da sequência;
- alterar o tamanho da sequência enquanto itera sobre ela, resultando em índices inválidos;

#### Exemplos

- **acessando um índice fora do alcance**
    ```python
    lista = [1, 2, 3]

    try:
        print(lista[3])  # Índices válidos são 0, 1, 2
    except IndexError:
        print("Erro: Índice fora do alcance da lista.")
    ```

    - a lista `lista` tem três elementos com índices `0`, `1` e `2`;
    - ao tentar acessar `lista[3]`, estamos buscando um quarto elemento inexistente;
    - o Python gera um `IndexError`, que é capturado no bloco `except`;

- **índices negativos fora do alcance**
    ```python
    lista = [10, 20, 30]

    try:
        print(lista[-4])  # Índices negativos válidos: -1, -2, -3
    except IndexError:
        print("Erro: Índice negativo fora do alcance da lista.")
    ```

    - em Python, índices negativos começam do final da lista (`-1` é o último elemento);
    - para uma lista de tamanho 3, índices negativos válidos são `-1`, `-2` e `-3`;
    - tentar acessar `lista[-4]` excede o limite negativo, gerando um `IndexError`;

- **modificando a lista durante a iteração**
    ```python
    lista = [1, 2, 3, 4]

    try:
        for i in range(len(lista)):
            lista.pop()
            print(lista[i])
    except IndexError:
        print("Erro: Índice fora do alcance após modificação da lista.")
    ```

    - o loop itera sobre os índices baseados no tamanho inicial da lista;
    - a cada iteração, `lista.pop()` remove o último elemento, diminuindo o tamanho da lista;
    - eventualmente, o índice `i` excede o tamanho atual da lista, resultando em um `IndexError`;

- **acesso em string**
    ```python
    texto = "Python"

    try:
        print(texto[10])
    except IndexError:
        print("Erro: Índice fora do alcance da string.")
    ```

    - a string `"Python"` tem 6 caracteres, com índices de `0` a `5`;
    - tentar acessar `texto[10]` está fora desses limites, gerando um `IndexError`;

---

### `KeyError`

O `KeyError` ocorre quando tenta-se acessar uma chave que não existe em um dicionário. Em outras palavras, estamos tentando obter o valor associado a uma chave inexistente.

Esse erro acontece nas seguintes situações :
- usar `dict[key]` com uma chave que não está no dicionário;
- tentar deletar uma chave que não existe;
- métodos como `pop()` sem valor padrão;

#### Exemplos

- **acessando uma chave inexistente**
    ```python
    dicionario = {'nome': 'Alice', 'idade': 30}

    try:
        print(dicionario['endereco'])
    except KeyError:
        print("Erro: A chave 'endereco' não existe no dicionário.")
    ```


    - o dicionário `dicionario` não possui a chave `'endereco'`;
    - tentar acessá-la diretamente gera um `KeyError`;

- **removendo uma chave inexistente**
    ```python
    dicionario = {'nome': 'Bob', 'idade': 25}

    try:
        del dicionario['telefone']
    except KeyError:
        print("Erro: Não é possível deletar a chave 'telefone' porque ela não existe.")
    ```

    - tentar deletar uma chave inexistente com `del` resulta em um `KeyError`;

- **iterando sobre chaves**
    ```python
    dicionario = {'a': 1, 'b': 2, 'c': 3}

    try:
        for chave in ['a', 'b', 'd']:
            print(f"{chave}: {dicionario[chave]}")
    except KeyError as e:
        print(f"Erro: A chave '{e.args[0]}' não existe no dicionário.")
    ```

    - ao iterar, tentamos acessar a chave `'d'`, que não existe;
    - o `KeyError` é capturado, e usa-se `e.args[0]` para obter a chave faltante;

---

### `ImportError`

O `ImportError` ocorre quando o Python não consegue importar um módulo, pacote ou componente específico. Isso pode acontecer por vários motivos, como o módulo não existir, o nome estar incorreto ou problemas com o caminho do módulo.

Esse erro acontece nas seguintes situações :
- tentar importar um módulo que não está instalado no ambiente python;
- escrever incorretamente o nome do módulo;
- tentar importar um componente que não existe dentro de um módulo;
- o módulo não está no caminho de pesquisa do python;

#### Exemplos

-  **importando um módulo inexistente**
    ```python
    try:
        import modulo_inexistente
    except ImportError:
        print("Erro: O módulo 'modulo_inexistente' não foi encontrado.")
    ```

    - tenta-se importar um módulo que não existe, resultando em um `ImportError`;

-  **erro de digitação no nome do módulo**
    ```python
    try:
        import mathh  # Deveria ser 'math'
    except ImportError:
        print("Erro: Módulo não encontrado. Verifique o nome do módulo.")
    ```

    - um simples erro de digitação impede o Python de encontrar o módulo, gerando um `ImportError`;

-  **importando função inexistente de um módulo**
    ```python
    try:
        from math import raiz_quadrada  # Deveria ser 'sqrt'
    except ImportError:
        print("Erro: Função 'raiz_quadrada' não encontrada no módulo 'math'.")
    ```

    - tenta-se importar uma função que não existe dentro do módulo, resultando em um `ImportError`;

-  **módulo não instalado**
    ```python
    try:
        import pandas
    except ImportError:
        print("Erro: O módulo 'pandas' não está instalado.")
    ```

    - se o módulo `pandas` não estiver instalado, o Python não pode importá-lo, gerando um `ImportError`;
    - solução: Instalar o módulo com `pip install pandas`;

-  **problema com o caminho do módulo**
    ```python
    try:
        import sys
        sys.path.append('/caminho/para/o/modulo')
        import meu_modulo
    except ImportError:
        print("Erro: Não foi possível importar 'meu_modulo' do caminho especificado.")
    ```

    - mesmo adicionando um novo caminho ao `sys.path`, se o módulo não estiver presente nesse caminho, o `ImportError` ocorrerá;

-  **usando `ModuleNotFoundError` no python 3.6+**
    ```python
    try:
        import modulo_inexistente
    except ModuleNotFoundError:
        print("Erro: Módulo não encontrado.")
    ```

    - no Python 3.6 e posteriores, `ModuleNotFoundError` é uma subclasse de `ImportError`;
    - captura especificamente erros em que o módulo não foi encontrado;

---

### `FileNotFoundError`

O `FileNotFoundError` ocorre quando o Python tenta abrir um arquivo que não existe no sistema. Isso geralmente acontece quando o caminho fornecido está incorreto ou o arquivo foi excluído ou movido. Esse erro é uma subclasse de `OSError` e é especificamente levantado para erros de sistema relacionados à abertura de arquivos inexistentes.

O `FileNotFoundError` pode ocorrer em diversos contextos :
- quando o arquivo que você tenta abrir não existe no caminho especificado;
- quando você tenta abrir um arquivo para leitura mas ele foi deletado, movido ou o caminho está incorreto;
- quando há erros de digitação no nome ou caminho do arquivo;

#### Exemplos

- **tentativa de abrir um arquivo inexistente**
    ```python
    try:
        arquivo = open('arquivo_inexistente.txt', 'r')
    except FileNotFoundError:
        print("Erro: O arquivo 'arquivo_inexistente.txt' não foi encontrado.")
    ```

    - tenta-se abrir um arquivo chamado `'arquivo_inexistente.txt'` para leitura;
    - como o arquivo não existe, o Python gera um `FileNotFoundError`, que é capturado pelo bloco `except`;

- **caminho incorreto**
    ```python
    try:
        arquivo = open('/caminho/incorreto/arquivo.txt', 'r')
    except FileNotFoundError:
        print("Erro: O caminho especificado para o arquivo está incorreto.")
    ```

    - o caminho fornecido para o arquivo está incorreto ou não existe no sistema;
    - o Python gera um `FileNotFoundError`, que é tratado no bloco `except`;

- **criando o arquivo se ele não existir**
    ```python
    caminho = 'novo_arquivo.txt'

    try:
        with open(caminho, 'r') as arquivo:
            conteudo = arquivo.read()
    except FileNotFoundError:
        with open(caminho, 'w') as arquivo:
            arquivo.write('Conteúdo inicial')
        print(f"O arquivo '{caminho}' foi criado com sucesso.")
    ```

    - tentamos abrir o arquivo para leitura; se o arquivo não existir, ele será criado no bloco `except` com o modo de escrita `'w'`, evitando o `FileNotFoundError`;

---

### `NameError`

O `NameError` ocorre quando tenta-se usar uma variável, função ou nome que não foi definido anteriormente. Isso significa que o Python não consegue encontrar uma referência ao nome que está sendo chamado no contexto atual.

O `NameError` pode ocorrer nas seguintes situações :
- tentar usar uma variável que nunca foi declarada;
- chamar uma função que não foi importada ou definida no escopo atual;
- nome de variável ou função digitado incorretamente;

#### Exemplos

- **uso de uma variável não definida**
    ```python
    try:
        print(x)
    except NameError:
        print("Erro: A variável 'x' não está definida.")
    ```

    - tenta-se imprimir a variável `x`, que não foi definida anteriormente, o que gera um `NameError`;
    - o erro é tratado e uma mensagem apropriada é exibida;

- **chamada de função não definida**
    ```python
    try:
        resultado = minha_funcao()
    except NameError:
        print("Erro: A função 'minha_funcao' não está definida.")
    ```

    - tenta-se chamar a função `minha_funcao()`, mas ela não foi definida ou importada;
    - o Python gera um `NameError` que é capturado e tratado no bloco `except`;

- **erro de digitação no nome da variável**
    ```python
    variavel = 10

    try:
        print(varaivel)  # Nome incorreto
    except NameError:
        print("Erro: A variável está mal escrita ou não foi definida.")
    ```

    - tenta-se imprimir `varaivel`, mas o nome correto é `variavel`; um simples erro de digitação resulta em um `NameError`;
    - o erro é tratado e uma mensagem explicativa é exibida;

- **verificação de nome global**
    ```python
    def minha_funcao():
        print("Função definida!")

    try:
        minha_funcao()
    except NameError:
        print("Erro: A função 'minha_funcao' não está definida no escopo global.")
    ```

    - tenta-se chamar uma função que foi corretamente definida, garantindo que não ocorra o `NameError`;
    - caso a função não esteja definida no escopo global, o erro seria capturado;

---

## cuidados

> [!CAUTION]
> Quando se usa os blocos `try` e `except` é importante mencionar que a captura de erros **`deve ser sempre`** pontual. Não se coloca blocos de códigos desnecessários dentro da cláusula `try`, senão outros erros não previstos podem acontecer.

Por exemplo :

```python
try:
    # todo o código está dentro do bloco try
    nova_lista = list(range(10))
    valor = nova_lista[0]
    resultado = valor * "2"
    resultado += 1
    print(f'{resultado = }')
except TypeError:
    print("Erro: Não é possível multiplicar um inteiro por uma string.")
```

O código acima vai gerar um erro, mas praticamente todo o código está dentro do bloc `try`. Isso não é uma boa prática. Pode tornar difícil saber exatamente o que está levantando o erro.

O ideal é isolar dentro do bloco `try` apenas o código passível do respectivo erro.

```python
nova_lista = list(range(10))
valor = nova_lista[0]

try:
    # isola apenas o trecho de código passível de erro
    resultado = valor * "2"
except TypeError:
    print("Erro: Não é possível multiplicar um inteiro por uma string.")

resultado += 1
print(f'{resultado = }')
```

## exercícios

<details>
<summary>Lista de Exercícios</summary>

1. **Exercícios ZeroDivisionError**
    1. Crie um programa que peça ao usuário dois números e divida o primeiro pelo segundo. Trate o **`ZeroDivisionError`** caso o segundo número seja zero.
    1. Escreva uma função que receba dois números como argumentos e retorne a divisão do primeiro pelo segundo. Trate o erro quando o divisor for zero.
    1. Simule uma calculadora que realize as operações básicas (adição, subtração, multiplicação e divisão). Garanta que divisões por zero sejam tratadas.
    1. Crie um programa que divida uma lista de números por um valor fornecido pelo usuário. Trate divisões por zero.
    1. Crie uma função recursiva que calcule a divisão sucessiva de uma lista de números por um divisor constante. Trate o erro de divisão por zero.
    1. Implemente um código que execute uma divisão baseada na entrada do usuário, convertendo a entrada em números e tratando **`ZeroDivisionError`** e **`ValueError`** simultaneamente.
    1. Escreva uma função que simule a divisão em operações bancárias. Ao realizar uma divisão por zero, exiba uma mensagem amigável.
    1. Modifique um código que realiza cálculos matemáticos complexos para verificar sempre se a divisão por zero pode ocorrer e trate o erro.
    1. Faça um programa que divida o total de vendas mensais por um número de meses. Verifique a possibilidade de divisão por zero no caso de meses iguais a zero.
    1. Crie uma função que calcule a média de números em uma lista, onde o denominador pode ser zero (caso a lista esteja vazia). Trate a divisão por zero.
1. **Exercícios ValueError**
    1. Crie um programa que peça ao usuário para inserir um número inteiro e trate o **`ValueError`** caso o usuário insira um valor não numérico.
    1. Implemente uma função que converta uma string para um número. Trate o erro se a string não puder ser convertida.
    1. Faça um programa que leia uma lista de números fornecida pelo usuário e trate **`ValueError`** para entradas inválidas (não numéricas).
    1. Escreva uma função que some todos os elementos de uma lista de strings que representam números. Trate possíveis erros de conversão.
    1. Crie um programa que solicite ao usuário uma data (dia, mês, ano) e trate **`ValueError`** caso a data seja inválida.
    1. Escreva um código que converta entradas do usuário em números inteiros e trate **`ValueError`** caso a entrada não seja válida.
    1. Crie um programa que leia um valor de temperatura e faça a conversão entre diferentes escalas (Celsius, Fahrenheit, Kelvin). Trate **`ValueError`** para entradas inválidas.
    1. Faça um programa que solicite ao usuário que insira valores numéricos em um formato específico (ex: `3.14`) e trate **`ValueError`** para valores inválidos.
    1. Implemente uma função que receba uma lista de strings e converta todas elas em números inteiros, tratando **`ValueError`** caso ocorra um erro.
    1. Faça um programa que peça ao usuário para inserir um número de telefone. Trate **`ValueError`** caso o número inserido seja inválido (contendo letras, por exemplo).
1. **Exercícios TypeError**
    1. Escreva uma função que some dois números e trate o **`TypeError`** caso um dos argumentos não seja um número.
    1. Crie uma função que multiplique dois números fornecidos como entrada. Trate o **`TypeError`** se um dos argumentos for uma string.
    1. Implemente uma função que concatene duas strings. Trate o **`TypeError`** se os argumentos não forem strings.
    1. Faça um programa que some os elementos de uma lista. Trate o **`TypeError`** caso a lista contenha elementos não numéricos.
    1. Crie uma função que execute operações aritméticas em uma lista. Trate o **`TypeError`** caso algum elemento não seja do tipo esperado.
    1. Implemente um programa que calcule a soma de uma lista de números e trate o **`TypeError`** se qualquer item da lista não for um número.
    1. Escreva um programa que receba uma lista e uma função como entrada e aplique a função a todos os elementos da lista. Trate o **`TypeError`** se os tipos forem incompatíveis.
    1. Crie uma função que execute uma divisão entre dois números, tratando o **`TypeError`** se um dos argumentos for uma string.
    1. Escreva um programa que peça ao usuário para fornecer duas entradas e concatene-as. Trate o **`TypeError`** se as entradas não forem strings.
    1. Faça um programa que peça ao usuário dois números e retorne a soma deles. Trate o **`TypeError`** se o usuário fornecer strings em vez de números.
1. **Exercícios IndexError**
    1. Crie um programa que solicite ao usuário para inserir um índice e retorne o elemento correspondente de uma lista. Trate **`IndexError`** caso o índice esteja fora do intervalo da lista.
    1. Implemente uma função que acesse o último elemento de uma lista sem usar índices negativos. Trate **`IndexError`** caso a lista esteja vazia.
    1. Faça um programa que percorra uma lista e tente acessar elementos com índices fora do intervalo. Trate **`IndexError`** adequadamente.
    1. Crie uma função que divida os elementos de uma lista por seus índices. Trate **`IndexError`** caso o índice não exista na lista.
    1. Escreva um programa que peça ao usuário para acessar um índice de uma string. Trate **`IndexError`** para índices inválidos.
    1. Crie um programa que tente acessar o primeiro e o último elemento de uma lista. Trate **`IndexError`** caso a lista esteja vazia.
    1. Faça um programa que peça ao usuário para inserir uma lista de elementos e um índice. Trate **`IndexError`** se o índice fornecido estiver fora dos limites.
    1. Escreva um código que percorra uma lista em um loop e, em cada iteração, tente acessar um índice além do tamanho da lista. Trate **`IndexError`**.
    1. Implemente um programa que modifique elementos de uma lista de acordo com o índice fornecido. Trate **`IndexError`** para índices inválidos.
    1. Crie um código que percorra uma lista de listas e tente acessar índices dentro das sublistas. Trate **`IndexError`** se o índice não existir em alguma sublista.
1. **Exercícios KeyError**
    1. Crie um dicionário simples e peça ao usuário para acessar um valor pela chave. Trate o **`KeyError`** caso a chave não exista.
    1. Faça um programa que use um dicionário para armazenar informações de alunos (nome, idade) e trate **`KeyError`** ao tentar acessar uma chave inexistente.
    1. Escreva um programa que atualize o valor de uma chave em um dicionário. Trate **`KeyError`** caso a chave não exista.
    1. Implemente uma função que receba um dicionário e uma lista de chaves. Para cada chave que não existir no dicionário, trate o **`KeyError`**.
    1. Crie um dicionário de produtos e preços. Peça ao usuário para inserir um nome de produto e exiba o preço. Trate **`KeyError`** se o produto não estiver no dicionário.
    1. Escreva uma função que busque informações de contato (nome, telefone) em um dicionário. Trate **`KeyError`** caso a chave inserida pelo usuário não esteja no dicionário.
    1. Faça um programa que permita que o usuário adicione e remova itens de um dicionário. Trate **`KeyError`** ao tentar remover uma chave inexistente.
    1. Crie uma função que percorra um dicionário de livros e retorne o preço de um livro específico. Trate **`KeyError`** se o livro não estiver no dicionário.
    1. Implemente um código que percorra um dicionário de alunos e verifique se determinadas chaves (nomes de alunos) existem. Trate **`KeyError`** adequadamente.
    1. Crie um programa que use um dicionário para armazenar notas de alunos. Peça ao usuário para inserir o nome de um aluno e exiba sua nota. Trate **`KeyError`** para alunos inexistentes.
1. **Exercícios ImportError**
    1. Escreva um programa que tente importar um módulo inexistente e trate o **`ImportError`**.
    1. Faça um programa que importe um módulo e execute uma função. Trate **`ImportError`** caso o módulo não exista.
    1. Crie um código que use `from` para importar uma função específica de um módulo. Trate **`ImportError`** caso a função não exista.
    1. Faça um programa que importe múltiplos módulos e trate **`ImportError`** para qualquer um que falhe.
    1. Implemente uma função que tente importar uma biblioteca externa e trate **`ImportError`** caso ela não esteja instalada.
    1. Crie um programa que importe um módulo, execute uma função e trate **`ImportError`** caso o módulo ou a função não existam.
    1. Escreva um código que tente importar uma biblioteca de visualização de dados (como `matplotlib`). Trate **`ImportError`** caso ela não esteja instalada.
    1. Faça um programa que importe um módulo baseado na entrada do usuário. Trate **`ImportError`** se o módulo não estiver disponível.
    1. Escreva um código que tente importar uma função matemática de um módulo e trate **`ImportError`** caso o módulo ou função não existam.
    1. Crie um programa que verifique a disponibilidade de um módulo e exiba uma mensagem amigável se houver um **`ImportError`**.
1. **Exercícios FileNotFoundError**
    1. Faça um programa que tente abrir um arquivo inexistente para leitura e trate o **`FileNotFoundError`**.
    1. Implemente uma função que verifique se um arquivo existe antes de abri-lo. Trate **`FileNotFoundError`** se o arquivo não for encontrado.
    1. Escreva um código que peça ao usuário o nome de um arquivo para abrir. Trate **`FileNotFoundError`** se o arquivo não existir.
    1. Crie uma função que leia o conteúdo de um arquivo fornecido pelo usuário. Trate **`FileNotFoundError`** caso o arquivo não esteja no caminho correto.
    1. Faça um programa que tente abrir um arquivo de configuração e trate **`FileNotFoundError`** se o arquivo não existir.
    1. Escreva um código que tente abrir múltiplos arquivos e trate **`FileNotFoundError`** para qualquer arquivo que não possa ser encontrado.
    1. Crie uma função que copie o conteúdo de um arquivo para outro. Trate **`FileNotFoundError`** se o arquivo de origem não existir.
    1. Implemente um programa que tente abrir um arquivo em um caminho fornecido pelo usuário e trate **`FileNotFoundError`** se o caminho estiver incorreto.
    1. Faça um programa que tente abrir um arquivo de log. Trate **`FileNotFoundError`** caso o arquivo de log não tenha sido criado.
    1. Escreva um código que percorra uma lista de arquivos e tente abri-los um por um, tratando **`FileNotFoundError`** para qualquer arquivo inexistente.
1. **Exercícios NameError**
    1. Escreva um código que tente imprimir uma variável não definida e trate o **`NameError`**.
    1. Crie um programa que peça ao usuário para definir uma variável e depois tente usá-la. Trate **`NameError`** se a variável não for definida.
    1. Escreva uma função que utilize uma variável global que não foi definida. Trate **`NameError`**.
    1. Faça um programa que tente usar uma função que não foi definida e trate **`NameError`**.
    1. Implemente um código que peça ao usuário para inserir uma variável e tente acessá-la. Trate **`NameError`** se a variável não estiver no escopo.
    1. Crie um programa que tente acessar uma variável dentro de uma função e trate **`NameError`** se a variável não estiver definida dentro do escopo da função.
    1. Escreva um código que defina uma variável condicionalmente e tente usá-la depois. Trate **`NameError`** caso ela não tenha sido definida.
    1. Faça um programa que simule uma calculadora. Trate **`NameError`** se o usuário tentar usar uma função não definida.
    1. Implemente um código que tente acessar um dicionário com uma variável não definida. Trate **`NameError`** se a variável não estiver no escopo.
    1. Crie uma função que use uma variável definida fora de seu escopo e trate **`NameError`** caso ela não exista.

</details>

## exceções múltiplas

Exceções múltiplas em Python ocorrem quando se deseja capturar e tratar diferentes tipos de erros no mesmo bloco `try-except`. Isso permite que o código lide com uma variedade de possíveis problemas de forma organizada e clara, sem precisar de um bloco `try-except` separado para cada tipo de exceção. Esse conceito é útil porque, muitas vezes, ao escrever um programa, diferentes tipos de erros podem ocorrer em uma mesma seção de código.

### por que usar exceções múltiplas?

1. **manter o código organizado** : em vez de criar vários blocos `try-except` para diferentes tipos de erros, pode-se lidar com vários erros de forma mais concisa;

1. **tratar diferentes cenários de falhas** : quando diferentes tipos de erros podem ocorrer, é importante tratá-los de maneira apropriada; por exemplo, um erro de valor inválido deve ser tratado de maneira diferente de um erro de divisão por zero;

1. **facilitar a depuração** : ao usar exceções múltiplas, pode-se capturar e tratar diferentes exceções com mensagens específicas, ajudando a identificar rapidamente o que deu errado;

### quando usar exceções múltiplas?

1. **quando diferentes tipos de erros podem ocorrer no mesmo bloco de código** : por exemplo, ao fazer operações matemáticas e trabalhar com conversão de dados ao mesmo tempo, é possível que ocorram tanto **`ZeroDivisionError`** quanto **`ValueError`**;

1. **quando os erros precisam de tratamentos diferentes** : se diferentes tipos de erros precisam ser tratados de forma distinta, é útil capturá-los separadamente em um bloco `except`;

1. **ao manipular código que lida com diferentes fontes de entrada** : se o programa lida com vários tipos de entrada, como arquivos, entradas de usuário e operações de rede, diferentes exceções podem ocorrer, e é bom capturá-las corretamente;

### quando não usar exceções múltiplas?

1. **quando apenas um tipo de erro é esperado** : se há um único erro que pode ser previsto, usar exceções múltiplas pode complicar o código desnecessariamente;

1. **quando o código fica confuso** : o uso excessivo de exceções múltiplas em um bloco de código muito longo pode tornar o código difícil de ler; nesse caso, seria melhor dividir o código em funções menores ou lidar com exceções separadamente;

1. **capturar exceções genéricas sem necessidade** : evite capturar exceções amplas como **`Exception`** sem um motivo claro, pois isso pode ocultar erros que deveriam ser tratados de forma mais específica;

### como usar exceções múltiplas?

Há duas formas principais de capturar exceções múltiplas em Python:

1. **listando exceções em uma única linha** : para capturar diferentes tipos de exceções com o mesmo bloco de tratamento, pode-se listá-las entre parênteses no bloco `except`.

    ```python
    try:
        x = int(input("Digite um número: "))
        resultado = 10 / x
    except (ValueError, ZeroDivisionError) as e:
        print(f"Ocorreu um erro: {e}")
    ```

    - o programa tenta converter a entrada do usuário em um número inteiro e depois realiza uma divisão;
    - se o usuário inserir algo que não seja um número (por exemplo, uma string), ocorrerá um **`ValueError`**;
    - se o usuário inserir `0`, ocorrerá um **`ZeroDivisionError`**;
    - ambos os erros são capturados e tratados no mesmo bloco `except`, com uma mensagem genérica exibida para o usuário;

1. **tratamento específico para cada exceção** : se quiser tratar diferentes exceções de maneiras distintas, pode criar vários blocos `except`.

    ```python
    try:
        x = int(input("Digite um número: "))
        resultado = 10 / x
    except ValueError:
        print("Você precisa digitar um número válido!")
    except ZeroDivisionError:
        print("Divisão por zero não é permitida!")
    ```

    - aqui, cada tipo de erro tem uma mensagem de erro específica para ajudar o usuário a entender melhor o que deu errado;
    - o **`ValueError`** é tratado separadamente do **`ZeroDivisionError`**, permitindo um feedback mais claro;

### como não usar exceções múltiplas?

1. **capturar exceções genéricas sem necessidade** : usar um bloco `except Exception` pode capturar todos os erros, mas isso pode ser perigoso, pois pode acabar ignorando erros importantes; sempre que possível, seja específico com as exceções que captura.

    ```python
    try:
        x = int(input("Digite um número: "))
        resultado = 10 / x
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    ```

    **por que evitar?** : capturar todas as exceções dessa forma impede que se trate adequadamente problemas específicos, além de dificultar a depuração, pois todas as exceções são tratadas da mesma forma;

1. **uso excessivo de exceções múltiplas** : exagerar no uso de exceções pode tornar o código confuso; em vez de tentar capturar muitos erros de uma só vez, é melhor dividir o código em funções menores e capturar exceções em contextos mais específicos.

### exemplo mais complexo de uso de exceções múltiplas

Aqui está um exemplo mais avançado que mostra como diferentes tipos de erros podem ser capturados e tratados de maneira apropriada.

```python
def processar_dados():
    nome_arquivo = input("Digite o nome do arquivo: ")

    try:
        with open(nome_arquivo, "r") as arquivo:
            conteudo = arquivo.read()

        numero = int(input("Digite um número: "))
        resultado = 100 / numero
        print(f"O resultado é {resultado}")

    except FileNotFoundError:
        print("O arquivo especificado não foi encontrado.")

    except ValueError:
        print("Você precisa digitar um número válido!")

    except ZeroDivisionError:
        print("Divisão por zero não é permitida!")

    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

processar_dados()
```

**explicação** :
- o programa tenta abrir um arquivo, ler seu conteúdo e depois realizar uma divisão;
- se o arquivo não existir, **`FileNotFoundError`** será capturado;
- se o usuário inserir um valor que não possa ser convertido em um número inteiro, **`ValueError`** será tratado;
- se o número inserido for zero, **`ZeroDivisionError`** será capturado;
- o bloco genérico `except Exception` captura qualquer outro erro que possa ocorrer, mas isso é usado apenas para garantir que nenhum erro seja ignorado;

---

## exercícios exceções múltiplas

<details>
<summary>Lista de Exercícios</summary>

1. **ZeroDivisionError e ValueError** : Crie um programa que peça ao usuário dois números e realize a divisão do primeiro pelo segundo. Trate a entrada inválida de um número (como uma string ou outro valor não numérico) e o caso de divisão por zero.
1. **TypeError e ZeroDivisionError** : Escreva uma função que receba dois argumentos e retorne a divisão do primeiro pelo segundo. Trate o erro se um dos argumentos não for um número (como uma string) e se o segundo número for zero.
1. **IndexError e ValueError** : Crie um programa que peça ao usuário para inserir um índice e depois retorne o elemento correspondente de uma lista pré-definida. Trate o caso de o índice estar fora do intervalo da lista e o caso de o usuário inserir um valor não numérico.
1. **KeyError e NameError** : Faça um programa que use um dicionário para armazenar os nomes e idades de pessoas. O programa deve pedir ao usuário um nome para procurar a idade correspondente no dicionário. Trate o erro de tentar acessar uma chave inexistente e o erro de tentar usar uma variável não definida.
1. **ImportError e NameError** : Crie um código que tente importar um módulo inexistente (ex: `parangaricutirimirruaro`) e depois use uma função de um módulo inexistente. Trate tanto o erro de importação quanto o erro de nome de função.
1. **FileNotFoundError e IOError** : Escreva um programa que peça ao usuário o nome de um arquivo para ler. Tente abrir o arquivo e ler seu conteúdo. Trate o erro caso o arquivo não exista e qualquer outro erro de leitura/escrita que possa ocorrer.
1. **ZeroDivisionError e KeyError** : Crie um programa que solicite dois números para realizar uma divisão. Caso o usuário insira `0` como o divisor, trate o erro de divisão por zero. Depois, tente acessar o resultado da divisão armazenado em um dicionário e trate o erro de chave inexistente.
1. **ValueError, IndexError e ZeroDivisionError** : Escreva um programa que leia uma lista de números fornecida pelo usuário, peça um índice e tente dividir o número do índice por outro número inserido pelo usuário. Trate entradas inválidas, divisões por zero e índices fora do intervalo da lista.
1. **TypeError, NameError e KeyError** : Crie uma função que receba dois números e retorne sua soma. Trate o erro caso um dos argumentos não seja um número e o erro de tentar usar uma variável não definida para armazenar o resultado. Depois, tente acessar o resultado em um dicionário e trate o erro de chave inexistente.
1. **ValueError e FileNotFoundError** : Faça um programa que peça ao usuário para inserir um número e depois o nome de um arquivo para armazenar esse número. Trate o erro se o valor inserido não for um número e o erro caso o arquivo não exista ao tentar acessá-lo.
1. **KeyError e IndexError** : Implemente um dicionário com listas de números como valores. Peça ao usuário para inserir uma chave e um índice. Tente acessar o valor correspondente e o índice dentro da lista associada à chave. Trate o erro de chave inexistente e índice fora dos limites da lista.
1. **ImportError e TypeError** : Escreva um código que tente importar um módulo que não está instalado e depois tente executar uma função que espera uma string, mas receba um número como argumento. Trate tanto o erro de importação quanto o erro de tipo.
1. **ZeroDivisionError, ValueError e FileNotFoundError** : Faça um programa que peça ao usuário para inserir dois números e depois divida o primeiro pelo segundo. Em seguida, tente gravar o resultado em um arquivo cujo nome é inserido pelo usuário. Trate os erros de divisão por zero, valor inválido e arquivo não encontrado.
1. **ValueError, NameError e TypeError** : Crie uma função que some dois números. Peça ao usuário para inserir os números e trate o erro de entrada inválida. Depois, trate o erro de usar uma variável não definida e o erro de tentar somar valores de tipos diferentes.
1. **IndexError, TypeError e KeyError** : Escreva um programa que percorra uma lista e um dicionário ao mesmo tempo. Tente acessar um índice inválido na lista e uma chave inexistente no dicionário, tratando ambos os erros. Além disso, trate o erro de tentar realizar operações com tipos incompatíveis.
1. **FileNotFoundError e ZeroDivisionError** : Crie um código que tente abrir um arquivo de texto e ler seu conteúdo. Depois, tente dividir um número lido do arquivo por outro número inserido pelo usuário. Trate os erros de arquivo não encontrado e divisão por zero.
1. **ImportError e NameError** : Faça um programa que tente importar uma biblioteca externa não instalada. Em seguida, tente usar uma variável que não foi definida. Trate os erros de importação e nome de variável indefinida.
1. **KeyError, IndexError e ValueError** : Escreva um programa que trabalhe com um dicionário de listas. O programa deve pedir ao usuário para inserir uma chave, um índice e um número. Trate o erro caso a chave ou o índice não existam, além de tratar entradas inválidas de números.
1. **FileNotFoundError, ValueError e IOError** : Faça um programa que peça ao usuário para inserir o nome de um arquivo para abrir, um número para ler do arquivo e trate os erros de arquivo inexistente, número inválido e outros problemas de leitura/escrita.
1. **NameError, ZeroDivisionError e KeyError** : Implemente um programa que calcule a média de valores armazenados em um dicionário. Trate os erros de usar uma variável não definida, tentar dividir pela quantidade zero de elementos e acessar uma chave inexistente no dicionário.

</details>

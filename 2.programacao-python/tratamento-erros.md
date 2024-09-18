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
1. [`except` genérico](#except-genérico)
1. [exercícios `except` genérico](#exercícios-except-genérico)
1. [comandos `else` e `finally`](#comandos-else-e-finally)
1. [exercícios `else` e `finally`](#exercícios-else-e-finally)
1. [capturando mensagens de erro](#capturando-mensagens-de-erro)
1. [exercícios mensagens de erro](#exercícios-mensagens-de-erro)

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

## `except` genérico

Em Python, o bloco `except` genérico captura qualquer tipo de exceção que ocorra dentro de um bloco `try`. Embora o uso de exceções genéricas possa parecer uma maneira conveniente de evitar que o programa falhe inesperadamente, essa prática pode ser prejudicial e levar a diversos problemas de depuração e manutenção de código.

### como funciona

O `except` genérico é um bloco de tratamento de exceções que captura **qualquer** exceção que ocorra no bloco `try`, sem especificar o tipo de erro :

```python
try:
    x = 10 / 0
except:
    print("Ocorreu um erro!")
```

Neste exemplo, qualquer exceção dentro do bloco `try` será capturada e tratada pelo bloco `except`, sem diferenciar o tipo de erro. Isso inclui exceções que você talvez não deseje capturar, como erros de sintaxe ou interrupções do sistema.

### Por que não se deve usar o `except` genérico

1. **Oculta o tipo de exceção real**: Ao capturar exceções de forma genérica, se perde a capacidade de identificar o que realmente causou o erro. Isso torna a depuração muito mais difícil, já que não há informações detalhadas sobre o tipo de exceção que ocorreu.

1. **Captura exceções que não quer capturar**: Algumas exceções, como **`KeyboardInterrupt`** (interrupção do programa pelo usuário) ou **`SystemExit`** (sinalizando o encerramento do programa), não deveriam ser capturadas e tratadas da mesma forma que outras exceções comuns. Usar `except` genérico pode capturar essas exceções e impedir o comportamento natural do sistema.

1. **Difícil de manter**: O uso de exceções genéricas torna o código mais difícil de manter, já que o tratamento de erros não está claro. Outros desenvolvedores (ou mesmo você no futuro) podem ter dificuldade para entender quais tipos de erros o código está preparado para tratar.

1. **Pode mascarar erros graves**: Capturar erros inesperados de forma genérica pode mascarar falhas sérias no programa. Por exemplo, um erro de lógica no código pode ser capturado silenciosamente, sem que o programador perceba que há um problema maior que precisa ser corrigido.

### exemplos de como o uso do `except` genérico pode ser prejudicial

#### exemplo 1: ocultando exceções inesperadas

Aqui, um erro de sintaxe no código será capturado pelo `except` genérico, mas o programador não perceberá o erro subjacente :

```python
try:
    resultado = 10 / 0
except:
    print("Algo deu errado!")
```

**Problema**:
- O erro **`ZeroDivisionError`** é silenciosamente capturado, mas o programador não tem ideia do que realmente deu errado.
- O bloco `except` simplesmente imprime uma mensagem genérica, sem fornecer informações úteis para resolver o problema.

**Consequência**:
- Isso dificulta a identificação do erro real. O programador pode pensar que o problema é menor, quando, na verdade, pode haver uma falha grave no código.

#### **exemplo 2: captura indesejada de exceções críticas**

No exemplo abaixo, o `except` genérico captura um **`KeyboardInterrupt`**, impedindo o usuário de interromper o programa com `Ctrl+C`:

```python
try:
    while True:
        pass  # Loop infinito
except:
    print("Ocorreu um erro!")
```

**Problema**:
- Se o usuário tentar interromper o programa com `Ctrl+C`, a exceção **`KeyboardInterrupt`** será capturada e tratada como um "erro" comum.
- Isso impede que o usuário encerre o programa como esperado.

**Consequência**:
- Capturar exceções como **`KeyboardInterrupt`** pode impedir o funcionamento correto do sistema e fazer com que o programa não responda adequadamente a interrupções externas.

#### **exemplo 3: mascarando erros graves**

Neste exemplo, um erro crítico que não deveria ser capturado é tratado de forma genérica:

```python
def abrir_arquivo():
    try:
        with open("arquivo_inexistente.txt", "r") as f:
            conteudo = f.read()
    except:
        print("Erro ao abrir o arquivo")

abrir_arquivo()
```

**Problema**:
- O arquivo não existe, então um **`FileNotFoundError`** ocorre. No entanto, a exceção é capturada de forma genérica.
- Isso mascara o erro real, e a única coisa que o programador vê é a mensagem "Erro ao abrir o arquivo".

**Consequência**:
- O código não fornece informações suficientes sobre o erro. Se o problema for mais grave do que a falta do arquivo (por exemplo, permissões inadequadas no sistema), ele não será diagnosticado corretamente.

### boas práticas

#### quando evitar

1. **Na maioria dos casos**: Em praticamente todas as situações, é melhor ser específico sobre quais exceções você deseja capturar e tratar. Isso torna o código mais legível e ajuda na depuração de erros.

    ```python
    try:
        resultado = 10 / 0
    except ZeroDivisionError:
        print("Erro: Divisão por zero.")
    ```

1. **Quando há exceções críticas**: Exceções como **`SystemExit`**, **`KeyboardInterrupt`**, e **`MemoryError`** geralmente não devem ser capturadas, pois interferem no comportamento normal do sistema. Capturar essas exceções de forma genérica pode resultar em consequências indesejadas.

#### quando usar

1. **Em situações de fallback seguro**: Se está implementando um sistema que precisa continuar funcionando a todo custo, como um servidor que precisa estar sempre disponível, capturar exceções genéricas pode ser aceitável, desde que seja acompanhado de um log detalhado que ajude na depuração posterior.

    ```python
    try:
        resultado = 10 / 0
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    ```

    Aqui, está sendo capturado todas as exceções, mas ainda fornecemos informações úteis sobre o erro, imprimindo a mensagem do erro original. Embora seja genérico, isso permite alguma transparência no que deu errado.

2. **Em scripts simples e descartáveis**: Se está criando um script rápido ou algo temporário, o uso de `except` genérico pode ser aceitável, já que o objetivo é mais a funcionalidade do que a robustez a longo prazo.

### consequências

1. **Dificuldade na manutenção**: O código se torna difícil de manter, já que os erros reais são mascarados. Outros programadores podem ter dificuldade em identificar e corrigir problemas.

2. **Falha na depuração**: A depuração se torna complexa, pois não há informações claras sobre o que exatamente deu errado. Em vez de corrigir o problema, o programador pode acabar "silenciando" o erro sem realmente resolvê-lo.

3. **Perda de controle sobre exceções críticas**: O sistema pode se comportar de maneira imprevisível ao capturar exceções que não deveriam ser capturadas, como interrupções de sistema ou problemas de memória.

## exercícios `except` genérico

<details>
<summary>Lista de Exercícios</summary>

1. **Ocultando erros de programação** : O código tenta converter uma entrada do usuário para um número inteiro e realizar uma divisão. Use um `except` genérico para capturar a exceção e veja como ele oculta erros inesperados.

    ```python
    def calcular_divisao():
        try:
            numero = int(input("Digite um número: "))
            resultado = 10 / numero
        except:
            print("Erro ocorreu!")

    calcular_divisao()
    ```

    - Por que o uso de `except` genérico pode ser prejudicial neste código? Quais exceções poderiam ser ocultas?

1. **Ocultando erros de digitação** : No código abaixo, há um erro de digitação na variável `numer`, que deveria ser `numero`. O `except` genérico oculta o erro, o que pode tornar a depuração mais difícil.

    ```python
    def calcular():
        try:
            numer = 10
            resultado = 100 / numero  # Erro de digitação
        except:
            print("Ocorreu um erro.")

    calcular()
    ```

    - Qual é o problema com o `except` genérico aqui? O que aconteceria se você corrigisse o erro e especificasse as exceções?

1. **Ocultando exceções de arquivos** : O código tenta abrir um arquivo que não existe. O `except` genérico impede que o erro `FileNotFoundError` seja tratado adequadamente.

    ```python
    def abrir_arquivo():
        try:
            with open("arquivo_inexistente.txt", "r") as f:
                conteudo = f.read()
        except:
            print("Erro ao abrir o arquivo.")

    abrir_arquivo()
    ```

    - Qual exceção está sendo capturada? Por que seria melhor capturar `FileNotFoundError` especificamente em vez de usar um `except` genérico?

1. **Ignorando erros de tipo** : O código tenta somar dois valores, mas um deles não é numérico. O `except` genérico esconde o erro de tipo (`TypeError`).

    ```python
    def somar(a, b):
        try:
            return a + b
        except:
            print("Ocorreu um erro.")

    somar(10, "vinte")
    ```

    - Por que o uso de `except` genérico é problemático aqui? Como você trataria especificamente a exceção `TypeError`?

1. **Ignorando divisões por zero** : O código tenta realizar uma divisão por zero, mas o `except` genérico não informa ao usuário que o problema é uma divisão por zero.

    ```python
    def dividir():
        try:
            resultado = 10 / 0
        except:
            print("Algo deu errado.")

    dividir()
    ```

    - Qual exceção está sendo capturada aqui? Por que é importante informar ao usuário qual foi o erro?

1. **Capturando todas as exceções** : O código tenta abrir um arquivo, converter uma entrada para número e fazer uma divisão. O `except` genérico captura todos os erros possíveis, sem distinção.

    ```python
    def processo():
        try:
            with open("arquivo.txt", "r") as f:
                conteudo = f.read()
            numero = int(input("Digite um número: "))
            resultado = 10 / numero
        except:
            print("Ocorreu um erro durante o processo.")

    processo()
    ```

    - Por que o uso de `except` genérico em várias operações é prejudicial? Como você poderia melhorar o tratamento de exceções?

1. **Ocultando exceções de `KeyError`** : No código abaixo, o dicionário não contém a chave "nome", mas o `except` genérico não permite que o erro `KeyError` seja mostrado corretamente.

    ```python
    def acessar_dicionario():
        dados = {"idade": 30}
        try:
            print(dados["nome"])
        except:
            print("Erro ao acessar o dicionário.")

    acessar_dicionario()
    ```

    - O que o `except` genérico está ocultando? Como você poderia capturar e tratar especificamente o erro `KeyError`?

1. **Ignorando exceções de importação** : O código tenta importar um módulo inexistente, mas o `except` genérico esconde o erro de `ImportError`.

    ```python
    def importar_modulo():
        try:
            import modulo_inexistente
        except:
            print("Erro ao importar módulo.")

    importar_modulo()
    ```

    - Por que o uso de `except` genérico pode ser problemático em operações de importação? Como você capturaria especificamente o erro `ImportError`?

1. **Ocultando erros lógicos** : Aqui, o código tenta acessar um índice inválido de uma lista. O `except` genérico oculta o erro `IndexError`.

    ```python
    def acessar_lista():
        lista = [1, 2, 3]
        try:
            print(lista[5])
        except:
            print("Erro ao acessar lista.")

    acessar_lista()
    ```

    - Por que o `except` genérico está ocultando o erro? Como você poderia capturar a exceção `IndexError` de forma adequada?

1. **Ocultando exceções de variáveis não definidas** : O código tenta usar uma variável não definida. O `except` genérico oculta o erro `NameError`, que indica que a variável não foi declarada.

    ```python
    def usar_variavel():
        try:
            print(variavel_inexistente)
        except:
            print("Erro ao usar variável.")

    usar_variavel()
    ```

    - O que está sendo capturado pelo `except` genérico? Por que é importante capturar o erro `NameError` especificamente?

</details>

## comandos `else` e `finally`

O tratamento de exceções em Python oferece recursos poderosos, e além do uso básico de `try` e `except`, dois blocos opcionais complementam o tratamento de erros: **`else`** e **`finally`**. Ambos têm papéis distintos que aumentam a flexibilidade e robustez do código.

### `else`

O bloco `else` é executado **somente** se **nenhuma exceção** for levantada dentro do bloco `try`. Ele é opcional e permite que se execute um código que deve ocorrer somente quando o bloco `try` for bem-sucedido, sem erros.

A estrutura geral é a seguinte :

```python
try:
    # código que pode gerar uma exceção
except SomeException:
    # código para tratar a exceção
else:
    # código que será executado se não houver exceções
```

- **Exemplo do uso**

```python
try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
except ValueError:
    print("Erro: O valor inserido não é um número válido.")
except ZeroDivisionError:
    print("Erro: Divisão por zero.")
else:
    print(f"O resultado da divisão é: {resultado}")
```

- o bloco `try` tenta converter a entrada do usuário para um número inteiro e depois realiza uma divisão;
- se uma exceção **`ValueError`** ou **`ZeroDivisionError`** for levantada, o código no bloco `except` correspondente será executado;
- se **nenhuma exceção** ocorrer, o bloco `else` será executado, exibindo o resultado da divisão;

#### vantagens

1. **clareza de propósito** : colocar o código no bloco `else` ajuda a separar o que deve acontecer em caso de sucesso do que ocorre em caso de erro; isso melhora a legibilidade, tornando o código mais intuitivo;
1. **evita o uso excessivo de código no `try`** : o código no bloco `try` deve ser apenas o necessário para detectar e tratar erros; o `else` permite que o código de sucesso seja separado, reduzindo o risco de capturar exceções inadvertidamente;
1. **melhora a manutenção do código** : com o `else`, é mais fácil entender e gerenciar o fluxo de execução, o que facilita a manutenção e expansão do código;

#### desvantagens

1. **pouco utilizado em alguns casos** : nem sempre é necessário; se todo o código puder ser contido no bloco `try` sem perda de clareza, o `else` pode parecer redundante;
1. **pode ser confundido com o fluxo do `try`** : novos programadores podem não entender de imediato o porquê de separar o código de sucesso no `else`, o que pode levar a uma má interpretação;

### `finally`

O bloco `finally` é executado **sempre**, independentemente de uma exceção ter sido levantada ou não. Ele é usado para garantir que o código crítico seja executado, como fechar arquivos, liberar recursos ou encerrar conexões com banco de dados, mesmo se ocorrer um erro.

A estrutura geral é:

```python
try:
    # código que pode gerar uma exceção
except SomeException:
    # código para tratar a exceção
finally:
    # código que sempre será executado, com ou sem exceção
```

- **Exemplo do uso**

```python
try:
    arquivo = open('arquivo.txt', 'r')
    conteudo = arquivo.read()
except FileNotFoundError:
    print("Erro: O arquivo não foi encontrado.")
else:
    print(conteudo)
finally:
    arquivo.close()
    print("Arquivo fechado.")
```

- o bloco `try` tenta abrir um arquivo e lê seu conteúdo;
- se o arquivo não for encontrado, um **`FileNotFoundError`** é levantado e tratado no bloco `except`;
- se o arquivo for encontrado, o conteúdo é exibido no bloco `else`;
- o bloco `finally` é executado sempre, fechando o arquivo, independentemente de ter havido uma exceção ou não;

#### Vantagens

1. **garantia de execução** : o `finally` garante que o código será executado, mesmo que uma exceção ocorra; isso é útil para operações como:
    - fechar arquivos ou liberar recursos;
    - desconectar de um banco de dados ou de uma API;
    - limpeza de variáveis ou processos temporários;

1. **robustez no código** : ele aumenta a robustez, pois, não importa o que aconteça no bloco `try` ou `except`, o código no `finally` será executado;

1. **previne vazamento de recursos** : em programas que lidam com recursos limitados ou externos (como arquivos ou conexões de rede), o `finally` é essencial para garantir que esses recursos sejam corretamente fechados ou liberados;

#### desvantagens

1. **pode ocultar exceções** : se um erro ocorrer dentro do bloco `finally`, ele pode sobrescrever uma exceção levantada no bloco `try`, ocultando o erro original; isso dificulta a depuração.

    ```python
    try:
        resultado = 10 / 0
    except ZeroDivisionError:
        print("Erro de divisão por zero.")
    finally:
        raise ValueError("Erro dentro do finally.")
    ```

    - neste caso, o erro **`ValueError`** do `finally` substitui a exceção **`ZeroDivisionError`**, o que pode confundir na hora da depuração, pois o erro original é perdido;

1. **execução de código irrelevante** : se o bloco `finally` contiver código que não é crítico para a execução final (como mensagens desnecessárias), ele pode aumentar a complexidade sem benefícios reais;

### quando usar `else` e `finally`

#### `else`

- **quando o código após o `try` só deve ser executado se não houver exceções** : isso torna o fluxo de execução mais claro e separado do tratamento de exceções;
- **quando o código dentro do `try` deve ser mínimo**, limitando-se apenas ao que pode gerar exceções, enquanto o código de "sucesso" vai no `else`;

#### `finally`

- **quando for necessário liberar recursos ou fazer "limpeza"**, como fechar arquivos, desconectar de uma rede ou liberar memória, independentemente de erros;
- **quando for fundamental garantir a execução de um bloco de código específico**, como garantir que um log seja escrito ou um backup seja criado, mesmo em caso de erro;

### quando evitar `else` e `finally`

- **evite `else` quando o código no bloco `try` for simples e fácil de ler** : se todo o código puder ser executado no `try` sem perda de clareza, o `else` pode não ser necessário;

- **evite `finally` se não houver recursos para liberar ou ações críticas a serem executadas** : se não há ações que devam ser garantidas após o bloco `try`, o uso do `finally` pode ser desnecessário e pode adicionar complexidade desnecessária ao código;

## exercícios `else` e `finally`

<details>
<summary>Lista de Exercícios</summary>

1. **Operação aritmética** : Escreva um código que peça ao usuário dois números e os divida. Utilize um bloco `try` para capturar erros de divisão por zero e tipos inválidos. No bloco `else`, exiba o resultado. No bloco `finally`, exiba uma mensagem indicando que a operação foi concluída.
1. **Leitura de arquivo** : Tente abrir um arquivo para leitura. Se o arquivo não for encontrado, capture a exceção com um `except`. Utilize o bloco `else` para ler o conteúdo e imprimir na tela. No `finally`, feche o arquivo, se ele tiver sido aberto.
1. **Verificação de índice** : Peça ao usuário uma lista e um índice. No `try`, tente acessar o elemento da lista usando o índice. Capture o erro de `IndexError`. No `else`, exiba o valor encontrado. No `finally`, exiba uma mensagem indicando o fim da operação.
1. **Conversão de tipos** : Peça ao usuário para digitar um número. No `try`, tente converter a entrada para `int`. Capture erros de conversão de tipos com `except`. No `else`, informe que a conversão foi bem-sucedida. No `finally`, imprima "Processo concluído".
1. **Remoção de item de dicionário** : Crie um dicionário com alguns elementos. No `try`, remova uma chave fornecida pelo usuário. Se a chave não existir, capture o erro `KeyError`. No `else`, exiba o dicionário atualizado. No `finally`, exiba uma mensagem indicando que a operação de remoção foi tentada.
1. **Escrita em arquivo** : Tente abrir um arquivo para escrita e adicionar algum conteúdo. Utilize `try` para capturar erros relacionados ao acesso ao arquivo. No `else`, informe que a escrita foi bem-sucedida. No `finally`, feche o arquivo.
1. **Execução de função matemática** : Peça ao usuário um número e tente calcular sua raiz quadrada usando `try`. Capture qualquer erro relacionado a valores negativos. No `else`, exiba o resultado da raiz quadrada. No `finally`, exiba uma mensagem final.
1. **Remoção de item de lista** : Peça ao usuário uma lista e um valor para remover. No `try`, tente remover o valor da lista. Capture erros caso o valor não esteja presente com `ValueError`. No `else`, exiba a lista atualizada. No `finally`, exiba uma mensagem indicando o fim da operação.
1. **Divisão com múltiplas exceções** : Escreva um código que tente dividir dois números inseridos pelo usuário. Capture erros de `ZeroDivisionError` e `TypeError`. No `else`, mostre o resultado da divisão. No `finally`, exiba uma mensagem de conclusão.
1. **Processamento de lista de inteiros** : Peça ao usuário uma lista de inteiros e tente somar os valores. Capture erros caso a lista contenha valores que não sejam inteiros. No `else`, exiba a soma. No `finally`, informe que o processamento foi concluído.
1. **Operação em dicionário** : Peça ao usuário para fornecer uma chave e um valor, e tente adicioná-los a um dicionário. Capture erros de tipo com `TypeError`. No `else`, exiba o dicionário atualizado. No `finally`, exiba uma mensagem indicando que a operação foi finalizada.
1. **Entrada de número positivo** : Solicite ao usuário um número positivo. No `try`, verifique se o número é maior que zero. Capture erros de entrada inválida. No `else`, mostre que a entrada foi válida. No `finally`, imprima "Fim do programa".
1. **Acesso a arquivos protegidos** : Tente abrir um arquivo protegido. Capture erros de permissão com `PermissionError`. No `else`, informe que o arquivo foi acessado corretamente. No `finally`, exiba uma mensagem indicando que a tentativa foi feita.
1. **Acesso a chaves em dicionários aninhados** : Peça ao usuário um dicionário aninhado e uma chave de primeiro nível para acessar. Capture erros de `KeyError` se a chave não existir. No `else`, exiba o valor da chave. No `finally`, exiba uma mensagem de fim.
1. **Verificação de múltiplos índices** : Peça ao usuário uma lista e múltiplos índices. Tente acessar os elementos de cada índice e capture `IndexError`. No `else`, mostre os valores acessados. No `finally`, exiba uma mensagem de conclusão.
1. **Cálculo de média** : Solicite uma lista de números do usuário. No `try`, tente calcular a média dos números. Capture erros de divisão por zero caso a lista esteja vazia. No `else`, exiba a média calculada. No `finally`, exiba uma mensagem final.
1. **Conversão de dados para float** : Peça ao usuário para fornecer uma lista de números (em string) e tente converter todos para `float`. Capture qualquer erro de `ValueError` ao tentar a conversão. No `else`, mostre a lista de floats. No `finally`, exiba uma mensagem de conclusão.
1. **Acesso a arquivos em um diretório** : Tente acessar um arquivo específico dentro de um diretório fornecido pelo usuário. Capture erros de `FileNotFoundError` caso o arquivo não exista. No `else`, exiba o conteúdo do arquivo. No `finally`, exiba uma mensagem indicando que a operação foi finalizada.

</details>

## capturando mensagens de erro

Capturar e exibir as mensagens de erro em Python é uma prática crucial para a depuração e manutenção de um código robusto. Com o tratamento de exceções, é possível acessar as mensagens de erro associadas às exceções geradas durante a execução do programa. Isso ajuda a identificar rapidamente a causa de um problema, melhorar a experiência do usuário e evitar falhas não tratadas.

### como funciona

Quando uma exceção é levantada (gerada) em Python, ela contém uma mensagem descritiva que indica o motivo do erro. Capturar essa mensagem permite entendê-la melhor e tomar decisões sobre como tratar o erro.

A captura da mensagem de erro geralmente é feita no bloco `except` ao manipular exceções, mas há formas mais detalhadas de capturar o rastreamento completo do erro e os detalhes sobre o contexto onde ele ocorreu.

#### captura básica de exceção com `as`

A forma mais simples de capturar a mensagem de erro é associando a exceção a uma variável usando o `as` dentro do bloco `except`. Essa variável conterá a mensagem de erro, que pode ser impressa ou registrada.

- **Exemplo: Captura básica com `ZeroDivisionError`**

```python
try:
    resultado = 10 / 0
except ZeroDivisionError as e:
    print(f"Erro: {e}")
```

- o bloco `try` tenta executar uma divisão por zero, o que gera uma exceção do tipo `ZeroDivisionError`;
- o bloco `except` captura essa exceção e a associa à variável `e`, que contém a mensagem de erro `"division by zero"`;
- a mensagem de erro é então impressa;

**Saída:**
```
Erro: division by zero
```

#### módulo `traceback`

O módulo `traceback` fornece informações detalhadas sobre o erro, incluindo o rastreamento da pilha (stack trace), que mostra a sequência de chamadas de função que levaram ao erro. Isso é especialmente útil para depurar grandes programas, pois ajuda a identificar onde, exatamente, o erro ocorreu.

- **Exemplo: Usando `traceback.print_exc()`**

```python
import traceback

try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Erro detectado:")
    traceback.print_exc()  # Exibe o rastreamento completo do erro
```

- o bloco `try` tenta realizar uma divisão por zero;
- `traceback.print_exc()` imprime o rastreamento completo da exceção, incluindo o local do código onde ocorreu o erro;

**Saída:**
```
Erro detectado:
Traceback (most recent call last):
  File "example.py", line 3, in <module>
    resultado = 10 / 0
ZeroDivisionError: division by zero
```

### acessando atributos específicos da exceção

Dependendo do tipo de exceção, pode-se acessar informações adicionais. Por exemplo, com exceções relacionadas a arquivos, como `FileNotFoundError`, pode-se acessar atributos como `filename` (nome do arquivo) e `strerror` (mensagem de erro).

- **Exemplo: `FileNotFoundError` com atributos adicionais**

```python
try:
    with open("arquivo_inexistente.txt", "r") as f:
        conteudo = f.read()
except FileNotFoundError as e:
    print(f"Erro: {e.strerror}")
    print(f"Arquivo não encontrado: {e.filename}")
```

- o bloco `try` tenta abrir um arquivo que não existe, o que gera uma exceção `FileNotFoundError`;
- a variável `e` contém informações detalhadas, como o nome do arquivo e a mensagem de erro;

**Saída:**
```
Erro: No such file or directory
Arquivo não encontrado: arquivo_inexistente.txt
```

### vantagens

- 1. **Facilita a depuração** : capturar e exibir mensagens de erro ajuda a entender o que está acontecendo no programa em tempo de execução; isso é crucial para identificar e corrigir bugs rapidamente;
- 1. **Permite mensagens de erro personalizadas** : pode-se capturar a mensagem de erro e, ao mesmo tempo, exibir uma mensagem personalizada que explique melhor o contexto do erro para o usuário ou para o desenvolvedor;

    Exemplo:
    ```python
    try:
        numero = int(input("Digite um número: "))
        resultado = 10 / numero
    except ValueError:
        print("Erro: O valor fornecido não é um número válido.")
    except ZeroDivisionError:
        print("Erro: Não é possível dividir por zero.")
    ```

- 1. **Melhora a experiência do usuário** : ao capturar mensagens de erro e tratá-las adequadamente, pode-se fornecer feedback amigável para o usuário, em vez de permitir que o programa quebre com uma exceção não tratada;

- 1. **Possibilita o uso de logs** : em sistemas maiores ou em ambientes de produção, é comum registrar as exceções em um arquivo de log para análise posterior; capturar a mensagem de erro permite gravá-la para monitoramento contínuo;

### desvantagens

- 1. **Pode esconder problemas graves** : capturar exceções sem o tratamento adequado ou sem re-exibi-las pode ocultar problemas maiores que deveriam parar o programa, dificultando a depuração;

- 2. **Pode aumentar a complexidade** : adicionar muitos blocos de captura de erro pode tornar o código mais difícil de ler e manter, especialmente se não for claro quais exceções estão sendo capturadas e por quê;

- 3. **Excessos no tratamento de erros** : se capturar mensagens de erro de maneira excessiva e tratar exceções que não necessariamente precisam ser tratadas, pode acabar mascarando problemas que deveriam ser abordados de outra forma, levando a comportamentos inesperados;

    Exemplo negativo:
    ```python
    try:
        resultado = 10 / 0
    except Exception as e:
        print("Erro desconhecido:", e)  # Captura genérica sem distinção
    ```

    - **Problema** : usar `except Exception` de maneira genérica pode capturar qualquer exceção, inclusive aquelas que não se espera, tornando o código mais difícil de depurar;

## exercícios mensagens de erro

<details>
<summary>Lista de Exercícios</summary>

1. **Exercício 1: ZeroDivisionError - Divisão Simples** : Peça ao usuário dois números e tente dividi-los. Capture o erro de divisão por zero e exiba a mensagem de erro.
1. **Exercício 2: ValueError - Conversão de String para Inteiro** : Peça ao usuário para inserir um número. Tente converter a entrada para `int`. Capture qualquer erro de `ValueError` e exiba a mensagem de erro.
1. **Exercício 3: TypeError - Soma de Tipos Diferentes** : Tente somar uma string e um número. Capture o erro de `TypeError` e exiba a mensagem de erro.
1. **Exercício 4: IndexError - Acessar Índice Inválido** : Crie uma lista com alguns elementos e peça ao usuário um índice. Tente acessar o elemento na posição fornecida. Capture o erro de `IndexError` e exiba a mensagem de erro.
1. **Exercício 5: KeyError - Acesso a Chave de Dicionário Inexistente** : Crie um dicionário com algumas chaves e peça ao usuário uma chave. Tente acessar o valor correspondente à chave fornecida. Capture o erro de `KeyError` e exiba a mensagem de erro.
1. **Exercício 6: ImportError - Importar Módulo Inexistente** : Tente importar um módulo que não existe. Capture o erro de `ImportError` e exiba a mensagem de erro.
1. **Exercício 7: FileNotFoundError - Abrir Arquivo Inexistente** : Tente abrir um arquivo que não existe no sistema. Capture o erro de `FileNotFoundError` e exiba a mensagem de erro.
1. **Exercício 8: NameError - Variável Não Definida** : Tente imprimir o valor de uma variável que não foi definida. Capture o erro de `NameError` e exiba a mensagem de erro.
1. **Exercício 9: ZeroDivisionError - Cálculo de Média** : Peça ao usuário uma lista de números e calcule a média. Capture qualquer erro de `ZeroDivisionError` se a lista estiver vazia e exiba a mensagem de erro.
1. **Exercício 10: ValueError - Entrada de Números** : Peça ao usuário para fornecer uma lista de números, mas digite uma string em vez de um número. Capture o erro de `ValueError` e exiba a mensagem de erro.
1. **Exercício 11: TypeError - Concatenar Tipos Diferentes** : Peça ao usuário um número e uma string. Tente concatená-los diretamente. Capture o erro de `TypeError` e exiba a mensagem de erro.
1. **Exercício 12: IndexError - Acesso em Lista Vazia** : Crie uma lista vazia e tente acessar o primeiro elemento. Capture o erro de `IndexError` e exiba a mensagem de erro.
1. **Exercício 13: KeyError - Remoção de Chave Inexistente** : Tente remover uma chave de um dicionário que não existe. Capture o erro de `KeyError` e exiba a mensagem de erro.
1. **Exercício 14: ImportError - Função Inexistente de Módulo** : Tente importar uma função específica de um módulo, mas use o nome errado da função. Capture o erro de `ImportError` e exiba a mensagem de erro.
1. **Exercício 15: FileNotFoundError - Leitura de Arquivo Inexistente** : Tente abrir e ler o conteúdo de um arquivo que não existe no diretório atual. Capture o erro de `FileNotFoundError` e exiba a mensagem de erro.
1. **Exercício 16: NameError - Função Não Definida** : Tente chamar uma função que não foi definida anteriormente. Capture o erro de `NameError` e exiba a mensagem de erro.
1. **Exercício 17: ZeroDivisionError - Função de Divisão** : Crie uma função que divide dois números. Peça ao usuário dois números e tente dividi-los. Capture o erro de `ZeroDivisionError` e exiba a mensagem de erro.
1. **Exercício 18: ValueError - Conversão de Lista de Strings para Inteiros** : Peça ao usuário uma lista de strings e tente converter todos os elementos para inteiros. Capture qualquer erro de `ValueError` e exiba a mensagem de erro.
1. **Exercício 19: TypeError - Multiplicação de Tipos Diferentes** : Tente multiplicar uma string por outro tipo não permitido (ex.: `None`). Capture o erro de `TypeError` e exiba a mensagem de erro.
1. **Exercício 20: IndexError - Listas Aninhadas** : Crie uma lista de listas e peça ao usuário para fornecer dois índices (um para a lista principal e outro para a lista interna). Tente acessar o elemento. Capture o erro de `IndexError` e exiba a mensagem de erro.

</details>

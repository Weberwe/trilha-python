# métodos das strings

As strings em Python são sequências imutáveis de caracteres que possuem vários métodos embutidos, os quais permitem realizar uma ampla variedade de operações.

1. `str.upper()` : o método `upper()` converte todos os caracteres alfabéticos de uma string para maiúsculas. Ele não afeta números, espaços em branco ou caracteres especiais.
    ```python
    # Exemplo básico
    texto = "hello world"
    print(texto.upper())  # saída : "HELLO WORLD"

    # Mistura de letras maiúsculas e minúsculas
    texto = "Python is Fun!"
    print(texto.upper())  # saída : "PYTHON IS FUN!"

    # String com números e caracteres especiais
    texto = "Python 3.12!"
    print(texto.upper())  # saída : "PYTHON 3.12!"
    ```

1. `str.lower()` : o método `lower()` converte todos os caracteres alfabéticos de uma string para minúsculas. Assim como `upper()`, ele não altera números, espaços em branco ou caracteres especiais.
    ```python
    # Exemplo básico
    texto = "HELLO WORLD"
    print(texto.lower())  # saída : "hello world"

    # Mistura de letras maiúsculas e minúsculas
    texto = "Python Is Fun!"
    print(texto.lower())  # saída : "python is fun!"

    # String com números e caracteres especiais
    texto = "Python 3.12!"
    print(texto.lower())  # saída : "python 3.12!"
    ```

1. `str.capitalize()` : o método `capitalize()` converte o primeiro caractere da string para maiúscula e todos os outros caracteres alfabéticos para minúscula. Se o primeiro caractere já for maiúsculo ou não for uma letra, ele permanece inalterado.
    ```python
    # Exemplo básico
    texto = "hello world"
    print(texto.capitalize())  # saída : "Hello world"

    # Primeira letra maiúscula, mas as demais já estão maiúsculas
    texto = "HELLO WORLD"
    print(texto.capitalize())  # saída : "Hello world"

    # String começando com número
    texto = "123 python"
    print(texto.capitalize())  # saída : "123 python"
    ```

1. `str.title()` : o método `title()` converte o primeiro caractere de cada palavra na string para maiúscula e o restante para minúscula. Este método considera qualquer caractere não alfabético (como espaços ou pontuação) como delimitador de palavras.
    ```python
    # Exemplo básico
    texto = "hello world"
    print(texto.title())  # saída : "Hello World"

    # Mistura de maiúsculas e minúsculas
    texto = "python is FUN!"
    print(texto.title())  # saída : "Python Is Fun!"

    # String com caracteres especiais
    texto = "welcome to python's world!"
    print(texto.title())  # saída : "Welcome To Python'S World!"
    ```

1. `str.strip()` : o método `strip()` remove os espaços em branco do início e do final da string. Além dos espaços em branco, você pode especificar caracteres adicionais a serem removidos.
    ```python
    # Exemplo básico
    texto = "   hello world   "
    print(texto.strip())  # saída : "hello world"

    # Removendo caracteres específicos
    texto = "***hello world***"
    print(texto.strip('*'))  # saída : "hello world"

    # Removendo múltiplos caracteres específicos
    texto = "!!!hello world###"
    print(texto.strip('!#'))  # saída : "hello world"
    ```

1. `str.lstrip()` : o método `lstrip()` remove os espaços em branco do início da string (lado esquerdo). Ele também pode remover caracteres específicos se forem fornecidos.
    ```python
    # Exemplo básico
    texto = "   hello world   "
    print(texto.lstrip())  # saída : "hello world   "

    # Removendo caracteres específicos
    texto = "***hello world***"
    print(texto.lstrip('*'))  # saída : "hello world***"

    # Removendo múltiplos caracteres específicos
    texto = "!!!hello world###"
    print(texto.lstrip('!#'))  # saída : "hello world###"
    ```

1. `str.rstrip()` : o método `rstrip()` remove os espaços em branco do final da string (lado direito). Ele também pode remover caracteres específicos se forem fornecidos.
    ```python
    # Exemplo básico
    texto = "   hello world   "
    print(texto.rstrip())  # saída : "   hello world"

    # Removendo caracteres específicos
    texto = "***hello world***"
    print(texto.rstrip('*'))  # saída : "***hello world"

    # Removendo múltiplos caracteres específicos
    texto = "!!!hello world###"
    print(texto.rstrip('!#'))  # saída : "!!!hello world"
    ```

1. `str.replace(old, new[, count])` : o método `replace()` substitui todas as ocorrências de uma substring por outra dentro da string. Se o argumento `count` for fornecido, ele limitará o número de substituições.
    ```python
    # Substituindo todas as ocorrências
    texto = "hello world"
    print(texto.replace("world", "Python"))  # saída : "hello Python"

    # Limitando o número de substituições
    texto = "banana"
    print(texto.replace("a", "o", 2))  # saída : "bonona"

    # Substituindo uma sequência de caracteres por outra
    texto = "abra kadabra"
    print(texto.replace("abra", "magic"))  # saída : "magic kadmagic"
    ```

1. `str.split(separator[, maxsplit])` : o método `split()` divide uma string em uma lista de substrings com base em um separador específico. Se `separator` não for especificado, espaços em branco serão usados por padrão. O argumento `maxsplit` limita o número de divisões.
    ```python
    # Exemplo básico com separador padrão (espaço em branco)
    texto = "hello world python"
    print(texto.split())  # saída : ['hello', 'world', 'python']

    # Dividindo com um separador específico
    texto = "hello,world,python"
    print(texto.split(','))  # saída : ['hello', 'world', 'python']

    # Limitando o número de divisões
    print(texto.split(',', 1))  # saída : ['hello', 'world,python']

    # Dividindo com múltiplos espaços
    texto = "hello   world   python"
    print(texto.split())  # saída : ['hello', 'world', 'python']
    ```

1. `str.join(iterable)` : o método `join()` combina elementos de um iterável (como listas ou tuplas) em uma única string, usando a string original como separador. Este método é frequentemente usado para converter listas de strings em uma única string.
    ```python
    # Exemplo básico com espaço como separador
    lista = ['hello', 'world', 'python']
    print(' '.join(lista))  # saída : "hello world python"

    # Usando outro separador
    print(','.join(lista))  # saída : "hello,world,python"

    # Usando uma string vazia como separador
    print(''.join(lista))  # saída : "helloworldpython"

    # Unindo elementos de uma lista de números (convertidos para strings)
    numeros = ['1', '2', '3', '4']
    print('-'.join(numeros))  # saída : "1-2-3-4"
    ```

1. `str.find(sub[, start[, end]])` : o método `find()` retorna o índice da primeira ocorrência da substring `sub` na string. Se a substring não for encontrada, ele retorna `-1`. Os parâmetros `start` e `end` são opcionais e podem limitar a busca a um intervalo específico.
    ```python
    # Encontrando a primeira ocorrência
    texto = "hello world"
    print(texto.find('world'))  # saída : 6

    # Buscando a partir de um índice específico
    print(texto.find('l', 4))  # saída : 9

    # Quando a substring não é encontrada
    print(texto.find('Python'))  # saída : -1

    # Buscando em um intervalo específico
    texto = "abracadabra"
    print(texto.find('abra', 1, 7))  # saída : 7
    ```

1. `str.rfind(sub[, start[, end]])` : o método `rfind()` é similar ao `find()`, mas busca pela última ocorrência da substring `sub` na string. Se a substring não for encontrada, ele retorna `-1`. Os parâmetros `start` e `end` são opcionais.
    ```python
    # Encontrando a última ocorrência
    texto = "abracadabra"
    print(texto.rfind('abra'))  # saída : 7

    # Buscando a partir de um índice específico
    print(texto.rfind('a', 0, 5))  # saída : 3

    # Quando a substring não é encontrada
    print(texto.rfind('Python'))  # saída : -1

    # Buscando em um intervalo específico
    print(texto.rfind('bra', 2, 7))  # saída : -1
    ```

1. `str.startswith(prefix[, start[, end]])` : o método `startswith()` verifica se a string começa com a substring `prefix`. Ele retorna `True` se a string começar com o prefixo e `False` caso contrário. Os parâmetros `start` e `end` podem limitar a verificação a um intervalo específico.
    ```python
    # Verificando se começa com determinado prefixo
    texto = "hello world"
    print(texto.startswith('hello'))  # saída : True

    # Verificando com um intervalo específico
    print(texto.startswith('world', 6))  # saída : True

    # Quando não começa com o prefixo
    print(texto.startswith('Python'))  # saída : False

    # Verificando com múltiplos prefixos
    print(texto.startswith(('hello', 'Hi')))  # saída : True
    ```

1. `str.endswith(suffix[, start[, end]])` : o método `endswith()` verifica se a string termina com a substring `suffix`. Ele retorna `True` se a string terminar com o sufixo e `False` caso contrário. Os parâmetros `start` e `end` podem limitar a verificação a um intervalo específico.
    ```python
    # Verificando se termina com determinado sufixo
    texto = "hello world"
    print(texto.endswith('world'))  # saída : True

    # Verificando com um intervalo específico
    print(texto.endswith('hello', 0, 5))  # saída : True

    # Quando não termina com o sufixo
    print(texto.endswith('Python'))  # saída : False

    # Verificando com múltiplos sufixos
    print(texto.endswith(('world', 'Python')))  # saída : True
    ```

1. `str.isalpha()` : o método `isalpha()` retorna `True` se todos os caracteres da string forem letras do alfabeto e a string não estiver vazia. Se houver números, espaços ou caracteres especiais, ele retorna `False`.
    ```python
    # Todos os caracteres são letras
    texto = "hello"
    print(texto.isalpha())  # saída : True

    # Contém números
    texto = "hello123"
    print(texto.isalpha())  # saída : False

    # Contém espaços
    texto = "hello world"
    print(texto.isalpha())  # saída : False

    # String vazia
    texto = ""
    print(texto.isalpha())  # saída : False
    ```

1. `str.isdigit()` : o método `isdigit()` retorna `True` se todos os caracteres da string forem dígitos (0-9) e a string não estiver vazia. Se houver letras, espaços ou caracteres especiais, ele retorna `False`.
    ```python
    # Todos os caracteres são dígitos
    texto = "123456"
    print(texto.isdigit())  # saída : True

    # Contém letras
    texto = "123abc"
    print(texto.isdigit())  # saída : False

    # Contém espaços
    texto = "123 456"
    print(texto.isdigit())  # saída : False

    # String vazia
    texto = ""
    print(texto.isdigit())  # saída : False
    ```

1. `str.isalnum()` : o método `isalnum()` retorna `True` se todos os caracteres da string forem letras ou dígitos e a string não estiver vazia. Se houver espaços ou caracteres especiais, ele retorna `False`.
    ```python
    # Todos os caracteres são alfanuméricos
    texto = "hello123"
    print(texto.isalnum())  # saída : True

    # Contém espaço
    texto = "hello 123"
    print(texto.isalnum())  # saída : False

    # Contém caracteres especiais
    texto = "hello@123"
    print(texto.isalnum())  # saída : False

    # String vazia
    texto = ""
    print(texto.isalnum())  # saída : False
    ```

1. `str.isspace()` : o método `isspace()` retorna `True` se todos os caracteres da string forem espaços em branco (incluindo tabulações, quebras de linha, etc.) e a string não estiver vazia. Se houver qualquer outro caractere, ele retorna `False`.
    ```python
    # Todos os caracteres são espaços em branco
    texto = "   "
    print(texto.isspace())  # saída : True

    # Contém um caractere não branco
    texto = "   a"
    print(texto.isspace())  # saída : False

    # String com quebra de linha
    texto = "\n\t"
    print(texto.isspace())  # saída : True

    # String vazia
    texto = ""
    print(texto.isspace())  # saída : False
    ```

1. `str.isupper()` : o método `isupper()` retorna `True` se todos os caracteres alfabéticos na string forem maiúsculos. Se houver caracteres minúsculos ou a string estiver vazia, ele retorna `False`.
    ```python
    # Todos os caracteres alfabéticos são maiúsculos
    texto = "HELLO"
    print(texto.isupper())  # saída : True

    # Contém caracteres minúsculos
    texto = "Hello"
    print(texto.isupper())  # saída : False

    # String com números e maiúsculas
    texto = "123 HELLO"
    print(texto.isupper())  # saída : True

    # String vazia
    texto = ""
    print(texto.isupper())  # saída : False
    ```

1. `str.islower()` : o método `islower()` retorna `True` se todos os caracteres alfabéticos na string forem minúsculos. Se houver caracteres maiúsculos ou a string estiver vazia, ele retorna `False`.
    ```python
    # Todos os caracteres alfabéticos são minúsculos
    texto = "hello"
    print(texto.islower())  # saída : True

    # Contém caracteres maiúsculos
    texto = "Hello"
    print(texto.islower())  # saída : False

    # String com números e minúsculas
    texto = "123 hello"
    print(texto.islower())  # saída : True

    # String vazia
    texto = ""
    print(texto.islower())  # saída : False
    ```

1. `str.zfill(width)` : o método `zfill()` retorna uma cópia da string original preenchida com zeros à esquerda para alcançar um determinado comprimento (`width`). Se a string for maior ou igual ao comprimento especificado, ela será retornada sem alterações.
    ```python
    # Preenchendo com zeros
    texto = "42"
    print(texto.zfill(5))  # saída : "00042"

    # String já maior que o comprimento especificado
    texto = "12345"
    print(texto.zfill(3))  # saída : "12345"

    # Aplicando em uma string negativa
    texto = "-42"
    print(texto.zfill(5))  # saída : "-0042"

    # Aplicando em uma string de caracteres
    texto = "abc"
    print(texto.zfill(5))  # saída : "00abc"
    ```

1. `str.center(width[, fillchar])` : o método `center()` retorna uma nova string de comprimento `width`, onde a string original é centralizada. Se o `fillchar` for fornecido, ele será usado para preencher os espaços em volta; caso contrário, o espaço será usado.
    ```python
    # Centralizando com espaços
    texto = "hello"
    print(texto.center(10))  # saída : "  hello   "

    # Centralizando com um caractere de preenchimento
    print(texto.center(10, '*'))  # saída : "**hello***"

    # Comprimento menor que a string original
    print(texto.center(4))  # saída : "hello"
    ```

1. `str.ljust(width[, fillchar])` : o método `ljust()` retorna uma nova string de comprimento `width`, onde a string original é justificada à esquerda. Se o `fillchar` for fornecido, ele será usado para preencher o espaço à direita; caso contrário, o espaço será usado.
    ```python
    # Justificando à esquerda com espaços
    texto = "hello"
    print(texto.ljust(10))  # saída : "hello     "

    # Justificando à esquerda com um caractere de preenchimento
    print(texto.ljust(10, '-'))  # saída : "hello-----"

    # Comprimento menor que a string original
    print(texto.ljust(4))  # saída : "hello"
    ```

1. `str.rjust(width[, fillchar])` : o método `rjust()` retorna uma nova string de comprimento `width`, onde a string original é justificada à direita. Se o `fillchar` for fornecido, ele será usado para preencher o espaço à esquerda; caso contrário, o espaço será usado.
    ```python
    # Justificando à direita com espaços
    texto = "hello"
    print(texto.rjust(10))  # saída : "     hello"

    # Justificando à direita com um caractere de preenchimento
    print(texto.rjust(10, '-'))  # saída : "-----hello"

    # Comprimento menor que a string original
    print(texto.rjust(4))  # saída : "hello"
    ```

1. `str.partition(sep)` : o método `partition()` divide a string em uma tupla de três elementos: a parte antes do separador `sep`, o próprio separador, e a parte após o separador. Se o separador não for encontrado, a tupla conterá a string original e duas strings vazias.
    ```python
    # Separando com um delimitador presente
    texto = "hello world python"
    print(texto.partition('world'))  # saída : ('hello ', 'world', ' python')

    # Separando com um delimitador ausente
    print(texto.partition('Python'))  # saída : ('hello world python', '', '')

    # Separando no início da string
    print(texto.partition('hello'))  # saída : ('', 'hello', ' world python')
    ```

1. `str.rpartition(sep)` : o método `rpartition()` é similar ao `partition()`, mas a divisão ocorre na última ocorrência do separador `sep`.
    ```python
    # Separando com um delimitador presente
    texto = "hello world world"
    print(texto.rpartition('world'))  # saída : ('hello world ', 'world', '')

    # Separando com um delimitador ausente
    print(texto.rpartition('Python'))  # saída : ('', '', 'hello world world')

    # Separando no início da string
    texto = "hello world"
    print(texto.rpartition('hello'))  # saída : ('', 'hello', ' world')
    ```

## execícios

< details>
<summary>Lista de Exercícios</summary>

### 1. `str.upper()`
1. Crie uma variável com uma frase e converta-a para letras maiúsculas usando `str.upper()`.
2. Receba uma string do usuário e exiba-a totalmente em maiúsculas.
3. Converta o nome de uma cidade para maiúsculas e exiba-o.
4. Converta a palavra "python" para maiúsculas e exiba o resultado.
5. Crie uma lista com várias palavras e converta cada uma para maiúsculas, exibindo o resultado.
6. Receba uma frase do usuário e converta apenas a primeira palavra para maiúsculas.
7. Armazene uma mensagem em uma variável e exiba-a em maiúsculas.
8. Receba o nome de um filme do usuário e exiba-o em maiúsculas.
9. Converta o título de um livro para maiúsculas e exiba-o.

### 2. `str.lower()`
1. Crie uma variável com uma frase e converta-a para letras minúsculas usando `str.lower()`.
2. Receba uma string do usuário e exiba-a totalmente em minúsculas.
3. Converta o nome de uma cidade para minúsculas e exiba-o.
4. Converta a palavra "PYTHON" para minúsculas e exiba o resultado.
5. Crie uma lista com várias palavras e converta cada uma para minúsculas, exibindo o resultado.
6. Receba uma frase do usuário e converta apenas a primeira palavra para minúsculas.
7. Armazene uma mensagem em uma variável e exiba-a em minúsculas.
8. Receba o nome de um filme do usuário e exiba-o em minúsculas.
9. Converta o título de um livro para minúsculas e exiba-o.

### 3. `str.capitalize()`
1. Crie uma variável com uma frase em letras minúsculas e use `str.capitalize()` para capitalizar a primeira letra.
2. Receba uma string do usuário e exiba-a com a primeira letra em maiúscula.
3. Converta a palavra "python" para "Python" usando `str.capitalize()`.
4. Crie uma lista com várias palavras e capitalize a primeira letra de cada uma, exibindo o resultado.
5. Receba uma frase do usuário e capitalize apenas a primeira palavra.
6. Armazene uma mensagem em uma variável e exiba-a com a primeira letra em maiúscula.
7. Receba o nome de um filme do usuário e exiba-o com a primeira letra em maiúscula.
8. Capitalize o título de um livro e exiba-o.
9. Receba o nome de uma cidade e capitalize a primeira letra.

### 4. `str.title()`
1. Crie uma variável com uma frase e use `str.title()` para capitalizar a primeira letra de cada palavra.
2. Receba uma string do usuário e exiba-a com a primeira letra de cada palavra em maiúscula.
3. Converta a frase "learning python is fun" para "Learning Python Is Fun" usando `str.title()`.
4. Crie uma lista de frases e aplique `str.title()` em cada uma, exibindo o resultado.
5. Receba uma frase do usuário e capitalize a primeira letra de cada palavra.
6. Armazene uma frase em uma variável e exiba-a com `str.title()`.
7. Receba o título de um filme e converta-o para `title case`.
8. Capitalize as palavras de um título de livro e exiba-o.
9. Receba uma frase e exiba-a com cada palavra iniciada com letra maiúscula.

### 5. `str.strip()`
1. Crie uma variável com uma string contendo espaços em branco no início e no final. Use `str.strip()` para removê-los.
2. Receba uma string do usuário com espaços extras e exiba-a sem esses espaços.
3. Remova espaços em branco de uma frase armazenada em uma variável.
4. Receba uma string de texto com espaços e pontuação extra, e use `str.strip()` para removê-los.
5. Crie uma lista de strings com espaços em branco e remova-os usando `str.strip()`.
6. Receba uma string com caracteres específicos no início e no fim e remova-os usando `str.strip()`.
7. Armazene uma frase com espaços e exiba-a sem os espaços no início e no final.
8. Receba uma string de texto e remova qualquer pontuação extra no início e no fim.
9. Receba uma frase do usuário e remova todos os espaços extras e caracteres especiais do início e fim.

### 6. `str.lstrip()`
1. Crie uma variável com uma string contendo espaços em branco no início. Use `str.lstrip()` para removê-los.
2. Receba uma string do usuário com espaços extras no início e exiba-a sem esses espaços.
3. Remova espaços em branco do início de uma frase armazenada em uma variável.
4. Receba uma string de texto com espaços extras no início e use `str.lstrip()` para removê-los.
5. Crie uma lista de strings com espaços em branco no início e remova-os usando `str.lstrip()`.
6. Receba uma string com caracteres específicos no início e remova-os usando `str.lstrip()`.
7. Armazene uma frase com espaços no início e exiba-a sem esses espaços.
8. Receba uma string de texto e remova qualquer pontuação extra no início.
9. Receba uma frase do usuário e remova todos os espaços extras e caracteres especiais do início.

### 7. `str.rstrip()`
1. Crie uma variável com uma string contendo espaços em branco no final. Use `str.rstrip()` para removê-los.
2. Receba uma string do usuário com espaços extras no final e exiba-a sem esses espaços.
3. Remova espaços em branco do final de uma frase armazenada em uma variável.
4. Receba uma string de texto com espaços extras no final e use `str.rstrip()` para removê-los.
5. Crie uma lista de strings com espaços em branco no final e remova-os usando `str.rstrip()`.
6. Receba uma string com caracteres específicos no final e remova-os usando `str.rstrip()`.
7. Armazene uma frase com espaços no final e exiba-a sem esses espaços.
8. Receba uma string de texto e remova qualquer pontuação extra no final.
9. Receba uma frase do usuário e remova todos os espaços extras e caracteres especiais do final.

### 8. `str.replace(old, new[, count])`
1. Crie uma string e substitua todas as ocorrências de "a" por "o" usando `str.replace()`.
2. Receba uma frase do usuário e substitua todas as ocorrências de uma palavra específica por outra.
3. Substitua todos os espaços em uma string por hífens usando `str.replace()`.
4. Crie uma lista de frases e substitua uma palavra específica em todas elas usando `str.replace()`.
5. Receba uma string e substitua todas as vírgulas por pontos.
6. Substitua todas as ocorrências da palavra "Python" por "programação" em uma string.
7. Receba uma frase e substitua apenas as primeiras 3 ocorrências de uma palavra específica.
8. Crie uma string com várias ocorrências de uma palavra e substitua-a por outra, limitando o número de substituições.
9. Substitua todos os números em uma string por "#" usando `str.replace()`.
10. Receba uma frase do usuário e substitua todas as ocorrências de uma letra específica, limitando o número de substituições.

### 9. `str.split(separator[, maxsplit])`
1. Crie uma string com várias palavras separadas por espaços e divida-a em uma lista de palavras usando `str.split()`.
2. Receba uma frase do usuário e divida-a em palavras usando espaços como separador.
3. Divida uma frase em uma lista de palavras usando vírgulas como separador.
4. Crie uma lista de frases e divida cada uma delas em palavras usando `str.split()`.
5. Receba uma string e divida-a em uma lista, limitando o número de divisões para 3.
6. Divida uma frase em palavras usando um caractere específico como separador.
7. Crie uma string com números separados por vírgulas e divida-a em uma lista de números.
8. Receba uma frase do usuário e divida-a em palavras, limitando o número de divisões para 2.
9. Divida uma string em partes, usando espaços como separador e limitando o número de divisões.
10. Receba uma frase e divida-a em palavras usando um separador específico, limitando o número de divisões.

### 10. `str.join(iterable)`
1. Crie uma lista de palavras e una-as em uma única string, separando-as por espaços usando `str.join()`.
2. Receba uma lista de palavras do usuário e una-as em uma única string com hífens como separador.
3. Una os elementos de uma lista de números em uma string, separando-os por vírgulas.
4. Crie uma lista de frases e una-as em uma única string, separando-as por espaços.
5. Receba uma lista de palavras e una-as em uma string com um caractere específico como separador.
6. Una os elementos de uma lista de palavras em uma string, separando-os por " - ".
7. Receba uma lista de nomes e una-os em uma string com vírgulas como separador.
8. Crie uma lista de palavras e una-as em uma string, separando-as por " | ".
9. Receba uma lista de frases e una-as em uma única string com pontos finais entre elas.
10. Crie uma lista de números e una-os em uma string com espaços como separador.

### 11. `str.find(sub[, start[, end]])`
1. Crie uma string e encontre a posição da primeira ocorrência de uma letra específica usando `str.find()`.
2. Receba uma frase do usuário e encontre a posição da primeira ocorrência de uma palavra específica.
3. Encontre a posição da primeira ocorrência de "Python" em uma string.
4. Crie uma lista de frases e encontre a posição de uma palavra específica em cada uma delas usando `str.find()`.
5. Receba uma string e encontre a posição da primeira ocorrência de uma letra específica, começando a busca em um índice específico.
6. Encontre a posição da primeira ocorrência de um número em uma string.
7. Receba uma frase e encontre a posição da primeira ocorrência de uma palavra específica, dentro de um intervalo específico.
8. Crie uma string e encontre a posição da primeira ocorrência de uma letra específica, buscando apenas em uma parte da string.
9. Receba uma frase do usuário e encontre a posição da primeira ocorrência de um caractere específico.
10. Encontre a posição da primeira ocorrência de uma palavra em uma string, começando a busca em um índice específico.

### 12. `str.rfind(sub[, start[, end]])`
1. Crie uma string e encontre a posição da última ocorrência de uma letra específica usando `str.rfind()`.
2. Receba uma frase do usuário e encontre a posição da última ocorrência de uma palavra específica.
3. Encontre a posição da última ocorrência de "Python" em uma string.
4. Crie uma lista de frases e encontre a posição da última ocorrência de uma palavra específica em cada uma delas usando `str.rfind()`.
5. Receba uma string e encontre a posição da última ocorrência de uma letra específica, começando a busca em um índice específico.
6. Encontre a posição da última ocorrência de um número em uma string.
7. Receba uma frase e encontre a posição da última ocorrência de uma palavra específica, dentro de um intervalo específico.
8. Crie uma string e encontre a posição da última ocorrência de uma letra específica, buscando apenas em uma parte da string.
9. Receba uma frase do usuário e encontre a posição da última ocorrência de um caractere específico.
10. Encontre a posição da última ocorrência de uma palavra em uma string, começando a busca em um índice específico.

### 13. `str.startswith(prefix[, start[, end]])`
1. Crie uma string e verifique se ela começa com uma letra específica usando `str.startswith()`.
2. Receba uma frase do usuário e verifique se ela começa com uma palavra específica.
3. Verifique se a string "Python is awesome" começa com a palavra "Python".
4. Crie uma lista de frases e verifique se cada uma começa com uma palavra específica usando `str.startswith()`.
5. Receba uma string e verifique se ela começa com uma letra específica, começando a verificação em um índice específico.
6. Verifique se uma string começa com um número específico.
7. Receba uma frase e verifique se ela começa com uma palavra específica, dentro de um intervalo específico.
8. Crie uma string e verifique se ela começa com uma letra específica, buscando apenas em uma parte da string.
9. Receba uma frase do usuário e verifique se ela começa com um caractere específico.
10. Verifique se uma string começa com uma palavra específica, começando a verificação em um índice específico.

### 14. `str.endswith(suffix[, start[, end]])`
1. Crie uma string e verifique se ela termina com uma letra específica usando `str.endswith()`.
2. Receba uma frase do usuário e verifique se ela termina com uma palavra específica.
3. Verifique se a string "Python is awesome" termina com a palavra "awesome".
4. Crie uma lista de frases e verifique se cada uma termina com uma palavra específica usando `str.endswith()`.
5. Receba uma string e verifique se ela termina com uma letra específica, começando a verificação em um índice específico.
6. Verifique se uma string termina com um número específico.
7. Receba uma frase e verifique se ela termina com uma palavra específica, dentro de um intervalo específico.
8. Crie uma string e verifique se ela termina com uma letra específica, buscando apenas em uma parte da string.
9. Receba uma frase do usuário e verifique se ela termina com um caractere específico.
10. Verifique se uma string termina com uma palavra específica, começando a verificação em um índice específico.

### 15. `str.isalpha()`
1. Crie uma string contendo apenas letras e verifique se `str.isalpha()` retorna `True`.
2. Receba uma string do usuário e verifique se ela contém apenas letras.
3. Verifique se a string "Python3" contém apenas letras usando `str.isalpha()`.
4. Crie uma lista de palavras e verifique se cada uma delas contém apenas letras.
5. Receba uma string e verifique se ela contém apenas letras, sem espaços ou caracteres especiais.
    ```python
    >>> texto = input('Digite um texto qualquer : ')
    Digite um texto qualquer : aqui tem um texto qualquer
    >>> texto
    'aqui tem um texto qualquer'
    >>>
    >>> if texto.isalpha():
    ...     print('o conteúdo dessa variável só tem caracteres alfabéticos')
    ... else:
    ...     print('essa string tem outras coisas além dos caracteres alfabéticos')
    ...
    essa string tem outras coisas além dos caracteres alfabéticos
    >>> |
    ```
6. Verifique se uma string composta por várias palavras contém apenas letras.
7. Receba uma frase do usuário e verifique se todas as palavras contêm apenas letras.
8. Verifique se uma string que contém um nome completo tem apenas letras.
9. Receba uma palavra do usuário e verifique se ela contém apenas letras, sem números ou símbolos.

### 16. `str.isdigit()`
1. Crie uma string contendo apenas números e verifique se `str.isdigit()` retorna `True`.
2. Receba uma string do usuário e verifique se ela contém apenas números.
3. Verifique se a string "12345" contém apenas números usando `str.isdigit()`.
4. Crie uma lista de strings e verifique se cada uma delas contém apenas números.
5. Receba uma string e verifique se ela contém apenas números, sem espaços ou caracteres especiais.
6. Verifique se uma string composta por um número de telefone contém apenas números.
7. Receba uma string do usuário e verifique se ela é um código postal válido (apenas números).
8. Verifique se uma string que contém a idade de uma pessoa tem apenas números.
9. Receba uma string do usuário e verifique se ela contém apenas números, sem letras ou símbolos.

### 17. `str.isalnum()`
1. Crie uma string contendo apenas letras e números e verifique se `str.isalnum()` retorna `True`.
2. Receba uma string do usuário e verifique se ela contém apenas letras e números.
3. Verifique se a string "Python3" contém apenas letras e números usando `str.isalnum()`.
4. Crie uma lista de strings e verifique se cada uma delas contém apenas letras e números.
5. Receba uma string e verifique se ela contém apenas letras e números, sem espaços ou caracteres especiais.
6. Verifique se uma string composta por um nome de usuário contém apenas letras e números.
7. Receba uma string do usuário e verifique se ela contém apenas letras e números, sem símbolos.
8. Verifique se uma string que contém uma senha tem apenas letras e números.
9. Receba uma string do usuário e verifique se ela contém apenas letras e números, sem espaços.

### 18. `str.isspace()`
1. Crie uma string contendo apenas espaços em branco e verifique se `str.isspace()` retorna `True`.
2. Receba uma string do usuário e verifique se ela contém apenas espaços.
3. Verifique se uma string composta por tabulações e espaços contém apenas espaços usando `str.isspace()`.
4. Crie uma lista de strings e verifique se cada uma delas contém apenas espaços.
5. Receba uma string e verifique se ela contém apenas espaços, sem letras ou números.
6. Verifique se uma string que aparenta estar vazia contém apenas espaços.
7. Receba uma string do usuário e verifique se ela contém apenas tabulações e espaços.
8. Verifique se uma string que contém múltiplos espaços consecutivos contém apenas espaços.
9. Receba uma string do usuário e verifique se ela contém apenas espaços, sem outros caracteres.

### 19. `str.isupper()`
1. Crie uma string em maiúsculas e verifique se `str.isupper()` retorna `True`.
2. Receba uma string do usuário e verifique se ela está totalmente em maiúsculas.
3. Verifique se a string "PYTHON" está totalmente em maiúsculas usando `str.isupper()`.
4. Crie uma lista de palavras e verifique se cada uma delas está em maiúsculas.
5. Receba uma string e verifique se ela está em maiúsculas, sem letras minúsculas.
6. Verifique se uma string que contém uma frase está toda em maiúsculas.
7. Receba uma string do usuário e verifique se ela contém apenas letras maiúsculas.
8. Verifique se uma string que contém o nome de uma cidade está em maiúsculas.
9. Receba uma string do usuário e verifique se ela está completamente em maiúsculas, sem caracteres minúsculos.

### 20. `str.islower()`
1. Crie uma string em minúsculas e verifique se `str.islower()` retorna `True`.
2. Receba uma string do usuário e verifique se ela está totalmente em minúsculas.
3. Verifique se a string "python" está totalmente em minúsculas usando `str.islower()`.
4. Crie uma lista de palavras e verifique se cada uma delas está em minúsculas.
5. Receba uma string e verifique se ela está em minúsculas, sem letras maiúsculas.
6. Verifique se uma string que contém uma frase está toda em minúsculas.
7. Receba uma string do usuário e verifique se ela contém apenas letras minúsculas.
8. Verifique se uma string que contém o nome de uma cidade está em minúsculas.
9. Receba uma string do usuário e verifique se ela está completamente em minúsculas, sem caracteres maiúsculos.

### 21. `str.zfill(width)`
1. Crie uma string numérica e use `str.zfill()` para preenchê-la com zeros à esquerda, completando um total de 10 caracteres.
2. Receba um número do usuário e complete-o com zeros à esquerda, usando `str.zfill()` para ter 8 dígitos.
3. Preencha um número de telefone com zeros à esquerda até ter um total de 12 caracteres.
4. Crie uma lista de números e preencha cada um com zeros à esquerda, até atingir 6 dígitos.
5. Receba uma string numérica do usuário e complete-a com zeros à esquerda para um total de 5 dígitos.
6. Use `str.zfill()` para garantir que um número de pedido tenha exatamente 10 dígitos, preenchendo com zeros à esquerda se necessário.
7. Receba um código postal e preencha-o com zeros à esquerda até ter 7 dígitos.
8. Preencha um número de série com zeros à esquerda até atingir 15 caracteres.
9. Receba um código de produto e complete-o com zeros à esquerda até ter 10 caracteres.

### 22. `str.center(width[, fillchar])`
1. Crie uma string e centralize-a em uma largura de 20 caracteres, preenchendo os espaços com traços (-).
    ```python
    >>> nome = 'Arnold'
    >>> nome = nome.center(20,'-')
    >>> print(nome)
    -------Arnold-------
    ```
2. Receba uma palavra do usuário e centralize-a em uma largura de 30 caracteres, usando asteriscos como preenchimento.
3. Centralize a frase "Python Rocks!" em uma largura de 40 caracteres, preenchendo os espaços com pontos (.).
4. Crie uma lista de palavras e centralize cada uma delas em uma largura de 15 caracteres, usando traços como preenchimento.
5. Receba uma string e centralize-a em uma largura de 25 caracteres, preenchendo os espaços com espaços em branco.
6. Use `str.center()` para centralizar um título de 10 caracteres em uma largura de 20, preenchendo com hífens (-).
7. Receba uma palavra do usuário e centralize-a em uma largura de 50 caracteres, preenchendo os espaços com iguais (=).
8. Centralize uma frase em uma largura de 60 caracteres, preenchendo os espaços com traços duplos (==).
9. Receba um título do usuário e centralize-o em uma largura de 35 caracteres, preenchendo os espaços com pontos de exclamação (!).

### 23. `str.ljust(width[, fillchar])`
1. Crie uma string e alinhe-a à esquerda em uma largura de 20 caracteres, preenchendo os espaços com traços (-).
2. Receba uma palavra do usuário e alinhe-a à esquerda em uma largura de 30 caracteres, usando asteriscos (*) como preenchimento.
3. Alinhe a frase "Python Rocks!" à esquerda em uma largura de 40 caracteres, preenchendo os espaços com pontos (.).
4. Crie uma lista de palavras e alinhe cada uma delas à esquerda em uma largura de 15 caracteres, usando traços como preenchimento.
5. Receba uma string e alinhe-a à esquerda em uma largura de 25 caracteres, preenchendo os espaços com espaços em branco.
6. Use `str.ljust()` para alinhar um título de 10 caracteres à esquerda em uma largura de 20, preenchendo com hífens (-).
7. Receba uma palavra do usuário e alinhe-a à esquerda em uma largura de 50 caracteres, preenchendo os espaços com iguais (=).
8. Alinhe uma frase à esquerda em uma largura de 60 caracteres, preenchendo os espaços com traços duplos (==).
9. Receba um título do usuário e alinhe-o à esquerda em uma largura de 35 caracteres, preenchendo os espaços com pontos de exclamação (!).

### 24. `str.rjust(width[, fillchar])`
1. Crie uma string e alinhe-a à direita em uma largura de 20 caracteres, preenchendo os espaços com traços (-).
2. Receba uma palavra do usuário e alinhe-a à direita em uma largura de 30 caracteres, usando asteriscos (*) como preenchimento.
3. Alinhe a frase "Python Rocks!" à direita em uma largura de 40 caracteres, preenchendo os espaços com pontos (.).
4. Crie uma lista de palavras e alinhe cada uma delas à direita em uma largura de 15 caracteres, usando traços como preenchimento.
5. Receba uma string e alinhe-a à direita em uma largura de 25 caracteres, preenchendo os espaços com espaços em branco.
6. Use `str.rjust()` para alinhar um título de 10 caracteres à direita em uma largura de 20, preenchendo com hífens (-).
7. Receba uma palavra do usuário e alinhe-a à direita em uma largura de 50 caracteres, preenchendo os espaços com iguais (=).
8. Alinhe uma frase à direita em uma largura de 60 caracteres, preenchendo os espaços com traços duplos (==).
9. Receba um título do usuário e alinhe-o à direita em uma largura de 35 caracteres, preenchendo os espaços com pontos de exclamação (!).

### 25. `str.partition(sep)`
1. Crie uma string contendo uma frase e separe-a em três partes usando `str.partition()`, com o separador sendo um espaço.
2. Receba uma frase do usuário e use `str.partition()` para separar a primeira palavra do restante.
3. Use `str.partition()` para dividir uma string em três partes, com o separador sendo uma vírgula.
4. Crie uma lista de frases e use `str.partition()` em cada uma para separar a primeira palavra do restante.
5. Receba uma string e use `str.partition()` para dividir a string em três partes, usando um hífen como separador.
6. Use `str.partition()` para separar uma frase em três partes, com o separador sendo o primeiro espaço encontrado.
7. Crie uma string com múltiplas palavras e use `str.partition()` para dividir a string na primeira ocorrência de uma palavra específica.
8. Receba uma string do usuário e use `str.partition()` para separar a string em três partes, usando um ponto final como separador.
9. Use `str.partition()` para dividir uma string de números em três partes, com o separador sendo um ponto (.)
10. Receba uma frase do usuário e use `str.partition()` para separar a frase na primeira ocorrência de uma palavra específica.

</details>


# índice

1. [introdução](#introdução)
1. [funções](#funções)
    1. [`re.search()`](#research)
    1. [`re.match()`](#rematch)
    1. [`re.findall()`](#refindall)
    1. [`re.sub()`](#resub)
    1. [`re.split()`](#resplit)
    1. [`re.compile()`](#recompile)
    1. [`re.escape()`](#reescape)
1. [metacaracteres](#metacaracteres)
    1. [`.` (ponto)](#-ponto)
    1. [`^` (circunflexo)](#-circunflexo)
    1. [`$` (cifrão)](#-cifrão)
    1. [`*` (asterisco)](#-asterisco)
    1. [`+` (mais)](#-mais)
    1. [`?` (interrogação)](#-interrogação)

# expressões regulares

## introdução

Uma [**expressão regular**](https://docs.python.org/pt-br/3/library/re.html) (ou regex) é uma sequência de caracteres que forma um padrão de busca. Essas expressões podem ser usadas para procurar, corresponder ou manipular textos.

No Python, para trabalhar com expressões regulares, utiliza-se o módulo **`re`**.

### importando módulo `re`

Para usar as expressões regulares, é preciso importar o módulo `re` :

```python
import re
```

Abaixo, a função `re.search()` é usada para procurar um padrão em uma string. Mais detalhes serão vistos adiante.

**exemplo :**

```python
import re

# definindo uma string
texto = "Hoje é um belo dia!"

# procurando pela palavra 'belo'
resultado = re.search("belo", texto)

# verificando se encontramos algo
if resultado:
    print("Padrão encontrado!")
else:
    print("Padrão não encontrado.")
```

Aqui, está sendo procurado a palavra "belo" na string "Hoje é um belo dia!". Se a palavra for encontrada, a seguinte mensagem será exibida :

```
Padrão encontrado!
```

Se o padrão não for encontrado, `re.search()` retorna `None`, o que será interpretado como falso.

**exemplo :**

```python
resultado = re.search("noite", texto)

if resultado:
    print("Padrão encontrado!")
else:
    print("Padrão não encontrado.")
```

Nesse caso, como "noite" não está presente na string, o resultado será:

```
Padrão não encontrado.
```

### case-sensitive

As expressões regulares possuem sensibilidade a maiúsculas e minúsculas (**case-sensitive**), o que significa que "belo" não é o mesmo que "Belo".

**exemplo :**

```python
resultado = re.search("Belo", texto)

if resultado:
    print("Padrão encontrado!")
else:
    print("Padrão não encontrado.")
```

Aqui, o padrão "Belo" não será encontrado porque no texto a palavra está escrita com letra minúscula.

```
Padrão não encontrado.
```

## resumo

Abaixo há três tabelas com o resumo da maior parte do conteúdo que será visto :

| Função | Explicação | Exemplo |
|---|---|---|
| `re.search(pattern, string, flags=0)` | Procura a primeira ocorrência do padrão na string. Retorna um objeto Match se encontrar, caso contrário retorna None. | `re.search(r'\d+', 'abc123def')` retorna um objeto Match correspondendo a '123'. |
| `re.match(padrao, string)` | Procura o padrão no início da string. Retorna um objeto Match se encontrar, caso contrário retorna None. | `re.match(r'\d+', '123abc')` retorna um objeto Match correspondendo a '123', mas `re.match(r'\d+', 'abc123')` retorna None. |
| `re.fullmatch(padrao, string)` | Procura o padrão em toda a string (do início ao fim). Retorna um objeto Match se encontrar, caso contrário retorna None. | `re.fullmatch(r'\d+', '123')` retorna um objeto Match, mas `re.fullmatch(r'\d+', '123abc')` retorna None. |
| `re.findall(padrao, string)` | Retorna uma lista com todas as ocorrências não sobrepostas do padrão na string. | `re.findall(r'\d+', 'abc123def456')` retorna ['123', '456']. |
| `re.finditer(padrao, string)` | Retorna um iterador que produz objetos Match para cada ocorrência não sobreposta do padrão na string. | `for m in re.finditer(r'\d+', 'abc123def456'): print(m.group())` imprime '123' e '456'. |
| `re.sub(padrao, substituicao, string)` | Substitui as ocorrências do padrão na string pela string de substituição. | `re.sub(r'\d+', 'NUM', 'abc123def')` retorna 'abcNUMdef'. |
| `re.split(padrao, string)` | Divide a string em uma lista usando o padrão como delimitador. | `re.split(r'\s+', 'olá mundo!')` retorna ['olá', 'mundo!']. |
| `re.compile(padrao)` | Compila o padrão em um objeto Pattern, que pode ser usado para realizar buscas e substituições de forma mais eficiente. | `padrao = re.compile(r'\d+')` cria um objeto Pattern que pode ser usado posteriormente com `padrao.search()`, `padrao.findall()`, etc. |
| `re.escape(padrao)` | Faz o escape de todos os caracteres especiais no padrão, para que sejam tratados como literais. | `re.escape('a.b')` retorna 'a\.b'. |

| Metacaractere | Explicação | Exemplo |
|---|---|---|
| `.` | Corresponde a qualquer caractere, exceto quebras de linha. | `a.c` corresponde a "abc", "a1c", etc. |
| `^` | Corresponde ao início da string ou linha. | `^Olá` corresponde a "Olá mundo", mas não a "O mundo diz Olá". |
| `$` | Corresponde ao final da string ou linha. | `mundo$` corresponde a "Olá mundo", mas não a "O mundo diz Olá". |
| `*` | Corresponde a zero ou mais ocorrências do elemento anterior. | `ab*c` corresponde a "ac", "abc", "abbc", etc. |
| `+` | Corresponde a uma ou mais ocorrências do elemento anterior. | `ab+c` corresponde a "abc", "abbc", mas não a "ac". |
| `?` | Corresponde a zero ou uma ocorrência do elemento anterior. | `ab?c` corresponde a "ac" e "abc". |
| `{}` | Especifica um número exato ou um intervalo de repetições. | `a{2}b` corresponde a "aab", `a{2,4}b` corresponde a "aab", "aaab" e "aaaab". |
| `[]` | Define um conjunto de caracteres. | `[abc]` corresponde a "a", "b" ou "c". |
| `[^]` | Define um conjunto de caracteres negado. | `[^abc]` corresponde a qualquer caractere que não seja "a", "b" ou "c". |
| `\` | Escapa um metacaractere ou representa uma sequência especial. | `\d` corresponde a qualquer dígito, `\.` corresponde a um ponto literal. |
| `\|` | Representa uma alternativa (OU). | `gato\|cachorro` corresponde a "gato" ou "cachorro". |
| `()` | Agrupa partes da expressão e cria um grupo de captura. | `(ab)+` corresponde a "ab", "abab", "ababab", etc. |

| Sequência | Explicação | Exemplo |
| `\w` | Corresponde a qualquer caractere alfanumérico ou sublinhado. | `\w+` corresponde a "palavra", "palavra123", "_palavra", etc. |
| `\W` | Corresponde a qualquer caractere que não seja alfanumérico ou sublinhado. | `\W+` corresponde a "espaço ", "!@#$", etc. |
| `\d` | Corresponde a qualquer dígito. | `\d+` corresponde a "123", "456789", etc. |
| `\D` | Corresponde a qualquer caractere que não seja um dígito. | `\D+` corresponde a "abc", "olá mundo", etc. |
| `\s` | Corresponde a qualquer espaço em branco (espaço, tabulação, nova linha, etc.). | `\s+` corresponde a " ", "\t\n", etc. |
| `\S` | Corresponde a qualquer caractere que não seja um espaço em branco. | `\S+` corresponde a "palavra", "123", etc. |
| `\b` | Corresponde a um limite de palavra. | `\bpalavra\b` corresponde a "palavra" em "a palavra é", mas não em "apalavraé". |
| `\B` | Corresponde a um local que não é um limite de palavra. | `\Bpalavra\B` corresponde a "palavra" em "apalavraé", mas não em "a palavra é". |

| Flag | Nome | Descrição                                                                                     |
|----|----|----|
| `re.IGNORECASE`  Ignore case (ou `re.I`) | Faz a correspondência sem diferenciar maiúsculas e minúsculas. |
| `re.MULTILINE` | Multiline (ou `re.M`) | Altera o comportamento de `^` e `$` para corresponder ao início e fim de cada linha, não apenas da string. |
| `re.DOTALL` | Dot all (ou `re.S`) | Faz com que o metacaractere `.` corresponda a todos os caracteres, incluindo quebras de linha. |
| `re.VERBOSE` | Verbose (ou `re.X`) | Permite adicionar espaços e comentários dentro do padrão regex para maior legibilidade. |
| `re.ASCII` | ASCII (ou `re.A`) | Faz com que escapes como `\w`, `\b`, `\s` correspondam apenas a caracteres ASCII. |
| `re.LOCALE` | Locale (ou `re.L`) | Faz com que escapes como `\w`, `\b`, `\s` dependam das convenções locais (obsoleto em Unicode). |
| `re.UNICODE` | Unicode (ou `re.U`) | Faz com que escapes como `\w`, `\b`, `\d` correspondam a caracteres Unicode (padrão no Python 3). |

**Observações:**

* essas tabelas incluem algumas das funcionalidades mais comuns, mas existem outros disponíveis;

## funções

### `re.search()`

A função `re.search()` procura o **primeiro** local onde o padrão é encontrado em qualquer parte da string. Se uma correspondência for encontrada, ela retorna um objeto de correspondência. Caso contrário, retorna `None`.

```python
re.search(padrão, string, flags=0)
```

- **`padrão`** : o padrão que você quer procurar (expressão regular);
- **`string`** : a string onde será feita a busca;
- **`flags`** : parâmetro opcional para modificar o comportamento da busca (isso será visto mais tarde);

1. **exemplo buscando palavra em frase**

    ```python
    import re

    # texto para busca
    texto = "O Python é uma linguagem poderosa."

    # procurando pela palavra "Python"
    resultado = re.search("Python", texto)

    # verificando se o padrão foi encontrado
    if resultado:
        print("Padrão encontrado:", resultado.group())
    else:
        print("Padrão não encontrado.")
    ```

    **Explicação**
    - **`re.search("Python", texto)`** : procura pela palavra "Python" em qualquer parte da string `texto`;
    - **`resultado.group()`** : se a correspondência for encontrada, `group()` retorna o texto que correspondeu ao padrão;

    **Saída**
    ```
    Padrão encontrado: Python
    ```

1. **exemplo caso padrão não encontrado**

    ```python
    # procurando pela palavra "Java"
    resultado = re.search("Java", texto)

    # verificando se o padrão foi encontrado
    if resultado:
        print("Padrão encontrado:", resultado.group())
    else:
        print("Padrão não encontrado.")
    ```

    Neste exemplo, a palavra "Java" não está presente no texto, então o resultado será :

    **Saída**
    ```
    Padrão não encontrado.
    ```

1. **exemplo usando `re.search()` com metacaracteres**

    Abaixo, é buscado qualquer palavra que comece com "P".

    ```python
    # procurando qualquer palavra que comece com "P"
    resultado = re.search(r"\bP\w+", texto)

    if resultado:
        print("Padrão encontrado:", resultado.group())
    else:
        print("Padrão não encontrado.")
    ```

    **Explicação**
    - **`\b`** : indica uma borda de palavra (mais detalhes adiante);
    - **`P\w+`** : procura por "P" seguido de um ou mais caracteres alfanuméricos;

    **Saída**
    ```
    Padrão encontrado: Python
    ```

### exercícios `re.search()`

<details>
<summary>Lista de Exercícios</summary>

1. Crie uma string que contenha o nome de três frutas separadas por vírgulas. Utilize a função `search()` para verificar se a fruta "banana" está presente na string.
1. Escreva uma string com uma frase sobre seu animal de estimação. Use `search()` para encontrar a palavra "cachorro" na frase e imprima o resultado.
1. Crie uma lista de compras como uma string. Utilize `search()` para verificar se "leite" está na lista.
1. Defina uma string que represente uma frase famosa. Use `search()` para localizar a palavra "liberdade" na frase.
1. Escreva uma string que contenha uma sequência de números de telefone. Utilize `search()` para buscar um número específico na sequência.
1. Crie uma string com um texto de uma receita culinária. Utilize `search()` para verificar se a palavra "açúcar" aparece na receita.
1. Defina uma string que contenha a letra do seu artista favorito. Use `search()` para verificar se uma palavra-chave relacionada ao tema da música está presente.
1. Crie uma string que contenha o nome de várias cidades. Utilize `search()` para procurar uma cidade específica e imprima se ela foi encontrada.
1. Escreva uma string que descreva um filme que você gosta. Utilize `search()` para verificar se o nome do ator principal está na descrição.
1. Defina uma string que contenha uma lista de tarefas a serem realizadas. Utilize `search()` para buscar uma tarefa específica e verifique se ela está listada.

</details>

---

### `re.match()`

A função `re.match()` tenta encontrar uma correspondência **no início da string**. Se a string começar com o padrão, ele retorna um objeto de correspondência. Caso contrário, retorna `None`.

```python
re.match(padrão, string, flags=0)
```

- **`padrão`** : o padrão que você quer procurar (expressão regular);
- **`string`** : a string onde será feita a busca;
- **`flags`** : parâmetro opcional para modificar o comportamento da busca (isso será visto mais tarde);

1. **exemplo verificando se uma string começa com uma palavra específica**

    ```python
    import re

    # texto para buscar
    texto = "Python é uma linguagem poderosa."

    # verificando se o texto começa com "Python"
    resultado = re.match("Python", texto)

    if resultado:
        print("Padrão encontrado:", resultado.group())
    else:
        print("Padrão não encontrado.")
    ```

    **Explicação**
    - **`re.match("Python", texto)`** : verifica se a string `texto` começa com "Python";
    - **`resultado.group()`** : retorna a correspondência encontrada, se houver;

    **Saída**
    ```
    Padrão encontrado: Python
    ```

1. **exemplo caso em que o padrão não está no início da string**

    ```python
    # texto para busca
    texto = "Aprender Python é muito interessante."

    # verificando se o texto começa com "Python"
    resultado = re.match("Python", texto)

    if resultado:
        print("Padrão encontrado:", resultado.group())
    else:
        print("Padrão não encontrado.")
    ```

    Neste caso, como "Python" não está no início da string, `re.match()` não encontrará correspondência.

    **Saída**
    ```
    Padrão não encontrado.
    ```

1. **exemplo usando `re.match()` com metacaracteres**

    Aqui vai ser verificado se a string começa com uma palavra que começa com "A".

    ```python
    # verificando se o texto começa com uma palavra que começa com "A"
    resultado = re.match(r"A\w+", texto)

    if resultado:
        print("Padrão encontrado:", resultado.group())
    else:
        print("Padrão não encontrado.")
    ```

    **Explicação**
    - **`A\w+`** : verifica se a string começa com "A" seguido de caracteres alfanuméricos;

    **Saída**
    ```
    Padrão encontrado: Aprender
    ```

### exercícios `re.match()`

<details>
<summary>Lista de Exercícios</summary>

1. Crie uma string que contenha o nome de uma cidade. Utilize a função `match()` para verificar se a string começa com a letra "S".
1. Escreva uma string que represente uma frase sobre sua cor favorita. Use `match()` para verificar se a frase começa com a palavra "Minha".
1. Defina uma string que contenha uma lista de países. Utilize `match()` para verificar se a string começa com "Brasil".
1. Crie uma string que descreva um esporte que você gosta. Utilize `match()` para verificar se a descrição começa com a palavra "Futebol".
1. Escreva uma string com o nome de um autor famoso. Use `match()` para verificar se o nome começa com a letra "A".
1. Defina uma string que contenha uma receita de culinária. Utilize `match()` para verificar se a receita começa com a palavra "Para".
1. Crie uma string que contenha uma citação inspiradora. Use `match()` para verificar se a citação começa com "A vida".
1. Escreva uma string que descreva um filme que você assistiu recentemente. Utilize `match()` para verificar se a descrição começa com o título do filme.
1. Defina uma string que contenha uma sequência de números. Use `match()` para verificar se a sequência começa com o número "1".
1. Crie uma string que represente uma lista de hobbies. Utilize `match()` para verificar se a string começa com "Ler".

</details>

---

### `re.fullmatch()`

A função `re.fullmatch()` verifica se **toda a string** corresponde exatamente ao padrão fornecido. Ela só retorna uma correspondência se a string inteira corresponder ao padrão; caso contrário, retorna `None`.

```python
re.fullmatch(padrão, string, flags=0)
```

- **`padrão`** : o padrão que você quer procurar (expressão regular);
- **`string`** : a string onde será feita a busca;
- **`flags`** : parâmetro opcional para modificar o comportamento da busca (isso será visto mais tarde);

1. **exemplo verificando se toda a string corresponde ao padrão**

    ```python
    import re

    # texto para verificação
    texto = "Python3"

    # verificando se a string inteira corresponde ao padrão
    resultado = re.fullmatch(r"Py....3", texto)

    if resultado:
        print("Padrão encontrado:", resultado.group())
    else:
        print("Padrão não encontrado.")
    ```

    **Explicação**
    - **`Py....3`** : esse padrão corresponde a uma palavra iniciada com Py, seguido de 4 caracteres quaisquer e finalizando com o número 3;
    - **`re.fullmatch(r"Py....3", texto)`** : verifica se toda a string `texto` corresponde ao padrão;

    **Saída**
    ```
    Padrão encontrado: Python3
    ```

    Aqui, o padrão `\w+` corresponde exatamente à string inteira, então há uma correspondência.

1. **exemplo caso em que a string não corresponde completamente**

    ```python
    # texto para fazer a verificação
    texto = "Python3!"

    # verificando se a string inteira corresponde ao padrão
    resultado = re.fullmatch(r"\w+", texto)

    if resultado:
        print("Padrão encontrado:", resultado.group())
    else:
        print("Padrão não encontrado.")
    ```

    Neste exemplo, o caractere de exclamação `!` não faz parte do padrão `\w+`, pois `\w` corresponde apenas a letras, números e underscores. Portanto, o resultado será:

    **Saída**
    ```
    Padrão não encontrado.
    ```

### exercícios `re.full match()`

<details>
<summary>Lista de Exercícios</summary>

1. Use `fullmatch()` para verificar se a string "Python3" corresponde à expressão regular que representa uma palavra que começa com "Python" seguida de um dígito.
1. Crie uma expressão regular que utilize `fullmatch()` para validar se a string "2024-10-07" é uma data no formato "aaaa-mm-dd".
1. Use `fullmatch()` para verificar se a string "abcde" corresponde a uma sequência de exatamente 5 letras minúsculas.
1. Escreva uma expressão regular que utilize `fullmatch()` para validar se a string "12345" é composta apenas por números.
1. Defina uma expressão regular que utilize `fullmatch()` para verificar se a string "email@exemplo.com" é um formato válido de e-mail.
1. Use `fullmatch()` para verificar se a string "senha123!" corresponde a uma senha que deve ter pelo menos 8 caracteres, incluindo letras, números e símbolos.
1. Crie uma expressão regular que utilize `fullmatch()` para validar se a string "ABC-123" tem um padrão que consiste em 3 letras maiúsculas, um hífen e 3 dígitos.
1. Use `fullmatch()` para verificar se a string "123-456-7890" corresponde a um número de telefone no formato "ddd-ddd-dddd".
1. Escreva uma expressão regular que utilize `fullmatch()` para verificar se a string "a*b+c?" é uma expressão que contém letras e os operadores de soma e multiplicação.
1. Defina uma expressão regular que utilize `fullmatch()` para validar se a string "Mariana" corresponde a um nome que começa com letra maiúscula e tem apenas letras.

</details>

---

### `re.findall()`

A função `re.findall()` encontra **todas as correspondências** do padrão na string e retorna uma lista com as correspondências. Diferente de `search()`, que retorna apenas a primeira correspondência, `findall()` retorna todas as ocorrências encontradas.

```python
re.findall(padrão, string, flags=0)
```

- **`padrão`** : o padrão que você quer procurar (expressão regular);
- **`string`** : a string onde será feita a busca;
- **`flags`** : parâmetro opcional para modificar o comportamento da busca;

1. **exemplo encontrando todas as palavras em uma string**

    ```python
    # texto para busca
    texto = "Python é uma linguagem poderosa e Python é popular."

    # procurando todas as palavras "Python"
    resultado = re.findall(r"Python", texto)

    # exibindo todas as correspondências
    print("Correspondências encontradas:", resultado)
    ```

    **Explicação**
    - **`findall(r"Python", texto)`** : encontra todas as ocorrências da palavra "Python" na string `texto`;
    - a função retorna uma lista com todas as correspondências;

    **Saída**
    ```
    Correspondências encontradas: ['Python', 'Python']
    ```

    Aqui, a função encontrou a palavra "Python" duas vezes no texto.

1. **exemplo encontrando todas as palavras em um texto**

    Agora, veja a busca por todas as palavras, ou seja, sequências de letras.

    ```python
    # procurando todas as palavras
    resultado = re.findall(r"\b\w+\b", texto)

    # exibindo todas as palavras encontradas
    print("Palavras encontradas:", resultado)
    ```

    **Explicação**
    - **`\b\w+\b`** : esse padrão encontra palavras completas. O `\b` representa a borda de uma palavra, e `\w+` corresponde a uma sequência de caracteres alfanuméricos;
    - **`findall()`** retorna todas as palavras encontradas como uma lista;

    **Saída**
    ```
    Palavras encontradas: ['Python', 'é', 'uma', 'linguagem', 'poderosa', 'e', 'Python', 'é', 'popular']
    ```

1. **exemplo encontrando todos os números em uma string**

    ```python
    # texto com números
    texto = "O preço é 100 reais e o desconto é 15%."

    # procurando todos os números
    resultado = re.findall(r"\d+", texto)

    # exibindo os números encontrados
    print("Números encontrados:", resultado)
    ```

    **Explicação**
    - **`\d+`** : esse padrão corresponde a um ou mais dígitos (números);
    - **`findall()`** : retorna todas as ocorrências de números na string;

    **Saída**
    ```
    Números encontrados: ['100', '15']
    ```

    Neste exemplo, a função encontrou dois números: "100" e "15".

1. **exemplo buscando por padrões mais complexos**

    Veja uma busca por todas as palavras que começam com uma letra maiúscula.

    ```python
    # texto com palavras que começam com maiúsculas
    texto = "Python é uma linguagem Popular desenvolvida por Guido van Rossum."

    # procurando todas as palavras que começam com letra maiúscula
    resultado = re.findall(r"\b[A-Z]\w*\b", texto)

    # exibindo as correspondências encontradas
    print("Palavras encontradas:", resultado)
    ```

    **Explicação**
    - **`\b[A-Z]\w*\b`** : o padrão corresponde a palavras que começam com uma letra maiúscula (A-Z) seguida de zero ou mais caracteres alfanuméricos (`\w*`);
    - a função retorna uma lista com todas as correspondências;

    **Saída**
    ```
    Palavras encontradas: ['Python', 'Popular', 'Guido', 'Rossum']
    ```

### exercícios `re.findall()`

<details>
<summary>Lista de Exercícios</summary>

1. Crie uma string que contenha várias cores separadas por espaços. Utilize a função `findall()` para encontrar todas as ocorrências da palavra "azul" na string.
1. Escreva uma string que contenha os nomes de frutas separados por vírgulas. Use `findall()` para localizar todas as ocorrências da fruta "maçã".
1. Defina uma string que contenha uma sequência de palavras relacionadas a tecnologia. Utilize `findall()` para encontrar todas as ocorrências da palavra "computador".
1. Crie uma string que descreva as suas atividades diárias. Utilize `findall()` para listar todas as ocorrências da palavra "trabalho" na descrição.
1. Escreva uma string que contenha várias cidades separadas por ponto e vírgula. Use `findall()` para localizar todas as ocorrências da cidade "Paris".
1. Defina uma string que contenha uma sequência de nomes de pessoas. Utilize `findall()` para encontrar todas as ocorrências do nome "Ana".
1. Crie uma string que contenha o nome de várias marcas de carros. Use `findall()` para localizar todas as ocorrências da marca "Toyota".
1. Escreva uma string que contenha a letra de uma música. Utilize `findall()` para listar todas as ocorrências da palavra "amor" na letra.
1. Defina uma string que contenha os títulos de livros separados por barras. Use `findall()` para localizar todas as ocorrências do título "O Hobbit".
1. Crie uma string que represente uma lista de ingredientes para uma receita. Utilize `findall()` para encontrar todas as ocorrências da palavra "farinha" na lista.

</details>

---

### `re.sub()`

A função `re.sub()` substitui todas as ocorrências de um padrão em uma string por um valor especificado. É muito útil quando se precisa fazer substituições complexas em um texto.

```python
re.sub(padrão, substituição, string, contagem=0, flags=0)
```

- **`padrão`** : o padrão (expressão regular) que você quer substituir;
- **`substituição`** : o texto ou valor que substituirá o padrão;
- **`string`** : a string onde será feita a substituição;
- **`contagem`** (opcional) : o número máximo de substituições a serem feitas. O valor padrão é 0, o que significa substituir todas as ocorrências;
- **`flags`** (opcional) : modificadores de comportamento das expressões regulares;

1. **exemplo substituindo uma palavra por outra**

    ```python
    import re

    # texto para fazer a substituição
    texto = "Eu adoro maçã. A maçã é minha fruta favorita."

    # substituindo "maçã" por "banana"
    resultado = re.sub(r"maçã", "banana", texto)

    # exibindo o resultado
    print("Texto após substituição:", resultado)
    ```

    **Explicação**
    - **`re.sub(r"maçã", "banana", texto)`** : substitui todas as ocorrências da palavra "maçã" por "banana";

    **Saída**
    ```
    Texto após substituição: Eu adoro banana. A banana é minha fruta favorita.
    ```

1. **exemplo limitando o número de substituições**

    ```python
    # substituindo "maçã" por "banana", mas limitando a 1 substituição
    resultado = re.sub(r"maçã", "banana", texto, count=1)

    # exibindo o resultado
    print("Texto após substituição:", resultado)
    ```

    **Explicação**
    - **`count=1`** : limita a substituição a apenas uma ocorrência;

    **Saída**
    ```
    Texto após substituição: Eu adoro banana. A maçã é minha fruta favorita.
    ```

1. **exemplo substituindo números por uma string fixa**

    Veja a substituição de todos os números em uma string pela palavra "número".

    ```python
    # texto com números
    texto = "O preço é 100 reais e o desconto é 15%."

    # substituindo números por "número"
    resultado = re.sub(r"\d+", "número", texto)

    # exibindo o resultado
    print("Texto após substituição:", resultado)
    ```

    **Explicação**
    - **`\d+`** : esse padrão encontra qualquer sequência de dígitos;
    - a função `re.sub()` substitui todos os números pela palavra "número";

    **Saída**
    ```
    Texto após substituição: O preço é número reais e o desconto é número%.
    ```

1. **exemplo usando uma função na substituição**

    Pode-se usar uma função para definir a lógica de substituição.

    ```python
    # Função que dobra o valor numérico encontrado
    def dobra(match):
        return str(int(match.group()) * 2)

    # texto com números
    texto = "O preço é 100 reais e o desconto é 15%."

    # substituindo números pela versão dobrada
    resultado = re.sub(r"\d+", dobra, texto)

    # exibindo o resultado
    print("Texto após substituição:", resultado)
    ```

    **Explicação**
    - **`dobra(match)`** : essa função recebe o objeto de correspondência e retorna o número dobrado;
    - **`re.sub(r"\d+", dobra, texto)`** : substitui todos os números pela versão dobrada deles;

    **Saída**
    ```
    Texto após substituição: O preço é 200 reais e o desconto é 30%.
    ```

### exercícios `re.sub()`

<details>
<summary>Lista de Exercícios</summary>

1. Crie uma string com uma frase que mencione a palavra "cachorro". Utilize a função `sub()` para substituir "cachorro" por "gato".
1. Escreva uma string que contenha o nome de várias frutas, separadas por vírgulas. Use `sub()` para substituir todas as ocorrências de "maçã" por "laranja".
1. Defina uma string que contenha a palavra "vermelho" repetida várias vezes. Utilize `sub()` para substituir "vermelho" por "azul".
1. Crie uma string que descreva um país famoso. Utilize `sub()` para substituir o nome do país por "Brasil".
1. Escreva uma string com o nome de uma cidade repetido duas vezes. Use `sub()` para substituir a primeira ocorrência da cidade por outra cidade de sua escolha.
1. Defina uma string que contenha uma frase sobre uma comida favorita. Utilize `sub()` para substituir o nome da comida por outra de sua escolha.
1. Crie uma string com o nome de vários filmes separados por espaços. Utilize `sub()` para substituir o nome de um filme específico por "Star Wars".
1. Escreva uma string com o nome de uma empresa várias vezes. Use `sub()` para substituir o nome da empresa por outro nome, como "TechCorp".
1. Defina uma string que contenha o nome de diferentes países. Utilize `sub()` para substituir o nome de um país por "Japão".
1. Crie uma string que contenha a descrição de um carro. Use `sub()` para substituir o nome do carro por outro modelo de sua escolha.

</details>

---

### `re.split()`

A função `re.split()` divide uma string em partes com base em um padrão de expressão regular. Ela funciona de maneira similar ao método `split()` de strings, mas permite o uso de padrões mais complexos.

```python
re.split(padrão, string, maxsplit=0, flags=0)
```

- **`padrão`** : o padrão (expressão regular) que define onde a string será dividida;
- **`string`** : a string que será dividida;
- **`maxsplit`** (opcional) : define o número máximo de divisões a serem feitas. O valor padrão é 0, o que significa dividir em todas as ocorrências do padrão;
- **`flags`** (opcional) : modificadores de comportamento das expressões regulares;

1. **exemplo dividindo uma string por espaços**

    ```python
    # texto para dividir
    texto = "Eu gosto de programar em Python."

    # dividindo a string por espaços
    resultado = re.split(r"\s+", texto)

    # exibindo o resultado
    print("Texto dividido:", resultado)
    ```

    **Explicação**
    - **`\s+`** : o padrão corresponde a um ou mais espaços em branco;
    - a função divide o texto em palavras, removendo os espaços;

    **Saída**
    ```
    Texto dividido: ['Eu', 'gosto', 'de', 'programar', 'em', 'Python.']
    ```

1. **exemplo dividindo uma string por números**

    Veja a divisão de uma string sempre que encontrar um número.

    ```python
    # texto com números
    texto = "Produto1 custa 100 reais e Produto2 custa 150 reais."

    # dividindo a string por números
    resultado = re.split(r"\d+", texto)

    # exibindo o resultado
    print("Texto dividido:", resultado)
    ```

    **Explicação**
    - **`\d+`** : o padrão encontra uma sequência de dígitos;
    - a função divide a string sempre que encontra um número;

    **Saída**
    ```
    Texto dividido: ['Produto', ' custa ', ' reais e Produto', ' custa ', ' reais.']
    ```

1. **exemplo limitando o número de divisões**

    Pode-se controlar quantas vezes a divisão será feita usando o parâmetro `maxsplit`.

    ```python
    # dividindo a string por espaços, mas limitando a 2 divisões
    resultado = re.split(r"\s+", texto, maxsplit=2)

    # exibindo o resultado
    print("Texto dividido:", resultado)
    ```

    **Explicação**
    - **`maxsplit=2`** : limita o número de divisões a 2;

    **Saída**
    ```
    Texto dividido: ['Produto1', 'custa', '100 reais e Produto2 custa 150 reais.']
    ```

1. **exemplo dividindo por pontuação**

    Agora, veja a divisão de uma string com base nos sinais de pontuação `!?.`.

    ```python
    # texto com pontuação
    texto = "Olá! Como você está? Eu estou bem."

    # dividindo a string por pontuação
    resultado = re.split(r"[!?.]+", texto)

    # exibindo o resultado
    print("Texto dividido:", resultado)
    ```

    **Explicação**
    - **`[!?.]+`** : o padrão corresponde a um ou mais caracteres de pontuação (`!`, `?`, ou `.`);
    - a função divide a string sempre que encontra um desses sinais;

    **Saída**
    ```
    Texto dividido: ['Olá', ' Como você está', ' Eu estou bem', '']
    ```

### exercícios `re.split()`

<details>
<summary>Lista de Exercícios</summary>

1. Crie uma string que contenha uma frase com várias palavras separadas por espaços. Utilize a função `split()` para dividir a string em uma lista de palavras.
1. Escreva uma string que contenha nomes de frutas separados por vírgulas. Use `split()` para separar as frutas e formar uma lista.
1. Defina uma string com uma lista de cidades separadas por ponto e vírgula. Utilize `split()` para separar cada cidade.
1. Crie uma string que contenha uma data no formato "dd/mm/yyyy". Use `split()` para separar o dia, o mês e o ano.
1. Escreva uma string com vários números de telefone separados por traços. Utilize `split()` para dividir os números em partes.
1. Defina uma string que contenha uma frase, e use `split()` para dividir a frase em uma lista de palavras usando como delimitador a letra "a".
1. Crie uma string com um parágrafo composto por várias frases separadas por ponto final. Use `split()` para separar o parágrafo em frases.
1. Escreva uma string que contenha várias palavras separadas por dois pontos. Utilize `split()` para criar uma lista de palavras.
1. Defina uma string que contenha um caminho de arquivo no formato "C:/pasta/subpasta/arquivo.txt". Utilize `split()` para separar as partes do caminho usando a barra ("/").
1. Crie uma string que contenha uma frase com palavras separadas por múltiplos espaços. Utilize `split()` sem passar nenhum argumento para dividir as palavras, removendo os espaços extras.

</details>

---

### `re.compile()`

A função `re.compile()` permite **compilar uma expressão regular** em um objeto de padrão reutilizável. Isso é particularmente útil quando se precisa usar a mesma expressão regular várias vezes no código, pois melhora a performance, evitando recompilar a expressão em cada uso.

```python
padrão_compilado = re.compile(padrão, flags=0)
```

- **`padrão`** : a expressão regular que você quer compilar;
- **`flags`** : parâmetro opcional para modificar o comportamento da expressão regular, como `re.IGNORECASE` para ignorar a diferença entre maiúsculas e minúsculas;

1. **exemplo compilando e reutilizando uma expressão regular**

    ```python
    import re

    # compilando o padrão para encontrar números
    padrão_números = re.compile(r"\d+")

    # texto para buscar
    texto = "O produto custa 250 reais e o desconto é de 10%."

    # usando o padrão compilado para encontrar todos os números
    resultado = padrão_números.findall(texto)

    # exibindo as correspondências
    print("Números encontrados:", resultado)
    ```

    **Explicação**
    - **`re.compile(r"\d+")`** : compila o padrão que encontra uma sequência de dígitos;
    - **`padrão_números.findall(texto)`** : usa o objeto compilado para encontrar todos os números no texto;

    **Saída**
    ```
    Números encontrados: ['250', '10']
    ```

    Aqui, o padrão compilado pode ser reutilizado várias vezes, sem precisar recompilar a expressão regular.

1. **exemplo melhorando a performance com `re.compile()`**

    Se for necessário aplicar o mesmo padrão várias vezes, `re.compile()` ajuda a melhorar a performance.

    ```python
    # compilando o padrão para encontrar palavras
    padrão_palavras = re.compile(r"\b\w+\b")

    # texto para busca
    texto = "Python é uma linguagem versátil e poderosa."

    # usando o padrão compilado várias vezes
    resultado1 = padrão_palavras.findall(texto)
    resultado2 = padrão_palavras.search(texto)
    resultado3 = padrão_palavras.sub("LINGUAGEM", texto)

    # exibindo os resultados
    print("Todas as palavras:", resultado1)
    print("Primeira palavra encontrada:", resultado2.group())
    print("Texto após substituição:", resultado3)
    ```

    **Explicação**
    - **`padrão_palavras.findall()`** : encontra todas as palavras;
    - **`padrão_palavras.search()`** : encontra a primeira palavra;
    - **`padrão_palavras.sub()`** : substitui todas as palavras pelo termo "LINGUAGEM";

    **Saída**
    ```
    Todas as palavras: ['Python', 'é', 'uma', 'linguagem', 'versátil', 'e', 'poderosa']
    Primeira palavra encontrada: Python
    Texto após substituição: LINGUAGEM LINGUAGEM LINGUAGEM LINGUAGEM LINGUAGEM LINGUAGEM LINGUAGEM
    ```

    Ao usar o padrão compilado, a busca é mais eficiente, especialmente em situações com muitas operações repetidas.

1. **exemplo usando flags com `re.compile()`**

    Pode-se adicionar **flags** ao compilar a expressão, como ignorar maiúsculas e minúsculas (`re.IGNORECASE`).

    ```python
    # compilando o padrão com a flag IGNORECASE
    padrão_ignorecase = re.compile(r"python", re.IGNORECASE)

    # texto com diferentes variações de capitalização
    texto = "Python é popular. python é versátil. PYTHON é poderoso."

    # encontrando todas as correspondências, ignorando maiúsculas/minúsculas
    resultado = padrão_ignorecase.findall(texto)

    # exibindo o resultado
    print("Correspondências encontradas:", resultado)
    ```

    **Explicação**
    - **`re.compile(r"python", re.IGNORECASE)`** : compila o padrão para encontrar "python" ignorando a capitalização;
    - **`padrão_ignorecase.findall(texto)`** : encontra todas as ocorrências, independentemente de maiúsculas e minúsculas;

    **Saída**
    ```
    Correspondências encontradas: ['Python', 'python', 'PYTHON']
    ```

### exercícios `re.compile()`

<details>
<summary>Lista de Exercícios</summary>

1. Crie uma expressão regular que busque por uma palavra específica dentro de uma string. Use `compile()` para compilar a expressão e, em seguida, aplique-a para verificar se a palavra "Python" está presente na frase "Estou aprendendo Python!".
1. Defina uma expressão regular que encontre todas as ocorrências de uma determinada palavra em um texto. Utilize `compile()` para compilar a expressão e, em seguida, aplique-a em uma string que contenha a palavra "banana" várias vezes.
1. Escreva uma expressão regular para verificar se uma string começa com um número. Use `compile()` para compilar a expressão e teste-a em diferentes strings como "123abc" e "abc123".
1. Crie uma expressão regular que valide um endereço de e-mail simples. Utilize `compile()` para compilar a expressão e aplique-a para verificar se "exemplo@email.com" é um e-mail válido.
1. Defina uma expressão regular para encontrar todas as ocorrências de um número em um texto. Use `compile()` para compilar a expressão e aplique-a a uma string que contenha várias sequências numéricas, como "Telefone: 1234, Código: 5678".
1. Crie uma expressão regular que busque por palavras que terminem com "ing". Compile a expressão usando `compile()` e aplique-a em uma lista de palavras, como "running", "playing", "sitting".
1. Escreva uma expressão regular para verificar se uma string contém apenas letras maiúsculas. Use `compile()` para compilar a expressão e aplique-a a strings como "HELLO" e "Hello".
1. Defina uma expressão regular que verifique se uma string contém um número específico de dígitos. Utilize `compile()` para compilar a expressão e teste-a em strings como "12345" e "123".
1. Crie uma expressão regular que localize todas as ocorrências de palavras que comecem com a letra "a". Utilize `compile()` para compilar a expressão e aplique-a em uma string contendo várias palavras, como "apple, banana, apricot".
1. Escreva uma expressão regular para validar um número de telefone no formato "xxx-xxx-xxxx". Use `compile()` para compilar a expressão e aplique-a a uma string como "123-456-7890".

</details>

---

### `re.escape()`

A função `re.escape()` escapa todos os caracteres especiais em uma string, tornando-os literais. Isso é útil quando se precisa lidar com strings que contêm caracteres especiais de regex (como `.` ou `*`), mas deseja tratá-los como caracteres normais e não como parte da sintaxe de expressões regulares.

```python
string_escapada = re.escape(string)
```

- **`string`** : a string que será escapada, ou seja, os caracteres especiais serão precedidos por uma barra invertida (`\`), para que sejam tratados como literais;

1. **exemplo escapando caracteres especiais**

    ```python
    # texto com caracteres especiais
    texto = "Preço: 100$ (desconto de 10%)."

    # escapando os caracteres especiais
    texto_escapado = re.escape(texto)

    # exibindo o texto escapado
    print("Texto escapado:", texto_escapado)
    ```

    **Explicação**
    - **`re.escape(texto)`** : escapa todos os caracteres especiais presentes no texto, como `$`, `(`, `)` e `%`, transformando-os em literais;

    **Saída**
    ```
    Texto escapado: Preço:\ 100\$\ \(desconto\ de\ 10%\)\.
    ```

    Aqui, todos os caracteres que têm significados especiais em expressões regulares (como `$`, `(`, `)`, `%`, etc.) são precedidos por uma barra invertida (`\`), tornando-os literais.

1. **exemplo usando `re.escape()` em um padrão de expressão regular**

    Quando se quer usar uma string contendo caracteres especiais como parte de um padrão literal em uma expressão regular, `re.escape()` é muito útil.

    ```python
    # texto e padrão que queremos buscar
    texto = "O arquivo data.log foi criado com sucesso."

    # escapando o ponto (.) no nome do arquivo
    padrão = re.escape("data.log")

    # Procurando o padrão escapado
    resultado = re.search(padrão, texto)

    if resultado:
        print("Padrão encontrado:", resultado.group())
    else:
        print("Padrão não encontrado.")
    ```

    **Explicação**
    - **`re.escape("data.log")`** : escapa o ponto (`.`), que normalmente tem um significado especial (corresponde a qualquer caractere);
    - **`re.search(padrão, texto)`** : procura pela string literal "data.log", em vez de tratar o `.` como um caractere coringa;

    **Saída**
    ```
    Padrão encontrado: data.log
    ```

    Aqui, o `.` é escapado para que ele seja tratado como um literal, e a busca encontra a correspondência exata da string "data.log".

1. **exemplo comparando uso com e sem `re.escape()`**

    Veja o que acontece quando se usa ou não `re.escape()` em um padrão com caracteres especiais.

    ```python
    import re

    # Texto para fazer a busca
    texto = "O arquivo dataXlog foi criado com sucesso."

    # Sem usar re.escape (o ponto é tratado como caractere coringa)
    resultado_sem_escape = re.search(r"data.log", texto)

    # Usando re.escape para tratar o ponto como literal
    padrão_escapado = re.escape("data.log")
    resultado_com_escape = re.search(padrão_escapado, texto)

    print("Sem re.escape:", resultado_sem_escape.group() if resultado_sem_escape else "Não encontrado")
    print("Com re.escape:", resultado_com_escape.group() if resultado_com_escape else "Não encontrado")

    ```

    **Explicação**
    - **Sem `re.escape()`** : o ponto (`.`) é tratado como coringa, correspondendo a qualquer caractere;
    - **Com `re.escape()`** : o ponto é tratado como um literal;

    **Saída**
    ```
    Sem re.escape: data.log
    Com re.escape: Não encontrado
    ```

    Neste caso, ambos os métodos funcionam, mas se houvesse outro caractere no lugar do ponto, a busca sem `re.escape()` poderia gerar resultados indesejados.

### exercícios `re.escape()`

<details>
<summary>Lista de Exercícios</summary>

1. Escreva uma string que contenha caracteres especiais como ".", "*", "+", e "?". Utilize a função `escape()` para gerar uma versão da string onde esses caracteres possam ser tratados literalmente em uma expressão regular.
1. Crie uma string que contenha barras invertidas ("\") e aplique a função `escape()` para transformar essa string em um formato seguro para uso em expressões regulares.
1. Defina uma string que contenha parênteses, colchetes e chaves. Utilize a função `escape()` para garantir que todos esses caracteres sejam tratados de forma literal em uma expressão regular.
1. Escreva uma string que inclua uma sequência de símbolos como "$", "^", e "|". Aplique `escape()` para assegurar que esses símbolos não sejam interpretados como metacaracteres quando usados em uma expressão regular.
1. Crie uma string contendo uma frase que inclua "?", ".", e "+" em seu texto. Utilize a função `escape()` para transformar essa frase em uma versão segura para uso em busca de padrões literais.
1. Escreva uma expressão regular que inclua o caractere "+" e use a função `escape()` para garantir que o caractere "+" seja tratado como literal ao invés de metacaractere.
1. Defina uma string que contenha um caminho de arquivo do tipo "C:\pasta\subpasta\arquivo.txt". Aplique `escape()` para permitir que esse caminho seja utilizado como literal em uma expressão regular.
1. Crie uma string que contenha o símbolo "@" e outros caracteres especiais de um endereço de e-mail. Use a função `escape()` para garantir que todos os caracteres sejam tratados literalmente.
1. Escreva uma string que contenha o texto "2+2=4" e utilize a função `escape()` para garantir que o símbolo "+" seja tratado de forma literal em uma expressão regular.
1. Defina uma string com caracteres como "*", "(", e ")", utilizados em uma fórmula matemática. Aplique a função `escape()` para tornar a string segura para busca literal usando expressões regulares.

</details>

---

## metacaracteres

### `.` (ponto)

O metacaractere `.` (ponto) em expressões regulares corresponde a **qualquer caractere**, exceto quebras de linha (por padrão). Isso significa que ele pode corresponder a letras, números, espaços ou qualquer outro símbolo, com exceção de uma nova linha.

1. **exemplo encontrar qualquer caractere**

    Veja o uso do `.` para encontrar qualquer caractere presente em uma posição específica.

    ```python
    import re

    # texto de exemplo
    texto = "A B C D E"

    # usando o ponto (.) para encontrar qualquer caractere (menos quebras de linha)
    resultado = re.findall(r"A.B", texto)

    # exibindo o resultado
    print("Resultado com '.':", resultado)
    ```

    **Explicação**
    - **`A.B`** : o padrão encontra "A", seguido de **qualquer caractere** (devido ao `.`), seguido de "B";
    - o padrão encontra a combinação "A B";

    **Saída**
    ```
    Resultado com '.': ['A B']
    ```

1. **exemplo usando o `.` com `re.split()`**

    ```python
    # texto de exemplo
    texto = "Palavra1 Palavra2 Palavra3"

    # dividindo por qualquer caractere (exceto nova linha)
    resultado = re.split(r"r.", texto)

    # exibindo o resultado
    print("Resultado de re.split() com '.':", resultado)
    ```

    **Explicação**
    - **`r.l`** : encontra qualquer sequência de "r", seguido de qualquer caractere (`.`), seguido de "l";
    - o `split()` divide o texto quando encontra esse padrão;

    **Saída**
    ```
    Resultado de re.split() com '.': ['Pa', 'vra1 Pa', 'vra2 Pa', 'vra3']
    ```

1. **exemplo substituindo caracteres com `re.sub()`**

    ```python
    # texto de exemplo
    texto = "123 abc !@#"

    # qualquer caractere (.) seguido por um não número será substituído por "X"
    resultado = re.sub(r".\D", "XX", texto)

    # exibindo o resultado
    print("Resultado de re.sub() com '.':", resultado)
    ```

    **Explicação**
    - o `.` encontra qualquer caractere, e o `re.sub()` substitui todos os caracteres por "X";

    **Saída**
    ```
    Resultado de re.sub() com '.': 12XXXXXXXX#
    ```

### exercícios `.`

<details>
<summary>Lista de Exercícios</summary>

1. Crie uma expressão regular que utilize o metacaractere ponto (`.`) para encontrar qualquer caractere entre duas letras "a". Aplique essa expressão à string "aba aca ada" e veja o que é retornado.
1. Escreva uma expressão regular que encontre todas as ocorrências de três caracteres consecutivos em uma string, onde o caractere do meio pode ser qualquer um. Utilize `.` para isso e aplique à string "abc 123 xyz".
1. Defina uma expressão regular que busque qualquer caractere antes e depois de uma vogal. Use o ponto (`.`) para representar os caracteres desconhecidos e aplique essa expressão à frase "o rato roeu a roupa".
1. Escreva uma expressão regular que utilize `.` para encontrar qualquer sequência de três caracteres, onde o primeiro e o último sejam números, e o caractere do meio pode ser qualquer um. Teste com a string "2a3 4+5 6!7".
1. Crie uma expressão regular que utilize o ponto (`.`) para localizar qualquer palavra de quatro caracteres em uma string. Aplique-a na frase "hoje faz sol e vou correr".
1. Defina uma expressão regular que busque por padrões onde o primeiro caractere é "c", o último é "o", e o caractere do meio pode ser qualquer um. Aplique à string "cao cto cno cqo".
1. Escreva uma expressão regular que utilize `.` para substituir todos os caracteres em uma senha fictícia, como "p@ssw0rd123", por asteriscos (*), exceto os números.
1. Crie uma expressão regular que busque por qualquer caractere que venha logo antes de um número. Utilize o metacaractere ponto (`.`) para representar o caractere desconhecido e aplique na string "x1 y2 z3".
1. Defina uma expressão regular que encontre qualquer palavra que tenha exatamente cinco letras, sendo a segunda uma vogal. Use `.` para os outros caracteres e aplique na frase "Python é fácil e divertido".
1. Escreva uma expressão regular que utilize o ponto (`.`) para encontrar todas as ocorrências onde o primeiro caractere de uma palavra seja "p", o último seja "r", e o caractere do meio pode ser qualquer um. Teste com a string "por par pir pur per".

</details>

---

### `^` (circunflexo)

O metacaractere `^` é usado para indicar o **início de uma string** ou linha (dependendo das flags usadas). Ele verifica se a string ou linha começa com um determinado padrão.

1. **exemplo verificar o início de uma string com `re.match()`**

    ```python
    # texto de exemplo
    texto = "Python é uma linguagem poderosa."

    # verificando se a string começa com "Python"
    resultado = re.match(r"^Python", texto)

    # exibindo o resultado
    if resultado:
        print("A string começa com 'Python'")
    else:
        print("A string não começa com 'Python'")
    ```

    **Explicação**
    - **`^Python`** : o `^` garante que "Python" só será correspondido se estiver no início da string;

    **Saída**
    ```
    A string começa com 'Python'
    ```

1. **exemplo usando `^` com `re.findall()`**

    ```python
    # texto de exemplo
    texto = "Python é poderoso.\npython é versátil."

    # encontrando "python" no início de cada linha (ignorando maiúsculas/minúsculas)
    resultado = re.findall(r"^python", texto, flags=re.IGNORECASE | re.MULTILINE)

    # exibindo o resultado
    print("Correspondências encontradas no início de linhas:", resultado)
    ```

    **Explicação**
    - **`^python`** : o `^` busca "python" no início da string. A flag `re.MULTILINE` permite que a busca seja feita no início de cada linha (não apenas da string inteira);
    - a flag `re.IGNORECASE` ignora a diferença entre maiúsculas e minúsculas;

    **Saída**
    ```
    Correspondências encontradas no início de linhas: ['Python', 'python']
    ```

1. **exemplo usando `^` para garantir o início da string com `re.sub()`**

    ```python
    # texto de exemplo
    texto = "Python é uma linguagem poderosa."

    # substituindo "Python" no início por "Java"
    resultado = re.sub(r"^Python", "Java", texto)

    # exibindo o resultado
    print("Resultado de re.sub() com '^':", resultado)
    ```

    **Explicação**
    - o padrão `^Python` só substitui "Python" se ele aparecer no início da string;

    **Saída**
    ```
    Resultado de re.sub() com '^': Java é uma linguagem poderosa.
    ```

### exercícios `^`

<details>
<summary>Lista de Exercícios</summary>

1. Crie uma expressão regular que utilize o metacaractere circunflexo (`^`) para verificar se uma string começa com a palavra "Olá". Teste a expressão com a frase "Olá, mundo!".
1. Escreva uma expressão regular que utilize `^` para verificar se uma string começa com um número. Aplique essa expressão à string "123abc".
1. Defina uma expressão regular que utilize `^` para verificar se uma string começa com a letra "P". Teste-a com as palavras "Python" e "java".
1. Crie uma expressão regular que utilize `^` para garantir que uma frase começa com a palavra "Era". Teste a expressão com a frase "Era uma vez".
1. Escreva uma expressão regular que utilize `^` para verificar se uma string começa com um símbolo como "@" ou "#". Teste-a com a string "@usuario123".
1. Defina uma expressão regular que utilize `^` para verificar se uma string começa com uma letra maiúscula. Aplique essa expressão à frase "Hoje é um bom dia".
1. Crie uma expressão regular que utilize `^` para verificar se uma string começa com a sequência "abc". Teste com a string "abcdef" e "xyzabc".
1. Escreva uma expressão regular que utilize `^` para verificar se uma string começa com um dígito (0-9). Aplique a expressão à string "8 maçãs".
1. Defina uma expressão regular que utilize `^` para verificar se uma string começa com a sequência "http". Aplique-a em uma URL como "http://example.com".
1. Crie uma expressão regular que utilize `^` para verificar se uma string começa com qualquer palavra de quatro letras. Aplique a expressão na frase "Lindo dia hoje!".

</details>

---

### `$` (cifrão)

O metacaractere `$` é usado para verificar se um padrão está presente no **final de uma string** ou linha (dependendo das flags).

1. **exemplo verificar o final de uma string com `re.search()`**

    ```python
    # texto de exemplo
    texto = "A linguagem Python é poderosa."

    # verificando se a string termina com "poderosa."
    resultado = re.search(r"poderosa\.$", texto)

    # exibindo o resultado
    if resultado:
        print("A string termina com 'poderosa.'")
    else:
        print("A string não termina com 'poderosa.'")
    ```

    **Explicação**
    - **`poderosa\.$`** : o padrão "poderosa." só será encontrado se estiver no final da string, graças ao `$`;

    **Saída**
    ```
    A string termina com 'poderosa.'
    ```

1. **exemplo usando `$` com `re.findall()`**

    ```python
    # texto de exemplo
    texto = "Eu gosto de Python.\nAmo programar em Python."

    # encontrando "Python" no final de cada linha
    resultado = re.findall(r"Python\.$", texto, flags=re.MULTILINE)

    # exibindo o resultado
    print("Correspondências encontradas no final de linhas:", resultado)
    ```

    **Explicação**
    - **`Python\.$`** : o padrão encontra "Python." no final de cada linha. A flag `re.MULTILINE` permite a verificação em cada linha, não apenas no final da string;

    **Saída**
    ```
    Correspondências encontradas no final de linhas: ['Python.']
    ```

1. **exemplo substituindo um padrão no final da string com `re.sub()`**

    ```python
    # texto de exemplo
    texto = "Eu adoro Python."

    # substituindo "Python." no final por "Java."
    resultado = re.sub(r"Python\.$", "Java.", texto)

    # exibindo o resultado
    print("Resultado de re.sub() com '$':", resultado)
    ```

    **Explicação**
    - o padrão `Python\.$` substitui "Python." por "Java." somente se "Python." estiver no final da string;

    **Saída**
    ```
    Resultado de re.sub() com '$': Eu adoro Java.
    ```

### exercícios `$`

<details>
<summary>Lista de Exercícios</summary>

1. Crie uma expressão regular que utilize o metacaractere cifrão (`$`) para verificar se uma string termina com a palavra "fim". Teste com a string "Essa é a última palavra: fim".
1. Escreva uma expressão regular que use o cifrão (`$`) para verificar se uma string termina com um número. Aplique à string "O total é 42".
1. Defina uma expressão regular que utilize o metacaractere `$` para verificar se uma string termina com a sequência "123". Teste com a string "Senha: abc123".
1. Crie uma expressão regular que utilize `$` para verificar se uma string termina com uma letra maiúscula. Aplique à frase "Hoje é um bom Dia".
1. Escreva uma expressão regular que utilize `$` para verificar se uma string termina com um ponto final. Teste com a frase "Este é o fim.".
1. Defina uma expressão regular que utilize `$` para verificar se uma string termina com a palavra "Python". Aplique à string "Eu estou aprendendo Python".
1. Crie uma expressão regular que utilize `$` para verificar se uma string termina com um espaço em branco. Teste com a frase "Aqui tem um espaço ".
1. Escreva uma expressão regular que utilize `$` para verificar se uma string termina com um símbolo como "!" ou "?". Aplique à string "Você está bem?".
1. Defina uma expressão regular que utilize `$` para verificar se uma string termina com três letras consecutivas. Teste com a string "finalabc".
1. Crie uma expressão regular que utilize `$` para verificar se uma string termina com um caractere numérico. Teste com a string "O resultado final foi 9".

</details>

---

### `*` (asterisco)

O metacaractere `*` significa **"zero ou mais ocorrências"** do padrão que o precede. Isso significa que o padrão anterior pode aparecer repetidamente (incluindo a possibilidade de não aparecer).

1. **exemplo encontrando padrões com `*`**

    ```python
    import re

    # texto de exemplo
    texto = "Aaaahhh! Isso é incrível!"

    # padrão : "a" seguido de zero ou mais "a"
    resultado = re.findall(r"Aa*", texto)

    # exibindo o resultado
    print("Resultado com '*':", resultado)
    ```

    **Explicação**
    - **`Aa*`** : procura por um "A" seguido de zero ou mais letras "a". Isso significa que ele pode encontrar "A", "Aa", "Aaa", etc;

    **Saída**
    ```
    Resultado com '*': ['Aaaa']
    ```

1. **exemplo usando `*` com `re.search()`**

    ```python
    # texto de exemplo
    texto = "123 abc 456 def"

    # Procurando dígitos seguidos de zero ou mais espaços
    resultado = re.search(r"\d*\s*", texto)

    # exibindo o resultado
    print("Resultado com '*':", resultado.group())
    ```

    **Explicação**
    - **`\d*\s*`** : encontra zero ou mais dígitos seguidos de zero ou mais espaços;

    **Saída**
    ```
    Resultado com '*': 123
    ```

    Aqui, ele encontra a sequência "123 " (três dígitos e um espaço).

1. **exemplo substituindo com `*` usando `re.sub()`**

    ```python
    # texto de exemplo
    texto = "Gatoooo"

    # substituindo "o" repetido por "o"
    resultado = re.sub(r"o*", "o", texto)

    # exibindo o resultado
    print("Resultado de re.sub() com '*':", resultado)
    ```

    **Explicação**
    - **`o*`** : substitui qualquer sequência de "o" (zero ou mais) por apenas um "o";

    **Saída**
    ```
    Resultado de re.sub() com '*': Gato
    ```

### exercícios `*`

<details>
<summary>Lista de Exercícios</summary>

1. Crie uma expressão regular que utilize o metacaractere asterisco (`*`) para encontrar ocorrências de uma letra seguida por zero ou mais letras "a". Teste com a string "baaa ba b".
1. Escreva uma expressão regular que utilize `*` para encontrar palavras que tenham a letra "s" seguida por zero ou mais letras "e". Aplique à string "seu selo sente".
1. Defina uma expressão regular que use `*` para verificar se uma string contém zero ou mais espaços em branco antes de uma palavra. Teste com a string "   exemplo".
1. Crie uma expressão regular que utilize `*` para encontrar sequências de números seguidos por zero ou mais zeros. Aplique à string "120 3000 45000".
1. Escreva uma expressão regular que utilize `*` para encontrar palavras que começam com "a" e podem ter qualquer número de letras depois, incluindo nenhuma. Teste com as palavras "a", "abacaxi", "análise".
1. Defina uma expressão regular que utilize `*` para verificar se uma string contém zero ou mais caracteres antes da palavra "fim". Aplique à string "isso é o fim".
1. Crie uma expressão regular que utilize `*` para encontrar sequências de caracteres que começam com "x" e podem ter zero ou mais caracteres após isso. Teste com "x", "xyz", "xabc".
1. Escreva uma expressão regular que utilize `*` para verificar se uma string contém zero ou mais caracteres especiais antes de um número. Aplique à string "@#1".
1. Defina uma expressão regular que utilize `*` para encontrar palavras que podem ter uma letra "e" no início e qualquer número de letras após isso, incluindo nenhuma. Teste com "e", "elefante", "esperança".
1. Crie uma expressão regular que utilize `*` para verificar se uma string contém zero ou mais vogais seguidas de uma letra "s". Teste com as strings "s", "ass", "ooos".

</details>

---

### `+` (mais)

O metacaractere `+` significa **"uma ou mais ocorrências"** do padrão que o precede. Ao contrário de `*`, o padrão deve aparecer pelo menos uma vez.

1. **exemplo encontrando padrões com `+`**

    ```python
    # texto de exemplo
    texto = "Eu tenho 1000 maçãs."

    # padrão : encontrar um ou mais dígitos seguidos de um espaço
    resultado = re.findall(r"\d+ ", texto)

    # exibindo o resultado
    print("Resultado com '+':", resultado)
    ```

    **Explicação**
    - **`\d+`** : procura por um ou mais dígitos. Isso significa que encontra números inteiros ou sequências de números;

    **Saída**
    ```
    Resultado com '+': ['1000 ']
    ```

1. **exemplo usando `+` para dividir strings com `re.split()`**

    ```python
    # texto de exemplo
    texto = "Palavra123Outra"

    # dividindo o texto por uma ou mais sequências de dígitos
    resultado = re.split(r"\d+", texto)

    # exibindo o resultado
    print("Resultado de re.split() com '+':", resultado)
    ```

    **Explicação**
    - **`\d+`** : divide a string em partes, usando uma ou mais ocorrências de dígitos como separador;

    **Saída**
    ```
    Resultado de re.split() com '+': ['Palavra', 'Outra']
    ```

### exercícios `+`

<details>
<summary>Lista de Exercícios</summary>

1. Crie uma expressão regular que utilize o metacaractere mais (`+`) para encontrar sequências de uma letra "a" seguida por uma ou mais letras "b". Teste com a string "ab, abb, a, aaa".
1. Escreva uma expressão regular que utilize `+` para verificar se uma string contém uma ou mais ocorrências do caractere "x". Aplique à string "xxxy", "xy", e "y".
1. Defina uma expressão regular que utilize `+` para encontrar palavras que começam com a letra "s" e são seguidas por uma ou mais letras "e". Teste com as palavras "se", "selo", "s".
1. Crie uma expressão regular que utilize `+` para verificar se uma string contém uma ou mais dígitos consecutivos. Aplique à string "a123b", "abc", e "456".
1. Escreva uma expressão regular que utilize `+` para encontrar sequências de letras "o" seguidas de uma ou mais letras "k". Teste com a string "ook, oook, ok".
1. Defina uma expressão regular que utilize `+` para verificar se uma string contém uma ou mais vogais seguidas por uma letra "n". Aplique à string "an", "eenn", e "onn".
1. Crie uma expressão regular que utilize `+` para encontrar sequências de caracteres que começam com "m" e são seguidas por uma ou mais letras "a". Teste com "ma", "maa", "m".
1. Escreva uma expressão regular que utilize `+` para verificar se uma string termina com um ou mais caracteres especiais. Aplique à string "abc!!!", "abc", e "abc??".
1. Defina uma expressão regular que utilize `+` para encontrar palavras que começam com a letra "c" e são seguidas por uma ou mais letras "a" ou "e". Teste com "ca", "ceee", "c".
1. Crie uma expressão regular que utilize `+` para verificar se uma string contém uma sequência de uma ou mais letras "r" seguidas de uma letra "s". Teste com "rs", "rrrs", e "r".

</details>

---

### `?` (interrogação)

O metacaractere `?` significa **"zero ou uma ocorrência"** do padrão que o precede. Ou seja, o padrão pode aparecer no máximo uma vez.

1. **exemplo encontrando padrões com `?`**

    ```python
    # texto de exemplo
    texto = "cor ou cor?reto"

    # padrão : encontrar "cor" seguido de uma letra opcional "?"
    resultado = re.findall(r"cor\??", texto)

    # exibindo o resultado
    print("Resultado com '?':", resultado)
    ```

    **Explicação**
    - **`cor\??`** : encontra "cor" seguido de zero ou uma interrogação;

    **Saída**
    ```
    Resultado com '?': ['cor', 'cor?']
    ```

1. **exemplo usando `?` com `re.fullmatch()`**

    ```python
    # texto de exemplo
    texto = "coloor"

    # verificando se o texto corresponde a "colo" seguido de zero ou uma letra "o"
    resultado = re.fullmatch(r"colo?", texto)

    # exibindo o resultado
    if resultado:
        print("Resultado com '?':", resultado.group())
    else:
        print("Nenhuma correspondência.")
    ```

    **Explicação**
    - **`colo?`** : o padrão espera a palavra "col" seguida de zero ou uma letra "o";

    **Saída**
    ```
    Nenhuma correspondência.
    ```

    Aqui, não há correspondência porque a palavra tem duas letras "o", enquanto o `?` permite no máximo uma.

1. **exemplo substituindo padrões opcionais com `re.sub()`**

    ```python
    # texto de exemplo
    texto = "correto"

    # substituindo "r?" por "RR"
    resultado = re.sub(r"r?", "RR", texto)

    # exibindo o resultado
    print("Resultado de re.sub() com '?':", resultado)
    ```

    **Explicação**
    - **`r?`** : o padrão "r?" encontra zero ou uma letra "r", substituindo-a por "RR";

    **Saída**
    ```
    Resultado de re.sub() com '?': RRcoRRRRRRetoRR
    ```

### exercícios `?`

<details>
<summary>Lista de Exercícios</summary>

1. Crie uma expressão regular que utilize o metacaractere interrogação (`?`) para encontrar ocorrências da letra "a" seguida opcionalmente pela letra "b". Teste com a string "a, ab, b, aa".
1. Escreva uma expressão regular que utilize `?` para verificar se uma string contém a letra "x" seguida opcionalmente por "y". Aplique à string "xy", "x", e "y".
1. Defina uma expressão regular que utilize `?` para encontrar palavras que podem ou não ter a letra "e" no final. Teste com as palavras "casa" e "casae".
1. Crie uma expressão regular que utilize `?` para verificar se uma string contém a sequência "ab" seguida opcionalmente por um espaço. Teste com "ab", "ab ", e "abc".
1. Escreva uma expressão regular que utilize `?` para encontrar sequências de dígitos que podem ter um sinal de mais (+) ou menos (-) antes deles. Aplique à string "+123", "-456", e "789".
1. Defina uma expressão regular que utilize `?` para verificar se uma string termina com uma letra "s" ou não. Teste com as palavras "cachorro" e "cachorros".
1. Crie uma expressão regular que utilize `?` para encontrar palavras que começam com "a" e podem ter uma letra "b" logo após. Teste com "a", "ab", "abc".
1. Escreva uma expressão regular que utilize `?` para verificar se uma string contém a letra "c" seguida opcionalmente por uma letra "d". Aplique à string "cd", "c", e "d".
1. Defina uma expressão regular que utilize `?` para encontrar sequências de caracteres que começam com "m" e podem ter uma letra "a" opcionalmente após. Teste com "m", "ma", "mb".
1. Crie uma expressão regular que utilize `?` para verificar se uma string contém uma sequência de uma vogal seguida opcionalmente por uma consoante. Teste com "a", "an", "i", e "it".

</details>

---

### `{}` (chaves)

O metacaractere `{}` é usado para definir **quantificadores específicos** em um padrão. Ele permite determinar quantas vezes o padrão anterior deve ocorrer. Existem três formas principais de usar `{}`:

- **`{n}`** : exatamente `n` ocorrências;
- **`{n,}`** : pelo menos `n` ocorrências;
- **`{n,m}`** : pelo menos `n` e no máximo `m` ocorrências;

1. **exemplo quantidade exata de ocorrências `{n}`**

    ```python
    import re

    # texto de exemplo
    texto = "Oooooops!"

    # padrão : encontrar "O" seguido exatamente de cinco letras "o"
    resultado = re.findall(r"Oo{5}", texto)

    # exibindo o resultado
    print("Resultado com '{5}':", resultado)
    ```

    **Explicação**
    - **`Oo{5}`** : o padrão encontra "O" seguido de exatamente 5 letras "o";

    **Saída**
    ```
    Resultado com '{5}': ['Oooooo']
    ```

1. **exemplo pelo menos `n` ocorrências `{n,}`**

    ```python
    # texto de exemplo
    texto = "Ahhhhh! Que legal!"

    # padrão : encontrar "h" repetido três ou mais vezes
    resultado = re.findall(r"h{3,}", texto)

    # exibindo o resultado
    print("Resultado com '{3,}':", resultado)
    ```

    **Explicação**
    - **`h{3,}`** : procura por três ou mais letras "h" seguidas;

    **Saída**
    ```
    Resultado com '{3,}': ['hhhh']
    ```

1. **exemplo entre `n` e `m` ocorrências `{n,m}`**

    ```python
    # texto de exemplo
    texto = "Hmm... Interessante."

    # padrão : encontrar "m" repetido entre 2 e 4 vezes
    resultado = re.findall(r"m{2,4}", texto)

    # exibindo o resultado
    print("Resultado com '{2,4}':", resultado)
    ```

    **Explicação**
    - **`m{2,4}`** : o padrão encontra "m" repetido entre 2 e 4 vezes;

    **Saída**
    ```
    Resultado com '{2,4}': ['mm']
    ```

### exercícios `{}`

<details>
<summary>Lista de Exercícios</summary>

1. Crie uma expressão regular que utilize o metacaractere chaves (`{}`) para encontrar sequências de exatamente 3 letras "a" consecutivas. Teste com a string "a aa aaa aaaa".
1. Escreva uma expressão regular que utilize `{}` para encontrar números que tenham exatamente 4 dígitos. Aplique à string "123 4567 8901 12345".
1. Defina uma expressão regular que utilize `{}` para verificar se uma string contém exatamente 2 letras "b" seguidas de qualquer caractere. Teste com a string "bb bbx bbb bbbb".
1. Crie uma expressão regular que utilize `{}` para encontrar palavras que contenham entre 2 e 4 letras "e" consecutivas. Teste com a string "bee beee beeee beeeee".
1. Escreva uma expressão regular que utilize `{}` para encontrar sequências de exatamente 5 números. Aplique à string "12345 67890 12 34567".
1. Defina uma expressão regular que utilize `{}` para encontrar qualquer sequência de 2 a 3 letras "x" seguidas de uma letra "y". Aplique à string "xxxy xxy xy xxxxxy".
1. Crie uma expressão regular que utilize `{}` para encontrar palavras que contenham de 3 a 6 letras "a" consecutivas. Teste com a string "a aa aaa aaaa aaaaaa".
1. Escreva uma expressão regular que utilize `{}` para verificar se uma string contém entre 1 e 3 letras "m" seguidas de qualquer caractere. Aplique à string "m mm mmm mmmm".
1. Defina uma expressão regular que utilize `{}` para encontrar sequências de exatamente 4 ou 5 dígitos. Teste com a string "1234 56789 123 45678".
1. Crie uma expressão regular que utilize `{}` para encontrar qualquer palavra que tenha de 2 a 5 letras "n" seguidas de uma letra "o". Aplique à string "nno nnno nnnno nnnnno".

</details>

---

### `[]` (colchetes)

O metacaractere `[]` define um **conjunto de caracteres**. Ele permite que se especifique um conjunto de caracteres que podem aparecer em uma posição específica na string. Qualquer caractere dentro dos colchetes será aceito para corresponder ao padrão.

1. **exemplo conjunto de caracteres simples**

    ```python
    # texto de exemplo
    texto = "Cão, Gato, Pato"

    # padrão : encontrar qualquer palavra que comece com "C", "G" ou "P"
    resultado = re.findall(r"[CGP]\w+", texto)

    # exibindo o resultado
    print("Resultado com '[CGP]':", resultado)
    ```

    **Explicação**
    - **`[CGP]\w+`** : o padrão encontra qualquer palavra que comece com "C", "G" ou "P";

    **Saída**
    ```
    Resultado com '[CGP]': ['Cão', 'Gato', 'Pato']
    ```

1. **exemplo intervalo de caracteres**

    ```python
    # texto de exemplo
    texto = "123abc456"

    # padrão : encontrar dígitos entre 1 e 3
    resultado = re.findall(r"[1-3]", texto)

    # exibindo o resultado
    print("Resultado com '[1-3]':", resultado)
    ```

    **Explicação**
    - **`[1-3]`** : o padrão encontra qualquer dígito entre 1 e 3;

    **Saída**
    ```
    Resultado com '[1-3]': ['1', '2', '3']
    ```

1. **exemplo negação dentro do conjunto**

    O uso de **`^`** dentro dos colchetes nega o conjunto, ou seja, procura por caracteres **que não** estão no conjunto.

    ```python
    # texto de exemplo
    texto = "123abc456def"

    # padrão : encontrar tudo que não seja um número
    resultado = re.findall(r"[^0-9]+", texto)

    # exibindo o resultado
    print("Resultado com '[^0-9]':", resultado)
    ```

    **Explicação**
    - **`[^0-9]+`** : o padrão encontra sequências de caracteres que **não** sejam números;

    **Saída**
    ```
    Resultado com '[^0-9]': ['abc', 'def']
    ```

1. **exemplo substituindo caracteres usando conjuntos**

    Veja um conjunto de caracteres para substituir todas as vogais por "X".

    ```python
    # texto de exemplo
    texto = "Python é divertido!"

    # substituindo todas as vogais por "X"
    resultado = re.sub(r"[aeiouAEIOU]", "X", texto)

    # exibindo o resultado
    print("Resultado de re.sub() com '[aeiou]':", resultado)
    ```

    **Explicação**
    - **`[aeiouAEIOU]`** : o padrão encontra qualquer vogal (maiúscula ou minúscula) e substitui por "X";

    **Saída**
    ```
    Resultado de re.sub() com '[aeiou]': PythXn é dXvXrtXdX!
    ```

### exercícios `[]`

<details>
<summary>Lista de Exercícios</summary>

1. Crie uma expressão regular que utilize colchetes (`[]`) para encontrar qualquer vogal (a, e, i, o, u) em uma string. Teste com a string "python regex tutorial".
1. Escreva uma expressão regular que utilize colchetes para encontrar qualquer número de 0 a 3. Aplique à string "0123456789".
1. Defina uma expressão regular que utilize colchetes para encontrar qualquer letra maiúscula de "A" a "F". Teste com a string "ABCDEFabcdefGHIJ".
1. Crie uma expressão regular que utilize colchetes para encontrar qualquer caractere que seja um ponto, vírgula ou ponto de exclamação. Aplique à string "Olá, mundo! Tudo bem?".
1. Escreva uma expressão regular que utilize colchetes para encontrar qualquer caractere alfanumérico (letras e números). Teste com a string "abc123!@#".
1. Defina uma expressão regular que utilize colchetes para encontrar qualquer uma das letras "p", "y", ou "t". Aplique à string "python regex tutorial".
1. Crie uma expressão regular que utilize colchetes para encontrar quaisquer dois dígitos consecutivos que estejam entre 5 e 9. Teste com a string "456789".
1. Escreva uma expressão regular que utilize colchetes para encontrar qualquer letra minúscula exceto "a", "e", "i", "o", e "u". Aplique à string "Python Regex".
1. Defina uma expressão regular que utilize colchetes para encontrar qualquer caractere que não seja uma letra ou número (use `[^...]`). Teste com a string "abc123!@#".
1. Crie uma expressão regular que utilize colchetes para encontrar qualquer uma das letras de "a" até "f" e qualquer número de 1 a 4. Aplique à string "abc123def456".

</details>

---

### `()` (parênteses)

Os parênteses **`()`** são usados para **agrupar** partes de uma expressão regular e permitir que sejam tratadas como uma única unidade. Isso também permite **capturar** essas partes da string, possibilitando o uso em substituições e extrações.

1. **exemplo agrupando com `()` para encontrar padrões complexos**

    ```python
    import re

    # texto de exemplo
    texto = "Área de código: +55, número: 12345-6789"

    # padrão : encontrar código de área e número de telefone usando agrupamento
    resultado = re.search(r"(\+\d{2}), número: (\d{5}-\d{4})", texto)

    # exibindo o resultado
    if resultado:
        print("Código de área:", resultado.group(1))
        print("Número de telefone:", resultado.group(2))
    ```

    **Explicação**
    - **`(\+\d{2})`** : captura o código de área, que começa com "+" seguido por dois dígitos;
    - **`(\d{5}-\d{4})`** : captura o número de telefone no formato "12345-6789";
    - **`group(1)` e `group(2)`** : retornam as partes capturadas pelo primeiro e segundo grupo;

    **Saída**
    ```
    Código de área: +55
    Número de telefone: 12345-6789
    ```

1. **exemplo usando grupos com `re.findall()`**

    ```python
    # texto de exemplo
    texto = "ID de produto: A123, B456, C789"

    # padrão : encontrar IDs de produto e capturá-los
    resultado = re.findall(r"([A-Z]\d{3})", texto)

    # exibindo o resultado
    print("IDs de produto encontrados:", resultado)
    ```

    **Explicação**
    - **`([A-Z]\d{3})`** : captura IDs de produto formados por uma letra maiúscula seguida por três dígitos;

    **Saída**
    ```
    IDs de produto encontrados: ['A123', 'B456', 'C789']
    ```

1. **exemplo substituindo com grupos usando `re.sub()`**

    ```python
    # texto de exemplo
    texto = "Preço: 100 dólares"

    # substituindo o valor e capturando a palavra "dólares"
    resultado = re.sub(r"(\d+) (dólares)", r"Valor: \1 \2", texto)

    # exibindo o resultado
    print("Resultado de re.sub() com grupos:", resultado)
    ```

    **Explicação**
    - **`\1`** : refere-se ao primeiro grupo capturado (o valor numérico);
    - **`\2`** : refere-se ao segundo grupo capturado (a palavra "dólares");

    **Saída**
    ```
    Resultado de re.sub() com grupos: Valor: 100 dólares
    ```

### exercícios `()`

<details>
<summary>Lista de Exercícios</summary>

1. Crie uma expressão regular que utilize parênteses (`()`) para capturar a sequência de letras "ab" dentro de uma string. Teste com a string "abc, abcd, efg".
1. Escreva uma expressão regular que utilize parênteses para capturar e extrair o número de uma data no formato "Dia: 25, Mês: 12, Ano: 2024". Aplique à string "Dia: 25, Mês: 12, Ano: 2024".
1. Defina uma expressão regular que utilize parênteses para agrupar e capturar duas palavras consecutivas. Teste com a string "palavra1 palavra2".
1. Crie uma expressão regular que utilize parênteses para capturar e inverter o nome e sobrenome em uma string no formato "Sobrenome, Nome". Aplique à string "Silva, João".
1. Escreva uma expressão regular que utilize parênteses para capturar um número de telefone no formato "(XX) XXXX-XXXX". Teste com a string "(21) 9876-1234".
1. Defina uma expressão regular que utilize parênteses para capturar grupos de três letras seguidas por um espaço. Aplique à string "abc def ghi".
1. Crie uma expressão regular que utilize parênteses para capturar a sequência de um código postal no formato "XXXXX-XXX". Teste com a string "12345-678".
1. Escreva uma expressão regular que utilize parênteses para capturar a parte de um endereço de e-mail antes do símbolo "@" e o domínio depois dele. Teste com "email@example.com".
1. Defina uma expressão regular que utilize parênteses para capturar a primeira e a última palavra de uma frase. Aplique à string "Python é divertido de aprender".
1. Crie uma expressão regular que utilize parênteses para capturar a parte inteira e a parte decimal de um número no formato "123.456". Teste com a string "Preço: 123.45".

</details>

---

### `|` (barra vertical)

O metacaractere **`|`** funciona como um **"ou lógico"** em expressões regulares, permitindo que você defina alternativas para correspondência. Ele tenta corresponder a parte antes do `|` ou a parte depois do `|`.

1. **exemplo alternativas com `|` para diferentes palavras**

    ```python
    # texto de exemplo
    texto = "Cachorro, Gato, Pássaro"

    # padrão : encontrar "Cachorro", "Gato" ou "Pássaro"
    resultado = re.findall(r"Cachorro|Gato|Pássaro", texto)

    # exibindo o resultado
    print("Animais encontrados:", resultado)
    ```

    **Explicação**
    - **`Cachorro|Gato|Pássaro`** : procura por qualquer uma dessas palavras na string;

    **Saída**
    ```
    Animais encontrados: ['Cachorro', 'Gato', 'Pássaro']
    ```

1. **exemplo usando `|` com `re.match()`**

    ```python
    # texto de exemplo
    texto = "Verde é uma cor"

    # padrão : encontrar "Verde" ou "Azul" no início da string
    resultado = re.match(r"Verde|Azul", texto)

    # exibindo o resultado
    if resultado:
        print("Cor encontrada:", resultado.group())
    else:
        print("Nenhuma cor encontrada.")
    ```

    **Explicação**
    - **`Verde|Azul`** : verifica se o texto começa com "Verde" ou "Azul";

    **Saída**
    ```
    Cor encontrada: Verde
    ```

1. **exemplo alternativas com padrões complexos**

    ```python
    # texto de exemplo
    texto = "Carro: ABC-1234 ou Moto: 9876-XYZ"

    # padrão : encontrar placas de carro ou moto
    resultado = re.findall(r"[A-Z]{3}-\d{4}|\d{4}-[A-Z]{3}", texto)

    # exibindo o resultado
    print("Placas encontradas:", resultado)
    ```

    **Explicação**
    - **`[A-Z]{3}-\d{4}`** : encontra placas de veículos no formato "ABC-1234" ou "XYZ-9876";

    **Saída**
    ```
    Placas encontradas: ['ABC-1234', 'XYZ-9876']
    ```

### exercícios `|`

<details>
<summary>Lista de Exercícios</summary>

1. Crie uma expressão regular que utilize a barra vertical (`|`) para encontrar ocorrências de "maçã" ou "laranja" em uma string. Teste com a string "Eu gosto de maçã e laranja".
1. Escreva uma expressão regular que utilize `|` para encontrar a palavra "cão" ou "gato" em uma frase. Aplique à string "O cão e o gato são animais de estimação".
1. Defina uma expressão regular que utilize `|` para encontrar números que podem ser "10" ou "20". Teste com a string "10 15 20 25".
1. Crie uma expressão regular que utilize `|` para encontrar as cores "azul", "verde" ou "vermelho". Teste com a string "As cores são azul, verde e vermelho".
1. Escreva uma expressão regular que utilize `|` para encontrar palavras que podem ser "carro", "moto" ou "bicicleta". Aplique à string "Eu tenho um carro e uma bicicleta".
1. Defina uma expressão regular que utilize `|` para capturar sequências de letras "a", "b" ou "c". Teste com a string "a b c d e f".
1. Crie uma expressão regular que utilize `|` para encontrar a palavra "dia" ou "noite" em uma string. Aplique à string "Eu prefiro o dia à noite".
1. Escreva uma expressão regular que utilize `|` para encontrar números que podem ser "100", "200" ou "300". Teste com a string "100 150 200 250 300".
1. Defina uma expressão regular que utilize `|` para encontrar palavras que sejam "sol" ou "lua". Aplique à string "O sol brilha durante o dia, e a lua à noite".
1. Crie uma expressão regular que utilize `|` para encontrar nomes de frutas "banana", "uva" ou "morango". Teste com a string "Eu comprei banana, uva e morango".

</details>

---

## sequências

### `\d` (dígitos)

- **`\d`** corresponde a qualquer **dígito numérico** de 0 a 9;
- **equivalente a**: `[0-9]`;

1. **exemplo encontrando todos os dígitos em uma string**

    ```python
    import re

    # texto de exemplo
    texto = "A senha é 12345 e o código de área é 55."

    # padrão : encontrar todos os dígitos na string
    resultado = re.findall(r"\d", texto)

    # exibindo o resultado
    print("Dígitos encontrados:", resultado)
    ```

    **Explicação**
    - **`\d`** encontra todos os dígitos individuais.

    **Saída**
    ```
    Dígitos encontrados: ['1', '2', '3', '4', '5', '5', '5']
    ```

1. **exemplo capturando sequências de dígitos**

    ```python
    # texto de exemplo
    texto = "Produto X custa 999 reais e Produto Y custa 1500 reais."

    # padrão : encontrar números inteiros
    resultado = re.findall(r"\d+", texto)

    # exibindo o resultado
    print("Números inteiros encontrados:", resultado)
    ```

    **Explicação**
    - **`\d+`** captura um ou mais dígitos consecutivos (números inteiros).

    **Saída**
    ```
    Números inteiros encontrados: ['999', '1500']
    ```

### exercícios `\d`

<details>
<summary>Lista de Exercícios</summary>

1. Crie uma expressão regular que utilize `\d` para encontrar qualquer dígito em uma string. Teste com a string "abc123def456".
1. Escreva uma expressão regular que utilize `\d` para encontrar todos os dígitos em uma frase contendo palavras e números. Aplique à string "Eu tenho 2 gatos e 3 cachorros".
1. Defina uma expressão regular que utilize `\d` para encontrar sequências de dois dígitos consecutivos. Teste com a string "12 34 56 78 90".
1. Crie uma expressão regular que utilize `\d` para capturar o ano de uma data no formato "dd/mm/aaaa". Aplique à string "Hoje é 07/10/2024".
1. Escreva uma expressão regular que utilize `\d` para verificar se uma string contém um número de telefone no formato "XXXXX-XXXX". Teste com a string "Meu número é 12345-6789".
1. Defina uma expressão regular que utilize `\d` para encontrar todos os números de uma sequência, separados por letras. Teste com "a1b2c3d4".
1. Crie uma expressão regular que utilize `\d` para capturar números de CPF no formato "XXX.XXX.XXX-XX". Teste com a string "Meu CPF é 123.456.789-09".
1. Escreva uma expressão regular que utilize `\d` para verificar se uma string contém um código postal (CEP) no formato "XXXXX-XXX". Teste com a string "CEP: 98765-432".
1. Defina uma expressão regular que utilize `\d` para encontrar números que representem a idade de pessoas em uma frase. Aplique à string "Maria tem 25 anos, João tem 30".
1. Crie uma expressão regular que utilize `\d` para capturar os números de uma sequência numérica com vários grupos de dígitos. Teste com a string "Grupo 1: 123, Grupo 2: 456, Grupo 3: 789".

</details>

---

### `\D` (não-dígitos)

- **`\D`** corresponde a qualquer caractere **que não seja um dígito**;
- **equivalente a**: `[^0-9]`;

1. **exemplo encontrando caracteres que não sejam dígitos**

    ```python
    # texto de exemplo
    texto = "Preço: 1500 reais"

    # padrão : encontrar tudo que não seja dígito
    resultado = re.findall(r"\D", texto)

    # exibindo o resultado
    print("Caracteres não numéricos encontrados:", resultado)
    ```

    **Explicação**
    - **`\D`** encontra qualquer caractere que **não** seja um dígito.

    **Saída**
    ```
    Caracteres não numéricos encontrados: ['P', 'r', 'e', 'ç', 'o', ':', ' ', ' ', 'r', 'e', 'a', 'i', 's']
    ```

1. **exemplo removendo todos os dígitos de uma string**

    ```python
    # texto de exemplo
    texto = "Meu número de telefone é 1234-5678."

    # padrão : substituir todos os dígitos por uma string vazia
    resultado = re.sub(r"\d", "", texto)

    # exibindo o resultado
    print("Texto sem dígitos:", resultado)
    ```

    **Explicação**
    - **`\d`** substitui cada dígito encontrado por uma string vazia.

    **Saída**
    ```
    Texto sem dígitos: Meu número de telefone é -.
    ```

### exercícios `\D`

<details>
<summary>Lista de Exercícios</summary>

1. Crie uma expressão regular que utilize `\D` para encontrar qualquer caractere que não seja um dígito em uma string. Teste com a string "abc123def456".
1. Escreva uma expressão regular que utilize `\D` para encontrar todas as letras em uma string que contém palavras e números. Aplique à string "A idade de João é 25 e a de Maria é 30".
1. Defina uma expressão regular que utilize `\D` para separar os dígitos de qualquer outro caractere em uma string. Teste com "123abc456def".
1. Crie uma expressão regular que utilize `\D` para capturar tudo o que não seja números em uma string que contém uma mistura de números e símbolos. Aplique à string "Preço: $100, Desconto: 20%".
1. Escreva uma expressão regular que utilize `\D` para encontrar o texto de uma string que contém um CPF, ignorando os números. Teste com a string "CPF: 123.456.789-09".
1. Defina uma expressão regular que utilize `\D` para encontrar todas as letras em uma string contendo números e letras. Teste com a string "abc123xyz456".
1. Crie uma expressão regular que utilize `\D` para remover todos os números de uma string, mantendo apenas os caracteres alfabéticos. Aplique à string "Casa123Rua456Bairro789".
1. Escreva uma expressão regular que utilize `\D` para capturar todos os caracteres que não são dígitos de uma string contendo uma data no formato "dd/mm/aaaa". Teste com a string "07/10/2024".
1. Defina uma expressão regular que utilize `\D` para identificar a parte textual de uma mensagem que mistura letras, números e símbolos. Aplique à string "Pedido #123456: Produto - Televisor".
1. Crie uma expressão regular que utilize `\D` para capturar e extrair tudo o que não seja números de uma string com endereços, como "Rua 25, Número 123, Bairro 789".

</details>

---

### `\w` (caracteres alfanuméricos)

- **`\w`** corresponde a qualquer **caractere alfanumérico** (letras, dígitos e o caractere sublinhado `_`);
- **equivalente a**: `[a-zA-Z0-9_]`;

1. **exemplo encontrando todas as palavras**

    ```python
    # texto de exemplo
    texto = "Palavras e números: 123_ABC"

    # padrão : encontrar todas as sequências alfanuméricas
    resultado = re.findall(r"\w+", texto)

    # exibindo o resultado
    print("Palavras e números encontrados:", resultado)
    ```

    **Explicação**
    - **`\w+`** captura sequências de caracteres alfanuméricos (palavras ou números).

    **Saída**
    ```
    Palavras e números encontrados: ['Palavras', 'e', 'números', '123_ABC']
    ```

1. **exemplo substituindo caracteres alfanuméricos**

    ```python
    # texto de exemplo
    texto = "Código: ABC_123"

    # padrão : substituir todos os caracteres alfanuméricos por "*"
    resultado = re.sub(r"\w", "*", texto)

    # exibindo o resultado
    print("Resultado de substituição:", resultado)
    ```

    **Explicação**
    - **`\w`** encontra cada caractere alfanumérico e o substitui por "*".

    **Saída**
    ```
    Resultado de substituição: ******: *******
    ```

### exercícios `\w`

<details>
<summary>Lista de Exercícios</summary>

1. Crie uma expressão regular que utilize `\w` para encontrar todas as letras e números em uma string. Teste com a string "abc123!@#".
1. Escreva uma expressão regular que utilize `\w` para encontrar qualquer caractere alfanumérico em uma frase com símbolos. Aplique à string "Python é legal! 2024 é o ano!".
1. Defina uma expressão regular que utilize `\w` para capturar todos os caracteres alfanuméricos de um nome de usuário em um e-mail (parte antes de "@"). Teste com a string "usuario_123@example.com".
1. Crie uma expressão regular que utilize `\w` para extrair todas as palavras de uma string contendo espaços e símbolos. Aplique à string "Python_3 é incrível! Vamos aprender?".
1. Escreva uma expressão regular que utilize `\w` para encontrar as palavras em uma URL, ignorando os caracteres de pontuação. Teste com a string "https://www.exemplo.com/caminho/pagina".
1. Defina uma expressão regular que utilize `\w` para capturar qualquer sequência de letras e números separadas por espaços, ignorando pontuação. Teste com a string "A senha é 123abc_ e o código é xyz789!".
1. Crie uma expressão regular que utilize `\w` para identificar todas as palavras e números em uma frase que também contém pontuações e símbolos. Aplique à string "Dia 12, mês 10, ano 2024 - Vamos lá!".
1. Escreva uma expressão regular que utilize `\w` para extrair todas as partes alfanuméricas de uma string com códigos mistos. Teste com a string "Código: 123abc, Senha: 789xyz!".
1. Defina uma expressão regular que utilize `\w` para encontrar nomes de variáveis e funções que contenham letras, números e sublinhados em um código de programação. Aplique à string "def minha_funcao(var1, var2): return var1 + var2".
1. Crie uma expressão regular que utilize `\w` para capturar todas as palavras alfanuméricas em uma string que contém uma frase com números e símbolos. Teste com "Eu tenho 2_irmãos e 1_primo!".

</details>

---

### `\W` (não-alfanuméricos)

- **`\W`** corresponde a qualquer caractere **que não seja alfanumérico**;
- **equivalente a**: `[^a-zA-Z0-9_]`;

1. **exemplo encontrando caracteres não alfanuméricos**

    ```python
    # texto de exemplo
    texto = "Nome: João & Maria! Número: 456."

    # padrão : encontrar todos os caracteres que não são alfanuméricos
    resultado = re.findall(r"\W", texto)

    # exibindo o resultado
    print("Caracteres não alfanuméricos encontrados:", resultado)
    ```

    **Explicação**
    - **`\W`** encontra tudo que **não** é um caractere alfanumérico.

    **Saída**
    ```
    Caracteres não alfanuméricos encontrados: [':', ' ', '&', ' ', '!', ' ', ':', ' ', '.']
    ```

1. **exemplo removendo caracteres não alfanuméricos**

    ```python
    # texto de exemplo
    texto = "Nome: Ana@exemplo.com"

    # padrão : substituir caracteres não alfanuméricos por uma string vazia
    resultado = re.sub(r"\W", "", texto)

    # exibindo o resultado
    print("Resultado sem caracteres especiais:", resultado)
    ```

    **Explicação**
    - **`\W`** remove todos os caracteres que não são letras, números ou sublinhados.

    **Saída**
    ```
    Resultado sem caracteres especiais: NomeAnaexemplocom
    ```

### exercícios `\W`

<details>
<summary>Lista de Exercícios</summary>

1. Crie uma expressão regular que utilize `\W` para encontrar todos os caracteres não alfanuméricos em uma string. Teste com a string "abc123!@#def$%&".
1. Escreva uma expressão regular que utilize `\W` para encontrar todos os espaços e símbolos em uma frase. Aplique à string "Python é incrível! Vamos aprender?".
1. Defina uma expressão regular que utilize `\W` para capturar todos os caracteres não alfanuméricos em uma URL. Teste com a string "https://www.exemplo.com/pagina-123".
1. Crie uma expressão regular que utilize `\W` para extrair os caracteres especiais de uma string de senha complexa. Aplique à string "senha123!@#ABC$%_".
1. Escreva uma expressão regular que utilize `\W` para encontrar todos os símbolos e pontuações em uma frase, ignorando letras e números. Teste com a string "Olá, tudo bem? Vamos ao cinema às 18h!".
1. Defina uma expressão regular que utilize `\W` para identificar todos os caracteres não alfanuméricos, como espaços e pontuações, em uma string de código. Aplique à string "def minha_funcao(): print('Olá, Mundo!')".
1. Crie uma expressão regular que utilize `\W` para capturar todos os caracteres que não sejam letras, números ou sublinhados em uma string de e-mail. Teste com "usuario_123@example.com".
1. Escreva uma expressão regular que utilize `\W` para separar todas as palavras de uma frase, usando os símbolos como delimitadores. Teste com a string "Café&Chá#Biscoito@Bolacha".
1. Defina uma expressão regular que utilize `\W` para encontrar os caracteres especiais em uma string de data no formato "dd/mm/aaaa". Aplique à string "07/10/2024".
1. Crie uma expressão regular que utilize `\W` para remover todos os caracteres não alfanuméricos de uma frase, deixando apenas letras, números e sublinhados. Teste com "Senha segura: abc123!@#XYZ".

</details>

---

### `\s` (espaços em branco)

- **`\s`** corresponde a qualquer **caractere de espaço em branco**, como espaços, tabulações (`\t`), novas linhas (`\n`), etc;
- **equivalente a**: `[ \t\n\r\f\v]`;

1. **exemplo encontrando todos os espaços em branco em uma string**

    ```python
    import re

    # texto de exemplo
    texto = "Palavras separadas por espaços e tabulações.\tAqui também."

    # padrão : encontrar todos os caracteres de espaço em branco
    resultado = re.findall(r"\s", texto)

    # exibindo o resultado
    print("Espaços em branco encontrados:", resultado)
    ```

    **Explicação**
    - **`\s`** encontra cada espaço em branco, incluindo espaços comuns e tabulações.

    **Saída**
    ```
    Espaços em branco encontrados: [' ', ' ', ' ', ' ', ' ', ' ', '\t', ' ']
    ```

1. **exemplo substituindo espaços em branco**

    ```python
    # texto de exemplo
    texto = "Texto com vários  espaços e linhas.\nAqui tem mais uma linha."

    # padrão : substituir todos os espaços em branco por "-"
    resultado = re.sub(r"\s", "-", texto)

    # exibindo o resultado
    print("Texto com substituição de espaços:", resultado)
    ```

    **Explicação**
    - **`\s`** substitui cada espaço em branco por um traço "-".

    **Saída**
    ```
    Texto com substituição de espaços: Texto-com-vários--espaços-e-linhas.-Aqui-tem-mais-uma-linha.
    ```

### exercícios `\s`

<details>
<summary>Lista de Exercícios</summary>

1. Crie uma expressão regular que utilize `\s` para encontrar todos os espaços em uma string. Teste com a string "Python é uma linguagem poderosa".
1. Escreva uma expressão regular que utilize `\s` para contar o número de espaços em branco em uma frase. Aplique à string "Aprendendo Python passo a passo".
1. Defina uma expressão regular que utilize `\s` para capturar todos os espaços entre palavras. Teste com a string "O dia está ensolarado e quente".
1. Crie uma expressão regular que utilize `\s` para substituir todos os espaços por sublinhados em uma frase. Aplique à string "Expressões regulares são úteis".
1. Escreva uma expressão regular que utilize `\s` para identificar espaços em branco e substituir por uma vírgula. Teste com a string "1 2 3 4 5".
1. Defina uma expressão regular que utilize `\s` para encontrar tabulações e espaços em uma string que contenha tanto tabulação quanto espaço. Aplique à string "Nome:\tJoão\t Idade: 25".
1. Crie uma expressão regular que utilize `\s` para identificar quebras de linha em uma string. Teste com a string "Primeira linha\nSegunda linha\nTerceira linha".
1. Escreva uma expressão regular que utilize `\s` para remover todos os espaços em uma frase, deixando as palavras juntas. Teste com "Removendo todos os espaços em branco".
1. Defina uma expressão regular que utilize `\s` para contar o número total de caracteres de espaço, incluindo espaços, tabulações e quebras de linha. Teste com a string "Linha 1\nLinha 2\tLinha 3".
1. Crie uma expressão regular que utilize `\s` para capturar todas as ocorrências de múltiplos espaços consecutivos e substituí-los por um único espaço. Aplique à string "Python    é   uma   linguagem   incrível".

</details>

---

### `\S` (não-espaços)

- **`\S`** corresponde a qualquer caractere **que não seja um espaço em branco**;
- **equivalente a**: `[^ \t\n\r\f\v]`;

1. **exemplo encontrando todos os caracteres que não são espaços**

    ```python
    # texto de exemplo
    texto = "Exemplo: Linha com espaços."

    # padrão : encontrar todos os caracteres que não são espaços
    resultado = re.findall(r"\S", texto)

    # exibindo o resultado
    print("Caracteres que não são espaços:", resultado)
    ```

    **Explicação**
    - **`\S`** encontra tudo que **não** é espaço em branco.

    **Saída**
    ```
    Caracteres que não são espaços: ['E', 'x', 'e', 'm', 'p', 'l', 'o', ':', 'L', 'i', 'n', 'h', 'a', 'c', 'o', 'm', 'e', 's', 'p', 'a', 'ç', 'o', 's', '.']
    ```

1. **exemplo removendo todos os espaços em branco**

    ```python
    # texto de exemplo
    texto = "Texto com espaços e tabulações.\tOutra linha."

    # padrão : substituir todos os espaços em branco por uma string vazia
    resultado = re.sub(r"\s", "", texto)

    # exibindo o resultado
    print("Texto sem espaços em branco:", resultado)
    ```

    **Explicação**
    - **`\s`** remove todos os espaços em branco da string.

    **Saída**
    ```
    Texto sem espaços em branco: Textocomespaçosetabulações.Outralinha.
    ```

### exercícios `\S`

<details>
<summary>Lista de Exercícios</summary>

1. Crie uma expressão regular que utilize `\S` para encontrar todos os caracteres que não sejam espaços em uma string. Teste com a string "Python é incrível!".
1. Escreva uma expressão regular que utilize `\S` para capturar todas as palavras de uma frase, ignorando os espaços em branco. Aplique à string "Aprendendo expressões regulares em Python".
1. Defina uma expressão regular que utilize `\S` para encontrar todos os caracteres contínuos que não sejam espaços em uma URL. Teste com "https://www.exemplo.com".
1. Crie uma expressão regular que utilize `\S` para capturar todos os símbolos e letras de uma string, ignorando os espaços. Aplique à string "O valor é: $100.00, desconto: 15%".
1. Escreva uma expressão regular que utilize `\S` para encontrar todos os caracteres não espaços em uma linha de código. Teste com a string "def minha_funcao(): print('Olá, Mundo!')".
1. Defina uma expressão regular que utilize `\S` para capturar todas as palavras e números de uma string com frases e números. Teste com "A idade de João é 25 anos e Maria tem 30".
1. Crie uma expressão regular que utilize `\S` para remover os espaços de uma frase, deixando os caracteres contínuos. Aplique à string "Removendo os espaços em branco".
1. Escreva uma expressão regular que utilize `\S` para capturar todos os caracteres de uma string, exceto os espaços e tabulações. Teste com a string "Nome: João\t Idade: 25".
1. Defina uma expressão regular que utilize `\S` para identificar todos os caracteres, exceto os espaços, em uma string contendo quebra de linhas. Aplique à string "Linha 1\nLinha 2\nLinha 3".
1. Crie uma expressão regular que utilize `\S` para capturar todos os caracteres não espaços de uma string com números e símbolos. Teste com "Códigos: 123-456; Senhas: abc!@#".

</details>

---

### `\b` (limite de palavra)

- **`\b`** corresponde a um **limite de palavra**, que pode ser o início ou o fim de uma palavra;
- um limite de palavra ocorre quando há uma transição entre um caractere alfanumérico e um não-alfanumérico (ou vice-versa);

1. **exemplo encontrando palavras exatas**

    ```python
    # texto de exemplo
    texto = "Estamos aprendendo expressões regulares no Python."

    # padrão : encontrar a palavra "Python"
    resultado = re.search(r"\bPython\b", texto)

    # exibindo o resultado
    if resultado:
        print("Palavra 'Python' encontrada:", resultado.group())
    else:
        print("Palavra não encontrada.")
    ```

    **Explicação**
    - **`\bPython\b`** procura pela palavra exata "Python", verificando se há um limite de palavra antes e depois dela.

    **Saída**
    ```
    Palavra 'Python' encontrada: Python
    ```

1. **exemplo substituindo palavras exatas**

    ```python
    # texto de exemplo
    texto = "Vamos estudar Python e aprender Python com exemplos."

    # padrão : substituir "Python" por "regex"
    resultado = re.sub(r"\bPython\b", "regex", texto)

    # exibindo o resultado
    print("Texto após substituição:", resultado)
    ```

    **Explicação**
    - **`\bPython\b`** garante que apenas a palavra exata "Python" seja substituída.

    **Saída**
    ```
    Texto após substituição: Vamos estudar regex e aprender regex com exemplos.
    ```

### exercícios `\b`

<details>
<summary>Lista de Exercícios</summary>

1. Crie uma expressão regular que utilize `\b` para encontrar a palavra "Python" em uma string. Teste com a string "Aprendendo Python é divertido".
1. Escreva uma expressão regular que utilize `\b` para capturar todas as ocorrências da palavra "programação" em uma frase. Aplique à string "A programação em Python e a programação em Java são populares".
1. Defina uma expressão regular que utilize `\b` para verificar se a palavra "teste" está presente em uma string, garantindo que não faça parte de outra palavra. Teste com "Isso é um teste".
1. Crie uma expressão regular que utilize `\b` para encontrar todas as palavras que começam com a letra "A" em uma frase. Aplique à string "Aprenda a programar em Python e a criar projetos".
1. Escreva uma expressão regular que utilize `\b` para substituir todas as ocorrências da palavra "bom" por "ótimo" em uma string. Teste com a frase "Isso é um bom exemplo".
1. Defina uma expressão regular que utilize `\b` para capturar todas as palavras terminadas em "ar" em uma string. Aplique à string "Cantar, dançar e jogar são atividades divertidas".
1. Crie uma expressão regular que utilize `\b` para contar quantas vezes a palavra "programa" aparece em uma string. Teste com "O programa é simples. Este programa é útil".
1. Escreva uma expressão regular que utilize `\b` para encontrar todas as palavras que têm exatamente 4 letras. Teste com a string "Cão, gato, peixe e pato são animais comuns".
1. Defina uma expressão regular que utilize `\b` para identificar se a palavra "ponto" está presente em uma string, ignorando casos onde é parte de outra palavra. Teste com "Um ponto é uma marca".
1. Crie uma expressão regular que utilize `\b` para capturar todas as palavras que contêm a letra "e". Aplique à string "Ela é muito inteligente e sempre aprende rapidamente".

</details>

---

### `\B` (não-limite de palavra)

- **`\B`** corresponde a qualquer posição que **não seja um limite de palavra**;
- usado para garantir que a correspondência ocorra no meio de uma palavra, e não nos seus limites;

1. **exemplo encontrando ocorrências dentro de palavras**

    ```python
    # texto de exemplo
    texto = "Expressões como sub, substring e superb."

    # padrão : encontrar "sub" que não esteja no início ou no fim de uma palavra
    resultado = re.findall(r"\Bsub\B", texto)

    # exibindo o resultado
    print("Ocorrências de 'sub' no meio de palavras:", resultado)
    ```

    **Explicação**
    - **`\Bsub\B`** encontra a sequência "sub" dentro de palavras, mas não se ela estiver no início ou no fim.

    **Saída**
    ```
    Ocorrências de 'sub' no meio de palavras: ['sub']
    ```

1. **exemplo usando `\b` para ignorar palavras completas**

    ```python
    # texto de exemplo
    texto = "submarine, submission, and subscribe are common terms."

    # padrão : encontrar ocorrências de "sub" que não estejam no início ou fim da palavra
    resultado = re.findall(r"\Bsub\B", texto)

    # exibindo o resultado
    print("Ocorrências de 'sub' no meio:", resultado)
    ```

    **Explicação**
    - **`\Bsub\B`** ignora ocorrências de "sub" que estão no início ou no final de palavras.

    **Saída**
    ```
    Ocorrências de 'sub' no meio: []
    ```

### exercícios `\B`

<details>
<summary>Lista de Exercícios</summary>

1. Crie uma expressão regular que utilize `\B` para encontrar a sequência "Python" quando ela estiver dentro de outra palavra. Teste com a string "Pythonista".
1. Escreva uma expressão regular que utilize `\B` para capturar a palavra "programação" quando ela estiver concatenada com outros caracteres. Aplique à string "programaçãoPython".
1. Defina uma expressão regular que utilize `\B` para verificar se a sequência "está" está presente em uma string onde é parte de outra palavra. Teste com "Amanhã estará melhor".
1. Crie uma expressão regular que utilize `\B` para encontrar todas as ocorrências da sequência "fun" que estejam dentro de palavras. Aplique à string "Fundamental e funcional".
1. Escreva uma expressão regular que utilize `\B` para identificar se "código" aparece em uma palavra longa. Teste com "programacódigo".
1. Defina uma expressão regular que utilize `\B` para capturar sequências que contêm "ar" no meio de palavras. Aplique à string "Programar é divertido".
1. Crie uma expressão regular que utilize `\B` para encontrar palavras que contêm a sequência "de" no meio. Teste com a string "Padeiro e Madeira".
1. Escreva uma expressão regular que utilize `\B` para capturar todas as ocorrências da sequência "ente" em palavras compostas. Teste com "Aventurente".
1. Defina uma expressão regular que utilize `\B` para identificar se a sequência "passo" está presente em uma string onde é parte de outra palavra. Teste com "passos a seguir".
1. Crie uma expressão regular que utilize `\B` para encontrar todas as palavras que têm "tor" no meio. Aplique à string "motor e ator".

</details>

---

## exemplos práticos

### exemplo removendo espaços em branco (trim)

```python
# texto de exemplo
texto = "   Olá,   mundo!   "

# padrão : remover espaços em branco no início e no fim da string
resultado = re.sub(r"^\s+|\s+$", "", texto)

# exibindo o resultado
print("Texto sem espaços extras:", resultado)
```

**Saída esperada**:
```
Texto sem espaços extras: Olá,   mundo!
```

---

### extraindo números de uma string complexa

```python
# texto de exemplo
texto = "O aluno 12345 tirou nota 8.5 em 2 provas."

# padrão : encontrar todos os números inteiros e decimais
resultado = re.findall(r"\d+\.\d+|\d+", texto)

# exibindo o resultado
print("Números encontrados:", resultado)
```

**Saída esperada**:
```
Números encontrados: ['12345', '8.5', '2']
```

---

### validando um endereço de e-mail

```python
# texto de exemplo
email = "exemplo@dominio.com"

# padrão : verificar se é um e-mail válido
resultado = re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email)

# exibindo o resultado
if resultado:
    print("E-mail válido!")
else:
    print("E-mail inválido.")
```

**Saída esperada**:
```
E-mail válido!
```

---

### removendo caracteres especiais de uma string

```python
# texto de exemplo
texto = "Aqui@Tem#Caracteres!Especiais?"

# padrão : remover todos os caracteres não alfanuméricos
resultado = re.sub(r"\W", "", texto)

# exibindo o resultado
print("Texto sem caracteres especiais:", resultado)
```

**Saída esperada**:
```
Texto sem caracteres especiais: AquiTemCaracteresEspeciais
```

---

### validando um número de telefone (formato brasileiro)

```python
# texto de exemplo
telefone = "(11) 98765-4321"

# padrão : validar número de telefone brasileiro
resultado = re.match(r"^\(\d{2}\) \d{5}-\d{4}$", telefone)

# exibindo o resultado
if resultado:
    print("Número de telefone válido!")
else:
    print("Número de telefone inválido.")
```

**Saída esperada**:
```
Número de telefone válido!
```

---

## exercícios `log`

<details>

<summary>Lista de Exercícios</summary>

Considere o seguinte repositório [`LogHub`](https://github.com/logpai/loghub). Para *todos* os próximos exercícios, use esse repositório para buscar as informações.

Baixe ele para sua máquina, descompacte-o e coloque-o junto do módulo que irá executar as Expressões Regulares. Use o módulo sys para buscar pelos arquivos `log` e realizar a busca especificada.

1. Exercícios Simples
    1. Encontre todas as ocorrências da palavra "error" em um arquivo de log.
    1. Busque por linhas que contenham a palavra "warning".
    1. Encontre todas as entradas que começam com "INFO".
    1. Busque por linhas que contenham endereços IP (ex: 192.168.1.1).
    1. Encontre todas as entradas que contenham a data no formato "YYYY-MM-DD".
    1. Busque por linhas que terminam com um ponto e vírgula.
    1. Encontre todas as ocorrências de um código de status HTTP (ex: 200, 404).
    1. Busque por linhas que contenham palavras que começam com a letra "F".
    1. Encontre todas as entradas que contêm a palavra "failed".
    1. Busque por logs que incluem "disk" e "error".
1. Exercícios Intermediários
    1. Encontre todas as entradas que contêm um timestamp (ex: "2024-10-07 12:34:56").
    1. Busque por linhas que contêm nomes de usuários (ex: "user123").
    1. Encontre todas as mensagens que incluem a palavra "success".
    1. Busque por entradas que tenham mais de 20 caracteres.
    1. Encontre todas as linhas que contêm números de telefone (ex: "(123) 456-7890").
    1. Busque por mensagens que começam com um número.
    1. Encontre todas as entradas que terminam com um número.
    1. Busque por logs que contenham a palavra "timeout".
    1. Encontre todas as entradas que têm o formato de um e-mail.
    1. Busque por mensagens que contêm a palavra "system" seguida de um número.
1. Exercícios Avançados
    1. Encontre todas as entradas que contêm URLs (ex: "http://example.com").
    1. Busque por linhas que contêm a palavra "exception" seguida de uma descrição.
    1. Encontre todas as ocorrências de palavras que começam com "net".
    1. Busque por entradas que têm "user" seguido de um ID numérico.
    1. Encontre todas as linhas que incluem "failed to" seguidas por uma ação.
    1. Busque por entradas que têm uma sequência de três letras maiúsculas (ex: "ABC").
    1. Encontre todas as linhas que têm "login" ou "logout".
    1. Busque por logs que incluem a palavra "critical".
    1. Encontre todas as entradas que têm "received" seguido por um número.
    1. Busque por entradas que contêm um caractere especial (ex: "#").
1. Exercícios Complexos
    1. Encontre todas as entradas que contêm um timestamp no formato "YYYY/MM/DD".
    1. Busque por mensagens que contêm "permission denied" e um nome de usuário.
    1. Encontre todas as entradas que têm a estrutura de um comando do sistema (ex: "mkdir /path/to/dir").
    1. Busque por logs que contêm uma sequência de 4 dígitos (ex: "1234").
    1. Encontre todas as entradas que têm "error" seguido por um código de erro (ex: "error 500").
    1. Busque por linhas que têm "failed" ou "success", seguidas por uma descrição.
    1. Encontre todas as entradas que contêm a palavra "network" e um endereço IP.
    1. Busque por logs que incluem um nome de arquivo (ex: "file.txt").
    1. Encontre todas as mensagens que contêm "running" e uma descrição de processo.
    1. Busque por entradas que têm "started" seguido por um nome de serviço.
1. Exercícios Desafiadores
    1. Encontre todas as entradas que contêm "user" seguido de um nome e um sobrenome.
    1. Busque por logs que incluem uma sequência de caracteres que não são letras ou números.
    1. Encontre todas as linhas que têm um status de processo (ex: "running", "stopped").
    1. Busque por entradas que contêm a palavra "service" e um número de versão (ex: "v1.2.3").
    1. Encontre todas as mensagens que incluem "session" e um ID de sessão numérico.
    1. Busque por logs que contêm "server" seguido por um endereço IP e um status.
    1. Encontre todas as entradas que têm "disconnected" e um nome de usuário.
    1. Busque por mensagens que contêm a palavra "restart" seguida de uma data.
    1. Encontre todas as linhas que têm "data" e um número de bytes.
    1. Busque por entradas que contêm "attempt" e um número de tentativas.
1. Exercícios Avançados (continuação)
    1. Encontre todas as entradas que contêm "process" seguido por um ID numérico.
    1. Busque por logs que incluem "configuration" e um arquivo de configuração.
    1. Encontre todas as mensagens que têm "completed" e um timestamp.
    1. Busque por entradas que contêm "download" e um URL.
    1. Encontre todas as linhas que têm "upload" e um nome de arquivo.
    1. Busque por logs que incluem "memory" e um valor numérico.
    1. Encontre todas as entradas que têm "failed" seguido de um motivo.
    1. Busque por mensagens que contêm "success" e uma descrição de ação.
    1. Encontre todas as linhas que têm "version" e um número de versão.
    1. Busque por entradas que contêm "user" e um endereço de e-mail.
1. Exercícios Desafiadores (continuação)
    1. Encontre todas as entradas que têm "unauthorized" e um nome de usuário.
    1. Busque por logs que incluem "connection" e um status.
    1. Encontre todas as mensagens que têm "timeout" e um número de segundos.
    1. Busque por entradas que contêm "session" e um estado (ex: "active", "inactive").
    1. Encontre todas as linhas que têm "request" e um código de resposta.
    1. Busque por logs que incluem "cache" e um número.
    1. Encontre todas as entradas que têm "database" e um nome de banco de dados.
    1. Busque por mensagens que contêm "disk" e um status.
    1. Encontre todas as linhas que têm "login" e um timestamp.
    1. Busque por entradas que contêm "service" e um nome de serviço.
1. Exercícios Complexos (continuação)
    1. Encontre todas as entradas que têm "resource" e um valor numérico.
    1. Busque por logs que incluem "event" e uma descrição de evento.
    1. Encontre todas as mensagens que têm "error" seguido por um código de erro.
    1. Busque por entradas que contêm "user" seguido por "logged in".
    1. Encontre todas as entradas que têm "transaction" e um valor monetário.
    1. Busque por logs que incluem "network" e "disconnected".
    1. Encontre todas as mensagens que têm "service" e uma descrição.
    1. Busque por entradas que contêm "script" seguido por um caminho de arquivo.
    1. Encontre todas as linhas que têm "health" e um status (ex: "OK", "FAIL").
    1. Busque por logs que incluem "upgrade" e um número de versão.
1. Exercícios Avançados (continuação)
    1. Encontre todas as entradas que contêm "error" e uma descrição do problema.
    1. Busque por mensagens que têm "system" e um estado (ex: "active", "inactive").
    1. Encontre todas as entradas que têm "API" e um status de resposta.
    1. Busque por logs que incluem "timeout" e uma descrição.
    1. Encontre todas as mensagens que têm "activity" e um timestamp.
    1. Busque por entradas que contêm "backup" e um caminho de arquivo.
    1. Encontre todas as linhas que têm "event" e um ID numérico.
    1. Busque por logs que incluem "notification" e um destinatário.
    1. Encontre todas as mensagens que têm "service" e um tempo de resposta.
    1. Busque por entradas que contêm "configuration" e um parâmetro.
1. Exercícios Desafiadores (continuação)
    1. Encontre todas as entradas que têm "login" e uma hora.
    1. Busque por logs que incluem "failed" e uma razão.
    1. Encontre todas as mensagens que têm "download" e um tamanho de arquivo.
    1. Busque por entradas que contêm "upload" e um status.
    1. Encontre todas as linhas que têm "process" e um ID de processo.
    1. Busque por logs que incluem "restart" e um serviço.
    1. Encontre todas as entradas que têm "completed" e um tempo.
    1. Busque por mensagens que têm "finished" e um timestamp.
    1. Encontre todas as linhas que têm "access" e um ID de acesso.
    1. Busque por entradas que contêm "status" e um código de status específico.

</details>

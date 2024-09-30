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

    # texto onde vamos fazer a substituição
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
    # texto onde vamos dividir
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

    # texto onde vamos buscar
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

    # Texto onde vamos fazer a busca
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

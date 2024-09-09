# arquivos

O processo de leitura de arquivos no Python envolve abrir um arquivo, ler seu conteúdo e, em seguida, fechá-lo. Python oferece diferentes modos de leitura, como `r` para leitura, `w` para escrita, e `a` para adicionar conteúdo. O processo é realizado por meio da função `open()`, que retorna um objeto de arquivo, usado para manipular o conteúdo.

Exemplo básico :

```python
with open('arquivo.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
```

Neste exemplo, o comando `with` garante que o arquivo seja fechado corretamente após sua utilização, mesmo em caso de erro. Mais adiante isso será visto com detalhes.

## pontos importantes

### finalidades :
- **processamento de dados** : utilizado para ler dados de arquivos de texto, csvs, logs, etc., e manipulá-los no código;
- **entrada e saída de dados** : permite salvar e carregar informações persistentes, facilitando o armazenamento de resultados ou configurações;

### vantagens :
- **simplicidade** : a leitura de arquivos é direta e fácil de implementar;
- **flexibilidade** : python pode manipular diversos tipos de arquivos (texto, binários, csv, json, etc.);
- **automação**: pode ser usada para automatizar tarefas que envolvem manipulação de dados em massa;

### desvantagens :
- **limitação de memória** : carregar arquivos grandes pode consumir muita memória, afetando o desempenho;
- **erro de codificação** : arquivos podem ter diferentes codificações (ex.: utf-8, ascii), e erros podem ocorrer ao ler arquivos com codificação incorreta;

### cuidados :
- **fechar o arquivo** : sempre garantir que o arquivo seja fechado após a leitura para evitar corrupção de dados ou consumo desnecessário de recursos;
- **exceções** : tratar exceções, como erros de arquivo não encontrado (`FileNotFoundError`) ou de permissões de leitura;
- **codificação** : verificar e definir corretamente a codificação ao abrir o arquivo;

Esses são os pontos essenciais para uma leitura segura e eficiente de arquivos em Python.

## `open()`

A função `open()` no Python é usada para abrir arquivos e manipular dados dentro deles. Essa função cria um objeto que permite que se leia, escreva ou adicione informações a um arquivo de texto ou binário. O uso de `open()` envolve a especificação de um caminho de arquivo e, opcionalmente, um modo de operação (como leitura ou escrita).

Veja sua sinxtaxe básica :

```python
arquivo = open('caminho_do_arquivo', 'modo')
```

A função `open()` retorna um objeto de arquivo que pode ser manipulado para realizar operações como leitura (`read`), escrita (`write`) ou adição de conteúdo (`append`), dependendo do modo escolhido.

### modos mais comuns:

1. **`'r'`** (leitura) : abre um arquivo para leitura. este é o modo padrão. o arquivo deve existir; caso contrário, um erro será gerado;
1. **`'w'`** (escrita) : abre um arquivo para escrita; se o arquivo não existir, ele será criado; se o arquivo já existir, o conteúdo será sobrescrito;
1. **`'a'`** (anexar) : abre o arquivo para anexar dados no final do arquivo. se o arquivo não existir, ele será criado;

### modos do `open()`

O Python possui diversas formas de abrir um arquivo. Abaixo há as formas mais comuns.

| Modo | Uso                                  | Comportamento                                          |
|------|--------------------------------------|--------------------------------------------------------|
| `r`  | leitura                              | abre o arquivo para leitura; gera erro se não existir; |
| `w`  | escrita (sobrescreve)                | abre o arquivo para escrita; cria ou sobrescreve.      |
| `a`  | anexar                               | abre o arquivo para anexar dados; cria se não existir; |

#### 1. modo de leitura `r`

O modo `r` é usado para **abrir um arquivo para leitura**. Quando um arquivo é aberto nesse modo, ele deve **existir previamente**, caso contrário, um erro será gerado (`FileNotFoundError`). O ponteiro do arquivo (a posição de leitura) começa no início do arquivo.

Veja sua sintaxe :

```python
arquivo = open('exemplo.txt', 'r')
conteudo = arquivo.read()  # lê todo o conteúdo do arquivo
arquivo.close()  # fecha o arquivo após a leitura
```

##### exemplo

Suponha que exista um arquivo `dados.txt` com o seguinte conteúdo :

```
Python é uma linguagem de programação.
Ela é poderosa e fácil de aprender.
```

Agora, vamos abrir esse arquivo e ler seu conteúdo :

```python
# abrindo o arquivo para leitura
arquivo = open('dados.txt', 'r')

conteudo = arquivo.read()  # lendo o conteúdo do arquivo

print(f'{conteudo = }')  # exibe o conteúdo no terminal
arquivo.close()  # fecha o arquivo
```

Se o arquivo `dados.txt` não existir, o Python levantará uma exceção :

```python
FileNotFoundError: [Errno 2] No such file or directory: 'dados.txt'
```

#### 2. modo de escrita `w`

O modo `w` é usado para **abrir um arquivo para escrita**. Esse modo **sobrescreve** o conteúdo do arquivo caso ele já exista. Se o arquivo **não existir**, ele será criado automaticamente. O ponteiro de escrita começa no início do arquivo.

Veja sua sintaxe :
```python
arquivo = open('exemplo.txt', 'w')
arquivo.write("Escrevendo algo no arquivo.")  # escreve no arquivo
arquivo.close()  # fecha o arquivo após a escrita
```

##### exemplo

Se deseja criar ou sobrescrever o arquivo `saida.txt` com o texto `"Aprendendo a escrever em arquivos!"`, pode usar o seguinte código :

```python
# abrindo o arquivo para escrita
arquivo = open('saida.txt', 'w')
arquivo.write("Aprendendo a escrever em arquivos!")  # escreve no arquivo
arquivo.close()  # fecha o arquivo
```

Se o arquivo `saida.txt` já existia e tinha algum conteúdo, todo o conteúdo anterior será apagado e substituído pela nova string.

#### 3. modo de anexar `a`

O modo `a` é usado para **abrir um arquivo e anexar dados ao final** do arquivo. Esse modo é útil quando se quer adicionar dados a um arquivo sem sobrescrever o conteúdo existente. Se o arquivo **não existir**, ele será criado. O ponteiro de escrita começa no **final** do arquivo, ou seja, novos dados são sempre adicionados após o conteúdo existente.

Veja sua sintaxe básica :

```python
arquivo = open('exemplo.txt', 'a')
arquivo.write("Adicionando uma nova linha.")  # anexa dados ao arquivo
arquivo.close()  # fecha o arquivo
```

##### exemplo

Se deseja adicionar novas entradas a um arquivo `log.txt`, sem apagar as entradas anteriores, pode usar o modo `a`:

```python
# abrindo o arquivo para anexar dados
arquivo = open('log.txt', 'a')
arquivo.write("Nova entrada de log.\n")  # anexa ao arquivo
arquivo.close()  # Fecha o arquivo
```

Isso adicionará a frase `"Nova entrada de log."` ao final do arquivo. Se executar o programa várias vezes, ele continuará adicionando essa frase ao final do arquivo, sem remover os dados anteriores.


## métodos do arquivo

A função `open()` em Python retorna um objeto de arquivo, que possui vários métodos para manipular seu conteúdo. Dentre os mais importantes, há os métodos `read()`, `readline()`, `readlines()`, `write()` e `writelines()`.

### `read()`

O método `read()` lê o conteúdo de um arquivo inteiro (ou parte dele, dependendo dos parâmetros passados).

Veja sua sintaxe :

```python
conteudo = arquivo.read(tamanho)
```

- **tamanho** (opcional): é o número de caracteres ou bytes a serem lidos; se omitido, `read()` lê o arquivo inteiro;

#### exemplo

```python
arquivo = open('exemplo.txt', 'r')

# lendo todo o conteúdo do arquivo
conteudo = arquivo.read()
print(conteudo)

arquivo.close()
```

Se o arquivo `exemplo.txt` contiver :
```
Primeira linha
Segunda linha
Terceira linha
```

A saída será :
```
Primeira linha
Segunda linha
Terceira linha
```

#### lendo parte do arquivo :

É possível especificar quantos caracteres ler com o argumento `tamanho`. Por exemplo:

```python
arquivo = open('exemplo.txt', 'r')

# lendo apenas os primeiros 10 caracteres
conteudo = arquivo.read(10)
print(conteudo)

arquivo.close()
```

Se o conteúdo do arquivo for o mesmo, a saída será :
```
Primeira
```

Aqui, foram lidos os primeiros 10 caracteres do arquivo.

### `readline()`

O método `readline()` lê **uma linha** do arquivo por vez. Ele é útil quando se deseja processar o arquivo linha por linha.

Veja sua sintaxe :

```python
linha = arquivo.readline(tamanho)
```

- **tamanho** (opcional) : limita o número máximo de caracteres a serem lidos da linha;

#### exemplo

```python
arquivo = open('exemplo.txt', 'r')

# lendo a primeira linha do arquivo
linha = arquivo.readline()
print(linha)

arquivo.close()
```

Se o arquivo contiver :
```
Primeira linha
Segunda linha
Terceira linha
```

A saída será :
```
Primeira linha
```

#### lendo todas as linhas com `readline()`

Se quiser ler todas as linhas do arquivo, pode usar um loop :

```python
arquivo = open('exemplo.txt', 'r')

linha = arquivo.readline()
while linha:
    print(linha, end='')  # end='' evita uma linha extra ao final
    linha = arquivo.readline()

arquivo.close()
```

A saída será:
```
Primeira linha
Segunda linha
Terceira linha
```

#### limitando o número de caracteres por linha

É possível limitar o número de caracteres que serão lidos por linha :

```python
arquivo = open('exemplo.txt', 'r')

# lendo apenas os primeiros 8 caracteres da primeira linha
linha = arquivo.readline(8)
print(linha)

arquivo.close()
```

Isso resultará em:
```
Primeira
```

### `readlines()`

O método `readlines()` lê **todas as linhas do arquivo de uma só vez** e as armazena em uma **lista**, onde cada linha é um elemento.

Veja sua sintaxe :

```python
linhas = arquivo.readlines()
```

#### exemplo
```python
arquivo = open('exemplo.txt', 'r')

# lendo todas as linhas do arquivo
linhas = arquivo.readlines()

# imprimindo a lista de linhas
print(linhas)

arquivo.close()
```

Se o arquivo contiver :

```
Primeira linha
Segunda linha
Terceira linha
```

A saída será :

```python
['Primeira linha\n', 'Segunda linha\n', 'Terceira linha\n']
```

Aqui, cada linha do arquivo se torna um item da lista. Note que os caracteres de nova linha (`\n`) são preservados.

Logo, é possível iterar sobre essa lista para processar cada linha individualmente :

```python
arquivo = open('exemplo.txt', 'r')

# lendo todas as linhas do arquivo
linhas = arquivo.readlines()

# iterando sobre as linhas e imprimindo uma a uma
for linha in linhas:
    print(linha, end='')

arquivo.close()
```

Isso exibirá :

```
Primeira linha
Segunda linha
Terceira linha
```

### `readline()` vs `readlines()`

Em suma :

- `readline()` lê **uma linha** por vez;
- `readlines()` lê **todas as linhas** de uma vez e as retorna como uma lista;

### `write()`

O método `write()` é usado para **escrever dados em um arquivo**. Pode ser utilizado em modos de escrita (`'w'`, `'a'`, `'w+'`, `'a+'`, etc.). Lembre-se de que o método **não adiciona automaticamente uma nova linha**, então precisará incluir `\n` manualmente se quiser pular linhas.

Veja a sintaxe :

```python
arquivo.write(texto)
```

- **texto**: é o conteúdo que você deseja escrever no arquivo. deve ser uma string;

#### exemplo

```python
arquivo = open('exemplo.txt', 'w')

# escrevendo texto no arquivo
arquivo.write("Primeira linha\n")
arquivo.write("Segunda linha\n")

arquivo.close()
```

Aqui :
- o arquivo `exemplo.txt` será sobrescrito (ou criado se não existir);
- o método `write()` insere as linhas fornecidas no arquivo;
- o `\n` é necessário para garantir que cada linha seja escrita em uma nova linha no arquivo;

#### exemplo

Se quiser **anexar** (adicionar) novas informações ao final de um arquivo, pode abrir o arquivo no modo de anexar (`'a'`) :

```python
arquivo = open('exemplo.txt', 'a')

# adicionando uma nova linha ao final do arquivo
arquivo.write("Terceira linha adicionada\n")

arquivo.close()
```

Isso não sobrescreverá o conteúdo existente, mas adicionará a nova linha ao final do arquivo.

#### importante :

- o método `write()` **não adiciona quebras de linha automaticamente**; portanto, se quiser que o texto vá para a próxima linha, adicione `\n` no final da string que está escrevendo;
- se usar o modo `'w'`, o arquivo será **sobrescrito**; todo o conteúdo anterior será apagado;

### `writelines()`

O método `writelines()` em Python é usado para **escrever uma sequência de strings** em um arquivo de uma só vez. A sequência pode ser uma lista, tupla ou qualquer objeto iterável que contenha strings.

Diferentemente do método `write()`, que escreve uma única string de cada vez, o `writelines()` permite escrever várias linhas de uma só vez, **sem adicionar automaticamente quebras de linha** (`\n`). Se quiser que cada linha seja escrita em uma nova linha no arquivo, precisará incluir manualmente o caractere de nova linha (`\n`) ao final de cada string da sequência.

Veja a sintaxe :

```python
arquivo.writelines(iteravel)
```

- **iterável**: um objeto que contém múltiplas strings, como uma lista ou tupla;

#### exemplo :

Aqui está um exemplo de como usar `writelines()` para escrever várias linhas em um arquivo :

```python
# abrindo o arquivo no modo de escrita
arquivo = open('exemplo.txt', 'w')

# lista de linhas para serem escritas
linhas = ["Primeira linha\n", "Segunda linha\n", "Terceira linha\n"]

# escrevendo todas as linhas no arquivo de uma vez
arquivo.writelines(linhas)

# fechando o arquivo
arquivo.close()
```

Neste exemplo :
- o arquivo `exemplo.txt` será criado ou sobrescrito;
- as três linhas da lista `linhas` são escritas de uma só vez no arquivo;
- note que cada string na lista termina com `\n` para garantir que as linhas sejam separadas no arquivo;

#### importante

O método `writelines()` **não adiciona automaticamente quebras de linha** (`\n`). Se as strings no iterável não tiverem `\n`, elas serão escritas consecutivamente, sem separação.

```python
arquivo = open('exemplo.txt', 'w')

# lista de linhas sem \n
linhas = ["Primeira linha", "Segunda linha", "Terceira linha"]

# escrevendo todas as linhas no arquivo
arquivo.writelines(linhas)

arquivo.close()
```

Neste caso, o conteúdo do arquivo será :

```
Primeira linhaSegunda linhaTerceira linha
```

#### iteráveis além de listas

É também possível usar qualquer objeto iterável que contenha strings, como uma tupla ou até um gerador.

#### exemplo com uma tupla

```python
arquivo = open('exemplo.txt', 'w')

# tupla de strings
linhas = ("Linha 1\n", "Linha 2\n", "Linha 3\n")

arquivo.writelines(linhas)

arquivo.close()
```

#### exemplo com um gerador

```python
arquivo = open('exemplo.txt', 'w')

# gerador de strings
linhas = (f"Linha {i}\n" for i in range(1, 4))

arquivo.writelines(linhas)

arquivo.close()
```

## `close()`

O método **`close()`** em Python é utilizado para **fechar um arquivo** que foi previamente aberto. Quando um arquivo é aberto com a função `open()`, ele ocupa recursos do sistema, como memória e descritores de arquivo, e precisa ser fechado para liberar esses recursos corretamente. Além disso, ao fechar um arquivo, todas as operações de leitura e escrita pendentes são finalizadas e os dados são garantidamente gravados no disco.

### detalhes

- **liberação de recursos**: fechar o arquivo libera os recursos do sistema operacional associados a ele. Se um arquivo permanecer aberto por muito tempo, especialmente em grandes aplicações, isso pode resultar em esgotamento de descritores de arquivo, levando a erros;

- **garantia de gravação completa**: para arquivos abertos para escrita, o método `close()` assegura que qualquer dado pendente seja gravado corretamente no disco. Se o arquivo não for fechado após a escrita, algumas mudanças podem não ser aplicadas (especialmente se os dados estiverem armazenados em buffers temporários);

- **após fechar o arquivo**: uma vez que o arquivo é fechado, não é possível realizar mais operações de leitura ou escrita até que ele seja reaberto;

### exemplo

```python
# abrindo um arquivo para escrita
arquivo = open('exemplo.txt', 'w')

# escrevendo dados no arquivo
arquivo.write("Este é um exemplo de uso do método close.\n")

# fechando o arquivo após a escrita
arquivo.close()
```

Aqui :
- o arquivo `exemplo.txt` foi aberto no modo de escrita (`'w'`);
- foi escrita uma linha de texto no arquivo;
- foi usado o método `arquivo.close()` para fechar o arquivo e garantir que os dados sejam salvos corretamente;

### efeitos de não fechar o arquivo

Se o método `close()` não for usado, pode causar problemas em certos cenários :

1. **dados não gravados** : no caso de operações de escrita, se o arquivo não for fechado, o python pode não gravar os dados imediatamente no arquivo físico; isso ocorre porque os sistemas operacionais frequentemente armazenam dados temporariamente em um buffer para otimizar o desempenho. o `close()` força a gravação final desses dados no disco.

Exemplo :

```python
arquivo = open('exemplo.txt', 'w')
arquivo.write("Texto sem fechar o arquivo.")
# Sem o close(), o texto pode não ser gravado completamente no arquivo.
```

2. **vazamento de recursos** : não fechar um arquivo pode levar a um vazamento de descritores de arquivo, especialmente em sistemas que têm um limite sobre o número de arquivos que podem ser abertos simultaneamente; isso pode resultar em erros ao tentar abrir novos arquivos.

3. **erros ao tentar acessar um arquivo já fechado** : se tentar ler ou escrever em um arquivo após tê-lo fechado, o python gerará um erro.

Exemplo :

```python
arquivo = open('exemplo.txt', 'r')
arquivo.close()
conteudo = arquivo.read()  # Tentativa de ler após fechar o arquivo
```

O Python levantará um erro `ValueError` :

```
ValueError: I/O operation on closed file.
```

### importância de `close()` com grandes volumes de dados

Quando trabalha com arquivos grandes ou abre muitos arquivos em sequência, o fechamento adequado dos arquivos torna-se ainda mais crítico. Manter arquivos abertos sem fechá-los pode resultar em erros como:

- **`OSError: Too many open files`** : se muitos arquivos forem abertos ao mesmo tempo sem serem fechados, o sistema pode esgotar seu limite de descritores de arquivo, o que gera este erro; fechar os arquivos conforme eles são usados ajuda a evitar esse problema.


## exercícios

<details>
<summary>Lista de Exercícios</summary>

1. exercícios sobre o método `read()`
    1. Abra um arquivo de texto chamado `dados.txt` e use o método `read()` para ler todo o conteúdo. Exiba o conteúdo no terminal.
    1. Crie um arquivo chamado `historico.txt`, escreva nele cinco frases e leia todo o conteúdo usando `read()`. Exiba as frases lidas.
    1. Abra o arquivo `historico.txt` e leia os primeiros 20 caracteres do arquivo usando `read()`. Exiba os caracteres no terminal.
    1. Crie um arquivo `poema.txt` com três estrofes de um poema. Use `read()` para ler todo o poema e exibi-lo no terminal.
    1. Crie um programa que abre o arquivo `numeros.txt` e usa `read()` para ler todo o conteúdo. Depois, converta o texto em uma lista de inteiros.
    1. Abra o arquivo `paragrafo.txt` contendo um parágrafo de texto e leia os primeiros 50 caracteres com `read()`.
    1. Crie um arquivo `livro.txt` contendo três capítulos de um livro. Leia o primeiro capítulo (considerando 1000 caracteres) com o método `read()`.
    1. Escreva um programa que lê o conteúdo completo de um arquivo `mensagem.txt` e conta o número de palavras usando `read()`.
    1. Crie um arquivo `diario.txt` e escreva 5 entradas de diário. Depois, leia e exiba as duas primeiras entradas (aproximadamente 100 caracteres) usando `read()`.
    1. Crie um arquivo `contos.txt` e escreva dois contos curtos. Use o método `read()` para ler o primeiro conto (aproximadamente 500 caracteres).
1. exercícios sobre o método `readline()`
    1. Crie um arquivo `compras.txt` com uma lista de compras (uma por linha). Leia e exiba a primeira linha usando o método `readline()`.
    1. Abra o arquivo `compras.txt` e use `readline()` para ler e exibir as três primeiras linhas.
    1. Crie um programa que abra o arquivo `agenda.txt` e use `readline()` para ler cada linha individualmente, mostrando o conteúdo no terminal.
    1. Abra o arquivo `alunos.txt`, que contém o nome de 10 alunos, e leia o nome do primeiro aluno usando `readline()`.
    1. Crie um programa que abra o arquivo `mensagens.txt` e leia cada linha usando um loop `while` até o final do arquivo, exibindo cada mensagem no terminal.
    1. Abra o arquivo `livros.txt` contendo uma lista de livros. Use `readline()` para ler e exibir o título do segundo livro.
    1. Crie um arquivo `tarefas.txt` com 5 tarefas diárias. Use `readline()` para ler e exibir todas as tarefas uma a uma em um loop.
    1. Crie um programa que leia as primeiras três linhas de um arquivo `nomes.txt` e exiba os nomes no terminal.
    1. Abra um arquivo `frases.txt` e leia frases usando `readline()`. Exiba apenas as frases que contêm mais de 50 caracteres.
    1. Crie um programa que leia um arquivo `receitas.txt` e use `readline()` para exibir uma receita de cada vez.
1. exercícios sobre o método `readlines()`
    1. Abra um arquivo `notas.txt` contendo as notas de 10 alunos, uma por linha. Use `readlines()` para ler todas as linhas de uma vez e exiba-as como uma lista.
    1. Crie um arquivo `filmes.txt` com 5 títulos de filmes, um por linha. Use `readlines()` para ler e exibir todos os títulos no terminal.
    1. Abra o arquivo `tarefas.txt`, use `readlines()` para ler todas as tarefas de uma vez e exiba a terceira tarefa da lista.
    1. Crie um arquivo `produtos.txt` com uma lista de produtos. Use `readlines()` para ler todos os produtos e depois exiba-os em ordem reversa.
    1. Escreva um programa que abre um arquivo `frases.txt`, leia todas as frases com `readlines()` e exiba apenas as frases que têm mais de 20 caracteres.
    1. Crie um arquivo `contatos.txt` com nomes e números de telefone, um por linha. Use `readlines()` para armazenar os contatos em uma lista.
    1. Abra o arquivo `livros.txt`, leia todas as linhas com `readlines()` e exiba o número total de linhas lidas.
    1. Crie um arquivo `dicionario.txt` com palavras e seus significados, uma por linha. Use `readlines()` para ler todas as palavras e exibi-las em formato de lista.
    1. Abra um arquivo `amigos.txt` e use `readlines()` para ler todos os nomes. Em seguida, exiba o primeiro e o último nome da lista.
    1. Crie um programa que leia todas as linhas de um arquivo `dados.txt` com `readlines()` e armazene-as em uma lista. Em seguida, itere sobre a lista e exiba cada linha com seu número de linha correspondente.
1. exercícios sobre o método `write()`
    1. Crie um arquivo `saida.txt` e escreva a frase "Python é incrível!" usando o método `write()`.
    1. Crie um programa que abre ou cria um arquivo `registro.txt` e usa o método `write()` para adicionar a frase "Registro de atividades".
    1. Escreva um programa que crie um arquivo `numeros.txt` e adicione os números de 1 a 10, cada número em uma linha, usando o método `write()`.
    1. Crie um arquivo `diario.txt` e use `write()` para adicionar uma entrada de diário contendo a data e um texto qualquer.
    1. Abra ou crie um arquivo `notas.txt` e escreva as notas de três matérias usando o método `write()`.
    1. Crie um arquivo `tarefa.txt` e use `write()` para adicionar três tarefas diárias. Certifique-se de usar `\n` para separar as tarefas em linhas diferentes.
    1. Abra o arquivo `mensagem.txt` e use `write()` para sobrescrever seu conteúdo com a frase "Novo conteúdo escrito com write()".
    1. Crie um arquivo `historico.txt` e use `write()` para registrar o histórico de eventos, escrevendo uma nova linha a cada execução.
    1. Escreva um programa que abra um arquivo `log.txt` e use `write()` para registrar a hora atual do sistema a cada execução do programa.
    1. Crie um arquivo `lista_de_compras.txt` e use o método `write()` para adicionar 5 itens de compras. Cada item deve estar em uma linha separada.
1. Exercícios sobre o Método `writelines()`
    1. Crie um arquivo `nomes.txt` e use o método `writelines()` para escrever uma lista de nomes (cada nome em uma linha).
    1. Crie um arquivo `numeros.txt` e use `writelines()` para escrever os números de 1 a 10, cada um em uma linha separada.
    1. Crie um programa que abre ou cria um arquivo `agenda.txt` e usa `writelines()` para adicionar três compromissos, cada um em uma linha.
    1. Crie um arquivo `tarefas.txt` e use `writelines()` para adicionar cinco tarefas de uma lista, cada tarefa em uma linha separada.
    1. Escreva um programa que cria ou abre um arquivo `cidades.txt` e usa `writelines()` para adicionar o nome de três cidades, cada uma em uma linha.
    1. Crie um arquivo `frutas.txt` e use `writelines()` para adicionar o nome de cinco frutas em uma lista, cada nome em uma linha.
    1. Abra ou crie um arquivo `enderecos.txt` e use `writelines()` para adicionar três endereços, cada um em uma linha.
    1. Escreva um programa que cria um arquivo `historico.txt` e usa `writelines()` para adicionar três eventos, cada evento em uma linha separada.
    1. Crie um programa que abre o arquivo `receitas.txt` e usa `writelines()` para adicionar três receitas, cada receita em uma linha separada.
    1. Crie um arquivo `projetos.txt` e use `writelines()` para adicionar os títulos de três projetos de uma lista, cada título em uma linha.

</details>

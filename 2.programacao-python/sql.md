# SQL

O SQL (Structured Query Language) é uma linguagem de programação usada para gerenciar dados em bancos de dados relacionais. O SQL é usado para executar operações como inserir, atualizar, selecionar e excluir dados de um banco de dados.

O SQL funciona através de comandos que são escritos em uma sintaxe específica. Os comandos do SQL são executados em um servidor de banco de dados que recebe as consultas, processa as instruções e retorna os resultados.

Existem várias instruções SQL que podem ser usadas para manipular dados em um banco de dados. Algumas das instruções mais comuns incluem :

- `SELECT` : é usada para recuperar dados de uma ou mais tabelas no banco de dados. A consulta `SELECT` permite filtrar e selecionar apenas os dados desejados;
- `INSERT` : é usada para inserir dados em uma tabela no banco de dados;
- `UPDATE` : é usada para atualizar dados existentes em uma tabela;
- `DELETE` : é usada para excluir dados de uma tabela;
- `CREATE` : é usada para criar uma nova tabela no banco de dados;
- `DROP` : é usada para excluir uma tabela do banco de dados;
- `ALTER` : é usada para modificar a estrutura de uma tabela existente;
- `JOIN` : é usada para combinar dados de duas ou mais tabelas em uma única consulta;
- `GROUP BY` : é usada para agrupar dados com base em uma ou mais colunas;
- `ORDER BY` : é usada para classificar os dados com base em uma ou mais colunas;

Para executar essas instruções, é necessário conectar-se ao servidor do banco de dados usando um software cliente que permita a entrada de comandos SQL. É possível conectar-se a um banco de dados local ou remoto usando um software cliente SQL como MySQL Workbench, pgAdmin, Oracle SQL Developer, entre outros.

Os comandos SQL são enviados do software cliente para o servidor do banco de dados para serem processados e executados. O servidor responde ao cliente com os resultados da consulta.

## sqlite

O [SQLite](https://www.sqlite.org/) é um sistema de gerenciamento de banco de dados relacional que suporta vários tipos de dados. Alguns dos tipos de dados suportados pelo SQLite são :

- `NULL` : usado para representar valores nulos ou ausentes;
- `INTEGER` : usado para armazenar números inteiros; o SQLite tem suporte para diferentes tipos de inteiros, como TINYINT, SMALLINT, MEDIUMINT, INT e BIGINT;
- `REAL` : usado para armazenar números de ponto flutuante, como números decimais;
- `TEXT` : usado para armazenar dados de texto, como nomes, descrições, mensagens etc; o SQLite suporta várias codificações de caracteres, como ASCII, UTF-8, UTF-16, entre outras;
- `BLOB` : usado para armazenar dados binários, como imagens, arquivos de áudio e vídeo;

O SQLite é um banco de dados relacional que é usado em muitos aplicativos para armazenar e acessar dados. É uma escolha popular para projetos de pequena escala, pois é leve e fácil de usar.

O Python possui uma biblioteca nativa para trabalhar com bancos de dados SQLite chamada `sqlite3`, presente desde a versão 2.5.

### básico

A seguir, há um passo a passo para usar o SQLite com o Python :

1. Importe a biblioteca 'sqlite3' :

    Antes de começar a trabalhar com o SQLite em Python, deve-se importar a biblioteca `sqlite3`.

    Para fazer isso, basta digitar :

    ```python
    import sqlite3
    ```

1. Conectando-se ao banco de dados :

    O próximo passo é conectar-se ao banco de dados SQLite. Para fazer isso, é preciso especificar o nome do arquivo de banco de dados SQLite. Se o arquivo não existir, ele será criado. Caso contrário, a conexão será estabelecida com o arquivo existente.

    ```python
    conn = sqlite3.connect('exemplo.db')
    ```

1. Criando uma tabela no banco de dados :

    Depois de estabelecer a conexão com o banco de dados, o próximo passo é criar uma tabela para armazenar nossos dados. Isso pode ser feito executando uma consulta SQL "CREATE TABLE" que especifica os nomes e tipos de coluna que deseja criar.

    ```python
    c = conn.cursor()

    query = '''
    CREATE TABLE usuarios
    (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        idade INTEGER
    )
    '''

    c.execute(query)
    ```

    Neste exemplo, está sendo criado uma tabela chamada `usuarios` com três colunas: `id`, `nome` e `idade`. A coluna `id` é definida como uma chave primária.

1. Inserindo dados na tabela :

    Agora que a tabela foi criada, é possível inserir dados nela. Para fazer isso, é preciso executar uma consulta SQL `INSERT` que insere os valores nas colunas correspondentes.

    ```python
    c.execute("INSERT INTO usuarios (nome, idade) VALUES ('Tutankamon', 15)")
    ```

    O comando `execute()` vai executar um comando no banco de dados.

1. Executar consultas no banco de dados :

    Depois de inserir dados na tabela, é possível executar consultas SQL `SELECT` para recuperar os dados da tabela. Isso pode ser feito usando o método `execute()` para executar a consulta e o método `fetchall()` para obter os resultados.

    ```python
    c.execute("SELECT * FROM usuarios")
    linhas = c.fetchall()

    for linha in linhas:
        print(linha)
    ```

    Este código executa uma consulta para selecionar todos os registros da tabela `usuarios` e, em seguida, exibe os resultados na tela.

1. Fechar a conexão com o banco de dados :

    Por fim, é importante fechar a conexão com o banco de dados após concluir todas as operações. Para fazer isso, usa-se o método `close()`.

    ```python
    conn.close()
    ```

1. Abaixo, há um exemplo completo de uma agenda telefônica :

    ```python
    import sqlite3

    # conecta-se ao banco de dados
    conn = sqlite3.connect('agenda.db')

    # cria uma tabela de contatos
    c = conn.cursor()

    query = '''
    CREATE TABLE contatos
    (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        telefone TEXT
    )'''
    c.execute(query)

    # insere contatos na tabela
    c.execute("INSERT INTO contatos (nome, telefone) VALUES (?, ?)", ('João Silva', '555-1234'))
    c.execute("INSERT INTO contatos (nome, telefone) VALUES (?, ?)", ('Maria Santos', '555-9876'))
    c.execute("INSERT INTO contatos (nome, telefone) VALUES (?, ?)", ('Pedro Souza', '555-5555'))

    # salva as alterações no banco de dados
    conn.commit()

    # executar uma consulta para recuperar todos os contatos da tabela
    c.execute("SELECT * FROM contatos")
    linhas = c.fetchall()

    # exibe os resultados na tela
    print("Contatos:")
    for lin
    ha in linhas:
        print(f"{linha[0]} - {linha[1]}: {linha[2]}")

    # fecha a conexão com o banco de dados
    conn.close()
    ```

    Neste exemplo, foi criada uma tabela chamada `contatos` com três colunas: `id`, `nome` e `telefone`. Em seguida, três contatos foram inseridos na tabela usando a query `INSERT`.

    Depois, as alterações no banco de dados são salvas usando o método `commit()`. Em seguida,  uma query com `SELECT` é usada para selecionar todos os registros da tabela. O método `fetchall()` é usado para obter todos os resultados.

    Por fim, os resultados são mostrados no terminal para visualizar os contatos adicionados na tabela.

    Note que para inserir os valores na tabela, foi usado o sinal de `interrogação (?)` como marcador de posição na consulta SQL, seguido pelos valores a serem inseridos na tabela. Isso é conhecido como `binding de parâmetros` e é uma técnica importante para evitar injeção de SQL e outros problemas de segurança.

## comando `SELECT`

É possível buscar dados e os filtrar eles usando a cláusula `WHERE`.

Veja o exemplo abaixo de uma atualização do código acima da agenda :

```python
# solicita o ID do contato a ser recuperado
contato_id = int(input("Digite o ID do contato que deseja visualizar: "))

# executar uma consulta para recuperar o contato especificado pelo usuário
c.execute("SELECT * FROM contatos WHERE id = ?", (contato_id,))
linha = c.fetchone()

# exibe o resultado na tela
if linha:
    pri
    nt(f"{linha[0]} - {linha[1]}: {linha[2]}")
else:
    print("Contato não encontrado")
```

Nesta ampliação do código, é pedido para o usuário digitar um ID do contato que quer visualizar. A função `fetchone()`, diferente da `fetchall()`, retorna apenas um registro.

Se nenhum registro corresponder ao ID especificado, exibimos uma mensagem informando que o contato não foi encontrado.

### campos específicos

Para buscar apenas os nomes dos contatos registrados na tabela `contatos` do exemplo da agenda, pode-se executar uma consulta SQL `SELECT` que seleciona apenas a coluna `nome`.

```python
# executa uma consulta para buscar apenas os nomes dos contatos
c.execute("SELECT nome FROM contatos")

# recupera os resultados da consulta e exibi-los na tela
resultados = c.fetchall()
for nome in resultados:
    print(nome[0])
```

Neste exemplo, foi executada uma query com `SELECT` que seleciona apenas a coluna `nome` da tabela `contatos`. Em seguida, o método `fetchall()` é usado para recuperar os resultados da consulta. Um loop `for` para exibir cada nome na tela.

Observe que, ao recuperar os resultados da consulta usando o método `fetchall()`, é retornado uma lista de tuplas, onde cada tupla representa um registro na tabela `contatos` contendo apenas um valor (o nome).

Por isso, ao exibir os nomes na tela no loop `for`, é usado a expressão `nome[0]` para acessar o primeiro valor da tupla (o nome).

### comando `IN`

A instrução SQL `IN` é usada para verificar se um valor está presente em uma lista de valores. A cláusula `IN` pode ser usada em uma consulta SQL para selecionar apenas os contatos cujos nomes estejam em uma lista específica.

```python
# seleciona apenas os contatos cujos nomes estão na lista
nomes = ['Alice', 'Bob', 'Carol']
c.execute(f"SELECT * FROM contatos WHERE nome IN ({', '.join(['?']*len(nomes))})", nomes)
resultados = c.fetchall()

# exibe os resultados na tela
for resultado in resultados:
    pri
    nt(f"{resultado['nome']}: {resultado['telefone']}")
```

Observe como a cláusula `WHERE` é usada para especificar que apenas os contatos cujos nomes estão na lista `nomes` sejam buscados. O método `.join()` é usado para juntar as strings na lista com vírgulas e, em seguida, a lista de nomes é passada como um segundo argumento para o método `execute`. Isso garante que os valores na lista sejam escapados corretamente antes de serem usados na consulta.

### comando `LIKE`

Para recuperar apenas os contatos que começam com a letra `A` (ou qualquer outra letra), pode-se usar a cláusula `WHERE` em sua consulta SQL com uma expressão de comparação.

```python
# inserindo mais contatos na tabela
c.execute("INSERT INTO contatos (nome, telefone) VALUES (?, ?)", ('Ana Paula', '555-7777'))
c.execute("INSERT INTO contatos (nome, telefone) VALUES (?, ?)", ('Alberto Santos', '555-8888'))

# executar uma consulta para recuperar apenas os contatos que começam com a letra "A"
c.execute("SELECT * FROM contatos WHERE nome LIKE 'A%'")

# recuperar os resultados da consulta e exibi-los na tela
resultados = c.fetchall()
for contato in resultados:
    print(contato)
```

Neste exemplo, após inserir os contatos na tabela, é executada uma consulta SQL `SELECT` para recuperar apenas os contatos cujo nome começa com a letra `A`. A cláusula `WHERE` é usada para especificar uma condição de filtragem que compara o valor da coluna `nome` com a expressão `'A%'`, que significa `qualquer valor que comece com a letra A`.

Em seguida, o método `fetchall()` é usada para recuperar os resultados da consulta, que são exibidos usando um loop `for`.

Observe que, neste exemplo, o operador `LIKE` foi usado para comparar os valores da coluna `nome`. Este operador permite que se use caracteres curinga (como `%` e `_`) para corresponder a qualquer sequência de caracteres ou um único caractere, respectivamente. Por exemplo, a expressão `'A%'` corresponde a qualquer valor que comece com a letra A, enquanto a expressão `%Paula` corresponde a qualquer valor que termine com a sequência `Paula`.

### comando `LIMIT`

Pode-se usar a condição `LIMIT` para limitar a quantidade de registros que se quer buscar.

Veja abaixo como usar na agenda :

```python
# executar uma consulta para buscar pelos 2 primeiros registros
c.execute("SELECT * FROM contatos LIMIT 2")
linhas = c.fetchall()
```

Neste exemplo, após inserir os contatos na tabela, executamos uma consulta SQL "SELECT" para selecionar os 2 primeiros registros da tabela, usando a cláusula `LIMIT 2`.

Em seguida, usa-se o método `fetchall()` para obter uma lista de todos os registros selecionados.

Observe que, neste exemplo, não foi solicitada a entrada do usuário, mas sim buscada diretamente pelos 2 primeiros registros da tabela. Se quiser permitir que o usuário especifique o número de registros a serem exibidos, basta modificar a consulta SQL para incluir uma variável que contenha o número de registros desejados, por exemplo: `LIMIT ?`, e passar o número de registros como um parâmetro na chamada de `execute()`.

### comando `ORDER BY`

A instrução SQL `ORDER BY` é usada para classificar as linhas de uma consulta em ordem crescente ou decrescente com base no valor de uma ou mais colunas. No exemplo da agenda, pode-se usar `ORDER BY` para classificar os contatos em ordem alfabética com base em seus nomes.

```python
# seleciona todos os contatos, classificados em ordem alfabética por nome
c.execute("SELECT * FROM contatos ORDER BY nome ASC")
resultados = c.fetchall()

for resultado in resultados:
    print(f"{resultado['nome']}: {resultado['telefone']}")
```

Observe como `ASC` é usado para classificar em ordem crescente. Se quiser classificar em ordem decrescente, pode-se usar `DESC` em vez de `ASC`.

## comando `COMMIT`

Em um banco de dados SQLite, o comando `COMMIT` é usado para confirmar as alterações feitas nas tabelas do banco de dados. Quando se faz uma alteração em uma tabela, como uma `inserção`, `atualização` ou `exclusão`, a alteração não é imediatamente gravada no disco, mas é armazenada em uma área temporária chamada `transação`. O objetivo dessa área é permitir que várias alterações sejam agrupadas e aplicadas de uma só vez, o que pode melhorar o desempenho e garantir a integridade dos dados.

O comando `COMMIT` é usado para confirmar todas as alterações realizadas na transação e gravar as alterações no disco. Se ocorrer um erro antes do comando `COMMIT` ser executado, as alterações serão revertidas e o banco de dados retornará ao seu estado anterior.

Veja um exemplo de como usar o comando `COMMIT` ao atualizar um registro na tabela `contatos` na agenda :

```python
# conecta ao banco de dados e obtém um cursor
conn = sqlite3.connect('agenda.db')
c = conn.cursor()

# atualiza o telefone do contato com nome 'Alice'
c.execute("UPDATE contatos SET telefone = ? WHERE nome = ?", ('555-1234', 'Alice'))

# confirma as alterações no banco de dados
conn.commit()

# fecha a conexão com o banco de dados
conn.close()
```

Observe como o método `commit()` é chamado após a atualização do registro. Isso garante que a atualização seja confirmada no banco de dados e persista mesmo após o programa ser encerrado.

É importante lembrar que o comando `COMMIT` deve ser usado com cuidado, pois pode causar perda de dados se usado incorretamente. Em geral, é uma boa prática executar o comando `COMMIT` apenas depois que todas as alterações na transação forem concluídas e verificadas.

## comando `UPDATE`

Para atualizar um registro na tabela de contatos, usa-se a cláusula `UPDATE` em uma consulta SQL.

```python
# solicita o ID do contato a ser atualizado
contato_id = int(input("Digite o ID do contato que deseja atualizar: "))

# solicita o novo número de telefone
novo_telefone = input("Digite o novo número de telefone: ")

# executar uma consulta para atualizar o número de telefone do contato especificado pelo usuário
c.execute("UPDATE contatos SET telefone = ? WHERE id = ?", (novo_telefone, contato_id))

# salva as alterações no banco de dados
conn.commit()

# exibe uma mensagem de confirmação na tela
print("Contato atualizado com sucesso")
```

Neste exemplo, após inserir os contatos na tabela, é solicitado ao usuário que digite o `ID` do contato que deseja atualizar e o novo número de telefone.

Em seguida, uma consulta SQL `UPDATE` é executada para atualizar o número de telefone do contato especificado, usando o operador `=` na cláusula `WHERE`. Observe que, neste caso, são usados dois sinais de interrogação na chamada de `execute()` para passar dois parâmetros: o novo número de telefone e o ID do contato.

Finalmente, o método `commit()` é usado para salvar as alterações no banco de dados e exibir uma mensagem de confirmação.

Observe que, neste exemplo, apenas o número de telefone do contato é atualizado. Se quiser permitir que o usuário atualize outros campos, basta modificar a consulta SQL para incluir as colunas e os novos valores correspondentes.

## comando `DELETE`

Para apagar um registro da tabela `contatos` no exemplo da agenda, pode-se executar uma consulta SQL `DELETE` que selecione o registro a ser excluído com base em sua chave primária.

```python
# apaga o contato com o ID 3
c.execute("DELETE FROM contatos WHERE id = ?", (3,))

# exibe todos os contatos restantes na tabela
c.execute("SELECT * FROM contatos")
resulta
dos = c.fetchall()
for contato in resultados:
    print(contato)
```

Neste exemplo, uma consulta SQL `DELETE` é executada e exclui o contato com o ID 3 da tabela `contatos`. Em seguida, uma consulta SQL `SELECT` é usada para recuperar todos os contatos restantes na tabela.

Observe que, ao executar a consulta SQL `DELETE`, usou-se um `ponto de interrogação (?)` como um marcador de posição para o valor do ID do contato a ser excluído. Em seguida, é passado o valor real do ID do contato como um segundo argumento para o método `execute()` na forma de uma tupla com um único elemento. Lembrando, isso evita vulnerabilidades de segurança como a injeção de SQL.

## `Foreign Key` e `JOIN`

Como visto anteriormente, usou-se uma `Chave Primária (Primary Key - PK)` para garantir que os registros na tabela sejam únicos. Além disso, a PK tem outra funcionalidade, que é garantir que os dados entre tabelas sejam íntegros através da `Chave Estrangeira (Foreign Key - FK)`.

Usando a agenda como exemplo para duas tabelas, pode-se criar uma tabela `contatos` que armazena informações básicas de contato (como nome e telefone) e uma tabela `enderecos` que armazena informações de endereço para cada contato. Pode-se então juntar essas tabelas usando a chave primária de `contatos` como uma chave estrangeira em `enderecos`.

```python
import sqlite3

# conecta-se ao banco de dados
conn = sqlite3.connect('agenda.db')

# cria uma tabela de contatos
c = conn.cursor()
c.execute('''
CREATE TABLE contatos
(
    id INTEGER PRIMARY KEY,
    nome TEXT,
    telefone TEXT
)
''')

# cria uma tabela de endereços
c.execute('''
CREATE TABLE enderecos
(
    id INTEGER PRIMARY KEY,
    contato_id INTEGER,
    rua TEXT,
    cidade TEXT,
    estado TEXT,
    cep TEXT,
    FOREIGN KEY(contato_id) REFERENCES contatos(id))
'''
)

# insere alguns contatos e endereços na tabela
c.execute(
    "INSERT INTO contatos (nome, telefone) VALUES (?, ?)",
    ('João Silva', '555-1234'))
contato_id = c.lastrowid
c.execute(
    "INSERT INTO enderecos (contato_id, rua, cidade, estado, cep) VALUES (?, ?, ?, ?, ?)",
    (contato_id, 'Rua A', 'São Paulo', 'SP', '01001-000'))

c.execute(
    "INSERT INTO contatos (nome, telefone) VALUES (?, ?)",
    ('Maria Santos', '555-9876'))
contato_id = c.lastrowid
c.execute(
    "INSERT INTO enderecos (contato_id, rua, cidade, estado, cep) VALUES (?, ?, ?, ?, ?)",
    (contato_id, 'Rua B', 'Rio de Janeiro', 'RJ', '02002-000'))

c.execute(
    "INSERT INTO contatos (nome, telefone) VALUES (?, ?)",
    ('Pedro Souza', '555-5555'))
contato_id = c.lastrowid
c.execute(
    "INSERT INTO enderecos (contato_id, rua, cidade, estado, cep) VALUES (?, ?, ?, ?, ?)",
    (contato_id, 'Rua C', 'Belo Horizonte', 'MG', '03003-000'))

# seleciona todos os contatos com seus respectivos endereços
c.execute("SELECT contatos.nome, contatos.telefone, enderecos.rua, enderecos.cidade, enderecos.estado, enderecos.cep FROM contatos JOIN enderecos ON contatos.id = enderecos.contato_id")
resultados = c.fetchall()

# exibe os contatos e endereços na tela
for contato in resultados:
    pri
    nt(f'Nome: {contato[0]}')
    print(f'Telefone: {contato[1]}')
    print(f'Rua: {contato[2]}')
    print(f'Cidade: {contato[3]}')
    print(f'Estado: {contato[4]}')
    print(f'CEP: {contato[5]}')
    print('')

# fecha a conexão com o banco de dados
conn.close()
```

Neste exemplo, a tabela `contatos` contém as colunas `id`, `nome` e `telefone`, enquanto a tabela `enderecos` contém as colunas `id`, `contato_id`, `rua`, `cidade`, `estado` e `cep`. A coluna `contato_id` em `enderecos` é uma chave estrangeira que faz referência à coluna `id` em `contatos`. A instrução SQL `JOIN` é usada para combinar as linhas nas duas tabelas, com base na correspondência entre as colunas `id` e `contato_id`.

A variável `c.lastrowid` é usada para recuperar o `id` do último registro inserido na tabela.

O resultado final é uma lista de todos os contatos com seus respectivos endereços, que é então exibida na tela. Se quiser apenas os nomes dos contatos, é possível alterar a instrução SQL para selecionar apenas a coluna `nome` da tabela `contatos` :

```python
# seleciona apenas os nomes dos contatos
c.execute("SELECT nome FROM contatos")
resultados = c.fetchall()

# exibe os nomes dos contatos na tela
for contato in resultados:
    pri
    nt(contato[0])
```

## erros com SQLite

O tratamento de erros e exceções é uma parte importante da programação em Python. Quando se está trabalhando com bancos de dados, é especialmente importante lidar com erros que possam ocorrer ao executar instruções SQL.

Uma maneira de lidar com erros é usar um bloco `try-except` em torno de nossas instruções SQL. Isso nos permite capturar exceções e lidar com elas de maneira apropriada.

Veja um exemplo de como fazer isso com a tabela `contatos` na agenda :

```python
import sqlite3
from sqlite3 import Error

# tenta inserir um novo contato e lidar com possíveis erros
try:
    # conecta-se ao banco de dados e obtém um cursor
    conn = sqlite3.connect('agenda.db')
    c = conn.cursor()

    # insere um novo contato na tabela
    c.execute("INSERT INTO contatos (nome, telefone) VALUES (?, ?)", ('Daniel', '555-4321'))

# captura qualquer exceção que possa ser levantada
except sqlite3.Error as e:
    print("Ocorreu um erro:", e)

# executar este bloco somente se a inserção for bem-sucedida
else:
    print("Novo contato inserido com sucesso!")

# finalmente, fecha a conexão com o banco de dados
finally:
    conn.close()
```

Observe como o bloco `try-except` é usado para capturar qualquer exceção que possa ser levantada durante a execução da consulta SQL. Se ocorrer um erro, é impresso uma mensagem de erro para o usuário. Independentemente de ocorrer um erro ou não, a conexão com o banco de dados é sempre fechada no bloco `finally`.

Segue abaixo alguns erros do `sqlite3` do Python :

1. `sqlite3.Error` : a classe base para todas as exceções do SQLite. Qualquer exceção relacionada ao SQLite deriva desta classe;
1. `sqlite3.InterfaceError` : subclasse de `sqlite3.Error`. Levantada quando há erros relacionados com a interface entre o SQLite e o código Python, como tentar conectar-se ao banco de dados de maneira inadequada;
1. `sqlite3.DatabaseError` : subclasse de `sqlite3.Error`. É levantada para erros relacionados ao banco de dados, como corrupção do banco de dados;
1. `sqlite3.DataError` : subclasse de `sqlite3.DatabaseError`. É levantada quando ocorrem erros ao processar tipos de dados, como tentar inserir um valor incorreto ou inválido no banco;
1. `sqlite3.OperationalError` : subclasse de `sqlite3.DatabaseError`. Esta exceção cobre uma ampla gama de problemas operacionais, como falha ao conectar ao banco de dados, deadlock ou falta de memória/disco;
1. `sqlite3.IntegrityError` : subclasse de `sqlite3.DatabaseError`. Ocorre quando há uma falha em manter a integridade do banco de dados, por exemplo, ao violar uma restrição `UNIQUE` ou `FOREIGN KEY`;
1. `sqlite3.InternalError` : subclasse de `sqlite3.DatabaseError`. Este erro ocorre quando há problemas internos no SQLite. Pode ser algo como uma falha na estrutura interna de dados;
1. `sqlite3.ProgrammingError` : subclasse de `sqlite3.DatabaseError`. É levantada quando há erros de programação, como usar um objeto de banco de dados incorretamente, ou passar argumentos inválidos para os métodos do SQLite;
1. `sqlite3.NotSupportedError` : subclasse de `sqlite3.DatabaseError`. Ocorre quando uma operação solicitada não é suportada pelo banco de dados, como o uso de uma funcionalidade que o SQLite não implementa;

## banco de dados em memória

Para usar o SQLite com um banco de dados em memória, pode-se usar a string especial `':memory:'` no lugar do nome do arquivo de banco de dados.

Aqui está um exemplo de como criar uma tabela `contatos` em um banco de dados SQLite em memória, inserir alguns dados e fazer uma consulta :

```python
import sqlite3

# conecta-se ao banco de dados em memória
conn = sqlite3.connect(':memory:')

# obter um cursor
c = conn.cursor()

# cria uma tabela "contatos"
c.execute('''
CREATE TABLE contatos
(
    nome text,
    telefone text,
    email text
)''')

# insere alguns dados
c.execute("INSERT INTO contatos VALUES ('Alice', '555-1234', 'alice@example.com')")
c.execute("INSERT INTO contatos VALUES ('Bob', '555-5678', 'bob@example.com')")
c.execute("INSERT INTO contatos VALUES ('Charlie', '555-9012', 'charlie@example.com')")

# faz uma consulta
c.execute("SELECT * FROM contatos")
resultados = c.fetchall()

# imprime os resultados
for linha in resultados:
    print(linha)

# fecha a conexão com o banco de dados
conn.close()
```

Observe que, no início do exemplo, a string `':memory:'` é usada para se conectar ao banco de dados em memória. Em seguida, a tabela `contatos` é criada, alguns dados são inseridos e uma consulta é feita. Finalmente, a conexão com o banco de dados é fechada.

Usar um banco de dados em memória pode ser útil em situações em que se precisa armazenar temporariamente dados que não precisam ser preservados depois que o programa é encerrado. Por exemplo, se precisar realizar cálculos complexos que envolvam grandes quantidades de dados, pode ser mais rápido e mais eficiente criar um banco de dados em memória para armazenar temporariamente os dados de entrada e saída.

## usando funções

Agora, veja uma alteração do código para utilizar uma funções para as conexões :

```python
import sqlite3

def criar_tabela_contatos():
    # conecta-se ao banco de dados
    conn = sqlite3.connect('agenda.db')

    # obtém um cursor
    c = conn.cursor()

    # cria uma tabela "contatos", se ela não existir
    c.execute('''
    CREATE TABLE IF NOT EXISTS contatos
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        telefone TEXT,
        email TEXT
    )''')

    # fecha a conexão com o banco de dados
    conn.close()

def inserir_contato(nome, telefone, email):
    # conecta-se ao banco de dados
    conn = sqlite3.connect('agenda.db')

    # obtém um cursor
    c = conn.cursor()

    # insere o contato na tabela "contatos"
    c.execute("INSERT INTO contatos (nome, telefone, email) VALUES (?, ?, ?)", (nome, telefone, email))

    # salva as alterações no banco de dados
    conn.commit()

    # fecha a conexão com o banco de dados
    conn.close()

def buscar_contatos():
    # conecta-se ao banco de dados
    conn = sqlite3.connect('agenda.db')

    # obtém um cursor
    c = conn.cursor()

    # faz uma consulta
    c.execute("SELECT * FROM contatos")
    resultados = c.fetchall()

    # fecha a conexão com o banco de dados
    conn.close()

    return resultados

# cria a tabela "contatos", se ela não existir
criar_tabela_contatos()

# insere alguns contatos
inserir_contato('Alice', '555-1234', 'alice@example.com')
inserir_contato('Bob', '555-5678', 'bob@example.com')
inserir_contato('Charlie', '555-9012', 'charlie@example.com')

# Buscar os contatos e imprimir os resultados
contatos = buscar_contatos()
for contato in contatos:
    print(contato)
```

Neste exemplo, existem três funções: `criar_tabela_contatos`, `inserir_contato` e `buscar_contatos`. A função `criar_tabela_contatos` é responsável por criar a tabela `contatos` se ela ainda não existir. A função `inserir_contato` é responsável por inserir um novo contato na tabela `contatos`. A função `buscar_contatos` é responsável por fazer uma consulta na tabela `contatos` e retornar os resultados.

Na parte principal do programa, é chamada a função `criar_tabela_contatos` para garantir que a tabela `contatos` exista. Em seguida, é chamada a função `inserir_contato` para inserir alguns contatos. Por fim, é chamada a função `buscar_contatos` para buscar todos os contatos na tabela `contatos` e mostrar os resultados.

## usando classes

Classe para conexão com o banco de dados :

```python
import sqlite3

class BancoDados:
    def __init__(self, banco_dados):
        self.conexao = sqlite3.connect(banco_dados)
        self.cursor = self.conexao.cursor()

    def close(self):
        self.conexao.close()

    def commit(self):
        self.conexao.commit()

    def execute(self, query, params=None):
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()

class Contato:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

    def salva(self, banco_dados):
        query = "INSERT INTO contatos (nome, telefone) VALUES (?, ?)"
        banco_dados.execute(query, (self.nome, self.telefone))
        banco_dados.commit()

    @staticmethod
    def busca_todos(database):
        query = "SELECT * FROM contatos"
        database.execute(query)
        results = database.fetchall()
        contacts = []
        for result in results:
            contact = Contato(result[1], result[2])
            contacts.append(contact)
        return contacts

database = BancoDados(':memory:')
database.execute("CREATE TABLE contatos (id INTEGER PRIMARY KEY, nome TEXT, telefone TEXT)")

contato_1 = Contato('Alice', '123456789')
contato_1.salva(database)

contato_2 = Contato('Bob', '987654321')
contato_2.salva(database)

contatos = Contato.busca_todos(database)
for contato in contatos:
    print(contato.nome, contato.telefone)

database.close()
```

Esse exemplo utiliza uma abordagem mais orientada a objetos para o uso do SQLite no Python. A classe `BancoDados` encapsula a conexão com o banco de dados e fornece métodos para executar consultas e atualizações no banco de dados, além de realizar o commit das transações.

A classe `Contato` representa os dados dos contatos que serão armazenados na tabela. Ela possui um método `salva` que recebe uma instância de `BancoDados` como parâmetro e insere o contato na tabela. Além disso, possui um método estático `busca_todos` que retorna todos os contatos da tabela em forma de objetos `Contato`.

No exemplo de uso, é criado um banco de dados em memória (`':memory:'`) e a tabela de contatos é criada. Dois contatos são criados e salvos na tabela utilizando a classe `Contato`. Em seguida, todos os contatos da tabela são recuperados e impressos na tela. Finalmente, a conexão com o banco de dados é fechada.

## exercícios

<details>
<summary>Lista de Exercícios</summary>

1. Exercícios Básicos
    1. Crie um banco de dados SQLite chamado `loja.db` e uma tabela chamada `produtos` com as colunas `id`, `nome` e `preco`.
    1. Escreva um programa em Python que insira três registros na tabela `produtos`.
    1. Crie uma consulta que retorne todos os registros da tabela `produtos` e exiba os resultados no terminal.
    1. Altere o valor do `preco` de um dos produtos da tabela `produtos` usando um comando `UPDATE`.
    1. Escreva um programa que exclua um registro da tabela `produtos` com base no `id`.
    1. Escreva um script em Python que crie uma tabela `clientes` com as colunas `id`, `nome` e `email`.
    1. Insira cinco registros na tabela `clientes` utilizando o comando `INSERT INTO`.
    1. Escreva um programa que consulte e exiba os nomes de todos os clientes cujo email termine com "gmail.com".
    1. Crie uma função Python que insira um novo cliente na tabela `clientes`.
    1. Altere o nome de um cliente na tabela `clientes` com base no `id` fornecido pelo usuário.
1. Manipulação e Consultas
    1. Crie um programa que selecione todos os produtos com preço acima de R$50,00 e exiba-os.
    1. Crie um índice na tabela `produtos` para a coluna `nome` e verifique se as consultas se tornaram mais rápidas.
    1. Escreva um programa que retorne o número total de registros na tabela `produtos`.
    1. Use a cláusula `LIKE` para encontrar todos os produtos que começam com a letra "A".
    1. Escreva um programa que verifique se uma tabela `vendas` já existe no banco de dados e, se não existir, crie-a.
    1. Crie um script que faça uma junção (`JOIN`) entre as tabelas `clientes` e `vendas` para exibir os produtos comprados por cada cliente.
    1. Escreva um programa que mostre os cinco produtos mais caros da tabela `produtos`.
    1. Utilize o comando `DISTINCT` para exibir apenas os nomes dos clientes únicos da tabela `clientes`.
    1. Crie uma consulta que agrupe os produtos pelo seu preço e exiba quantos produtos possuem o mesmo preço.
    1. Escreva um script que adicione uma coluna `data_de_compra` à tabela `vendas` e insira valores de data.
1. Transações e Tratamento de Erros
    1. Escreva um programa que execute uma transação para inserir um produto e, em caso de erro, faça o rollback.
    1. Crie uma função que realize várias inserções em massa na tabela `produtos` utilizando transações.
    1. Escreva um programa que tente excluir um produto inexistente e capture o erro utilizando `try-except`.
    1. Crie um programa que atualize múltiplos registros de uma vez, utilizando uma transação.
    1. Escreva um script que faça uma operação `DELETE` com rollback, onde, se algum erro ocorrer, os dados não são apagados.
    1. Crie uma função que receba um nome de tabela e retorne todos os registros dessa tabela, tratando possíveis exceções.
    1. Escreva um script que insira um cliente na tabela `clientes` e simule um erro proposital para testar o rollback da transação.
    1. Escreva um programa que bloqueie uma linha específica da tabela `produtos` durante uma transação e faça o commit somente após o desbloqueio.
    1. Utilize o comando `SAVEPOINT` para criar um ponto de salvamento durante uma transação e faça rollback para esse ponto.
    1. Escreva um programa que leia dados de um arquivo CSV e insira os dados no banco de dados, tratando erros de duplicidade.
1. Avançado: Consultas e Funções
    1. Escreva uma consulta que retorne o nome do produto e a quantidade de vezes que ele foi vendido, utilizando a cláusula `GROUP BY`.
    1. Crie um programa que adicione um índice único à tabela `clientes` baseado no email e trate erros de duplicidade ao inserir novos clientes.
    1. Escreva uma consulta que retorne a soma total dos preços dos produtos vendidos.
    1. Escreva um programa que exclua todos os produtos que não foram vendidos nos últimos seis meses.
    1. Crie uma função Python que retorne o preço médio dos produtos da tabela `produtos`.
    1. Escreva um script que faça uma cópia de segurança do banco de dados `loja.db` para um novo arquivo.
    1. Crie uma consulta que utilize a função `COALESCE` para substituir valores nulos por um valor padrão.
    1. Escreva um programa que atualize os preços dos produtos com base em uma tabela temporária de promoções.
    1. Utilize a função `datetime` do SQLite para filtrar vendas feitas nos últimos 30 dias.
    1. Crie uma função Python que permita pesquisar clientes por parte do nome ou email.
1. Trabalhando com Relacionamentos
    1. Crie uma tabela `vendas` que faça referência à tabela `clientes` com uma chave estrangeira.
    1. Escreva um programa que insira registros na tabela `vendas`, garantindo que o `id_cliente` exista na tabela `clientes`.
    1. Crie uma função que exclua um cliente da tabela `clientes` e todas as suas vendas associadas na tabela `vendas`.
    1. Crie um programa que faça uma junção entre as tabelas `produtos` e `vendas` e exiba todos os produtos vendidos.
    1. Escreva um programa que atualize o email de um cliente e todas as suas vendas associadas, garantindo a integridade referencial.
    1. Crie uma consulta que retorne todos os clientes que não realizaram nenhuma compra.
    1. Escreva um script que exclua todos os registros da tabela `vendas` onde o cliente associado não existe mais na tabela `clientes`.
    1. Crie um programa que permita ao usuário adicionar um novo produto e fazer uma venda em uma única operação.
    1. Escreva uma consulta que retorne o cliente que fez a compra mais cara, incluindo o nome do produto.
    1. Crie uma consulta que utilize a cláusula `EXISTS` para verificar se há produtos sem vendas associadas na tabela `vendas`.

</details>

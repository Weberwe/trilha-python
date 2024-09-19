# índice

1. [módulo `sys`](#módulo-sys)
    - [exercícios módulo `sys`](#exercícios-módulo-sys)
1. [módulo `os`](#módulo-os)
    - [exercícios módulo `os`](#exercícios-módulo-os)
1. [módulo `random`](#módulo-random)
    - [exercícios módulo `random`](#exercícios-módulo-random)
1. [módulo `time`](#módulo-time)
    - [exercícios módulo `time`](#exercícios-módulo-time)
1. [módulo `string`](#módulo-string)
    - [exercícios módulo `string`](#exercícios-módulo-string)
1. [módulo `math`](#módulo-math)
    - [exercícios módulo `math`](#exercícios-módulo-math)
1. [módulo `json`](#módulo-json)
    - [exercícios módulo `json`](#exercícios-módulo-json)
1. [variável `__name__`](#variável-__name__)
    1. [exercícios `__name__`](#exercícios-name)
1. [`wildcards`](#wildcards)
    1. [exercícios wildcards](#exercícios-wildcards)
1. [`datetime`](#datetime)
    1. [exercícios `datetime`](#exercícios-datetime)

# módulos

## módulo `sys`

O módulo `sys` em Python é um dos módulos built-in que fornecem funções e variáveis usadas para manipular diferentes partes do ambiente de execução do Python. Esse módulo é essencial para interagir com o sistema e o interpretador do Python.

1. [`sys.argv`](#sysargv)
1. [`sys.exit`](#sysexit)
1. [`sys.path`](#syspath)
1. [`sys.stdin` `sys.stdout` `sys.stderr`](#sysstdin-sysstdout-sysstderr)
1. [`sys.platform`](#sysplatform)
1. [`sys.getsizeof`](#sysgetsizeof)
1. [`sys.version` e `sys.version_info`](#sysversion-e-sysversion_info)
1. [índice](#índice)

### `sys.argv`

O atributo `sys.argv` é uma lista que armazena os argumentos passados ao script via linha de comando. O primeiro item da lista (`sys.argv[0]`) é sempre o nome do script. Os outros elementos são os argumentos que o usuário passou ao rodar o script.

**exemplo** :
Considere um script chamado `script.py` que é executado com alguns argumentos.

```python
# script.py
import sys

# imprime o nome do script
print("Nome do script :", sys.argv[0])

# verifica se foram passados argumentos
if len(sys.argv) > 1:
    # imprime os argumentos
    print("Argumentos :", sys.argv[1:])
else:
    print("Nenhum argumento foi passado.")
```

Se rodar o script com o comando :

```bash
python script.py argumento1 argumento2
```

A saída será :

```
Nome do script : script.py
Argumentos : ['argumento1', 'argumento2']
```

### `sys.exit()`

O `sys.exit()` é usado para encerrar o programa. Ele pode aceitar um argumento opcional para especificar o código de saída. Se for um número inteiro, o sistema usará esse número como código de status. O valor `0` geralmente indica que o programa foi finalizado com sucesso, e qualquer valor diferente de zero indica que ocorreu um erro.

**exemplo** :

```python
# script.py
import sys

def verificar_entrada():
    if len(sys.argv) < 2:
        print("Erro: Nenhum argumento foi passado!")
        sys.exit(1)  # Código de saída 1 indica erro
    else:
        print(f"Argumento fornecido: {sys.argv[1]}")

verificar_entrada()
```

Se rodarmos o script sem argumentos:

```bash
python script.py
```

A saída será:

```
Erro: Nenhum argumento foi passado!
```

E o código de saída será `1`, indicando que houve um erro.

### `sys.path`

O `sys.path` é uma lista de strings que especifica os diretórios onde o Python procura módulos quando se usa a instrução `import`. O Python verifica cada diretório dessa lista ao tentar localizar o módulo que você está importando.

**exemplo** :

```python
# script.py
import sys

# imprime o caminho de busca dos módulos
print("Caminhos de busca:")
for caminho in sys.path:
    print(caminho)
```

Se quiser adicionar um diretório específico para que o Python busque módulos nele, pode fazer o seguinte :

```python
import sys

# adiciona um novo caminho de busca
sys.path.append('/meu/diretorio/de/modulos')

# agora o python também buscará nesse caminho
print("Novo caminho de busca adicionado.")
```

Isso pode ser útil quando se tem módulos personalizados em diretórios fora do padrão.

### `sys.stdin`, `sys.stdout`, `sys.stderr`

Esses três atributos representam a entrada padrão (`sys.stdin`), a saída padrão (`sys.stdout`) e a saída de erro padrão (`sys.stderr`) do sistema.

- `sys.stdin` : usado para ler dados de entrada;
- `sys.stdout` : usado para exibir saídas normais;
- `sys.stderr` : usado para exibir mensagens de erro;

Por padrão, `sys.stdout` e `sys.stderr` são o console, e `sys.stdin` é o teclado, mas é possível redirecioná-los.

**exemplo** 1 : redirecionando a saída para um arquivo

```python
# script.py
import sys

# redireciona a saída padrão para um arquivo
with open("saida.txt", "w") as f:
    sys.stdout = f
    print("Essa mensagem será gravada no arquivo, não no console.")
```

Aqui, ao executar o script, a mensagem será escrita no arquivo `saida.txt`, em vez de aparecer no console. Posteriormente será visto como manipular arquivos.

**exemplo** 2 : usando `sys.stdin` para ler da entrada padrão

```python
# script.py
import sys

print("Digite algo:")
entrada = sys.stdin.read(5)  # Lê até 5 caracteres da entrada
print("Você digitou:", entrada)
```

Esse código permite que o usuário digite algo, e o Python lê até 5 caracteres.

### `sys.platform`

O `sys.platform` retorna uma string que identifica o sistema operacional em que o Python está sendo executado. Isso pode ser útil para garantir que o código seja executado corretamente em diferentes sistemas operacionais.

**exemplo** :

```python
# script.py
import sys

print(f"Este código está rodando no sistema: {sys.platform}")

if sys.platform.startswith("win"):
    print("O sistema é Windows.")
elif sys.platform.startswith("linux"):
    print("O sistema é Linux.")
elif sys.platform == "darwin":
    print("O sistema é macOS.")
```

### `sys.getsizeof()`

O `sys.getsizeof()` retorna o tamanho em bytes de um objeto em Python. Isso pode ser útil para verificar o consumo de memória de diferentes estruturas de dados.

**exemplo** :

```python
# script.py
import sys

lista = [1, 2, 3, 4, 5]
dicionario = {1: 'a', 2: 'b', 3: 'c'}

print(f"Tamanho da lista : {sys.getsizeof(lista)} bytes")
print(f"Tamanho do dicionário : {sys.getsizeof(dicionario)} bytes")
```

### `sys.version` e `sys.version_info`

- `sys.version` retorna a versão completa do Python como uma string;
- `sys.version_info` retorna a versão como uma tupla, o que é útil para verificações de compatibilidade;

**exemplo** :

```python
# script.py
import sys

print("Versão do Python (string):", sys.version)
print("Versão do Python (tupla):", sys.version_info)

# Verifica se está rodando no Python 3.x
if sys.version_info[0] == 3:
    print("Este script está sendo executado no Python 3.")
```

## exercícios módulo `sys`

<details>
<summary>Lista de Exercícios</summary>

1. Obtenha o caminho completo do Python instalado no sistema. Utilize `sys.executable` para imprimir o caminho.
1. Mostre a versão do Python que está sendo usada. Utilize `sys.version` para exibir a versão completa do Python.
1. Liste todos os diretórios em que o Python procura por módulos. Use `sys.path` para exibir os diretórios de busca.
1. Adicione um novo caminho ao `sys.path`. Adicione um diretório fictício à lista de caminhos de busca por módulos.
1. Faça com que o programa saia com um código de erro 1. Utilize `sys.exit(1)` para sair com o código de erro 1.
1. Implemente um programa que peça para o usuário inserir um número e saia se o número for negativo. Utilize `sys.exit()` para terminar o programa se a condição for satisfeita.
1. Mostre o tamanho da referência de um objeto. Utilize `sys.getsizeof()` para imprimir o tamanho de diferentes tipos de objetos (por exemplo, `int`, `str`, `list`).
1. Obtenha o nome da plataforma que o Python está executando. Use `sys.platform` para mostrar o nome da plataforma.
1. Escreva um programa que leia argumentos da linha de comando e os imprima. Utilize `sys.argv` para capturar e exibir argumentos passados via linha de comando.
1. Calcule a soma de dois números passados como argumentos da linha de comando. Use `sys.argv` para capturar dois números e calcule a soma deles.
1. Verifique quantos argumentos foram passados ao programa via linha de comando. Utilize `len(sys.argv)` para contar os argumentos passados.
1. Limite o recursão máxima do Python para 100 chamadas. Utilize `sys.setrecursionlimit(100)` e faça um programa para verificar o novo limite.
1. Imprima o limite máximo de recursão atual do Python. Utilize `sys.getrecursionlimit()` para exibir o limite.
1. Implemente uma função recursiva para calcular o fatorial e teste os limites de recursão. Use `sys.getrecursionlimit()` e ajuste o limite para testar diferentes profundidades de recursão.
1. Verifique se o sistema tem suporte para Unicode. Utilize `sys.maxunicode` para verificar a maior representação de Unicode disponível no sistema.
1. Calcule e mostre o número máximo de objetos que podem ser armazenados em uma variável. Utilize `sys.maxsize` para exibir o maior número que o Python consegue manipular.
1. Escreva um programa que imprima a saída de um número grande e identifique como ele é representado no sistema. Utilize `sys.float_info` para exibir os detalhes de representação de números em ponto flutuante.
1. Crie um programa que exiba o nome do arquivo atualmente sendo executado. Utilize `sys.argv[0]` para exibir o nome do script Python em execução.
1. Exiba o tamanho máximo de um número inteiro suportado pelo sistema. Utilize `sys.maxsize` para mostrar o maior número de inteiro que o Python suporta.
1. Capture e exiba o status final do interpretador Python antes da saída. Use `sys.flags` para exibir os diferentes sinais e flags que controlam o comportamento do interpretador.

</details>

## módulo `os`

O módulo `os` do Python fornece várias funcionalidades para interagir com o sistema operacional de maneira independente da plataforma. Isso significa que ele funciona tanto no Windows, quanto no Linux ou macOS, facilitando operações como manipulação de arquivos, diretórios, variáveis de ambiente, e muito mais.

1. [`os.name`](#osname)
1. [`os.getenv()` e `os.environ`](#osgetenv-e-osenviron)
1. [`os.getcwd()` e `os.chdir`](#osgetcwd-e-oschdir)
1. [`os.listdir()`](#oslistdir)
1. [`os.mkdir()` e `os.makedirs()`](#osmodir-e-osmakedirs)
1. [`os.remove()` e `os.rmdir()`](#osremove-e-osrmdir)
1. [`os.rename()`](#osrename)
1. [`os.path`](#ospath)
1. [`os.system()`](#ossystem)
1. [`os.popen()`](#ospopen)
1. [índice](#índice)

### `os.name`

O `os.name` retorna uma string que indica o nome do sistema operacional no qual o código está sendo executado. Dependendo do sistema, a string pode ser:
- `'posix'` para sistemas como Linux e macOS;
- `'nt'` para sistemas Windows;

**exemplo** :

```python
# main.py
import os

print(f"Sistema operacional: {os.name}")

if os.name == 'nt':
    print("Este código está sendo executado no Windows.")
else:
    print("Este código está sendo executado em um sistema tipo Unix (Linux ou macOS).")
```

### `os.getenv()` e `os.environ`

O `os.getenv()` permite acessar variáveis de ambiente, enquanto `os.environ` é um dicionário que contém todas as variáveis de ambiente do sistema.

**exemplo** 1 : acessando uma variável de ambiente

```python
# main.py
import os

# acessa a variável de ambiente path
path = os.getenv('PATH')
print(f"Variável PATH: {path}")
```

**exemplo** 2 : listando todas as variáveis de ambiente

```python
# main.py
import os

# imprime todas as variáveis de ambiente
for chave, valor in os.environ.items():
    print(f"{chave}: {valor}")
```

**exemplo** 3: definindo uma variável de ambiente temporária

```python
# main.py
import os

# Define uma variável de ambiente temporária
os.environ['MINHA_VARIAVEL'] = 'valor_exemplo'

# Verifica se foi definida
print(f"MINHA_VARIAVEL: {os.getenv('MINHA_VARIAVEL')}")
```

### `os.getcwd()` e `os.chdir()`

O `os.getcwd()` retorna o diretório de trabalho atual (onde o script está sendo executado), e `os.chdir()` altera o diretório de trabalho para outro especificado.

**exemplo** 1 : obtendo o diretório atual

```python
# main.py
import os

# obtém o diretório de trabalho atual
diretorio_atual = os.getcwd()
print(f"Diretório atual: {diretorio_atual}")
```

**exemplo** 2 : mudando o diretório atual

```python
# main.py
import os

# muda o diretório de trabalho para "/home/user" (ou outro caminho válido no seu sistema)
os.chdir("/home/user")

# Verifica o diretório atual após a mudança
print(f"Novo diretório atual: {os.getcwd()}")
```

### `os.listdir()`

O `os.listdir()` retorna uma lista de todos os arquivos e diretórios em um determinado caminho.

**exemplo** :

```python
# main.py
import os

# Lista todos os arquivos e diretórios no diretório atual
arquivos = os.listdir()
print("Arquivos e diretórios no diretório atual:")
for arquivo in arquivos:
    print(arquivo)
```

Também é possível passar um caminho específico :

```python
# main.py
import os

# lista arquivos em um diretório específico
arquivos = os.listdir("/home/user")
print("Arquivos no diretório /home/user:")
for arquivo in arquivos:
    print(arquivo)
```

### `os.mkdir()` e `os.makedirs()`

- `os.mkdir()` cria um único diretório;
- `os.makedirs()` cria um diretório, incluindo todos os diretórios intermediários, se necessário;

**exemplo** 1 : criando um único diretório

```python
# main.py
import os

# cria um diretório chamado "novo_diretorio" no diretório atual
os.mkdir("novo_diretorio")
print("Diretório 'novo_diretorio' criado.")
```

**exemplo** 2 : criando diretórios intermediários

```python
# main.py
import os

# cria o diretório "dir1/dir2/dir3", incluindo todos os diretórios intermediários
os.makedirs("dir1/dir2/dir3")
print("Diretórios 'dir1/dir2/dir3' criados.")
```

### `os.remove()` e `os.rmdir()`

- `os.remove()` exclui um arquivo;
- `os.rmdir()` exclui um diretório vazio;

**exemplo** 1 : excluindo um arquivo

```python
# main.py
import os

# remove um arquivo chamado "arquivo.txt"
os.remove("arquivo.txt")
print("Arquivo 'arquivo.txt' removido.")
```

**exemplo** 2 : excluindo um diretório vazio

```python
# main.py
import os

# remove um diretório vazio chamado "meu_diretorio"
os.rmdir("meu_diretorio")
print("Diretório 'meu_diretorio' removido.")
```

### `os.rename()`

O `os.rename()` renomeia um arquivo ou diretório.

**exemplo** :

```python
# main.py
import os

# renomeia o arquivo "arquivo_velho.txt" para "arquivo_novo.txt"
os.rename("arquivo_velho.txt", "arquivo_novo.txt")
print("Arquivo renomeado para 'arquivo_novo.txt'.")
```

### `os.path`

O módulo `os` também contém o submódulo `os.path`, que oferece várias funções para manipulação de caminhos de arquivos.

**exemplo** 1 : verificando se um arquivo ou diretório existe

```python
# main.py
import os

# Verifica se o arquivo "meu_arquivo.txt" existe
if os.path.exists("meu_arquivo.txt"):
    print("O arquivo 'meu_arquivo.txt' existe.")
else:
    print("O arquivo 'meu_arquivo.txt' não existe.")
```

**exemplo** 2 : verificando se é um arquivo ou um diretório

```python
# main.py
import os

caminho = "meu_arquivo.txt"

if os.path.isfile(caminho):
    print(f"{caminho} é um arquivo.")
elif os.path.isdir(caminho):
    print(f"{caminho} é um diretório.")
else:
    print(f"{caminho} não é um arquivo nem um diretório.")
```

**exemplo** 3 : unindo partes de um caminho

```python
# main.py
import os

# junta diferentes partes de um caminho
caminho_completo = os.path.join("/home/user", "documentos", "arquivo.txt")
print(f"Caminho completo: {caminho_completo}")
```

### `os.system()`

O `os.system()` executa comandos diretamente no sistema operacional, como se fosse executado no terminal.

**exemplo** :

```python
# main.py
import os

# Executa o comando 'ls' no Linux/macOS ou 'dir' no Windows
os.system("ls")  # Use "dir" no Windows
```

Esse comando executa a listagem de arquivos no diretório atual (o comando específico varia conforme o sistema operacional).

### `os.popen()`

Enquanto `os.system()` executa um comando sem capturar a saída, `os.popen()` permite capturar a saída do comando.

**exemplo** :

```python
# main.py
import os

# executa o comando 'ls' e captura sua saída
comando = os.popen("ls")  # Use "dir" no Windows
saida = comando.read()

# exibe a saída capturada
print("Saída do comando:")
print(saida)
```

## exerícios módulo `os`

<details>
<summary>Lista de Exercícios</summary>

1. Liste todos os arquivos e diretórios do diretório atual. Utilize `os.listdir()` para listar o conteúdo do diretório atual.
1. Crie um novo diretório chamado `novo_diretorio` no diretório atual. Use `os.mkdir()` para criar o diretório.
1. Altere o diretório de trabalho atual para o diretório `novo_diretorio`. Utilize `os.chdir()` para alterar o diretório de trabalho.
1. Mostre o caminho completo do diretório de trabalho atual. Use `os.getcwd()` para obter o diretório atual.
1. Remova o diretório `novo_diretorio`. Utilize `os.rmdir()` para remover o diretório criado.
1. Crie um diretório aninhado chamado `pasta1/pasta2/pasta3`. Use `os.makedirs()` para criar a estrutura de diretórios.
1. Remova os diretórios aninhados `pasta1/pasta2/pasta3`. Utilize `os.removedirs()` para remover a árvore de diretórios.
1. Renomeie um arquivo ou diretório. Crie um arquivo ou diretório e renomeie-o usando `os.rename()`.
1. Obtenha informações sobre um arquivo, como seu tamanho e data de modificação. Utilize `os.stat()` para exibir informações detalhadas de um arquivo.
1. Verifique se um arquivo ou diretório existe. Use `os.path.exists()` para verificar se um arquivo ou diretório existe.
1. Verifique se o caminho é um diretório. Utilize `os.path.isdir()` para verificar se o caminho fornecido é um diretório.
1. Verifique se o caminho é um arquivo. Use `os.path.isfile()` para verificar se o caminho fornecido é um arquivo.
1. Obtenha o nome do diretório de um caminho fornecido. Utilize `os.path.dirname()` para extrair o diretório de um caminho.
1. Obtenha o nome do arquivo de um caminho fornecido. Use `os.path.basename()` para extrair o nome do arquivo de um caminho.
1. Separe a extensão do nome de um arquivo. Utilize `os.path.splitext()` para separar o nome e a extensão de um arquivo.
1. Junte dois caminhos de forma adequada ao sistema operacional. Use `os.path.join()` para combinar dois caminhos.
1. Obtenha o caminho absoluto de um arquivo. Utilize `os.path.abspath()` para converter um caminho relativo em absoluto.
1. Descubra o tamanho de um arquivo em bytes. Use `os.path.getsize()` para obter o tamanho de um arquivo.
1. Obtenha o nome de usuário que está executando o programa. Utilize `os.getlogin()` para exibir o nome do usuário atual.
1. Obtenha o ID do processo atual. Use `os.getpid()` para obter o ID do processo em execução.
1. Obtenha o ID do processo pai. Utilize `os.getppid()` para obter o ID do processo pai.
1. Defina uma nova variável de ambiente e exiba seu valor. Use `os.environ` para definir uma nova variável de ambiente e depois acesse seu valor.
1. Exiba todas as variáveis de ambiente do sistema. Utilize `os.environ` para listar todas as variáveis de ambiente.
1. Remova uma variável de ambiente do sistema. Use `os.environ.pop()` para remover uma variável de ambiente.
1. Execute um comando do sistema operacional usando Python. Utilize `os.system()` para executar um comando, como listar arquivos (`ls` ou `dir`).
1. Obtenha o caminho do diretório inicial do usuário. Use `os.path.expanduser('~')` para obter o diretório inicial do usuário.
1. Obtenha o separador de diretórios do sistema operacional atual. Utilize `os.sep` para exibir o separador de diretórios (`/` no Linux/Mac, `\` no Windows).
1. Obtenha o caminho do dispositivo null do sistema operacional. Use `os.devnull` para obter o caminho para o dispositivo null (`/dev/null` no Unix, `NUL` no Windows).
1. Suspenda a execução do programa por 5 segundos. Utilize `os.sleep(5)` para pausar a execução por 5 segundos.
1. Obtenha uma lista de todos os drives disponíveis no sistema (apenas Windows). Use `os.listdir()` com as letras dos drives e filtre os que estão disponíveis no sistema (Windows).

</details>

## módulo `random`

O módulo `random` do Python é utilizado para gerar números aleatórios e realizar operações aleatórias, como escolher itens de uma lista, embaralhar elementos e gerar números em diferentes intervalos. Ele é amplamente utilizado em várias aplicações, como simulações, jogos, amostragem e mais.

1. [`random.random()`](#randomrandom)
1. [`random.uniform()`](#randomuniform)
1. [`random.randint()`](#randomrandint)
1. [`random.randrange()`](#randomrandrange)
1. [`random.choice()`](#randomchoice)
1. [`random.choices()`](#randomchoices)
1. [`random.sample()`](#randomsample)
1. [`random.shuffle()`](#randomshuffle)
1. [`random.seed()`](#randomseed)
1. [`random.gauss()`](#randomgauss)
1. [`random.betavariate()`](#randombetavariate)
1. [índice](#índice)

### `random.random()`

A função `random()` gera um número de ponto flutuante (decimal) entre 0.0 e 1.0, incluindo 0, mas excluindo 1.

**exemplo** :

```python
# main.py
import random

numero = random.random()
print(f"Número aleatório entre 0 e 1: {numero}")
```

Saída típica :
```
Número aleatório entre 0 e 1: 0.573019845657438
```

### `random.uniform()`

A função `uniform(a, b)` gera um número de ponto flutuante entre os valores `a` e `b`, incluindo ambos os limites.

**exemplo** :

```python
# main.py
import random

numero = random.uniform(10, 20)
print(f"Número aleatório entre 10 e 20: {numero}")
```

Saída típica :
```
Número aleatório entre 10 e 20: 15.678921305495
```

### `random.randint()`

A função `randint(a, b)` gera um número inteiro aleatório entre `a` e `b`, incluindo ambos os limites.

**exemplo** :

```python
# main.py
import random

numero = random.randint(1, 6)
print(f"Número inteiro aleatório entre 1 e 6: {numero}")
```

Saída típica :
```
Número inteiro aleatório entre 1 e 6: 4
```

### `random.randrange()`

A função `randrange(start, stop, step)` gera um número inteiro aleatório no intervalo de `start` até `stop - 1`, com um incremento de `step`.

**exemplo** :

```python
# main.py
import random

numero = random.randrange(0, 10, 2)
print(f"Número aleatório par entre 0 e 10: {numero}")
```

Saída típica :
```
Número aleatório par entre 0 e 10: 4
```

Aqui, o valor gerado será um número par entre 0 e 8 (pois o `stop` é 10, mas o intervalo é até 9, e os números são gerados de 2 em 2).

### `random.choice()`

A função `choice(seq)` escolhe aleatoriamente um item de uma sequência, como uma lista, tupla ou string.

**exemplo** :

```python
# main.py
import random

opcoes = ['pedra', 'papel', 'tesoura']
escolha = random.choice(opcoes)
print(f"Escolha aleatória: {escolha}")
```

Saída típica :
```
Escolha aleatória: papel
```

### `random.choices()`

A função `choices(population, k)` retorna uma lista com `k` elementos escolhidos aleatoriamente de uma população, permitindo repetições.

**exemplo** :

```python
# main.py
import random

cores = ['vermelho', 'verde', 'azul', 'amarelo']
escolhas = random.choices(cores, k=3)
print(f"Escolhas aleatórias: {escolhas}")
```

Saída típica :
```
Escolhas aleatórias: ['azul', 'verde', 'azul']
```

### `random.sample()`

A função `sample(population, k)` retorna uma lista com `k` elementos escolhidos aleatoriamente de uma população, sem repetições.

**exemplo** :

```python
# main.py
import random

numeros = list(range(1, 50))
sorteados = random.sample(numeros, k=6)
print(f"Números sorteados: {sorteados}")
```

Saída típica :
```
Números sorteados: [12, 8, 42, 33, 19, 7]
```

### `random.shuffle()`

A função `shuffle(seq)` embaralha os itens de uma lista in-place, ou seja, a própria lista é modificada.

**exemplo** :

```python
import random

cartas = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
random.shuffle(cartas)
print(f"Cartas embaralhadas: {cartas}")
```

Saída típica:
```
Cartas embaralhadas: ['7', '2', 'J', '4', '8', '3', 'A', 'K', '9', '10', '6', '5', 'Q']
```

### `random.seed()`

O comportamento da aleatoriedade no Python pode ser controlado usando `seed()`. Isso é útil quando você deseja que uma sequência de números aleatórios seja reprodutível.

**exemplo** :

```python
# main.py
import random

random.seed(10)
print(random.random())  # Sempre produzirá o mesmo resultado se seed(10) for usado.
print(random.random())  # Os mesmos números serão gerados sempre que seed(10) for usado.
```

Saída (sempre a mesma com `seed(10)`) :
```
0.5714025946899135
0.4288890546751146
```

### `random.gauss()`

A função `gauss(mu, sigma)` gera números aleatórios seguindo uma distribuição normal (ou gaussiana). O parâmetro `mu` é a média da distribuição, e `sigma` é o desvio padrão.

**exemplo** :

```python
# main.py
import random

media = 0
desvio_padrao = 1

for _ in range(5):
    print(random.gauss(media, desvio_padrao))
```

Saída típica :
```
-0.3653743596198731
1.0199221852790466
0.1918015869367224
-0.9074770176164197
-0.19738118153188115
```

### `random.betavariate()`

A função `betavariate(alpha, beta)` gera números seguindo uma distribuição beta, onde `alpha` e `beta` são parâmetros da distribuição.

**exemplo** :

```python
# main.py
import random

alpha = 2.0
beta = 5.0

for _ in range(5):
    print(random.betavariate(alpha, beta))
```

Saída típica :
```
0.2944020013389468
0.4153640288354197
0.28646777115539996
0.292441360879948
0.21664462489450598
```

## exercícios módulo `random`

<details>
<summary>Lista de Exercícios</summary>

1. Gere um número aleatório inteiro entre 1 e 10. Use `random.randint(1, 10)`.
1. Gere um número de ponto flutuante aleatório entre 0 e 1. Utilize `random.random()`.
1. Escolha aleatoriamente um elemento de uma lista. Use `random.choice()` com uma lista como argumento.
1. Escolha aleatoriamente 3 elementos diferentes de uma lista de 10 itens. Utilize `random.sample()` para selecionar 3 elementos.
1. Embaralhe aleatoriamente os elementos de uma lista. Use `random.shuffle()` para embaralhar os itens da lista.
1. Gere um número de ponto flutuante entre 5 e 10. Utilize `random.uniform(5, 10)`.
1. Gere um número aleatório de ponto flutuante com distribuição normal (gaussiana) com média 0 e desvio padrão 1. Use `random.gauss(0, 1)`.
1. Simule o lançamento de um dado de 6 lados 100 vezes e conte quantas vezes cada número apareceu. Use `random.randint()` e armazene os resultados em um dicionário ou lista.
1. Gere uma sequência aleatória de 5 números inteiros entre 1 e 50, sem repetição. Utilize `random.sample(range(1, 51), 5)`.
1. Gere uma senha aleatória de 8 caracteres usando letras e números. Use `random.choices()` com letras e números como entrada.
1. Escolha aleatoriamente um nome de uma lista de alunos. Utilize `random.choice()`.
1. Simule uma moeda sendo lançada 100 vezes e conte quantas vezes deu cara e quantas vezes deu coroa. Use `random.choice(['cara', 'coroa'])` em um loop.
1. Gere uma sequência aleatória de 6 números entre 1 e 60 (como uma simulação de loteria). Utilize `random.sample()` para gerar a sequência.
1. Gere um número aleatório entre 1 e 100 que seja múltiplo de 5. Use `random.choice(range(5, 101, 5))`.
1. Simule um jogo de roleta onde os números variam de 0 a 36. Utilize `random.randint(0, 36)` para simular a roleta.
1. Gere uma cor hexadecimal aleatória. Use `random.choice()` para selecionar valores de `0-9` e `A-F` e formar uma cor hexadecimal.
1. Crie uma lista de 10 números aleatórios e ordene-os em ordem crescente. Utilize `random.randint()` para gerar a lista e `sorted()` para ordená-la.
1. Implemente uma função que retorna um número aleatório par entre 1 e 100. Use `random.choice(range(2, 101, 2))`.
1. Simule o lançamento de dois dados e calcule a soma dos dois resultados. Utilize `random.randint(1, 6)` duas vezes e some os resultados.
1. Embaralhe uma lista de cartas (A, 2, 3, ..., K) e distribua 5 cartas. Use `random.shuffle()` e depois extraia os primeiros 5 elementos.
1. Simule o sorteio de uma rifa em que há 100 números e 5 são sorteados. Utilize `random.sample(range(1, 101), 5)`.
1. Gere uma lista de 10 números aleatórios entre 1 e 20, sem repetição, e verifique se há números repetidos. Use `random.sample()` e depois verifique duplicatas (não devem existir).
1. Gere uma sequência de 20 números aleatórios de ponto flutuante entre 0 e 1 e calcule a média. Use `random.random()` em um loop e calcule a média.
1. Implemente uma função que retorne um caractere aleatório de uma string. Utilize `random.choice()` para selecionar um caractere de uma string fornecida.
1. Crie um sistema simples de sorteio de prêmios, onde uma lista de prêmios é dada e um prêmio é escolhido aleatoriamente. Use `random.choice()` para selecionar o prêmio.
1. Simule a seleção de 3 alunos para um trabalho em grupo de uma turma de 20 alunos. Utilize `random.sample()` para selecionar 3 alunos de uma lista de 20.
1. Implemente uma função que simule o lançamento de 5 dados e retorne a soma dos valores. Utilize `random.randint()` em um loop para somar os resultados.
1. Crie um programa que simule uma senha de 4 dígitos numéricos. Use `random.choices(string.digits, k=4)` para gerar a senha.
1. Gere uma sequência aleatória de 8 caracteres composta de letras maiúsculas e minúsculas. Utilize `random.choices(string.ascii_letters, k=8)`.
1. Simule a geração de números de uma loteria onde 6 números são sorteados entre 1 e 49. Use `random.sample(range(1, 50), 6)`.
1. Implemente uma função que retorna um número aleatório ímpar entre 1 e 50. Use `random.choice(range(1, 51, 2))`.
1. Crie um programa que simule o embaralhamento de um baralho de cartas (semelhante ao exercício 20). Utilize `random.shuffle()` para embaralhar as cartas.
1. Gere uma lista de 10 números aleatórios entre 1 e 100 e encontre o maior valor. Use `random.randint()` para gerar a lista e `max()` para encontrar o maior valor.
1. Simule um jogo de dados em que 5 dados são lançados e o jogador ganha se a soma for maior que 18. Use `random.randint(1, 6)` em um loop e calcule a soma.
1. Crie uma função que simule uma rodada de "pedra, papel e tesoura" entre dois jogadores. Utilize `random.choice(['pedra', 'papel', 'tesoura'])` para cada jogador.
1. Simule a escolha de um elemento de uma lista ponderada, onde alguns elementos têm mais chances de serem escolhidos. Use `random.choices()` com pesos fornecidos.
1. Implemente uma função que retorne uma lista de 5 números aleatórios inteiros entre 10 e 100. Utilize `random.randint(10, 100)` em um loop ou `random.sample()`.
1. Implemente um jogo simples de adivinhação onde o programa gera um número entre 1 e 20 e o usuário tem que adivinhar. Utilize `random.randint(1, 20)` para gerar o número e peça ao usuário para adivinhar.
1. Gere uma lista de 5 números de ponto flutuante entre 0 e 10 e calcule o valor mínimo. Utilize `random.uniform(0, 10)` e `min()` para encontrar o menor valor.
1. Implemente um jogo de "cara ou coroa" onde o usuário pode jogar quantas vezes quiser. Use `random.choice(['cara', 'coroa'])`.
1. Crie uma função que gere uma lista de 5 números aleatórios entre 0 e 1 e retorne o maior valor. Utilize `random.random()` em um loop e `max()` para o maior valor.
1. Simule a distribuição de cartas em um jogo de pôquer para 4 jogadores. Use `random.sample()` para distribuir as cartas de um baralho.
1. Crie uma função que retorne uma letra aleatória (maiúscula ou minúscula). Use `random.choice(string.ascii_letters)`.
1. Simule o lançamento de uma moeda 1000 vezes e conte quantas vezes deu "cara". Use `random.choice()` em um loop.
1. Gere uma sequência aleatória de 20 números inteiros entre 0 e 100 e calcule a média. Utilize `random.randint(0, 100)` e `sum()` para calcular a média.

</details>

## módulo `time`

O módulo `time` do Python oferece várias funções para trabalhar com tempo, como a manipulação de horas, minutos, segundos, e funções para medir o tempo que uma ação leva para ser concluída. Ele é muito utilizado para calcular a duração de eventos, fazer pausas (delays) no código, além de obter e manipular o tempo no formato de segundos desde a *"época"* (epoch), que geralmente é 1º de janeiro de 1970 no sistema UNIX.

1. [`time.time()`](#timetime)
1. [`time.sleep()`](#timesleep)
1. [`time.localtime()`](#timelocaltime)
1. [`time.strftime()`](#timestrftime)
1. [`time.gmtime([])`](#timegmtime)
1. [`time.mktime(t)`](#timemktimet)
1. [`time.asctime([struct_time])`](#timeasctimestruct_time)
1. [`time.ctime([])`](#timectime)
1. [`time.perf_counter()`](#timeperf_counter)
1. [`time.monotonic()`](#timemonotonic)
1. [`time.process_time()`](#timeprocess_time)
1. [exemplos práticos do módulo `time`](#exemplos-práticos-do-módulo-time)
1. [índice](#índice)

### `time.time()`

Essa função retorna o número de segundos desde a *"época"*, ou seja, um número do tipo *float* que representa o tempo em segundos.  A *"época"* (epoch) é o ponto de referência para a contagem do tempo. No Unix, a *epoch* é definida como meia-noite (00:00:00) de 1 de janeiro de 1970.

**exemplo :**
```python
import time
segundos = time.time()
print(f"Segundos desde 1º de janeiro de 1970: {segundos}")
```

### `time.sleep(segundos)`

A função `sleep(seconds)` faz com que o programa pause ou "durma" por um determinado número de segundos. É útil em casos onde se deseja que o código aguarde um certo tempo antes de prosseguir.

**exemplo :**
```python
import time
print("Esperando 5 segundos...")
time.sleep(5)
print("Fim da espera.")
```

### `time.localtime()`

A função `localtime([seconds])` converte o tempo dado em segundos desde a *epoch* em um objeto de tempo local (`struct_time`). Se nenhum argumento for fornecido, ela utiliza o tempo atual (retornado por `time.time()`). O objeto `struct_time` tem vários atributos como `tm_year` (ano), `tm_mon` (mês), `tm_mday` (dia do mês), `tm_hour` (hora), etc.

**exemplo :**
```python
import time
tempo_atual = time.localtime()
print(f"Ano atual: {tempo_atual.tm_year}")
print(f"Mês atual: {tempo_atual.tm_mon}")
print(f"Dia atual: {tempo_atual.tm_mday}")
```

### `time.strftime()`

A função `strftime(formato[, struct_time])` converte um objeto `struct_time` em uma string formatada, de acordo com a especificação de formato fornecida. Por exemplo, `%Y` para ano completo, `%m` para mês, `%d` para dia do mês, `%H` para hora (formato 24h), `%M` para minutos, `%S` para segundos.

Mais Formatos [aqui](https://docs.python.org/3/library/time.html#time.strftime)

**exemplo :**
```python
import time
tempo_atual = time.localtime()
formato = time.strftime("%Y-%m-%d %H:%M:%S", tempo_atual)
print(f"Data e hora formatada: {formato}")
```

### `time.gmtime()`

Semelhante a `time.localtime()`, a função `gmtime([seconds])` retorna o tempo no fuso horário UTC (Tempo Universal Coordenado), em vez do fuso horário local.

**exemplo :**
```python
import time
tempo_utc = time.gmtime()
print(f"Ano atual (UTC): {tempo_utc.tm_year}")
```

### `time.mktime()`

A função `mktime(t)` faz o inverso de `time.localtime()` ou `time.gmtime()`, convertendo uma estrutura de tempo (`struct_time`) em segundos desde a *epoch*.

**exemplo :**
```python
import time
tempo_local = time.localtime()
segundos = time.mktime(tempo_local)
print(f"Segundos desde a epoch para a hora local: {segundos}")
```

### `time.asctime()`

A função `asctime([struct_time])` converte um objeto `struct_time` em uma string no formato: `'Dia_sem Mês Dia Hora:Min:Seg Ano'`. Se não for fornecido nenhum argumento, usa o tempo local.

**exemplo :**
```python
import time
print(time.asctime())  # Exemplo de saída: 'Tue Sep  6 10:05:12 2024'
```

### `time.ctime()`

A função `ctime([segundos])` converte o tempo, em segundos desde a epoch, em uma string legível. Se nenhum argumento for passado, usa o tempo atual.

**exemplo :**
```python
import time
print(time.ctime())  # Exemplo de saída: 'Tue Sep  6 10:05:12 2024'
```

### `time.perf_counter()`

A função `perf_counter()` retorna o valor de um temporizador de alta resolução, medido em segundos. É útil para medir o tempo de execução de trechos de código.

**exemplo :**
```python
import time
inicio = time.perf_counter()
time.sleep(2)
fim = time.perf_counter()
print(f"Tempo decorrido: {fim - inicio} segundos")
```

### `time.monotonic()`

A função `monotonic()` é similar a `time.perf_counter()`, mas este temporizador não pode ser ajustado para frente ou para trás (não é afetado por mudanças no relógio do sistema).

**exemplo :**
```python
import time
inicio = time.monotonic()
time.sleep(1)
fim = time.monotonic()
print(f"Tempo decorrido: {fim - inicio} segundos")
```

### `time.process_time()`

A função `process_time()` retorna o tempo de CPU usado pelo processo atual, em segundos.

**exemplo :**
```python
import time
inicio = time.process_time()
# Simulando um processo que consome CPU
for i in range(1000000):
    pass
fim = time.process_time()
print(f"Tempo de CPU usado: {fim - inicio} segundos")
```

---

### exemplos práticos do módulo `time`

#### exemplo de contagem regressiva

Use `time.sleep()` para implementar uma contagem regressiva.

```python
import time

def contagem_regressiva(segundos):
    while segundos:
        mins, secs = divmod(segundos, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        segundos -= 1
    print("Tempo esgotado!")

contagem_regressiva(10)
```

#### medição do tempo de execução de uma função

Usando `time.perf_counter()` para medir quanto tempo uma função leva para ser executada.

```python
import time

def funcao_lenta():
    print("Executando uma função lenta...")
    time.sleep(3)
    print("Função concluída.")

inicio = time.perf_counter()
funcao_lenta()
fim = time.perf_counter()

print(f"A função demorou {fim - inicio:.2f} segundos para ser executada.")
```

#### imprimindo a data e hora atual formatada

Usando `time.strftime()` para formatar a hora em um formato legível.

```python
import time

agora = time.localtime()
formato = time.strftime("%A, %d de %B de %Y, %H:%M:%S", agora)
print(f"Data e hora atual: {formato}")
```

#### medindo o tempo de cpu usado por um processo

Usando `time.process_time()` para ver quanto tempo de CPU foi utilizado.

```python
import time

inicio = time.process_time()
for i in range(10000000):
    pass
fim = time.process_time()

print(f"Tempo de CPU usado: {fim - inicio:.4f} segundos")
```

## exercícios módulo `time`

<details>
<summary>Lista de Exercícios</summary>

1. Exibindo o Tempo Atual. Use a função `time.time()` para exibir a quantidade de segundos desde o "Epoch" (01/01/1970).
1. Exibindo o Tempo em Formato Estruturado. Use a função `time.gmtime()` para exibir a data e hora atual no formato UTC (tempo universal coordenado).
1. Formatando o Tempo Local. Utilize a função `time.localtime()` para exibir a data e hora local. Em seguida, formate essa saída para mostrar apenas o ano, mês e dia.
1. Formatando uma Data Customizada. Use `time.strftime()` para formatar a data atual no formato `"Ano-Mês-Dia Hora:Minuto:Segundo"`.
1. Convertendo uma String de Data para um Struct_time. Utilize a função `time.strptime()` para converter a string `"12/09/2024 14:30:00"` para um objeto `struct_time`.
1. Exibindo Apenas o Ano Atual. Use a função `time.localtime()` para obter o ano atual e exibi-lo.
1. Medição de Tempo de Execução de Código. Crie um script que utilize `time.time()` para medir quanto tempo demora para executar um loop que itera 1 milhão de vezes.
1. Pausando a Execução do Programa. Use `time.sleep()` para pausar a execução do programa por 5 segundos.
1. Imprimindo um Relógio Simples. Crie um loop que utilize `time.sleep()` e `time.localtime()` para imprimir a hora atual a cada segundo, como um relógio simples.
1. Calculando a Diferença Entre Duas Datas. Use a função `time.mktime()` para calcular a diferença em segundos entre duas datas fornecidas.
1. Convertendo Tempo UTC para Tempo Local. Use a função `time.gmtime()` para pegar o tempo atual em UTC e, em seguida, converta para a hora local usando `time.localtime()`.
1. Exibindo o Tempo em Milissegundos. Modifique o programa para exibir o tempo atual em milissegundos usando `time.time()`.
1. Gerando um Timestamp Customizado. Crie um timestamp customizado para a data `01/01/2020 00:00:00` usando `time.mktime()`.
1. Exibindo a Data Atual em Diferentes Formatos. Use `time.strftime()` para exibir a data atual em três formatos diferentes (como "dd-mm-aaaa", "aaaa/mm/dd", etc.).
1. Validando uma Data a Partir de uma String. Use `time.strptime()` para validar se a string `"30/02/2020"` é uma data válida.
1. Verificando se é Horário de Verão. Use a função `time.localtime()` para verificar se o horário atual está em horário de verão (DST).
1. Simulando uma Contagem Regressiva. Crie um script que faça uma contagem regressiva de 10 segundos usando `time.sleep()`.
1. Comparando Duas Datas. Use `time.mktime()` para comparar duas datas fornecidas e determine qual é a mais recente.
1. Exibindo o Dia da Semana Atual. Utilize `time.localtime()` para determinar o dia da semana (onde 0 é segunda-feira e 6 é domingo).
1. Calculando o Tempo Restante para o Próximo Ano. Calcule quantos segundos faltam para o início do próximo ano (01/01/2025 00:00:00) a partir da data e hora atual.
1. Imprimindo a Data e Hora de 7 Dias Atrás. Use `time.time()` e `time.localtime()` para calcular e exibir a data e hora de 7 dias atrás.
1. Formatando o Tempo para Horário Completo e Amigável. Use `time.strftime()` para formatar a hora atual no formato `"12-hour:minute AM/PM"`.
1. Convertendo uma Data e Hora para o Timestamp. Crie uma data e hora arbitrária, como `"25/12/2024 15:00:00"`, e converta para o timestamp usando `time.mktime()`.
1. Exibindo o Mês Atual. Extraia e exiba o mês atual usando `time.localtime()`.
1. Implementando um Temporizador de 10 Segundos. Crie um programa que avise o usuário após 10 segundos, utilizando `time.sleep()`.
1. Calculando o Intervalo de Tempo Entre Duas Execuções. Crie um programa que execute duas funções e calcule o intervalo de tempo entre elas usando `time.perf_counter()`.
1. Convertendo uma Hora UTC para Horário Local. Pegue a hora UTC usando `time.gmtime()` e converta para a hora local usando `time.localtime()`.
1. Exibindo o Tempo de Início do Script. Use `time.ctime()` para exibir o horário em que o script foi iniciado.
1. Exibindo a Data Atual em Diferentes Idiomas. Use `time.strftime()` e altere as configurações de idioma do sistema para exibir a data atual em diferentes idiomas (pode ser feito manualmente no sistema operacional).

</details>

## módulo `string`

O módulo `string` do Python fornece constantes e funções úteis para manipular strings, principalmente quando se trabalha com caracteres e conjuntos de caracteres predefinidos. Ele ajuda a tornar operações comuns mais simples e legíveis, fornecendo acesso a letras, dígitos, pontuações, espaços em branco, e métodos úteis para formatação de strings.

1. [`string.ascii_letters`](#stringascii_letters)
1. [`string.ascii_lowercase`](#stringascii_lowercase)
1. [`string.ascii_uppercase`](#stringascii_uppercase)
1. [`string.digits`](#stringdigits)
1. [`string.hexdigits`](#stringhexdigits)
1. [`string.octdigits`](#stringoctdigits)
1. [`string.punctuation`](#stringpunctuation)
1. [`string.whitespace`](#stringwhitespace)
1. [`string.printable`](#stringprintable)
1. [`string.capwords`](#stringcapwordss-sepnone)
1. [exemplos práticos do módulo `string`](#exemplos-práticos-do-módulo-string)
1. [índice](#índice)

### `string.ascii_letters`

Contém todas as letras maiúsculas e minúsculas do alfabeto em inglês, combinando `ascii_lowercase` (minúsculas) e `ascii_uppercase` (maiúsculas). Útil quando se deseja gerar uma sequência de letras ou validar se um caractere é uma letra.

**exemplo :**
```python
import string
print(string.ascii_letters)  # Saída: 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
```

### `string.ascii_lowercase`

Contém todas as letras minúsculas do alfabeto em inglês (`'abcdefghijklmnopqrstuvwxyz'`). Ideal para operações que envolvem apenas letras minúsculas.

**exemplo :**
```python
import string
print(string.ascii_lowercase)  # Saída: 'abcdefghijklmnopqrstuvwxyz'
```

### `string.ascii_uppercase`

Contém todas as letras maiúsculas do alfabeto em inglês (`'ABCDEFGHIJKLMNOPQRSTUVWXYZ'`). Útil para operações que envolvem apenas letras maiúsculas.

**exemplo :**
```python
import string
print(string.ascii_uppercase)  # Saída: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
```

### `string.digits`

Contém todos os dígitos decimais de 0 a 9 (`'0123456789'`). Muito útil para validar ou gerar números.

**exemplo :**
```python
import string
print(string.digits)  # Saída: '0123456789'
```

### `string.hexdigits`

Contém todos os dígitos hexadecimais, incluindo os números de 0 a 9 e as letras de A a F (tanto maiúsculas quanto minúsculas). A sequência é `'0123456789abcdefABCDEF'`. Usado em conversões ou validações de números hexadecimais.

**exemplo :**
```python
import string
print(string.hexdigits)  # Saída: '0123456789abcdefABCDEF'
```

### `string.octdigits`

Contém todos os dígitos octais, de 0 a 7 (`'01234567'`). Ideal para trabalhar com números no sistema octal.

**exemplo :**
```python
import string
print(string.octdigits)  # Saída: '01234567'
```

### `string.punctuation`

Contém todos os caracteres de pontuação comuns, como `!`, `@`, `#`, etc. Útil para remover ou validar a presença de pontuação em uma string.

**exemplo :**
```python
import string
print(string.punctuation)  # Saída: '!"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~'
```

### `string.whitespace`

Contém todos os caracteres que são considerados espaço em branco, como o espaço (`' '`), tabulação (`'\t'`), nova linha (`'\n'`), etc. Excelente para tarefas de limpeza de strings.

**exemplo :**
```python
import string
print(repr(string.whitespace))  # Saída: ' \t\n\r\x0b\x0c'
```

### `string.printable`

Contém todos os caracteres imprimíveis, que são a união de letras, dígitos, pontuação e espaços em branco. Ideal para validar se uma string contém apenas caracteres que podem ser impressos.

**exemplo :**
```python
import string
print(string.printable)  # Saída: todos os caracteres imprimíveis
```

### `string.capwords(s, sep=None)`

Essa função converte uma string de forma que a primeira letra de cada palavra seja maiúscula (capitaliza a string). Ela é semelhante ao método `str.title()`, mas usa o espaço como separador por padrão. Caso você passe um separador (como vírgula ou ponto), a função usa esse separador para detectar as palavras.

**exemplo :**
```python
import string
frase = "olá mundo, python é incrível"
print(string.capwords(frase))  # Saída: 'Olá Mundo, Python É Incrível'
```

---

### exemplos práticos do módulo `string`

#### gerar uma senha aleatória

Usando os caracteres disponíveis em `string.ascii_letters`, `string.digits` e `string.punctuation` para criar uma senha aleatória.

**exemplo :**
```python
import string
import random

def gerar_senha(tamanho=8):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

senha = gerar_senha(12)
print(f"Senha gerada: {senha}")
```

#### validar se uma string é alfabética

Verificar se uma string contém apenas letras utilizando `string.ascii_letters`.

**exemplo :**
```python
import string

def eh_alfabetica(texto):
    for caractere in texto:
        if caractere not in string.ascii_letters:
            return False
    return True

print(eh_alfabetica("Python"))  # Saída: True
print(eh_alfabetica("Python3"))  # Saída: False
```

#### remover pontuação de uma string

Utilizando `string.punctuation` para remover todos os sinais de pontuação de uma frase.

**exemplo :**
```python
import string

def remover_pontuacao(texto):
    return ''.join(caractere for caractere in texto if caractere not in string.punctuation)

frase = "Olá, mundo! Python é incrível."
frase_sem_pontuacao = remover_pontuacao(frase)
print(frase_sem_pontuacao)  # Saída: 'Olá mundo Python é incrível'
```

#### verificar se uma string contém apenas caracteres imprimíveis

Verificar se uma string contém apenas caracteres que podem ser impressos utilizando `string.printable`.

**exemplo :**
```python
import string

def eh_imprimivel(texto):
    return all(caractere in string.printable for caractere in texto)

print(eh_imprimivel("Python 3.10!"))  # Saída: True
print(eh_imprimivel("Texto\nNão Imprimível"))  # Saída: True (nova linha ainda é considerada imprimível)
```

#### capitalize todas as palavras de uma string

Utilizando `string.capwords()` para transformar a primeira letra de cada palavra em maiúscula.

**exemplo :**
```python
import string

frase = "python é uma linguagem incrível"
frase_capitalizada = string.capwords(frase)
print(frase_capitalizada)  # Saída: 'Python É Uma Linguagem Incrível'
```

## exercícios módulo `string`

<details>
<summary>Lista de Exercícios</summary>

1. Exibindo o Alfabeto Minúsculo. Use `string.ascii_lowercase` para exibir todas as letras minúsculas do alfabeto inglês.
1. Exibindo o Alfabeto Maiúsculo. Use `string.ascii_uppercase` para exibir todas as letras maiúsculas do alfabeto inglês.
1. Exibindo Todos os Dígitos. Use `string.digits` para exibir todos os dígitos (de 0 a 9).
1. Exibindo Caracteres Hexadecimais. Use `string.hexdigits` para exibir todos os caracteres válidos em um número hexadecimal.
1. Exibindo Caracteres Octais. Use `string.octdigits` para exibir todos os dígitos válidos em um número octal.
1. Exibindo Símbolos de Pontuação. Use `string.punctuation` para exibir todos os símbolos de pontuação.
1. Exibindo Todos os Caracteres Imprimíveis. Use `string.printable` para exibir todos os caracteres imprimíveis.
1. Exibindo os Caracteres de Espaçamento. Use `string.whitespace` para exibir todos os caracteres considerados espaço em branco (espaços, tabulações, etc.).
1. Verificando se uma String é Alfanumérica. Crie uma função que verifique se uma string contém apenas caracteres alfanuméricos utilizando `string.ascii_letters` e `string.digits`.
1. Convertendo uma String para Maiúscula. Utilize `string.ascii_uppercase` para criar uma função que converta qualquer string para letras maiúsculas.
1. Convertendo uma String para Minúscula. Use `string.ascii_lowercase` para criar uma função que converta qualquer string para letras minúsculas.
1. Removendo Pontuação de uma String. Crie uma função que remova todos os símbolos de pontuação de uma string utilizando `string.punctuation`.
1. Substituindo Espaços por Underlines. Use `string.whitespace` para substituir todos os espaços de uma string por underscores (`_`).
1. Gerando uma Senha Aleatória. Use `string.ascii_letters` e `string.digits` para gerar uma senha aleatória de 8 caracteres.
1. Verificando se uma String é Hexadecimal. Crie uma função que verifique se uma string contém apenas caracteres válidos para um número hexadecimal, usando `string.hexdigits`.
1. Removendo Dígitos de uma String. Crie uma função que remova todos os dígitos de uma string utilizando `string.digits`.
1. Verificando se uma String é uma Palavra. Crie uma função que verifique se uma string contém apenas letras (maiúsculas ou minúsculas), usando `string.ascii_letters`.
1. Formatando uma String de Forma Capitalizada. Utilize `string.capwords()` para capitalizar cada palavra de uma frase.
1. Gerando um Identificador de Produto. Crie uma função que gere um identificador de produto aleatório, contendo letras e números, utilizando `string.ascii_uppercase` e `string.digits`.
1. Gerando um Nome de Arquivo Seguro. Crie uma função que remova qualquer caractere especial de uma string, exceto letras, números e underscore, utilizando `string.ascii_letters`, `string.digits` e `'_`.
1. Contando o Número de Dígitos em uma String. Crie uma função que conte quantos dígitos existem em uma string usando `string.digits`.
1. Validando um Identificador. Crie uma função que valide se um identificador contém apenas letras, números e underscores utilizando `string.ascii_letters`, `string.digits`, e `'_'`.
1. Separando Palavras de uma Frase. Utilize `string.whitespace` para separar as palavras de uma frase em uma lista, ignorando os espaços em branco.
1. Gerando uma Frase sem Espaços. Crie uma função que remova todos os espaços de uma frase utilizando `string.whitespace`.
1. Gerando um Token de Sessão Aleatório. Crie uma função que gere um token aleatório de 16 caracteres utilizando `string.printable`.
1. Formatando um Texto em Blocos de 4 Dígitos. Crie uma função que pegue uma sequência de números e formate em blocos de 4 dígitos separados por hífens (ex.: "1234-5678-9012").
1. Verificando se uma String é uma Data Válida. Crie uma função que verifique se uma string contém uma data no formato "dd/mm/yyyy" usando `string.digits` e `string.punctuation`.
1. Criando uma String de Números Sequenciais. Crie uma função que gere uma string contendo todos os números de 0 a 9 em sequência usando `string.digits`.
1. Convertendo um Texto para Código Morse. Crie uma função que converta uma string para código Morse, utilizando `string.ascii_uppercase` e `string.digits` para mapear os caracteres.
1. Formatando uma String com Pontuação e Espaçamento. Utilize `string.capwords()` para formatar uma frase, ajustando os espaços em branco e a capitalização de cada palavra.
1. Criando uma Função de Busca de Palavras. Crie uma função que receba um texto e uma palavra e retorne quantas vezes a palavra aparece no texto, ignorando a pontuação com `string.punctuation`.
1. Verificando se uma String é um Número Binário. Crie uma função que verifique se uma string contém apenas os caracteres '0' e '1', utilizando `string.digits`.
1. Formatando um Texto para Ficar Legível. Use `string.capwords()` para formatar um texto inteiro, capitalizando as primeiras letras de cada palavra.
1. Gerando uma String de Símbolos Aleatórios. Crie uma função que gere uma string de 10 caracteres contendo apenas símbolos de `string.punctuation`.
1. Verificando se uma String é Imprimível. Crie uma função que verifique se todos os caracteres de uma string são imprimíveis, utilizando `string.printable`.
1. Contando Caracteres Não Imprimíveis em uma String. Crie uma função que conte quantos caracteres não imprimíveis existem em uma string, utilizando `string.printable`.
1. Gerando uma Senha Segura. Crie uma função que gere uma senha aleatória contendo letras maiúsculas, minúsculas, números e símbolos, utilizando `string.ascii_letters`, `string.digits`, e `string.punctuation`.
1. Verificando se uma Senha é Segura. Crie uma função que verifique se uma senha contém pelo menos uma letra maiúscula, uma minúscula, um número e um símbolo de pontuação.
1. Contando a Frequência de Letras em uma String. Crie uma função que conte quantas vezes cada letra aparece em uma string utilizando `string.ascii_lowercase` ou `string.ascii_uppercase`.
1. Gerando uma Sequência de Caracteres Alternados. Crie uma função que gere uma string alternando entre letras maiúsculas e minúsculas, utilizando `string.ascii_uppercase` e `string.ascii_lowercase`.
1. Verificando Caracteres Permitidos em Identificadores. Crie uma função que verifique se uma string é um identificador válido (apenas letras, números e underscores), utilizando `string.ascii_letters` e `string.digits`.
1. Removendo Pontuação e Espaços de uma String. Crie uma função que remova todos os espaços e pontuações de uma string, utilizando `string.whitespace` e `string.punctuation`.
1. Verificando se uma String Contém Apenas Letras e Espaços. Crie uma função que verifique se uma string contém apenas letras e espaços, utilizando `string.ascii_letters` e `string.whitespace`.
1. Gerando uma Chave de Produto Aleatória. Crie uma função que gere uma chave de produto no formato "ABCD-EFGH-IJKL", utilizando `string.ascii_uppercase` e `string.digits`.
1. Formatando um Número de Cartão de Crédito. Crie uma função que formate um número de cartão de crédito no formato "XXXX-XXXX-XXXX-XXXX", usando `string.digits`.
1. Verificando se uma String Contém Apenas Caracteres de Controle. Crie uma função que verifique se uma string contém apenas caracteres de controle (não imprimíveis), utilizando `string.whitespace` e verificando com `string.printable`.
1. Substituindo Dígitos por Palavras. Crie uma função que substitua cada dígito em uma string pela respectiva palavra (ex.: "1" por "um", "2" por "dois"), utilizando `string.digits`.
1. Gerando um Código de Desconto Aleatório. Crie uma função que gere um código de desconto de 8 caracteres, utilizando letras maiúsculas e números, com `string.ascii_uppercase` e `string.digits`.
1. Validando um Nome de Usuário. Crie uma função que valide um nome de usuário, verificando se contém apenas letras, números e underscores, utilizando `string.ascii_letters` e `string.digits`.
1. Contando Caracteres de Espaçamento. Crie uma função que conte quantos caracteres de espaçamento existem em uma string, utilizando `string.whitespace`.

</details>

## módulo `math`

O módulo `math` do Python é uma biblioteca padrão que fornece funções matemáticas básicas e avançadas. Ele inclui uma série de operações que vão desde funções trigonométricas, logaritmos, até manipulações de números de ponto flutuante e constantes matemáticas. O `math` é particularmente útil em cálculos científicos e estatísticos.

1. [constantes matemáticas](#constantes-matemáticas)
1. [funções aritméticas](#funções-aritméticas)
1. [funções exponenciais e logarítmicas](#funções-exponenciais-e-logarítmicas)
1. [funções trigonométricas](#funções-trigonométricas)
1. [funções hiperbólicas](#funções-hiperbólicas)
1. [funções de arredondamento](#funções-de-arredondamento)
1. [funções de comparação](#funções-de-comparação)
1. [exemplos práticos do módulo `math`](#exemplos-práticos-do-módulo-math)
1. [índice](#índice)

### constantes matemáticas

- `math.pi` : representa o valor de π (aproximadamente 3.14159);
- `math.e` : representa o valor da constante de euler (aproximadamente 2.71828);
- `math.inf` : representa o valor de infinito;
- `math.nan` : representa um valor que não é um número (not a number);

```python
import math

print(math.pi)  # 3.141592653589793
print(math.e)   # 2.718281828459045
print(math.inf)  # inf
print(math.nan)  # nan
```

### funções aritméticas

- `math.ceil(x)` : retorna o menor número inteiro maior ou igual a `x`;
- `math.floor(x)` : retorna o maior número inteiro menor ou igual a `x`;
- `math.fabs(x)` : retorna o valor absoluto de `x`;
- `math.factorial(x)` : retorna o fatorial de `x` (x!);
- `math.gcd(x, y)` : calcula o maior divisor comum entre `x` e `y`;

```python
print(math.ceil(4.3))    # 5
print(math.floor(4.7))   # 4
print(math.fabs(-5.4))   # 5.4
print(math.factorial(5)) # 120
print(math.gcd(60, 48))  # 12
```

### funções exponenciais e logarítmicas

- `math.exp(x)` : retorna `e` elevado à potência de `x` (e^x);
- `math.log(x)` : retorna o logaritmo natural de `x` (base `e`);
- `math.log10(x)` : retorna o logaritmo de base 10 de `x`;
- `math.pow(x, y)` : retorna `x` elevado à potência de `y` (x^y);
- `math.sqrt(x)` : retorna a raiz quadrada de `x`;

```python
print(math.exp(1))        # 2.718281828459045 (valor de e)
print(math.log(10))       # 2.302585092994046 (logaritmo natural)
print(math.log10(1000))   # 3.0 (log de base 10)
print(math.pow(2, 3))     # 8.0 (2^3)
print(math.sqrt(25))      # 5.0 (raiz quadrada de 25)
```

### funções trigonométricas

- `math.sin(x)` : retorna o seno de `x` (em radianos);
- `math.cos(x)` : retorna o cosseno de `x` (em radianos);
- `math.tan(x)` : retorna a tangente de `x` (em radianos);
- `math.degrees(x)` : converte o valor de `x` de radianos para graus;
- `math.radians(x)` : converte o valor de `x` de graus para radianos;

```python
angle = math.radians(90)  # convertendo 90 graus para radianos
print(math.sin(angle))    # 1.0 (seno de 90 graus)

print(math.degrees(math.pi))  # 180.0 (π radianos é igual a 180 graus)
```

### funções hiperbólicas

- `math.sinh(x)` : retorna o seno hiperbólico de `x`;
- `math.cosh(x)` : retorna o cosseno hiperbólico de `x`;
- `math.tanh(x)` : retorna a tangente hiperbólica de `x`;

```python
print(math.sinh(1))  # 1.1752011936438014
print(math.cosh(1))  # 1.5430806348152437
print(math.tanh(1))  # 0.7615941559557649
```

### funções de arredondamento

- `math.trunc(x)` : remove a parte decimal de `x`, retornando apenas a parte inteira;
- `math.modf(x)` : retorna a parte fracionária e a parte inteira de `x` como uma tupla;

```python
print(math.trunc(4.8))    # 4
print(math.modf(4.8))     # (0.7999999999999998, 4.0)
```

### funções de comparação

- `math.isfinite(x)` : retorna `true` se `x` for um número finito;
- `math.isinf(x)` : retorna `true` se `x` for infinito;
- `math.isnan(x)` : retorna `true` se `x` não for um número (nan);

```python
print(math.isfinite(100))   # True
print(math.isinf(math.inf)) # True
print(math.isnan(float('nan'))) # True
```

### exemplos práticos do módulo `math`

#### calculando a hipotenusa de um triângulo retângulo

Imagine que se conheça os dois catetos de um triângulo retângulo e deseja calcular a hipotenusa. A fórmula da hipotenusa é dada por:

> hipotenusa = (cateto1 ** 2 +  cateto2 ** 2) ** (1/2)

Será usada a fórmula `math.sqrt()` para calcular a raiz quadrada.

```python
import math

cateto1 = 3
cateto2 = 4

hipotenusa = math.sqrt(math.pow(cateto1, 2) + math.pow(cateto2, 2))
print(f"A hipotenusa do triângulo é: {hipotenusa}")
```

**Saída** :
```
A hipotenusa do triângulo é: 5.0
```

#### calculando o logaritmo de base 10 de um número

```python
import math

numero = 1000
logaritmo = math.log10(numero)
print(f"O logaritmo de base 10 de {numero} é {logaritmo}")
```

**Saída** :
```
O logaritmo de base 10 de 1000 é 3.0
```

#### convertendo ângulos de graus para radianos

Muitos cálculos trigonométricos usam ângulos em radianos. Pode-se converter facilmente graus para radianos com `math.radians()`.

```python
import math

graus = 180
radianos = math.radians(graus)
print(f"{graus} graus são {radianos} radianos")
```

**Saída** :
```
180 graus são 3.141592653589793 radianos
```

#### gerando números aleatórios com a distribuição normal

Em muitos casos, pode-se desejar gerar números com base em uma distribuição normal. Isso pode ser feito com `random.gauss()`, mas a biblioteca `math` fornece as funções de probabilidade que pode-se usar para esses cálculos.

```python
import math

mu = 0   # média
sigma = 1  # desvio padrão
valores = [math.exp(mu + sigma * x) for x in range(-3, 4)]
print(valores)
```

## exercícios módulo `math`

<details>
<summary>Lista de Exercícios</summary>

1. Exercícios de Funções Aritméticas
    1. **Arredondamento para Cima** : Dado um número decimal, use `math.ceil()` para arredondá-lo para o próximo número inteiro.
    1. **Arredondamento para Baixo** : Dado um número decimal, use `math.floor()` para arredondá-lo para o número inteiro anterior.
    1. **Valor Absoluto** : Use `math.fabs()` para encontrar o valor absoluto de um número negativo.
    1. **Fatorial** : Dado um número inteiro `n`, calcule o fatorial de `n` usando `math.factorial()`.
    1. **Maior Divisor Comum** : Use `math.gcd()` para encontrar o maior divisor comum entre dois números inteiros.
    1. **Divisão e Módulo** : Dado um número decimal, use `math.modf()` para separá-lo em parte inteira e parte fracionária.
    1. **Truncamento** : Dado um número decimal, use `math.trunc()` para remover a parte decimal.
    1. **Comparação de Valores** : Use `math.isclose()` para comparar dois números com precisão definida (tolerância).
1. Exercícios de Funções Exponenciais e Logarítmicas
    1. **Exponencial** : Use `math.exp()` para calcular o valor de `e` elevado a uma potência.
    1. **Potenciação** : Calcule `x` elevado à potência de `y` usando `math.pow()`.
    1. **Raiz Quadrada** : Dado um número positivo, calcule sua raiz quadrada usando `math.sqrt()`.
    1. **Logaritmo Natural** : Dado um número `n`, calcule o logaritmo natural (base `e`) de `n` usando `math.log()`.
    1. **Logaritmo de Base 10** : Use `math.log10()` para calcular o logaritmo de um número na base 10.
    1. **Logaritmo com Base Arbitrária** : Dado um número `n` e uma base `b`, calcule o logaritmo de `n` na base `b` usando `math.log(x, base)`.
    1. **Crescimento Exponencial** : Escreva uma função que calcule o crescimento exponencial de uma população usando `math.exp()`.
1. Exercícios de Funções Trigonométricas
    1. **Cálculo de Seno** : Dado um ângulo em radianos, calcule o seno do ângulo usando `math.sin()`.
    1. **Cálculo de Cosseno** : Dado um ângulo em radianos, calcule o cosseno do ângulo usando `math.cos()`.
    1. **Cálculo de Tangente** : Dado um ângulo em radianos, calcule a tangente do ângulo usando `math.tan()`.
    1. **Converta Graus para Radianos** : Dado um valor em graus, use `math.radians()` para convertê-lo em radianos.
    1. **Converta Radianos para Graus** : Dado um valor em radianos, use `math.degrees()` para convertê-lo em graus.
    1. **Arco Seno** : Use `math.asin()` para encontrar o arco seno de um valor.
    1. **Arco Cosseno** : Use `math.acos()` para encontrar o arco cosseno de um valor.
    1. **Arco Tangente** : Use `math.atan()` para encontrar o arco tangente de um valor.
    1. **Identidade Trigonométrica** : Verifique a identidade trigonométrica `sin^2(x) + cos^2(x) = 1` para um valor `x`.
1. Exercícios de Funções Hiperbólicas
    1. **Seno Hiperbólico** : Dado um valor `x`, calcule o seno hiperbólico usando `math.sinh()`.
    1. **Cosseno Hiperbólico** : Dado um valor `x`, calcule o cosseno hiperbólico usando `math.cosh()`.
    1. **Tangente Hiperbólica** : Dado um valor `x`, calcule a tangente hiperbólica usando `math.tanh()`.
1. Exercícios de Funções de Comparação
    1. **Verificar se um Número é Finito** : Use `math.isfinite()` para verificar se um número é finito.
    1. **Verificar se um Número é Infinito** : Use `math.isinf()` para verificar se um número é infinito.
    1. **Verificar se um Valor é NaN (Not a Number)** : Use `math.isnan()` para verificar se um valor não é um número.
    1. **Verificar Proximidade entre Números** : Use `math.isclose()` para verificar se dois números são aproximadamente iguais com uma certa tolerância.
1. Exercícios com Constantes
    1. **Valor de Pi** : Calcule a circunferência de um círculo dado seu raio usando `math.pi`.
    1. **Valor de e** : Use a constante `math.e` para calcular o valor de `e` elevado à potência de um número.
    1. **Cálculo com Infinito** : Use `math.inf` para verificar o comportamento de operações com valores infinitos.
    1. **Comparando Infinito com Números Finitos** : Verifique se `math.inf` é maior que um número muito grande.
1. Exercícios de Funções Estatísticas
    1. **Cálculo de Média** : Dada uma lista de números, calcule a média aritmética.
    1. **Cálculo de Variância** : Dada uma lista de números, calcule a variância dos valores.
    1. **Cálculo do Desvio Padrão** : Dada uma lista de números, calcule o desvio padrão dos valores.
1. Exercícios de Aplicações Práticas
    1. **Calculando a Hipotenusa** : Use `math.hypot()` para calcular a hipotenusa de um triângulo retângulo, dado os valores dos catetos.
    1. **Distância Euclidiana** : Dado dois pontos `(x1, y1)` e `(x2, y2)` no plano cartesiano, calcule a distância euclidiana entre eles usando `math.hypot()`.
    1. **Cálculo de Juros Compostos** : Escreva uma função que calcule o montante total após `n` anos com juros compostos, utilizando `math.pow()`.
    1. **Cálculo de Probabilidade Normal** : Use `math.erf()` para calcular a função de distribuição cumulativa de uma variável com distribuição normal.
    1. **Aproximação de Pi com Série de Leibniz** : Use uma fórmula matemática para aproximar o valor de `pi` somando os primeiros `n` termos da série de Leibniz.
    1. **Conversão de Coordenadas Polares para Cartesianas** : Dado um raio `r` e um ângulo `theta` em radianos, converta para coordenadas cartesianas usando funções trigonométricas.
    1. **Conversão de Coordenadas Cartesianas para Polares** : Dado um ponto `(x, y)` no plano cartesiano, converta para coordenadas polares usando `math.atan2()`.
    1. **Cálculo de Volume de uma Esfera** : Calcule o volume de uma esfera dado seu raio, usando a fórmula `4/3 * π * r^3`.
    1. **Equação Quadrática** : Dada uma equação quadrática `ax^2 + bx + c = 0`, calcule as raízes usando a fórmula de Bhaskara e `math.sqrt()`.
    1. **Resolvendo uma Equação Exponencial** : Resolva uma equação exponencial do tipo `e^x = y` usando `math.log()`.
    1. **Cálculo de Proporção** : Dada uma proporção, use `math.log()` para resolver uma equação de proporções entre duas variáveis.
    1. **Aproximação Linear** : Dado um conjunto de pontos, escreva um programa que calcule a melhor linha reta que aproxima os pontos (método dos mínimos quadrados).

</details>

## módulo `json`

O módulo `json` do Python é utilizado para trabalhar com dados no formato JSON (JavaScript Object Notation). O JSON é um formato de intercâmbio de dados amplamente utilizado, especialmente em APIs web, porque é simples e fácil de ler para humanos e máquinas. Com o módulo `json`, é possível converter dados entre objetos Python e strings JSON, o que é conhecido como **serialização** e **desserialização**.

1. [dumping e loading](#dumping-e-loading)
1. [`json.dumps()`](#jsondumps)
1. [`json.loads()`](#jsonloads)
1. [`json.dump()`](#jsondump)
1. [`json.load()`](#jsonload)
1. [índice](#índice)

### dumping e loading

- **serialização (dumping)** : converte objetos Python (listas, dicionários, etc.) em uma string JSON;
- **desserialização (loading)** : converte uma string JSON em objetos Python (tipicamente dicionários e listas);

### `json.dumps()`

Essa função **serializa** um objeto Python em uma string JSON. É usada quando se deseja converter um objeto Python (como um dicionário) em uma string JSON que pode ser armazenada ou enviada para uma API.

- **sintaxe** : `json.dumps(obj, *, skipkeys=False, ensure_ascii=True, indent=None, separators=None, default=None, sort_keys=False)`

    - `obj` : o objeto Python a ser convertido;
    - `skipkeys` : se `True`, chaves não suportadas (como tuplas) são ignoradas;
    - `ensure_ascii` : se `True`, a string resultante conterá apenas caracteres ASCII;
    - `indent` : especifica o número de espaços usados para formatar a saída (em formato indentado);
    - `sort_keys` : se `True`, as chaves dos dicionários serão ordenadas;

**Exemplo**
```python
import json

dados = {
    "nome": "João",
    "idade": 30,
    "cidade": "São Paulo",
    "habilidades": ["Python", "C++", "JavaScript"]
}

json_string = json.dumps(dados, indent=4)  # serializa e adiciona indentação
print(json_string)
```

**Saída**
```json
{
    "nome": "João",
    "idade": 30,
    "cidade": "São Paulo",
    "habilidades": [
        "Python",
        "C++",
        "JavaScript"
    ]
}
```

### `json.loads()`

Essa função **desserializa** uma string JSON em um objeto Python. É usada para interpretar dados JSON (geralmente recebidos de uma API) como dicionários, listas e outros objetos Python.

- **sintaxe** : `json.loads(s, *, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None)`

    - `s`: a string JSON que será convertida;
    - `object_hook`: uma função que pode ser usada para modificar o comportamento da desserialização;

**Exemplo**
```python
import json

json_string = '{"nome": "João", "idade": 30, "cidade": "São Paulo", "habilidades": ["Python", "C++", "JavaScript"]}'
dados = json.loads(json_string)

print(dados)
```

**Saída**
```python
{
    'nome': 'João',
    'idade': 30,
    'cidade': 'São Paulo',
    'habilidades': ['Python', 'C++', 'JavaScript']
}
```

### `json.dump()`

Essa função é semelhante a `json.dumps()`, mas em vez de converter um objeto em uma string JSON, ela grava o JSON diretamente em um arquivo.

- **sintaxe** : `json.dump(obj, fp, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False)`

    - `obj` : o objeto Python que será convertido;
    - `fp` : o objeto de arquivo onde os dados JSON serão gravados;

**Exemplo**
```python
import json

dados = {
    "nome": "João",
    "idade": 30,
    "cidade": "São Paulo",
    "habilidades": ["Python", "C++", "JavaScript"]
}

with open('dados.json', 'w') as arquivo:
    json.dump(dados, arquivo, indent=4)
```

Nesse exemplo, o dicionário `dados` é gravado em um arquivo chamado `dados.json` com formatação indentada.

### `json.load()`

Essa função lê dados JSON de um arquivo e os converte em um objeto Python.

- **sintaxe** : `json.load(fp, *, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None)`

    - `fp` : o arquivo contendo os dados JSON;

**Exemplo**
```python
import json

with open('dados.json', 'r') as arquivo:
    dados = json.load(arquivo)

print(dados)
```

Aqui, o conteúdo do arquivo `dados.json` será carregado em um dicionário Python.

---

## exercícios módulo `json`

<details>
<summary>Lista de Exercícios</summary>

1. Exercícios para o Método `json.dumps()`
    1. **Serialização Simples** : Converta um dicionário Python simples contendo informações de uma pessoa (nome, idade, cidade) em uma string JSON usando `json.dumps()`.
    1. **Lista de Números** : Converta uma lista de números inteiros em uma string JSON usando `json.dumps()`.
    1. **Indentação na Serialização** : Serialize um dicionário Python com o parâmetro `indent=4` para formatar o JSON de maneira legível.
    1. **Serializar com Chaves Ordenadas** : Serialize um dicionário e utilize o parâmetro `sort_keys=True` para garantir que as chaves fiquem em ordem alfabética no JSON.
    1. **Serializar com Caracteres Especiais** : Serialize um dicionário que contém caracteres especiais (acentos, símbolos) e use o parâmetro `ensure_ascii=False` para manter os caracteres como estão.
    1. **Serialização de Tupla** : Tente serializar uma tupla de números e veja como ela é convertida para JSON.
    1. **Ignorar Chaves Inválidas** : Tente serializar um dicionário que contenha uma chave inválida (como uma tupla) e use o parâmetro `skipkeys=True` para ignorar as chaves inválidas.
    1. **Serializar Objetos Aninhados** : Serialize um dicionário que contenha outros dicionários e listas aninhados, usando `json.dumps()`.
    1. **Serializar com Separadores Personalizados** : Use o parâmetro `separators` em `json.dumps()` para personalizar os separadores entre os elementos (exemplo: `', '` para separar os itens da lista e `': '` para separar chaves e valores).
1. Exercícios para o Método `json.loads()`
    1. **Desserializar uma String JSON Simples** : Dada uma string JSON contendo informações de um produto (nome, preço, quantidade), use `json.loads()` para convertê-la em um dicionário Python.
    1. **Desserializar Lista** : Converta uma string JSON contendo uma lista de números em uma lista Python usando `json.loads()`.
    1. **Desserializar uma Lista de Dicionários** : Dada uma string JSON contendo uma lista de dicionários com informações de vários estudantes, use `json.loads()` para convertê-la em uma lista de dicionários Python.
    1. **Erro ao Desserializar** : Dada uma string JSON com erro de sintaxe, tente usá-la com `json.loads()` e capture o erro `JSONDecodeError` adequadamente.
    1. **Desserializar Números com Vírgula Flutuante** : Converta uma string JSON contendo números decimais (como `2.5`, `3.14`) em uma lista de números Python.
    1. **Verificar Tipo após Desserializar** : Após desserializar uma string JSON, verifique o tipo dos dados retornados (exemplo: verificar se é um dicionário ou lista).
    1. **Desserializar Booleanos** : Converta uma string JSON que contenha valores booleanos (`true`, `false`) em um dicionário Python usando `json.loads()`.
    1. **Desserializar Null** : Use `json.loads()` para converter uma string JSON que contenha `null` e verifique como o Python representa esse valor.
1. Exercícios para o Método `json.dump()`
    1. **Serialização para Arquivo** : Converta um dicionário Python para JSON e grave o resultado em um arquivo `dados.json` usando `json.dump()`.
    1. **Salvar Lista em Arquivo** : Salve uma lista de strings como JSON em um arquivo usando `json.dump()`.
    1. **Gravar JSON Formatado** : Converta um dicionário Python em JSON e grave no arquivo `formatado.json` com indentação de 4 espaços para facilitar a leitura.
    1. **Serializar com Separadores Personalizados** : Use o parâmetro `separators` ao gravar JSON em um arquivo para ajustar os separadores entre chaves e valores.
    1. **Ignorar Chaves Inválidas em Arquivo** : Grave um dicionário em um arquivo, ignorando chaves inválidas (como tuplas), utilizando o parâmetro `skipkeys=True`.
    1. **Serializar com Ordenação de Chaves** : Grave um dicionário em um arquivo JSON, ordenando as chaves de forma alfabética com o parâmetro `sort_keys=True`.
    1. **Escrever Múltiplos Objetos em um Arquivo** : Serialize e grave dois objetos Python em um único arquivo JSON (por exemplo, dois dicionários separados por linhas).
    1. **Gravação de JSON com Unicode** : Grave um dicionário com caracteres Unicode em um arquivo, sem que eles sejam escapados, utilizando o parâmetro `ensure_ascii=False`.
    1. **Gravar JSON em Modo de Acrescentar (Append)** : Abra um arquivo JSON existente e adicione mais dados (um novo dicionário) ao final do arquivo, sem sobrescrever o conteúdo original.
1. Exercícios para o Método `json.load()`
    1. **Ler um Arquivo JSON Simples** : Crie um arquivo JSON com informações de uma pessoa e use `json.load()` para carregá-lo como um dicionário Python.
    1. **Ler Lista de Números** : Crie um arquivo JSON contendo uma lista de números inteiros e use `json.load()` para carregá-los em uma lista Python.
    1. **Ler Arquivo JSON Formatado** : Abra um arquivo JSON que contenha dados com indentação e carregue-o usando `json.load()`.
    1. **Tratar Erro ao Ler Arquivo JSON Inválido** : Tente ler um arquivo com JSON inválido e trate o erro `JSONDecodeError` corretamente.
    1. **Ler JSON de Arquivo Grande** : Crie um arquivo JSON com milhares de linhas e use `json.load()` para carregá-lo. Verifique o tempo de execução.
    1. **Modificar e Regravar JSON Lido** : Após carregar um arquivo JSON como um dicionário Python, modifique os valores e grave as mudanças de volta no arquivo usando `json.dump()`.
    1. **Ler Arquivo com Booleanos** : Crie um arquivo JSON que contenha valores booleanos (`true`, `false`) e carregue-o em um dicionário Python.
    1. **Ler Arquivo com Valor Nulo** : Crie um arquivo JSON com valores `null` e use `json.load()` para carregá-lo e verificar como esses valores são representados em Python.
    1. **Ler Dados JSON Aninhados** : Crie um arquivo JSON que contenha um dicionário com outros dicionários e listas aninhadas, e use `json.load()` para carregá-lo.
    1. **Ler e Comparar Tipos** : Após carregar um arquivo JSON com `json.load()`, verifique se o tipo dos dados lidos corresponde ao tipo esperado (exemplo: lista, dicionário).
1. Exercícios Combinando `json.dumps()`, `json.loads()`, `json.dump()`, `json.load()`
    1. **Serializar e Desserializar Ciclo** : Converta um dicionário em JSON usando `json.dumps()`, depois use `json.loads()` para reverter a string JSON de volta para um dicionário.
    1. **Gravar e Ler de Arquivo** : Use `json.dump()` para gravar um dicionário em um arquivo e, em seguida, use `json.load()` para ler esse arquivo de volta para um objeto Python.
    1. **Manipulação Completa de JSON em Arquivo** : Serialize um objeto Python com `json.dumps()`, grave-o em um arquivo usando `json.dump()`, depois carregue-o do arquivo usando `json.load()` e faça uma alteração no objeto, finalizando com a regravação do arquivo.
    1. **Conversão e Verificação** : Converta uma lista de números em JSON, grave em um arquivo, leia novamente com `json.load()` e verifique se a lista lida é idêntica à original.

</details>

## variável `__name__ `

No Python, a variável especial `__name__` é uma variável interna definida automaticamente pelo interpretador sempre que um módulo é executado. Ela é usada para identificar o contexto em que um módulo Python está sendo executado, e seu valor pode mudar dependendo de como o módulo é utilizado.

### como funciona

Existem duas situações principais em que a variável `__name__` pode assumir valores diferentes:

1. **quando o módulo é executado diretamente** :
    - se o arquivo Python é executado diretamente (por exemplo, chamando o script diretamente pelo terminal ou pelo Python), o valor da variável `__name__` será `"__main__"`;
    - isso significa que o código do arquivo está sendo executado como o programa principal;

1. **quando o módulo é importado** :
    - se o arquivo Python é importado em outro arquivo como um módulo, a variável `__name__` recebe o nome do próprio módulo;
    - o nome do módulo é o nome do arquivo sem a extensão `.py`;

- **Exemplo**

Considere o seguinte código num arquivo chamado `funcoes.py`:

```python
# funcoes.py
def exibe_texto():
    print('Esta função foi chamada')
    print(f'{__name__ = }')

if __name__ == "__main__":
    exibe_texto()
```

- executando diretamente o arquivo `funcoes.py`

Quando se executa o arquivo diretamente (por exemplo, com o comando `python funcoes.py`), a variável `__name__` terá o valor `"__main__"`. Portanto, a saída será:

```
Esta função foi chamada
__name__ = '__main__'
```

- importando o módulo em outro arquivo

Agora, suponha que se tenha outro arquivo, chamado `main.py`, que importa o módulo `funcoes.py`:

```python
# main.py
import funcoes

funcoes.exibe_texto()
```

Ao executar `main.py`, a variável `__name__` no arquivo `funcoes.py` terá o valor `"funcoes"` (o nome do módulo). Isso ocorre porque `funcoes.py` está sendo importado como um módulo e não está sendo executado diretamente. A saída será:

```
Esta função foi chamada
__name__ = 'funcoes'
```

### usos comum

O principal motivo para usar a condição `if __name__ == "__main__":` em um script Python é para separar o código que deve ser executado apenas quando o módulo é executado diretamente daquele que deve ser executado quando o módulo é importado.

Essa prática é especialmente útil quando se deseja que um arquivo Python possa ser usado tanto como um script executável quanto como um módulo que pode ser importado por outros scripts sem que o código dentro da condição `if __name__ == "__main__":` seja executado automaticamente.

#### executar código de teste ou funcionalidade principal

Um arquivo Python pode ter múltiplas funções e classes. Ao usar `if __name__ == "__main__":`, pode-se escrever uma **função principal** ou blocos de teste que só serão executados quando o arquivo for rodado diretamente, sem interferir no comportamento quando o arquivo é importado como módulo em outro script.

- **Exemplo**

```python
# calculadora.py

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

if __name__ == "__main__":
    # testando a função quando o arquivo é executado diretamente
    print(soma(10, 5))  # saída: 15
    print(subtracao(10, 5))  # saída: 5
```

Aqui, ao rodar `python calculadora.py`, as funções `soma` e `subtracao` serão testadas, mas quando esse módulo for importado em outro arquivo, como `import calculadora`, esses testes não serão executados.

#### reaproveitar código como biblioteca

Ao dividir seu código em módulos reutilizáveis, pode-se evitar que blocos de código de execução (como testes ou configurações específicas) sejam executados quando esses módulos são importados em outro lugar. Isso permite o reaproveitamento de funções e classes sem efeitos colaterais indesejados.

Por exemplo, se alguém quiser usar apenas a função `soma()` do arquivo `calculadora.py`, ela poderá importá-la sem executar os testes:

```python
from calculadora import soma
resultado = soma(3, 4)
```

### vantagens

#### modularidade

Ao usar essa abordagem, consegue-se manter o código organizado e modular. Isso facilita a criação de bibliotecas ou pacotes onde várias partes do código podem ser importadas e reutilizadas em diferentes scripts, sem executar blocos de teste ou de configuração que são específicos para execução direta.

#### facilita o teste e depuração

É comum usar o bloco `if __name__ == "__main__":` para rodar uma série de testes simples ou demonstrações de como as funções do arquivo funcionam. Isso facilita a verificação rápida do comportamento de um módulo enquanto ele está sendo desenvolvido, sem a necessidade de escrever scripts de teste separados. Além disso, a integração com bibliotecas de testes como `unittest` se torna mais natural.

#### reaproveitamento de código

Como mencionado anteriormente, essa técnica possibilita que o mesmo arquivo seja usado de duas maneiras:
- como um **script executável** que pode rodar diretamente, com funcionalidades testáveis;
- como uma **biblioteca de funções ou classes** que pode ser importada sem rodar o código fora do escopo pretendido;

#### flexibilidade em aplicações mais complexas

Em programas mais complexos, pode-se usar esse padrão para definir comportamentos diferentes para quando o módulo é executado diretamente ou quando é importado em outro contexto. Por exemplo, pode-se ter um arquivo que tanto pode ser um módulo importável quanto um aplicativo completo, dependendo de como ele é invocado.

## exercícios `__name__`

<details>
<summary>Lista de Exercícios</summary>

1. **Exercício básico 1** : Crie um arquivo Python que tenha uma função chamada `saudacao()`, que imprima "Olá, mundo!". Use `if __name__ == "__main__":` para chamar essa função somente se o arquivo for executado diretamente.
1. **Exercício básico 2** : Crie um arquivo com uma função `soma(a, b)` que retorna a soma de dois números. Use `if __name__ == "__main__":` para testar essa função, imprimindo o resultado da soma de 3 e 4.
1. **Exercício de importação 1** : Crie dois arquivos Python. No primeiro, crie uma função `multiplica(a, b)` que retorna a multiplicação de dois números. No segundo arquivo, importe essa função e use-a sem executar nenhum código adicional do primeiro arquivo.
1. **Exercício de importação 2** : No arquivo principal, crie uma função `subtrai(a, b)` e, usando `if __name__ == "__main__":`, teste essa função. Depois, importe essa função em outro arquivo e teste-a novamente.
1. **Executar diretamente** : Crie um arquivo Python que defina uma função `imprime_lista(lista)` que imprime cada elemento de uma lista. Use `if __name__ == "__main__":` para testar a função com uma lista de números de 1 a 5.
1. **Evitar execução ao importar** : Crie um arquivo com uma função `imprime_ola()` que imprime "Olá!". No mesmo arquivo, use `if __name__ == "__main__":` para testar a função. Em outro arquivo, importe a função `imprime_ola()` e certifique-se de que nada mais seja executado ao importá-la.
1. **Múltiplas funções** : Crie um arquivo com duas funções: `dobro(n)` que retorna o dobro de um número e `triplo(n)` que retorna o triplo. Teste ambas as funções no bloco `if __name__ == "__main__":` com os números 2 e 3.
1. **Executar código adicional ao rodar diretamente** : Crie uma função `imprime_nome(nome)` que imprime "Olá, [nome]!". No bloco `if __name__ == "__main__":`, adicione um código que recebe o nome do usuário usando `input()` e o passe para a função `imprime_nome()`.
1. **Teste condicional** : Crie uma função `verifica_par(n)` que retorna `True` se um número for par e `False` se for ímpar. No bloco `if __name__ == "__main__":`, teste a função com o número 10 e imprima o resultado.
1. **Definição de constantes** : Crie um arquivo que defina uma constante `PI = 3.14`. No bloco `if __name__ == "__main__":`, calcule a área de um círculo com raio 5 e imprima o resultado.
1. **Importar e executar código** : Crie dois arquivos. No primeiro, crie uma função `quadrado(n)` que retorna o quadrado de um número e teste-a no bloco `if __name__ == "__main__":`. No segundo, importe e teste a função `quadrado()` sem executar o código adicional do primeiro arquivo.
1. **Verificação de strings** : Crie uma função `verifica_palindromo(palavra)` que retorna `True` se uma palavra for um palíndromo (mesma palavra lida de trás para frente). Use o bloco `if __name__ == "__main__":` para testar a função com a palavra "ana".
1. **Conversão de temperaturas** : Crie duas funções: `celsius_para_fahrenheit(c)` e `fahrenheit_para_celsius(f)`. Use o bloco `if __name__ == "__main__":` para testar as duas funções convertendo 100°C para Fahrenheit e 212°F para Celsius.
1. **Sequência de Fibonacci** : Crie uma função `fibonacci(n)` que imprime os primeiros `n` números da sequência de Fibonacci. No bloco `if __name__ == "__main__":`, peça ao usuário um número e imprima a sequência correspondente.
1. **Tabuada** : Crie uma função `tabuada(n)` que imprime a tabuada de multiplicação de 1 até 10 para o número `n`. No bloco `if __name__ == "__main__":`, peça ao usuário para digitar um número e imprima a tabuada desse número.
1. **Cálculo de fatorial** : Crie uma função `fatorial(n)` que calcula o fatorial de um número. Use o bloco `if __name__ == "__main__":` para testar a função com o número 5 e imprimir o resultado.
1. **Maior número de uma lista** : Crie uma função `maior_numero(lista)` que retorna o maior número de uma lista. No bloco `if __name__ == "__main__":`, crie uma lista de números e teste a função.
1. **Contagem de caracteres** : Crie uma função `conta_caracteres(string)` que retorna o número de caracteres em uma string. Teste essa função no bloco `if __name__ == "__main__":` com a string "Python".
1. **Média de uma lista** : Crie uma função `media(lista)` que retorna a média dos elementos de uma lista. Teste essa função no bloco `if __name__ == "__main__":` com uma lista de 5 números.
1. **Concatenação de strings** : Crie uma função `concatena_strings(s1, s2)` que retorna a concatenação de duas strings. No bloco `if __name__ == "__main__":`, peça ao usuário para digitar duas palavras e imprima a concatenação delas.

</details>

## wildcards

O uso de **wildcards** (`*`) ao importar módulos em Python, como em `from módulo import *`, permite que todas as funções, classes, e variáveis públicas do módulo sejam importadas de uma só vez, sem que seja necessário especificar explicitamente quais elementos você deseja importar.

### vantagens

1. **simplicidade** : facilita a importação quando você precisa de muitos elementos de um módulo, sem a necessidade de listar individualmente cada função ou classe;

    ```python
    from math import *

    print(sqrt(16))  # Não precisa especificar 'math.sqrt'
    ```

1. **conveniente em scripts curtos ou exploração interativa** : em ambientes interativos como o jupyter notebook, é prático quando você quer explorar rapidamente um módulo sem se preocupar com nomes específicos;

---

### desvantagens

1. **colisões de nomes** : ao importar tudo de um módulo, pode-se acabar sobrescrevendo funções ou variáveis que têm o mesmo nome em outros módulos ou no escopo atual do seu código, o que pode gerar erros difíceis de detectar;

    ```python
    from math import *
    from cmath import *

    print(sqrt(-1))  # De qual módulo 'sqrt' está sendo chamado?
    ```

1. **reduz a legibilidade** : quando se usa `import *`, fica difícil para outros desenvolvedores (e até para você mesmo) saber de onde vêm certas funções ou variáveis, especialmente em projetos grandes;

1. **carga desnecessária** : pode-se acabar importando funções ou variáveis que não são utilizadas, o que pode resultar em uma maior utilização de memória;

### por que usar?

- se está escrevendo scripts curtos, testes rápidos ou scripts de automação simples, o uso de `import *` pode ser conveniente para economizar tempo e tornar o código mais curto;
- em ambientes interativos, como no jupyter ou repl, o uso pode acelerar a experimentação;

### por que não usar?

- em projetos maiores ou bibliotecas, o uso de `import *` é desaconselhado porque reduz a clareza do código e aumenta o risco de colisão de nomes;
- torna a manutenção e depuração mais complicadas, especialmente quando múltiplos módulos estão envolvidos;

### alternativa recomendada

Se sabe exatamente quais funções ou classes deseja utilizar, é preferível importar apenas o necessário:

```python
from math import sqrt, pi
```

## exercícios wildcards

<details>
<summary>Lista de Exercícios</summary>

1. `from math import *` : Calcule a raiz quadrada de 49 e o logaritmo natural de 20.
1. `from random import *` : Gere 10 números aleatórios entre 1 e 100 e calcule a média.
1. `from time import *` : Exiba a data e a hora atual, e faça o código esperar 5 segundos antes de continuar.
1. `from os import *` : Crie um novo diretório chamado "exercicios" no sistema de arquivos atual.
1. `from sys import *` : Exiba o caminho do interpretador Python que está sendo usado.
1. `from json import *` : Converta um dicionário Python em uma string JSON e depois reconverta para um dicionário.

</details>

## `datetime`

O módulo `datetime` é fundamental para trabalhar com datas e horas, oferecendo uma ampla gama de funcionalidades para manipulação, formatação e cálculos com objetos de data e hora.

### visão geral

O módulo `datetime` fornece classes para manipular datas e horas de maneira simples e complexa. As principais classes disponíveis são:

1. **`date`** : representa uma data (ano, mês, dia);
1. **`time`** : representa um horário (hora, minuto, segundo, microsegundo);
1. **`datetime`** : combina informações de data e hora;
1. **`timedelta`** : representa a diferença entre duas datas, horas ou ambas;
1. **`tzinfo`** : fornece informações de fuso horário;
1. **`timezone`** : implementação concreta de `tzinfo` para fusos horários fixos;

### classe `date`

A classe `date` representa uma data no calendário gregoriano, composta por ano, mês e dia.

```python
from datetime import date

# data atual
hoje = date.today()
print(hoje)  # exemplo : 2024-04-27

# criando uma data específica
data_especifica = date(2023, 12, 25)
print(data_especifica)  # 2023-12-25
```

#### atributos

- **`year`** : ano (ex.: 2024);
- **`month`** : mês (1-12);
- **`day`** : dia do mês (1-31);

#### métodos comuns

- **`today()`** : retorna a data atual;
- **`fromtimestamp(timestamp)`** : cria uma data a partir de um timestamp POSIX;
- **`weekday()`** : retorna o dia da semana como um inteiro (0=segunda, 6=domingo);
- **`isoformat()`** : retorna a data no formato ISO 8601 (YYYY-MM-DD);

#### exemplo

```python
from datetime import date

# data atual
hoje = date.today()
print(f"Hoje é: {hoje}")

# dia da semana
dia_semana = hoje.weekday()
dias = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']
print(f"Dia da semana: {dias[dia_semana]}")

# formatação ISO
print("Formato ISO:", hoje.isoformat())
```

### classe `time`

A classe `time` representa um horário, independentemente da data.

```python
from datetime import time

# horário atual (não necessariamente o sistema)
horario = time(14, 30, 45)
print(horario)  # 14:30:45
```

#### atributos

- **`hour`** : hora (0-23);
- **`minute`** : minuto (0-59);
- **`second`** : segundo (0-59);
- **`microsecond`** : microssegundo (0-999999);
- **`tzinfo`** : informações de fuso horário;

#### métodos comuns

- **`isoformat()`** : retorna o horário no formato ISO 8601 (HH:MM:SS.microsegundos);

#### exemplo

```python
from datetime import time

# criando um horário específico
horario = time(9, 15, 30)
print(f"Horário: {horario}")

# formatação ISO
print("Formato ISO:", horario.isoformat())
```

### classe `datetime`

A classe `datetime` combina informações de data e hora em um único objeto.

```python
from datetime import datetime

# data e hora atual
agora = datetime.now()
print(agora)  # exemplo : 2024-04-27 14:30:45.123456

# criando uma data e hora específica
data_hora = datetime(2023, 12, 25, 18, 30, 0)
print(data_hora)  # 2023-12-25 18:30:00
```

#### atributos

- **`year`**, **`month`**, **`day`**;
- **`hour`**, **`minute`**, **`second`**, **`microsecond`**;
- **`tzinfo`**;

#### métodos comuns

- **`now()`** : retorna a data e hora atual.;
- **`utcnow()`** : retorna a data e hora atual em UTC.;
- **`fromtimestamp(timestamp)`** : cria um `datetime` a partir de um timestamp POSIX.;
- **`strftime(formato)`** : formata o `datetime` em uma string de acordo com o formato especificado.;
- **`strptime(string, formato)`** : cria um `datetime` a partir de uma string e um formato.;

#### exemplo

```python
from datetime import datetime

# data e hora atual
agora = datetime.now()
print(f"Agora: {agora}")

# formatação personalizada
formatado = agora.strftime("%d/%m/%Y %H:%M:%S")
print(f"Formatado: {formatado}")

# parsing de string para datetime
data_str = "25/12/2023 18:30:00"
data_convertida = datetime.strptime(data_str, "%d/%m/%Y %H:%M:%S")
print(f"Data convertida: {data_convertida}")
```

### classe `timedelta`

A classe `timedelta` representa uma diferença entre duas datas, horas ou ambos. É útil para realizar cálculos com datas e horas.

```python
from datetime import timedelta

# diferenca de 5 dias
diferenca = timedelta(days=5)
print(diferenca)  # 5 days, 0:00:00

# diferenca de 2 semanas, 3 dias e 4 horas
diferenca_complexa = timedelta(weeks=2, days=3, hours=4)
print(diferenca_complexa)  # 17 days, 4:00:00
```

#### atributos

- **`days`**;
- **`seconds`**;
- **`microseconds`**;
- **`weeks`**, **`hours`**, **`minutes`**, **`milliseconds`**, etc. (passados como argumentos);

#### exemplo

```python
from datetime import datetime, timedelta

# data atual
agora = datetime.now()

# adicionando 10 dias
futuro = agora + timedelta(days=10)
print(f"Futuro: {futuro}")

# subtraindo 2 horas
passado = agora - timedelta(hours=2)
print(f"Passado: {passado}")

# diferença entre duas datas
data1 = datetime(2023, 1, 1)
data2 = datetime(2024, 1, 1)
diferenca = data2 - data1
print(f"Diferença: {diferenca}")  # 365 days, 0:00:00
```

### classes `tzinfo` e `timezone`

A classe `tzinfo` é uma classe abstrata que fornece informações sobre fusos horários. A classe `timezone` é uma implementação concreta de `tzinfo` para fusos horários com deslocamento fixo em relação ao UTC.

#### trabalhando com fusos horários

```python
from datetime import datetime, timezone, timedelta

# UTC
utc = timezone.utc
agora_utc = datetime.now(utc)
print(f"UTC: {agora_utc}")

# Fuso horário com deslocamento de +3 horas
fuso_plus3 = timezone(timedelta(hours=3))
agora_plus3 = datetime.now(fuso_plus3)
print(f"UTC+3: {agora_plus3}")

# Fuso horário com deslocamento de -5 horas
fuso_minus5 = timezone(timedelta(hours=-5))
agora_minus5 = datetime.now(fuso_minus5)
print(f"UTC-5: {agora_minus5}")
```
<!--
#### exemplo Avançado com `pytz`

Para fusos horários mais complexos que envolvem regras de horário de verão, é recomendado usar a biblioteca `pytz` (não faz parte do módulo `datetime` padrão).

```python
from datetime import datetime
import pytz

# Fuso horário de São Paulo
fuso_sp = pytz.timezone('America/Sao_Paulo')
agora_sp = datetime.now(fuso_sp)
print(f"São Paulo: {agora_sp}")

# Fuso horário de Nova York
fuso_ny = pytz.timezone('America/New_York')
agora_ny = datetime.now(fuso_ny)
print(f"Nova York: {agora_ny}")
```

*Nota: Para usar `pytz`, você precisa instalá-lo via `pip install pytz`.* -->

### formatação e parsing

A formatação e parsing de datas e horas são essenciais para converter objetos `datetime` em strings e vice-versa.

#### `strftime` - formatação

O método `strftime` permite formatar objetos `datetime` em strings usando códigos de formatação.

| Código | Descrição                             | Exemplo |
|--------|---------------------------------------|---------|
| `%Y`   | ano com século (e.g., 2024)           | 2024    |
| `%m`   | mês como número decimal (01-12)       | 04      |
| `%d`   | dia do mês (01-31)                     | 27      |
| `%H`   | hora (00-23)                           | 14      |
| `%M`   | minuto (00-59)                         | 30      |
| `%S`   | segundo (00-59)                        | 45      |
| `%f`   | microssegundos (000000-999999)         | 123456  |
| `%A`   | nome completo do dia da semana        | Sábado  |
| `%B`   | nome completo do mês                   | Abril   |

**Exemplo**

```python
from datetime import datetime

agora = datetime.now()
formato = agora.strftime("%d/%m/%Y %H:%M:%S")
print(f"Formatado: {formato}")  # exemplo : 27/04/2024 14:30:45
```

#### `strptime` - parsing

O método `strptime` converte uma string em um objeto `datetime` de acordo com o formato especificado.

**Exemplo**

```python
from datetime import datetime

data_str = "25/12/2023 18:30:00"
formato = "%d/%m/%Y %H:%M:%S"
data_hora = datetime.strptime(data_str, formato)
print(f"Data e Hora: {data_hora}")  # 2023-12-25 18:30:00
```

### operações comuns

#### comparando datas e horas

Objetos `datetime` podem ser comparados diretamente.

```python
from datetime import datetime

data1 = datetime(2023, 1, 1)
data2 = datetime(2024, 1, 1)

if data1 < data2:
    print("data1 é anterior a data2")
else:
    print("data1 não é anterior a data2")
```

#### extraindo componentes

É possível acessar os componentes individuais de um objeto `datetime`.

```python
from datetime import datetime

agora = datetime.now()
print(f"Ano: {agora.year}")
print(f"Mês: {agora.month}")
print(f"Dia: {agora.day}")
print(f"Hora: {agora.hour}")
print(f"Minuto: {agora.minute}")
print(f"Segundo: {agora.second}")
```

#### substituindo componentes

É possível criar um novo objeto `datetime` com alguns componentes alterados usando o método `replace`.

```python
from datetime import datetime

agora = datetime.now()
novo_datetime = agora.replace(year=2025, month=12)
print(novo_datetime)
```

### manipulação avançada com `timedelta`

Além de adicionar ou subtrair `timedelta`, também é possível realizar operações mais complexas.

#### diferença entre datas

```python
from datetime import datetime

data1 = datetime(2024, 4, 27)
data2 = datetime(2023, 12, 25)
diferenca = data1 - data2
print(f"Diferença: {diferenca.days} dias")
```

#### multiplicação e divisão com `timedelta`

```python
from datetime import timedelta

delta = timedelta(days=2, hours=3)
multiplicado = delta * 3
print(multiplicado)  # 6 days, 9:00:00

dividido = delta / 2
print(dividido)  # 1 day, 15:00:00
```

### fusos horários avançados com `zoneinfo` (python 3.9+)

A partir do Python 3.9, o módulo `zoneinfo` foi introduzido para fornecer suporte nativo a fusos horários com base no banco de dados IANA.

#### uso básico

```python
from datetime import datetime
from zoneinfo import ZoneInfo

# fuso horário de São Paulo
fuso_sp = ZoneInfo("America/Sao_Paulo")
agora_sp = datetime.now(fuso_sp)
print(f"São Paulo: {agora_sp}")

# fuso horário de Tóquio
fuso_tokyo = ZoneInfo("Asia/Tokyo")
agora_tokyo = datetime.now(fuso_tokyo)
print(f"Tóquio: {agora_tokyo}")
```

#### conversão entre fusos horários

```python
from datetime import datetime
from zoneinfo import ZoneInfo

# hora atual em UTC
utc = ZoneInfo("UTC")
agora_utc = datetime.now(utc)
print(f"UTC: {agora_utc}")

# convertendo para horário de Nova York
fuso_ny = ZoneInfo("America/New_York")
agora_ny = agora_utc.astimezone(fuso_ny)
print(f"Nova York: {agora_ny}")
```

*Nota: É necessário ter o banco de dados de fusos horários disponível no sistema para que `zoneinfo` funcione corretamente.*

### exemplos práticos

Veja alguns exemplos práticos.

#### exemplo 1: calculando idade

```python
from datetime import date

def calcular_idade(data_nascimento):
    hoje = date.today()
    idade = hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))
    return idade

nascimento = date(1990, 5, 15)
idade = calcular_idade(nascimento)
print(f"Idade: {idade} anos")
```

#### exemplo 2: agendamento de eventos

```python
from datetime import datetime, timedelta

# data e hora do evento
evento = datetime(2024, 12, 31, 23, 59, 59)
agora = datetime.now()

# tempo restante
tempo_restante = evento - agora
print(f"Tempo restante para o evento: {tempo_restante}")

# verificando se o evento já passou
if agora > evento:
    print("O evento já ocorreu.")
else:
    print("O evento ainda está por vir.")
```

#### exemplo 3: formatação de logs

```python
from datetime import datetime

def log_mensagem(mensagem):
    agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{agora}] {mensagem}")

log_mensagem("Iniciando o processo...")
log_mensagem("Processo concluído com sucesso.")
```

#### exemplo 4: calculo julian date

```python
import sys
from datetime import datetime, timedelta

def calcula_julian():
    try:
        dias = int(input('digite o nr dias : '))
    except ValueError as erro:
        print('digite um numero valido')
        print(f'{erro = }')
        sys.exit(0)

    agora = datetime.now()
    ano_atual = agora.year

    inicio = datetime(ano_atual,1,1)

    julian_date = inicio + timedelta(days=dias-1)

    return julian_date

if __name__ == '__main__':
    for _ in range(10):
        julian = calcula_julian()
        print(julian.strftime("%d/%m/%Y"))
```

### Boas Práticas

1. **Sempre usar `datetime.now(tz=timezone.utc)` para armazenar datas e horas em UTC**, facilitando a conversão para outros fusos horários e evitando problemas com horário de verão;
1. **Utilizar o módulo `zoneinfo` (Python 3.9+)`** para manipulação avançada de fusos horários;
1. **Evitar a manipulação manual de strings para datas e horas**, preferindo métodos como `strftime` e `strptime` para garantir consistência;
1. **Utilizar `timedelta` para cálculos de diferenças de tempo**, garantindo precisão e evitando erros comuns em cálculos manuais;

## exercícios `datetime`

<details>
<summary>Lista de Exercícios</summary>

1. Exercícios sobre `date`
    1. Crie um objeto `date` que represente a data do seu aniversário.
    1. Exiba o ano, mês e dia da data atual usando o objeto `date`.
    1. Usando o método `today()`, exiba a data atual no formato `dd/mm/yyyy`.
    1. Crie uma função que receba um ano, mês e dia como argumentos e retorne o dia da semana dessa data.
    1. Utilize o método `fromtimestamp()` para criar uma data a partir do timestamp `1609459200` (representando 1 de janeiro de 2021).
    1. Exiba a data atual no formato ISO 8601 (`yyyy-mm-dd`) utilizando o método `isoformat()`.
    1. Crie uma função que receba duas datas e retorne a diferença entre elas em dias.
    1. Verifique se o dia 25 de dezembro de 2025 será uma sexta-feira.
    1. Crie um programa que pergunte a data de nascimento do usuário e calcule quantos dias faltam até o próximo aniversário.
    1. Escreva uma função que receba uma lista de datas e retorne a mais recente.
1. Exercícios sobre `time`
    1. Crie um objeto `time` que represente o horário 14:35:00.
    1. Exiba as horas, minutos e segundos de um objeto `time` que representa 18:45:30.
    1. Usando o método `isoformat()`, exiba o horário `08:15:45` no formato ISO (`hh:mm:ss`).
    1. Crie uma função que receba duas horas diferentes e retorne a diferença em segundos.
    1. Crie um objeto `time` que inclua microssegundos e exiba-os.
    1. Modifique um objeto `time` para alterar apenas os minutos, sem mudar os outros componentes.
    1. Escreva um programa que pergunte ao usuário a hora atual e exiba a hora em 12 horas (AM/PM).
    1. Verifique se o horário `23:59:59` é anterior ao horário `00:00:00` do dia seguinte.
    1. Crie uma função que receba um horário e adicione 15 minutos a ele.
    1. Exiba o horário atual sem exibir microssegundos.
1. Exercícios sobre `datetime`
    1. Crie um objeto `datetime` que represente 1º de janeiro de 2022 às 12:30:45.
    1. Exiba apenas a data de um objeto `datetime` que contém informações de data e hora.
    1. Utilize o método `now()` para exibir a data e hora atuais no formato `dd/mm/yyyy hh:mm:ss`.
    1. Converta o timestamp `1635724800` para um objeto `datetime`.
    1. Crie uma função que receba uma string no formato `dd/mm/yyyy hh:mm:ss` e converta-a para um objeto `datetime`.
    1. Crie uma função que receba uma data e hora e exiba o dia da semana correspondente.
    1. Adicione 10 dias e 5 horas a um objeto `datetime`.
    1. Crie um programa que pergunte ao usuário uma data e hora e calcule quantos dias faltam até o ano novo.
    1. Verifique se o `datetime(2023, 5, 20, 14, 30)` é anterior ao `datetime(2024, 1, 1, 0, 0)`.
    1. Escreva uma função que, dado um objeto `datetime`, retorne o nome do mês (ex.: Janeiro).
1. Exercícios sobre `timedelta`
    1. Crie um objeto `timedelta` que represente 3 dias, 2 horas e 30 minutos.
    1. Subtraia 7 dias da data atual utilizando `timedelta`.
    1. Crie uma função que receba duas datas e retorne a diferença entre elas em horas.
    1. Multiplique um objeto `timedelta` de 2 horas por 5 e exiba o resultado.
    1. Escreva um programa que calcule a diferença entre o horário atual e o meio-dia de hoje.
    1. Adicione 30 dias a uma data específica utilizando `timedelta`.
    1. Crie uma função que retorne quantos segundos existem em 3 dias, 5 horas e 10 minutos.
    1. Verifique se a diferença entre duas datas é maior que 1 mês, usando `timedelta`.
    1. Subtraia 45 minutos do horário atual e exiba o resultado.
    1. Calcule a diferença entre a meia-noite e o horário atual em minutos.
1. Exercícios sobre `timezone` e `zoneinfo`
    1. Crie um objeto `timezone` para o fuso horário UTC e exiba a hora atual em UTC.
    1. Converta o horário atual de UTC para o fuso horário de `UTC+3`.
    1. Crie uma função que receba uma data e hora e converta para o fuso horário de Nova York usando `zoneinfo`.
    1. Exiba a hora atual no fuso horário de Tóquio utilizando `zoneinfo`.
    1. Verifique a diferença de horas entre São Paulo e Londres usando `zoneinfo`.
    1. Crie um objeto `datetime` que represente a hora atual com o fuso horário UTC e converta-o para o fuso horário de `America/Sao_Paulo`.
    1. Crie uma função que receba duas datas em diferentes fusos horários e retorne qual é anterior.
    1. Converta a data e hora atual do fuso horário `UTC+5` para o fuso horário `UTC-2`.
    1. Crie um programa que pergunte ao usuário a cidade e exiba a hora atual dessa cidade usando `zoneinfo`.
    1. Verifique a diferença de tempo entre duas cidades à sua escolha utilizando `zoneinfo`.
1. Exercícios sobre classes
    1. Crie uma classe `Evento` com os atributos `nome` e `data_inicio` (um objeto `datetime`). Adicione um método que retorne o nome do evento e sua data no formato `dd/mm/yyyy hh:mm`.
    1. Implemente uma classe `Tarefa` que tenha os atributos `descricao`, `data_criacao` (um objeto `date`) e `data_entrega` (outro objeto `date`). Adicione um método que informe quantos dias faltam até a entrega.
    1. Desenvolva uma classe `Relogio` que tenha o atributo `hora_atual` (um objeto `time`). Adicione um método que exiba o horário no formato de 12 horas com AM/PM.
    1. Crie uma classe `Compromisso` com os atributos `descricao`, `data_compromisso` (um objeto `datetime`) e `duracao` (um objeto `timedelta`). Adicione um método que retorne a data de término do compromisso.
    1. Implemente uma classe `EventoRepetido` com os atributos `nome`, `data_inicio` (um objeto `datetime`) e `frequencia` (um objeto `timedelta`). Adicione um método que retorne a próxima data do evento com base na frequência.
    1. Escreva uma classe `JornadaDeTrabalho` com os atributos `hora_inicio` e `hora_fim` (ambos objetos `time`). Adicione um método que calcule a quantidade de horas trabalhadas.
    1. Crie uma classe `AluguelDeCarro` com os atributos `data_inicio`, `data_fim` (objetos `datetime`). Adicione um método que calcule o valor total do aluguel, sabendo que o preço por dia é de R$100.
    1. Desenvolva uma classe `DataFormatada` com um atributo `data` (um objeto `date`). Adicione métodos para retornar a data nos formatos `yyyy-mm-dd` e `dd/mm/yyyy`.
    1. Implemente uma classe `Viagem` com os atributos `destino`, `data_partida` e `data_retorno` (ambos objetos `datetime`). Adicione um método que informe quantos dias a viagem vai durar.
    1. Crie uma classe `Projeto` com os atributos `nome_projeto`, `data_inicio`, `data_prevista_termino` (ambos objetos `date`). Adicione um método que retorne se o projeto está dentro do prazo (comparando a data atual com a data de término).
    1. Desenvolva uma classe `RegistroDePonto` com os atributos `hora_entrada` e `hora_saida` (objetos `datetime`). Adicione um método que calcule a quantidade de horas trabalhadas em um dia.
    1. Escreva uma classe `Aluno` com os atributos `nome`, `data_nascimento` (um objeto `date`). Adicione um método que calcule a idade do aluno.
    1. Crie uma classe `Treinamento` com os atributos `modalidade`, `hora_inicio`, `hora_fim` (objetos `time`). Adicione um método que exiba o tempo total de duração do treinamento.
    1. Implemente uma classe `Lembrete` com os atributos `mensagem`, `data_lembrete` (um objeto `datetime`). Adicione um método que verifique se o lembrete está configurado para uma data no passado ou futuro.
    1. Desenvolva uma classe `ConsultaMedica` com os atributos `paciente`, `data_consulta` (um objeto `datetime`) e `duracao` (um objeto `timedelta`). Adicione um método que exiba o horário de término da consulta.
    1. Crie uma classe `Encontro` com os atributos `local`, `data` (um objeto `date`) e `hora` (um objeto `time`). Adicione um método que exiba a data e hora do encontro no formato: `dd/mm/yyyy às hh:mm`.
    1. Escreva uma classe `Contrato` com os atributos `nome_cliente`, `data_assinatura` (um objeto `date`) e `data_vencimento` (outro objeto `date`). Adicione um método que calcule quantos dias faltam para o vencimento do contrato.
    1. Implemente uma classe `Corrida` com os atributos `distancia`, `hora_inicio` (um objeto `datetime`) e `tempo_estimado` (um objeto `timedelta`). Adicione um método que retorne a previsão de término da corrida.
    1. Desenvolva uma classe `ReservaDeQuarto` com os atributos `numero_quarto`, `data_checkin` e `data_checkout` (objetos `datetime`). Adicione um método que informe quantas noites o hóspede vai ficar no hotel.
    1. Crie uma classe `Feriado` com os atributos `nome`, `data_feriado` (um objeto `date`). Adicione um método que informe quantos dias faltam para o próximo feriado a partir da data atual.

</details>

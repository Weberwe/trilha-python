Índice

1. [módulo `sys`](#módulo-sys)
    1. [`sys.argv`](#sysargv)
    1. [`sys.exit`](#sysexit)
    1. [`sys.path`](#syspath)
    1. [`sys.stdin` `sys.stdout` `sys.stderr`](#sysstdin-sysstdout-sysstderr)
    1. [`sys.platform`](#sysplatform)
    1. [`sys.getsizeof`](#sysgetsizeof)
    1. [`sys.version` e `sys.version_info`](#sysversion-e-sysversion_info)
1. [exercícios módulo `sys`](#exercícios-módulo-sys)
1. [módulo `os`](#módulo-os)
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
1. [exercícios módulo `os`](#exercícios-módulo-os)
1. [módulo `random`](#módulo-random)
    1. [`random.random()`](#randomrandom)
    1. [`random.uniform(a, b)`](#randomuniformab)
    1. [`random.randint(a, b)`](#randomrandintab)
    1. [`random.randrange(start, stop, step)`](#randomrandrangestartstopstep)
    1. [`random.choice(seq)`](#randomchoiceseq)
    1. [`random.choices(population, k=1)`](#randomchoicespopulatiok)
    1. [`random.sample(population, k)`](#randomsamplepopulationk)
    1. [`random.shuffle(seq)`](#randomshuffleseq)
    1. [`random.seed()`](#randomseed)
    1. [`random.gauss(mu, sigma)`](#randomgaussmusgima)
    1. [`random.betavariate(alpha, beta)`](#randombetavariatealphabeta)
1. [exercícios módulo `random`](#exercícios-módulo-random)
1. [módulo `time`](#módulo-time)
    1.[`time.time()`](#timetime)
    1.[`time.sleep(segundos)`](#timesleepsegundos)
    1.[`time.localtime([segundos])`](#timelocaltimesegundos)
    1.[`time.strftime(formato[, struct_time])`](#timestrftimeformatostruct_time)
    1.[`time.gmtime([segundos])`](#timegmtimesegundos)
    1.[`time.mktime(t)`](#timemktimet)
    1.[`time.asctime([struct_time])`](#timeasctimestruct_time)
    1.[`time.ctime([segundos])`](#timectimesegundos)
    1.[`time.perf_counter()`](#timeperf_counter)
    1.[`time.monotonic()`](#timemonotonic)
    1.[`time.process_time()`](#timeprocess_time)
1. [exercícios módulo `time`](#exercícios-módulo-time)

# módulos

## módulo `sys`

O módulo `sys` em Python é um dos módulos built-in que fornecem funções e variáveis usadas para manipular diferentes partes do ambiente de execução do Python. Esse módulo é essencial para interagir com o sistema e o interpretador do Python.

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

### `random.uniform(a, b)`

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

### `random.randint(a, b)`

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

### `random.randrange(start, stop, step)`

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

### `random.choice(seq)`

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

### `random.choices(population, k=1)`

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

### `random.sample(population, k)`

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

### `random.shuffle(seq)`

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

### `random.gauss(mu, sigma)`

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

### `random.betavariate(alpha, beta)`

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

### `time.time()`

Essa função retorna o número de segundos desde a *"época"*, ou seja, um número do tipo *float* que representa o tempo em segundos.  A *"época"* (epoch) é o ponto de referência para a contagem do tempo. No Unix, a *epoch* é definida como meia-noite (00:00:00) de 1 de janeiro de 1970.

**exemplo :**
```python
import time
segundos = time.time()
print(f"Segundos desde 1º de janeiro de 1970: {segundos}")
```

### `time.sleep(segundos)`

Essa função faz com que o programa pause ou "durma" por um determinado número de segundos. É útil em casos onde se deseja que o código aguarde um certo tempo antes de prosseguir.

**exemplo :**
```python
import time
print("Esperando 5 segundos...")
time.sleep(5)
print("Fim da espera.")
```

### `time.localtime([segundos])`

Essa função converte o tempo dado em segundos desde a *epoch* em um objeto de tempo local (`struct_time`). Se nenhum argumento for fornecido, ela utiliza o tempo atual (retornado por `time.time()`). O objeto `struct_time` tem vários atributos como `tm_year` (ano), `tm_mon` (mês), `tm_mday` (dia do mês), `tm_hour` (hora), etc.

**exemplo :**
```python
import time
tempo_atual = time.localtime()
print(f"Ano atual: {tempo_atual.tm_year}")
print(f"Mês atual: {tempo_atual.tm_mon}")
print(f"Dia atual: {tempo_atual.tm_mday}")
```

### `time.strftime(formato[, struct_time])`

Converte um objeto `struct_time` em uma string formatada, de acordo com a especificação de formato fornecida. Por exemplo, `%Y` para ano completo, `%m` para mês, `%d` para dia do mês, `%H` para hora (formato 24h), `%M` para minutos, `%S` para segundos.

Mais Formatos [aqui](https://docs.python.org/3/library/time.html#time.strftime)

**exemplo :**
```python
import time
tempo_atual = time.localtime()
formato = time.strftime("%Y-%m-%d %H:%M:%S", tempo_atual)
print(f"Data e hora formatada: {formato}")
```

### `time.gmtime([segundos])`

Semelhante a `time.localtime()`, mas retorna o tempo no fuso horário UTC (Tempo Universal Coordenado), em vez do fuso horário local.

**exemplo :**
```python
import time
tempo_utc = time.gmtime()
print(f"Ano atual (UTC): {tempo_utc.tm_year}")
```

### `time.mktime(t)`

Faz o inverso de `time.localtime()` ou `time.gmtime()`, convertendo uma estrutura de tempo (`struct_time`) em segundos desde a *epoch*.

**exemplo :**
```python
import time
tempo_local = time.localtime()
segundos = time.mktime(tempo_local)
print(f"Segundos desde a epoch para a hora local: {segundos}")
```

### `time.asctime([struct_time])`

Converte um objeto `struct_time` em uma string no formato: `'Dia_sem Mês Dia Hora:Min:Seg Ano'`. Se não for fornecido nenhum argumento, usa o tempo local.

**exemplo :**
```python
import time
print(time.asctime())  # Exemplo de saída: 'Tue Sep  6 10:05:12 2024'
```

### `time.ctime([segundos])`

Converte o tempo, em segundos desde a epoch, em uma string legível. Se nenhum argumento for passado, usa o tempo atual.

**exemplo :**
```python
import time
print(time.ctime())  # Exemplo de saída: 'Tue Sep  6 10:05:12 2024'
```

### `time.perf_counter()`

Retorna o valor de um temporizador de alta resolução, medido em segundos. É útil para medir o tempo de execução de trechos de código.

**exemplo :**
```python
import time
inicio = time.perf_counter()
time.sleep(2)
fim = time.perf_counter()
print(f"Tempo decorrido: {fim - inicio} segundos")
```

### `time.monotonic()`

Similar a `time.perf_counter()`, mas este temporizador não pode ser ajustado para frente ou para trás (não é afetado por mudanças no relógio do sistema).

**exemplo :**
```python
import time
inicio = time.monotonic()
time.sleep(1)
fim = time.monotonic()
print(f"Tempo decorrido: {fim - inicio} segundos")
```

### `time.process_time()`

Retorna o tempo de CPU usado pelo processo atual, em segundos.

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

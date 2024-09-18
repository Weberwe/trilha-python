Índice

1. [conceito de namespace](#conceito-de-namespace)
1. [tipos de namespaces](#tipos-de-namespaces)
    1. [1. namespace local](#1-namespace-local)
    1. [2. namespace global](#2-namespace-global)
    1. [3. namespace built-in](#3-namespace-built-in)
1. [hierarquia dos namespaces](#hierarquia-dos-namespaces)
1. [modificando variáveis globais dentro de funções](#modificando-variáveis-globais-dentro-de-funções)
1. [namespaces e módulos](#namespaces-e-módulos)
1. [exercícios](#exercícios)

# namespaces

Namespaces em Python são sistemas que garantem que os nomes de variáveis, funções, classes e outros identificadores usados em um programa sejam únicos e não entrem em conflito uns com os outros. Eles funcionam como contêineres que mapeiam nomes para objetos correspondentes, de forma que diferentes partes de um código possam usar os mesmos nomes sem interferir umas nas outras.

## conceito de namespace

Um namespace é essencialmente uma tabela de símbolos (ou um mapeamento) que relaciona nomes com objetos (valores, funções, classes, etc.). Cada nome é uma chave, e o objeto associado a ele é o valor.

Exemplo :

Imagine que tenha duas variáveis com o mesmo nome em contextos diferentes :

```python
def funcao1():
    variavel = 10
    print(variavel)

def funcao2():
    variavel = 20
    print(variavel)

funcao1()  # saída : 10
funcao2()  # saída : 20
```

Aqui, `variavel` é usada em ambas as funções, mas cada uso pertence a um namespace diferente (o namespace de cada função). Portanto, as duas variáveis `variavel` não entram em conflito, pois estão em namespaces separados.

## tipos de namespaces

Em Python, existem três tipos principais de namespaces:

1. **namespace local**
2. **namespace global**
3. **namespace built-in**

### 1. namespace local

Este é o namespace que é criado cada vez que uma função é chamada. Ele contém os nomes das variáveis locais e outros objetos definidos dentro da função. Quando a função termina, seu namespace local é destruído.

```python
def minha_funcao():
    x = 5  # x está no namespace local de minha_funcao
    print(x)

minha_funcao()  # saída : 5
```

Dentro de `minha_funcao`, `x` pertence ao namespace local da função.

### 2. namespace global

O namespace global é o espaço que contém todos os nomes definidos no nível principal de um script ou módulo. Ele existe desde o início da execução do programa até o seu término. Todas as variáveis, funções e classes definidas fora de qualquer função pertencem ao namespace global.

```python
x = 10  # x está no namespace global

def minha_funcao():
    print(x)

minha_funcao()  # saída : 10
```

Aqui, `x` pertence ao namespace global, e `minha_funcao` pode acessar `x` diretamente, pois ela não tem uma variável `x` no seu namespace local.

### 3. namespace built-in

O namespace built-in é criado pelo próprio Python e contém todas as funções e objetos que estão sempre disponíveis, como `print()`, `len()`, `int()`, entre outros. Este namespace é acessível de qualquer lugar no código.

```python
print(len("Python"))  # len é uma função built-in
```

A função `len()` pertence ao namespace built-in, por isso pode ser usada sem precisar importar ou definir.

### hierarquia dos namespaces

A Python segue uma ordem específica para resolver nomes, conhecida como a regra LEGB :

1. **Local** : o primeiro lugar que Python procura por um nome é no namespace local (dentro de uma função, por exemplo);
2. **Enclosing** : se o nome não é encontrado no namespace local, Python procura no namespace da função que contém outra função (para casos de funções aninhadas);
3. **Global** : se não for encontrado no namespace local ou enclosing, Python procura no namespace global;
4. **Built-in** : finalmente, se o nome não for encontrado em nenhum dos namespaces anteriores, Python procura no namespace built-in;

Exemplo :

```python
x = "global"

def funcao_externa():
    x = "enclosing"

    def funcao_interna():
        x = "local"
        print(x)

    funcao_interna()

funcao_externa()  # saída : local
```

Aqui, a função `funcao_interna` encontra `x` no seu namespace local. Se a linha `x = "local"` fosse removida, ela procuraria `x` no namespace enclosing (o namespace de `funcao_externa`), e assim por diante até encontrar o nome ou gerar um erro.

## modificando variáveis globais dentro de funções

Se quiser modificar uma variável global dentro de uma função, precisa usar a palavra-chave `global`. Caso contrário, Python considerará que está criando uma nova variável local.

```python
x = 10

def modificar_x():
    global x
    x = 20

modificar_x()
print(x)  # saída : 20
```

Aqui, `global x` informa ao Python que `x` dentro da função refere-se à `x` do namespace global.

## namespaces e módulos

Cada módulo em Python tem seu próprio namespace global, que é independente dos namespaces globais de outros módulos. Isso permite que tenha variáveis e funções com os mesmos nomes em diferentes módulos sem que eles entrem em conflito.

Exemplo :

```python
# modulo1.py
x = 10

def mostrar():
    print("Modulo 1:", x)

# modulo2.py
x = 20

def mostrar():
    print("Modulo 2:", x)

# main.py
import modulo1
import modulo2

modulo1.mostrar()  # saída : Modulo 1: 10
modulo2.mostrar()  # saída : Modulo 2: 20
```

Aqui, `modulo1` e `modulo2` têm suas próprias variáveis `x`, e elas não interferem uma na outra porque estão em namespaces separados.

## exercícios

<details>
<summary>Lista de Exercícios</summary>

1. Crie um módulo chamado `animais.py` com uma variável global `especies` e uma função `listar_especies()`. No script principal, importe o módulo e altere a variável `especies` diretamente. Em seguida, use a função `listar_especies()` para imprimir as espécies.
1. Crie um módulo chamado `numeros.py` com uma variável global `n` e uma função `incrementar_n()` que aumenta o valor de `n` em 1. No script principal, importe o módulo e chame `incrementar_n()` duas vezes. Imprima o valor de `n` após cada chamada da função.
1. Crie um módulo chamado `contas.py` com uma variável global `saldo` e uma função `depositar(valor)` que adiciona um valor ao saldo. No script principal, importe o módulo e faça um depósito de `100` e depois de `50`. Imprima o saldo após cada depósito.
1. Crie um módulo chamado `mensagens.py` com uma variável global `mensagem` e uma função `atualizar_mensagem(nova_mensagem)`. No script principal, importe o módulo e atualize a `mensagem` para `"Olá, Mundo!"` e imprima o valor da mensagem após a atualização.
1. Crie um módulo chamado `configuracoes.py` com uma variável global `config` e uma função `alterar_configuracao(chave, valor)`. No script principal, importe o módulo e altere uma configuração específica. Imprima o valor da configuração alterada.
1. Crie um módulo chamado `matematica.py` com uma função `adicionar(a, b)` que retorna a soma de dois números e uma variável global `resultado`. No script principal, importe o módulo e use a função `adicionar()` para calcular a soma de `5` e `7`, e depois imprima o valor da variável `resultado`.
1. Crie um módulo chamado `util.py` com uma função `multiplicar(a, b)` que retorna o produto de dois números e uma variável global `produto`. No script principal, importe o módulo, use a função `multiplicar()` e depois imprima o valor da variável `produto`.
1. Crie um módulo chamado `lista_util.py` com uma função `adicionar_elemento(lista, elemento)` que adiciona um elemento a uma lista e uma variável global `lista`. No script principal, importe o módulo e adicione dois elementos à lista, imprimindo a lista após cada adição.
1. Crie um módulo chamado `calendario.py` com uma função `adicionar_dia(dias)` que adiciona dias à variável global `data` e uma variável global `data`. No script principal, importe o módulo e adicione `10` dias à data. Imprima a data após a adição.
1. Crie um módulo chamado `personagem.py` com uma variável global `nome` e uma função `alterar_nome(novo_nome)`. No script principal, importe o módulo, altere o nome do personagem e imprima o nome alterado.
1. Crie um módulo chamado `valores.py` com uma função `atribuir_valor(chave, valor)` e uma variável global `valores`. No script principal, importe o módulo e atribua valores a várias chaves. Imprima o dicionário `valores` após as atribuições.
1. Crie um módulo chamado `estatisticas.py` com uma função `calcular_media(lista)` que retorna a média dos valores em uma lista e uma variável global `media`. No script principal, importe o módulo e calcule a média de uma lista de números, imprimindo o valor da variável `media`.
1. Crie um módulo chamado `configuracoes_usuario.py` com uma função `definir_preferencias(preferencias)` e uma variável global `preferencias`. No script principal, importe o módulo e defina e imprima preferências de usuário.
1. Crie um módulo chamado `dados_pessoais.py` com uma função `atualizar_dados(nome, idade)` e variáveis globais `nome` e `idade`. No script principal, importe o módulo, atualize e imprima os dados pessoais.
1. Crie um módulo chamado `historia.py` com uma função `adicionar_evento(evento)` que adiciona eventos à lista global `eventos`. No script principal, importe o módulo e adicione três eventos à lista. Imprima a lista após cada adição.
1. Crie um módulo chamado `itens.py` com uma função `adicionar_item(item)` e uma variável global `itens`. No script principal, importe o módulo e adicione três itens à lista. Imprima a lista de itens após cada adição.
1. Crie um módulo chamado `estoque.py` com uma função `adicionar_estoque(item, quantidade)` e uma variável global `estoque`. No script principal, importe o módulo e adicione estoque para dois itens diferentes, imprimindo o estoque após cada adição.
1. Crie um módulo chamado `email.py` com uma função `enviar_email(destinatario, assunto, corpo)` e uma variável global `enviado`. No script principal, importe o módulo e envie um e-mail, alterando o valor da variável `enviado` para `True` após o envio. Imprima o valor da variável.
1. Crie um módulo chamado `jogador.py` com uma função `atualizar_pontuacao(pontuacao)` e uma variável global `pontuacao`. No script principal, importe o módulo e atualize a pontuação do jogador em três etapas. Imprima a pontuação após cada atualização.
1. Crie um módulo chamado `projetos.py` com uma função `adicionar_projeto(nome)` e uma variável global `projetos`. No script principal, importe o módulo e adicione três projetos à lista. Imprima a lista de projetos após cada adição.

</details>

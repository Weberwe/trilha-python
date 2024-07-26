Índice Usando o Python

1. [pep 8](#pep-8)
1. [usando o python](#usando-o-python)
1. [interpretador python](#interpretador-python)
1. [módulo python](#módulo-python)
1. [explicando exemplos](#explicando-exemplos)
1. [comandos de saída e entrada de dados](#comando-de-saída-e-entrada-de-dados)
1. [comentários](#comentários)
1. [o que foi visto até agora](#o-que-foi-visto-até-agora)

# pep 8
Antes de iniciar o Python é preciso saber que existe a `PEP 8`.

A PEP 8 existe para melhorar a leitura do código Python. Uma vez o Guido van Rossum (autor do Python) disse que `um código é lido com muito mais frequência do que é escrito`.

Um código pode ser escrito em alguns minutos ou um dia inteiro, mas uma vez escrito, ele nunca mais terá que ser escrito novamente (muito provavelmente alterado em algum ponto). E DEFINITIVAMENTE ele terá que ser lido novamente. Pode ser difícil de relembrar o que um determinado trecho de código feito há alguns dias, semanas, meses ou até mesmo anos está fazendo se ele não estiver bem claro e documentado.

Seguir as orientações da PEP 8 ajuda a manter uma boa legibilidade das variáveis; saber que há espaço em branco suficiente para tornar o código mais fácil de ler; saber que os comentários são precisos e ajudam a lembrar o que ele faz. Além desses aspectos, também facilita para ler o código de outros programadores.

O manual de referência para todas essas boas práticas está documentado na [PEP 8 - Style Guide for Python Code](https://peps.python.org/pep-0008) (em inglês). PEP é uma abreviação de Python Enhancement Proposals (Propostas de Melhoramentos do Python).

Conforme novas funcionalidades do Python são apresentadas, sua respectiva PEP 8 será mostrada.

# usando o python
O Python pode ser utilizado de diversas formas.

As duas mais comuns são:
- [Interpretador Python](#interpretador-python) : ele é acessado pelo Prompt de Comando digitando python e também é conhecido como *Modo Interativo*;
- [Módulo Python](#módulo-python) : arquivo com extensão .py;

> [!TIP]
> Ative a visualização das extensões de arquivos de seu sistema operacional.
>
> [Como ativar no Windows](https://support.microsoft.com/pt-br/windows/extens%C3%B5es-de-nome-de-arquivo-comuns-no-windows-da4a4430-8e76-89c5-59f7-1cdbbc75cb01);
>
> [Como ativar no macOS](https://support.apple.com/pt-br/guide/mac-help/mchlp2304/mac);
>
> Como ativar no Linux : se usa Linux, provavelmente você já sabe como;

## interpretador python
Uma vez que o Python é instalado, é possível iniciar o interpretador através do terminal (Linux e macOS) ou Prompt de Comando (Windows). Para isso, basta realizar a chamada do python no shell.

Chamada do Python no Linux / macOS :
```shell
$ python
Python 3.12.3 (main, Apr 23 2024, 09:16:07) [GCC 13.2.1 20240417] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> |
```

Chamada do Python no Windows :
```powershell
C:\> python
Python 3.12.3 (tags/v3.12.2:6abddd9, Feb 6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> |
```

Pode-se sair do interpretador digitando :
```shell
>>> quit()
```
ou
```shell
>>> exit()
```
ou ainda segurando as teclas `Ctrl + z` no Windows ou `Ctrl + d` no Linux/macOS;

Os recursos de edição de linha do interpretador incluem edição interativa, substituição de histórico e completamento de código.

Quando os comandos são lidos a partir do terminal/console, diz-se que o interpretador está em modo interativo. Nesse modo, ele solicita um próximo comando através do *prompt primário*, representado por três sinais de maior `>>>`; para linhas de continuação do comando atual, o *prompt secundário* padrão é formado por três pontos `...`.

Veja alguns exemplos de uso do interpretador :
```python
$ python
Python 3.12.3 (main, Apr 23 2024, 09:16:07) [GCC 13.2.1 20240417] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 10
10
>>> 30 + 12
42
>>>
>>> 'um texto'
'um texto'
>>> "outro texto"
'outro texto'
>>>
>>> True is False
False
>>>
>>> 4/1 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11
2.9760461760461765
>>>
>>> a_terra_eh_plana = True
>>> if a_terra_eh_plana:
...     print('Cuidado com o Cthulhu!')
...
Cuidado com o Cthulhu!
>>> |
```
Há também uma forma de executar comandos python diretamente do terminal (fora do interpretador), mas isso será visto mais adiante.

`PS.:` nos sistemas Linux e macOS pode haver uma diferença na versão do interpretador. Muitos pacotes antigos ainda presentes nesses sistemas são dependentes da versão 2 do Python para funcionar corretamente, número esse que diminui a cada ano. Por causa disso, em algumas versões mais antigas do Linux e do macOS ainda é necessário digitar `python3` para que a terceira versão seja executada e não a segunda.

## módulo python
Outra forma de usar o Python é através de arquivos com a extensão `.py`, que são chamados de *módulos* no Python.

Quando se usa um módulo Python, qualquer comando lá colocado é executado apenas quando ele é chamado após o `python` no terminal.

Por exemplo, imagine que há um módulo chamado `resposta.py` que, quando chamado, vai exibir uma pergunta e sua resposta.

Módulo `resposta.py` :
```python
valor = 42

print('Qual é a resposta da vida, do universo e tudo mais?')

if valor != 42:
    print('Resposta errada!')
else:
    print(f'A resposta é : {valor}')
```
Chamando o módulo `resposta.py` usando o interpretador python :
```shell
$ python resposta.py
Qual é a resposta da vida, do universo e tudo mais?
A resposta é : 42
```

## explicando exemplos
A partir de agora muitos exemplos serão mostrados. Qualquer exemplo mostrado em *Modo Interativo* também pode ser usado em um *módulo* Python.

Usando o módulo *main.py* e sua chamada pelo interpretador :
```python
# usando o módulo main.py
n_1 = 10
n_2 = 32

print(f'A expressão {n_1} + {n_2} é igual a {n_1 + n_2}.')
```
```shell
$ python main.py
A expressão 10 + 32 é igual a 42.
```

Usando o mesmo exemplo diretamente no interpretador :
```python
>>> # usando o Interpretador Python
>>> n_1 = 10
>>> n_2 = 32
>>>
>>> print(f'A expressão {n_1} + {n_2} é igual a {n_1 + n_2}.')
A expressão 10 + 32 é igual a 42.
>>>
>>> |
```

## comando de saída e entrada de dados

Os algoritmos precisam ser 'alimentados' com dados proveniente do meio externo para efetuarem as operações e cálculos que são necessários para alcançar algum objetivo. Com essa finalidade, utiliza-se comandos de entrada e saída. Por hora, o foco será na saída de dados.

### saída de dados

Para que um algoritmo em Python possa mostrar os dados que calculou dentro do módulo, usa-se o comando `print()`. Em português, pode ser lido como "imprimir" algo na tela.

Veja como fica :
```python
>>> nome = 'Arnoldão'
>>> print(nome)
Arnoldão
>>> print(10 + 32)
42
```

Esse comando, também permite mostrar mais de um objeto, desde que esteja separado por vírgula.
```python
>>> nome = 'Arnoldão'
>>> valor = 10
>>> print(nome, valor)
Arnoldão 10
>>> print(nome, 3.141592)
Arnoldão 3.141592
>>> print(52 - valor)
42
```

Ele também funciona no modo interativo, mostrando e executando alguns comandos de dentro da string, como a quebra de linha `\n`, por exemplo. Mais adiante isso será visto com mais detalhes.

## comentários
Quando se desenvolve códigos, é muito importante criar o hábito de manter seu código bem documentado. Deixar ele claro para outras pessoas e até para você mesmo do futuro quando precisa voltar e realizar alterações nele meses depois de criado.

Comentários em Python começam com o caractere cerquilha `#` e se estende até o final da linha. Um comentário pode aparecer no início da linha ou após espaço em branco ou código, mas não dentro de uma string literal. Nela, ele será interpretado como apenas mais um caractere da string.

Exemplos :
```python
>>> # este é o primeiro comentário
>>> num = 1 # e este é o segundo comentário
>>>         # ... e agora o terceiro!
>>> texto = '# isto não é um comentário porque está dentro das aspas'
>>> texto
'# isto não é um comentário porque está dentro das aspas'
```

### pep 8 - comentários
<details>
  <summary>Detalhes</summary>

Os comentários possuem 3 regras básicas :
- limite o tamanho da linha dos comentários e das strings de documentação em 79 caracteres;
- use frases completas, iniciando com letra maiúscula;
- tenha certeza de atualizar os comentários se o código for alterado;

Existem diversos tipos de comentários em Python. Conforme os estudos avançam, mais tipos serão vistos.

### comentários de linha
Comentários de linha explicam um único treco de código. São úteis para relembrar, ou explicar para outros desenvolvedores, porque certa linha de código é necessária.

A PEP 8 sugere que :
- use os comentários de linha com moderação;
- escreva o comentário do código na mesma linha a que se referem;
- separe os comentários de linha com dois ou mais espaços;
- inicie o comentário com um `#` e um simples espaço;
- não use para explicar o óbvio;

```python
>>> x = 5  # este é um comentário de linha
```

Às vezes, um nome de variavel pode servir melhor que um comentário :
```python
>>> x = 'Arnold Schwarzenegger'  # nome do ator
>>>
>>> nome_ator = 'Arnold Schwarzenegger'
```

Comentários de linha como o abaixo são uma má prática porque eles são óbvios e poluem o código :
```python
>>> lista_vazia = []  # inicializa uma lista vazia
>>>
>>> x = 5
>>> x = x * 5  # multiplica x por 5
```
</details>

## o que foi visto até agora

Até agora foram vistos os tipos primitivos, como declarar variáveis, constantes, como usar expressões aritméticas e lógicas, parênteses, comandos de atribuição e comentários.

Tudo o que foi visto pode ser usado diretamente no Interpretador do Python.

<details>
  <summary>Lista de Exercícios</summary>

Refaça todos os exercícios do arquivo [tipos-primitivos](tipos-primitivos.md#expressões-aritméticas) a partir das expressões aritméticas, mas agora usando o interpretador do Python.

Use um ou mais módulos Python para salvar a execução de seus códigos.

</details>


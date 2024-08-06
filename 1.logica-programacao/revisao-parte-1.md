Índice Revisao - Parte 1

1. [tipos primitivos](#tipos-primitvos)
1. [variáveis](#variáveis)
1. [int](#int)
1. [float](#float)
1. [combinando int e float](#combinando-int-e-float)
1. [str](#str)
1. [bool](#bool)
1. [condicional if-elif-else](#condicional-if-elif-else)

# revisão

## tipos primitivos

O Python possui 4 tipos primitivos básicos, são eles :
* **int** : representa os números inteiros negativos, zero e positivos;
* **float** : representa os números de ponto flutuante negativos, zero e positivos;
* **string** : representa tudo que é texto entre as simples e duplas;
* **boolean** : representa o verdadeiro e falso, das comparações;

## variáveis

Variáveis são usadas para armazenar valores dos tipos de Python. É uma boa prática usar nomes de variáveis que façam sentido com seu uso.

Por exemplo :
```python
# números inteiros (int)
idade = 25
anos_de_experiencia = 3
quantidade_de_alunos = 30
numero_de_livros = 10
pontuacao = 85
dias_no_ano = 365
numero_de_irmaos = 2
quantidade_de_copos = 6
anos_de_estudo = 15
numero_do_andar = 4

# números de ponto flutuante (float)
preco = 19.99
altura = 1.75
peso = 68.5
distancia = 12.34
nota_final = 8.7
temperatura = 22.0
salario = 3500.75
media_dos_alunos = 7.4
taxa_de_crescimento = 1.03
velocidade_media = 60.5

# strings (str)
nome = ´João´
cidade = "São Paulo"
pais = "Brasil"
curso = ´Engenharia´
profissao = "médico"
nome_da_empresa = "Oscorp"
modelo_do_carro = "Civic"
marca_do_celular = "Samsung"
cor_favorita = "azul"
time_do_coracao = "Grêmio"

# booleanos (bool)
esta_chovendo = True
tem_aula_hoje = False
janela_aberta = True
luz_acesa = False
internet_funcionando = True
tarefa_completa = False
estudando_python = True
ferias_chegando = False
fim_de_semana = True
trabalho_entregue = False

# constantes
NUMERO_MAXIMO_DE_TENTATIVAS = 5  # int
NOME_DO_PROJETO = "Desenvolvimento de Software"  # str
VELOCIDADE_DA_LUZ = 299792458  # int
NOME_DA_EMPRESA = "Senac Tech"  # str
PI = 3.14159  # float
NUMERO_JOGADORES_CAMPO = 11  # int
COR_DO_INTERNACIONAL = 'vermelho'  # str
HA_VIDA_TERRA = True  # bool
```

Repare que as variáveis acima não possuem qualquer acentuação nos seus nomes (diferente dos textos que possuem), as palavras diferentes são ligadas por um sublinhado e seus nomes fazem referência ao seu conteúdo, para facilitar a leitura e identificação no código.

As variáveis são reconhecidas por terem todas as letras minúsculas (caixa baixa) enquanto que as constantes são reconhecidas por terem seus nomes em letras maiúsculas (caixa alta).

As variáveis tem por característica terem seus valores **ALTERADOS** (podem ou não) durante a execução do programa, enquanto que as constantes tem por característica terem valores **NÃO ALTERÁVEIS** (que não deveriam) durante a execução do programa.

## precedência dos operadores

Há uma precedência fixa entre todos os operadores usados.

Veja a tabela abaixo :

| prioridade | operador símbolo | operador nome | tipo operador |
| :----: | :----: | :----: | :----: |
| 1 | `()` | parênteses | operadores aritméticos |
| 2 | `**` | potência | operadores aritméticos |
| 3 | `*`<br>`/`<br>`//`<br>`%` | multiplicaçao<br>divisão<br>divisão inteira<br>módulo | operadores aritméticos |
| 4 | `+`<br>`-` | soma<br>subtração | operadores aritméticos |
| 5 | `==`<br>`>`<br>`<`<br>`>=`<br>`<=`<br>`!=` | igual a<br>maior que<br>menor que<br>maior ou igual a<br>menor ou igual a<br>diferente de | operadores relacionais |
| 6 | `not` | negação | operadores lógicos |
| 7 | `and` | conjunção | operadores lógicos |
| 8 | `or` | disjunção | operadores lógicos |

## int

O tipo inteiro, com abreviação de `int`, são usados para representar os números negativos (-10, -42, -1), o zero (0) e lembrando que não é usado a representação de -0 e os números positivos (1, 30, 42).

Veja abaixo as operações realizadas com os números inteiros :

```python
# adição de dois inteiros:
a = 5
b = 3
resultado = a + b
print(resultado)  # Saída: 8

# subtração de dois inteiros:
x = 10
y = 4
diferenca = x - y
print(diferenca)  # Saída: 6

# multiplicação de dois inteiros:
largura = 7
altura = 5
area = largura * altura
print(area)  # Saída: 35

# divisão de dois inteiros (divisão inteira):
total = 20
partes = 4
divisao = total // partes
print(divisao)  # Saída: 5

# resto da divisão de dois inteiros (módulo):
numero = 17
divisor = 3
resto = numero % divisor
print(resto)  # Saída: 2

# potenciação:
base = 2
expoente = 3
potencia = base ** expoente
print(potencia)  # Saída: 8

# uso de parênteses para alterar a precedência:
resultado = (5 + 3) * 2
print(resultado)  # Saída: 16

# comparação de igualdade:
idade_joao = 18
idade_maria = 18
mesma_idade = idade_joao == idade_maria
print(mesma_idade)  # Saída: True

# comparação de diferença:
nota1 = 7
nota2 = 8
notas_diferentes = nota1 != nota2
print(notas_diferentes)  # Saída: True

# comparação maior que:
saldo_banco = 1500
saldo_minimo = 1000
acima_do_minimo = saldo_banco > saldo_minimo
print(acima_do_minimo)  # Saída: True

# comparação menor que:
velocidade_carro = 80
velocidade_limite = 90
abaixo_limite = velocidade_carro < velocidade_limite
print(abaixo_limite)  # Saída: True

# comparação maior ou igual a:
temperatura = 30
temperatura_minima = 30
dentro_do_padrao = temperatura >= temperatura_minima
print(dentro_do_padrao)  # Saída: True

# comparação menor ou igual a:
pessoas_na_fila = 10
capacidade_maxima = 15
pode_entrar = pessoas_na_fila <= capacidade_maxima
print(pode_entrar)  # Saída: True

# uso de constante:
PI = 3.14
raio = 5
circunferencia = 2 * PI * raio
print(circunferencia)  # Saída: 31.400000000000002

# soma com variável e constante:
INCREMENTO = 10
valor = 25
novo_valor = valor + INCREMENTO
print(novo_valor)  # Saída: 35

# subtração com variável e constante:
DESCONTO = 5
preco_original = 50
preco_com_desconto = preco_original - DESCONTO
print(preco_com_desconto)  # Saída: 45

# expressão complexa com várias operações:
resultado = (4 + 5) * 2 - (3 ** 2) // 2
print(resultado)  # Saída: 11

# divisão com resultado decimal:
a = 10
b = 4
divisao_decimal = a / b
print(divisao_decimal)  # Saída: 2.5

# uso de variável para armazenar resultado de uma expressão:
numero1 = 15
numero2 = 5
resultado_expressao = (numero1 * 2 + numero2) / 3
print(resultado_expressao)  # Saída: 11.666666666666666
```

## float

O tipo ponto flutuante, com abreviação de `float`, são usados para representar os números negativos (-10.9, -42.0, -1.000001), o zero (0.0) e lembrando que não é usado a representação de -0.0 e os números positivos (1.00000000002, 30.123, 42.0).

Veja abaixo as operações realizadas com os números de ponto flutuante :

```python
# adição de dois floats:
a = 5.2
b = 3.1
resultado = a + b
print(resultado)  # Saída: 8.3

# subtração de dois floats:
x = 10.5
y = 4.2
diferenca = x - y
print(diferenca)  # Saída: 6.3

# multiplicação de dois floats:
largura = 7.5
altura = 5.2
area = largura * altura
print(area)  # Saída: 39.0

# divisão de dois floats:
total = 20.0
partes = 4.0
divisao = total / partes
print(divisao)  # Saída: 5.0

# resto da divisão de dois floats (módulo):
numero = 17.5
divisor = 3.2
resto = numero % divisor
print(resto)  # Saída: 1.8999999999999986

# potenciação:
base = 2.0
expoente = 3.0
potencia = base ** expoente
print(potencia)  # Saída: 8.0

# uso de parênteses para alterar a precedência:
resultado = (5.5 + 3.3) * 2.0
print(resultado)  # Saída: 17.6

# comparação de igualdade:
preco_produto1 = 18.50
preco_produto2 = 18.50
mesmo_preco = preco_produto1 == preco_produto2
print(mesmo_preco)  # Saída: True

# comparação de diferença:
nota1 = 7.5
nota2 = 8.0
notas_diferentes = nota1 != nota2
print(notas_diferentes)  # Saída: True

# comparação maior que:
saldo_banco = 1500.75
saldo_minimo = 1000.00
acima_do_minimo = saldo_banco > saldo_minimo
print(acima_do_minimo)  # Saída: True

# comparação menor que:
velocidade_carro = 80.5
velocidade_limite = 90.0
abaixo_limite = velocidade_carro < velocidade_limite
print(abaixo_limite)  # Saída: True

# comparação maior ou igual a:
temperatura = 30.0
temperatura_minima = 30.0
dentro_do_padrao = temperatura >= temperatura_minima
print(dentro_do_padrao)  # Saída: True

# comparação menor ou igual a:
pessoas_na_fila = 10.5
capacidade_maxima = 15.0
pode_entrar = pessoas_na_fila <= capacidade_maxima
print(pode_entrar)  # Saída: True

# uso de constante:
PI = 3.14
raio = 5.0
circunferencia = 2 * PI * raio
print(circunferencia)  # Saída: 31.400000000000002

# soma com variável e constante:
INCREMENTO = 10.0
valor = 25.5
novo_valor = valor + INCREMENTO
print(novo_valor)  # Saída: 35.5

# subtração com variável e constante:
DESCONTO = 5.0
preco_original = 50.0
preco_com_desconto = preco_original - DESCONTO
print(preco_com_desconto)  # Saída: 45.0

# expressão complexa com várias operações:
resultado = (4.5 + 5.2) * 2.0 - (3.0 ** 2) // 2.0
print(resultado)  # Saída: 11.4

# divisão com resultado decimal:
a = 10.0
b = 4.0
divisao_decimal = a / b
print(divisao_decimal)  # Saída: 2.5

# uso de variável para armazenar resultado de uma expressão:
numero1 = 15.5
numero2 = 5.2
resultado_expressao = (numero1 * 2.0 + numero2) / 3.0
print(resultado_expressao)  # Saída: 12.066666666666668
```

## combinando int e float

Tanto o tipo inteiro `int` quanto o tipo ponto flutuante `float` são tipos numéricos, então eles podem ser usados juntos para as operações acima.

Veja exemplos :

```python
# adição de um inteiro e um float:
a = 5
b = 3.2
resultado = a + b
print(resultado)  # Saída: 8.2

# subtração de um float por um inteiro:
x = 10.5
y = 4
diferenca = x - y
print(diferenca)  # Saída: 6.5

# multiplicação de um inteiro por um float:
largura = 7
altura = 5.2
area = largura * altura
print(area)  # Saída: 36.4

# divisão de um inteiro por um float:
total = 20
partes = 4.0
divisao = total / partes
print(divisao)  # Saída: 5.0

# divisão de um float e um inteiro (divisão inteira):
total = 23.4
partes = 4
divisao = total // partes
print(divisao)  # Saída: 5.0

# resto da divisão de um inteiro por um float (módulo):
numero = 17
divisor = 3.2
resto = numero % divisor
print(resto)  # Saída: 1.3999999999999986

# potenciação com base float e expoente inteiro:
base = 2.5
expoente = 3
potencia = base ** expoente
print(potencia)  # Saída: 15.625

# uso de parênteses para alterar a precedência com inteiro e float:
resultado = (5 + 3.3) * 2
print(resultado)  # Saída: 16.6

# comparação de igualdade entre inteiro e float:
idade_joao = 18
idade_maria = 18.0
mesma_idade = idade_joao == idade_maria
print(mesma_idade)  # Saída: True

# soma de uma constante inteira com uma variável float:
INCREMENTO = 10
valor = 25.5
novo_valor = valor + INCREMENTO
print(novo_valor)  # Saída: 35.5

# expressão complexa com inteiros e floats:
resultado = (4 + 5.5) * 2 - (3 ** 2) // 2.0
print(resultado)  # Saída: 10.0
```

## str

O tipo texto, chamado de String `str`, é o tipo usado para representar tudo que é texto e que está entre aspas simples `'...'`, aspas duplas `"..."` e aspas triplas `'''...'''` e `"""..."""`, essa última conhecida como strings literais.

A indexação de strings em Python é uma maneira de acessar caracteres individuais dentro de uma string.

A indexação de strings começa do 0. Isso significa que o primeiro caractere da string está no índice 0, o segundo caractere está no índice 1, e assim por diante.
Por exemplo, para a string "Python", o caractere 'P' está no índice 0, 'y' está no índice 1, 't' está no índice 2, etc.

```python
texto = "Python"
print(texto[0])  # Output: P
print(texto[1])  # Output: y
```

Índices negativos são usados para acessar caracteres a partir do final da string. O índice -1 refere-se ao último caractere, -2 ao penúltimo, e assim por diante.
Por exemplo, para a string "Python", o caractere 'n' está no índice -1 e 'o' está no índice -2.

```python
texto = "Python"
print(texto[-1])  # Output: n
print(texto[-2])  # Output: o
```

O fatiamento permite extrair uma parte da string. A sintaxe é texto[início:fim], onde:
- início é o índice onde o fatiamento começa (inclusivo),
- fim é o índice onde o fatiamento termina (exclusivo),

Se o início ou fim não forem fornecidos, o fatiamento usará o início ou o final da string, respectivamente.

```python
texto = "Python"
print(texto[:3])    # Output: Pyt (do início até o índice 2)
print(texto[3:])    # Output: hon (do índice 3 até o final)
```

Veja alguns exemplos :

```python
# concatenando duas strings:
saudacao = "Olá"
nome = "Mundo"
mensagem = saudacao + " " + nome
print(mensagem)  # Saída: Olá Mundo

# concatenando strings com números:
parte1 = "Número"
parte2 = " 42"
resultado = parte1 + parte2
print(resultado)  # Saída: Número 42

# multiplicação de uma string:
repeticao = "Ha" * 3
print(repeticao)  # Saída: HaHaHa

# uso do caractere de nova linha \n:
mensagem = "Primeira linha\nSegunda linha"
print(mensagem)
# Saída:
# Primeira linha
# Segunda linha

# uso do caractere de tabulação \t:
mensagem = "Nome:\tJoão"
print(mensagem)
# Saída:
# Nome:    João

# uso da barra invertida \ para escapar caracteres:
caminho = "C:\\Users\\Nome"
print(caminho)  # Saída: C:\Users\Nome

# concatenando com \n:
linha1 = "Esta é a primeira linha"
linha2 = "Esta é a segunda linha"
mensagem = linha1 + "\n" + linha2
print(mensagem)
# Saída:
# Esta é a primeira linha
# Esta é a segunda linha

# concatenando com \t:
chave = "Chave:"
valor = "12345"
mensagem = chave + "\t" + valor
print(mensagem)
# Saída:
# Chave:  12345

# uso de aspas simples dentro de uma string com aspas duplas:
mensagem = "Ela disse: 'Olá!'"
print(mensagem)  # Saída: Ela disse: 'Olá!'

# uso de aspas duplas dentro de uma string com aspas simples:
mensagem = 'Ele respondeu: "Bom dia!"'
print(mensagem)  # Saída: Ele respondeu: "Bom dia!"

# concatenando com variáveis:
nome = "Ana"
saudacao = "Bom dia, " + nome + "!"
print(saudacao)  # Saída: Bom dia, Ana!

# multiplicação de strings com espaços:
ponto = ". "
linha = ponto * 10
print(linha)  # Saída: . . . . . . . . . .

# uso do caractere de nova linha para formatação:
lista_compras = "Itens:\n- Maçã\n- Banana\n- Laranja"
print(lista_compras)
# Saída:
# Itens:
# - Maçã
# - Banana
# - Laranja

# uso do caractere de tabulação para formatação:
tabela = "Produto\tPreço\nMaçã\t1.50\nBanana\t0.75"
print(tabela)
# Saída:
# Produto    Preço
# Maçã       1.50
# Banana     0.75

# uso da barra invertida para incluir aspas duplas:
mensagem = "Ele disse: \"Bom trabalho!\""
print(mensagem)  # Saída: Ele disse: "Bom trabalho!"

# uso da barra invertida para incluir aspas simples:
mensagem = 'Ela disse: \'Até logo!\''
print(mensagem)  # Saída: Ela disse: 'Até logo!'

# concatenando strings literais:
mensagem = "Python " + "é " + "divertido!"
print(mensagem)  # Saída: Python é divertido!

# uso de caracteres especiais em uma string:
texto = "Linha1\nLinha2\tTabbed\nCaminho: C:\\Usuários\\Nome"
print(texto)
# Saída:
# Linha1
# Linha2  Tabbed
# Caminho: C:\Usuários\Nome

# concatenando strings com múltiplas linhas:
mensagem = "Olá,\n" + "Este é um exemplo de mensagem\n" + "com múltiplas linhas."
print(mensagem)
# Saída:
# Olá,
# Este é um exemplo de mensagem
# com múltiplas linhas.

# multiplicação de strings para criar um padrão:
padrao = "AB" * 5
print(padrao)  # Saída: ABABABABAB

# uso de aspas duplas dentro de aspas duplas com escape:
frase = "Ele disse: \"Isso é incrível!\""
print(frase)  # Saída: Ele disse: "Isso é incrível!"

# uso de aspas simples dentro de aspas simples com escape:
frase = 'Ela respondeu: \'Sim, estou de acordo.\''
print(frase)  # Saída: Ela respondeu: 'Sim, estou de acordo.'

# uso de caracteres de nova linha \n em uma string longa:
mensagem = "Linha 1\nLinha 2\nLinha 3"
print(mensagem)
# Saída:
# Linha 1
# Linha 2
# Linha 3

# uso de tabulação \t para alinhar texto:
tabela = "Nome\tIdade\tCidade\nAna\t30\tSão Paulo\nCarlos\t25\tRio de Janeiro"
print(tabela)
# Saída:
# Nome    Idade    Cidade
# Ana     30       São Paulo
# Carlos  25       Rio de Janeiro

# uso de barra invertida para escapar uma barra invertida:
caminho = "C:\\Usuários\\Publico"
print(caminho)  # Saída: C:\Usuários\Publico

# uso de aspas simples dentro de uma string com aspas duplas sem escape:
mensagem = "O livro se chama 'Python para Iniciantes'"
print(mensagem)  # Saída: O livro se chama 'Python para Iniciantes'

# uso de aspas duplas dentro de uma string com aspas simples sem escape:
mensagem = 'Ele disse: "Boa sorte!"'
print(mensagem)  # Saída: Ele disse: "Boa sorte!"

# string literal com múltiplas linhas usando aspas triplas:
mensagem = '''Esta é uma string
que ocupa múltiplas linhas,
sem a necessidade de caracteres de nova linha.'''
print(mensagem)
# Saída:
# Esta é uma string
# que ocupa múltiplas linhas,
# sem a necessidade de caracteres de nova linha.

# uso de aspas triplas dentro de aspas triplas:
texto = """Ela disse: "Isso é 'fantástico'!"
E ele respondeu: "Concordo completamente."""
print(texto)
# Saída:
# Ela disse: "Isso é 'fantástico'!"
# E ele respondeu: "Concordo completamente."

# acessando o primeiro caractere
texto = "Python"
print(texto[0])  # Output: P

# acessando o terceiro caractere
texto = "Python"
print(texto[2])  # Output: t

# acessando o último caractere
texto = "Python"
print(texto[-1])  # Output: n

# acessando o penúltimo caractere
texto = "Python"
print(texto[-2])  # Output: o

# fatiando os primeiros três caracteres
texto = "Python"
print(texto[:3])  # Output: Pyt

# fatiando os caracteres do índice 2 ao 5
texto = "Python"
print(texto[2:6])  # Output: thon

# fatiando a partir do índice 4 até o final
texto = "Python"
print(texto[4:])  # Output: hon

# fatiando até o índice 4
texto = "Python"
print(texto[:4])  # Output: Pyt

# fatiando uma string com tamanho variável
texto = "Indexação"
print(texto[3:7])  # Output: exaç

# fatiando uma string com caracteres especiais
texto = "Hello, World!"
print(texto[7:])  # Output: World!

# acessando um caractere em uma string de números
texto = "123456"
print(texto[4])  # Output: 5

# fatiando uma string para pegar caracteres de um espaço em branco
texto = "Python Programming"
print(texto[7:11])  # Output: Prog

# fatiando uma string para pegar caracteres de uma palavra específica
texto = "A quick brown fox"
print(texto[2:9])  # Output: quick b

# fatiando uma string para pegar a última palavra
texto = "A quick brown fox"
print(texto[11:])  # Output: brown fox
```

## bool

O tipo lógico, chamado de boolean `bool` no Python, é usado quando se quer representar um valor lógico de verdadeiro ou falso. Ele é muito usado nas estruturas de decisões como `if-elif-else` e `while`, por exemplo.

Veja alguns exemplos :

```python
# comparação de igualdade entre inteiros:
a = 5
b = 5
resultado = a == b
print(resultado)  # Saída: True

# comparação de diferença entre inteiros:
a = 5
b = 3
resultado = a != b
print(resultado)  # Saída: True

# comparação maior que entre inteiros:
a = 10
b = 5
resultado = a > b
print(resultado)  # Saída: True

# comparação menor que entre inteiros:
a = 5
b = 10
resultado = a < b
print(resultado)  # Saída: True

# comparação maior ou igual entre inteiros:
a = 10
b = 10
resultado = a >= b
print(resultado)  # Saída: True

# comparação menor ou igual entre inteiros:
a = 5
b = 10
resultado = a <= b
print(resultado)  # Saída: True

# comparação de igualdade entre strings:
palavra1 = "python"
palavra2 = "python"
resultado = palavra1 == palavra2
print(resultado)  # Saída: True

# comparação de diferença entre strings:
palavra1 = "python"
palavra2 = "Python"
resultado = palavra1 != palavra2
print(resultado)  # Saída: True

# uso do operador and (e lógico):
a = True
b = False
resultado = a and b
print(resultado)  # Saída: False

# uso do operador or (ou lógico):
a = True
b = False
resultado = a or b
print(resultado)  # Saída: True

# uso do operador not (não lógico):
a = True
resultado = not a
print(resultado)  # Saída: False

# combinação de operadores relacionais e lógicos:
a = 10
b = 5
c = 7
resultado = (a > b) and (c < a)
print(resultado)  # Saída: True

# comparação entre float e inteiro:
a = 10.0
b = 10
resultado = a == b
print(resultado)  # Saída: True

# comparação de strings com diferentes casos:
palavra1 = "pythoN"
palavra2 = "python"
resultado = palavra1 == palavra2
print(resultado)  # Saída: False

# verificação se um número é par:
numero = 4
resultado = numero % 2 == 0
print(resultado)  # Saída: True

# verificação se um número é ímpar:
numero = 5
resultado = numero % 2 != 0
print(resultado)  # Saída: True

# outra forma de verificar se um número é par ou ímpar
numero = 5
valor = numero // 2
valor = valor * 2
resultado = valor == numero
print(resultado)

# combinação de operadores and, or e not:
a = True
b = False
c = True
resultado = (a and b) or (not c)
print(resultado)  # Saída: False

# comparação entre variáveis booleanas:
a = True
b = False
resultado = a == b
print(resultado)  # Saída: False
```

## condicional if-elif-else

Condicionais são usados para tomar decisões no seu código. Com base em condições (que são expressões que retornam `True` ou `False`), você pode executar diferentes blocos de código.

### condicionais simples

* **`if`** : verifica uma condição. Se a condição for verdadeira (`True`), o bloco de código dentro do if será executado.
    ```python
    if teste_condicional:
        # Código a ser executado se a condição for verdadeira
    ```
* **`elif`** : é uma abreviação de `else if` e verifica uma condição alternativa se a condição anterior (`if`) não for verdadeira. Pode haver múltiplos `elif`.
    ```python
    if teste_condicional1:
        # Código se teste_condicional1 for verdadeira
    elif teste_condicional2:
        # Código se teste_condicional1 for falsa e teste_condicional2 for verdadeira
    ```
* **`else`** :executa um bloco de código se todas as condições anteriores (`if` e `elif`) forem falsas.
    ```python
    if teste_condicional1:
        # Código se teste_condicional1 for verdadeira
    elif teste_condicional2:
        # Código se teste_condicional1 for falsa e teste_condicional2 for verdadeira
    else:
        # Código se todas as condições anteriores forem falsas
    ```

### condicinais aninhadas

Permite decisões mais complexas ao verificar condições adicionais dentro de blocos `if`, `elif` ou `else`.

```python
if teste_condicional1:
    # Código executado se teste_condicional1 for verdadeira
    if teste_condicional2:
        # Código executado se teste_condicional2 for verdadeira e teste_condicional1 for verdadeira
    elif teste_condicional3:
        # Código executado se teste_condicional3 for verdadeira e teste_condicional1 for verdadeira
    else:
        # Código executado se nenhuma teste_condicional2 ou teste_condicional3 for verdadeira, mas condição1 for verdadeira
elif teste_condicional4:
    # Código executado se teste_condicional4 for verdadeira e teste_condicional1 for falsa
else:
    # Código executado se nenhuma das condições anteriores for verdadeira
```

### exemplos

Veja exemplos da condição `if`-`elif`-`else` :

```python
# verificação simples com if:
idade = 18
if idade >= 18:
    print("Você é maior de idade.")

# usando if e else:
idade = 16
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

# usando if, elif e else:
nota = 85
if nota >= 90:
    print("Aprovado com Distinção")
elif nota >= 70:
    print("Aprovado")
else:
    print("Reprovado")

# verificação de idade para categoria de ingresso:
idade = 22
if idade < 12:
    print("Ingresso infantil")
elif idade < 18:
    print("Ingresso juvenil")
else:
    print("Ingresso adulto")

# verificação de temperatura:
temperatura = 30
if temperatura < 15:
    print("Está frio.")
elif temperatura < 25:
    print("Está agradável.")
else:
    print("Está quente.")

# verificação de número par ou ímpar:
numero = 7
if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")

# checando se um número está entre dois valores:
numero = 15
if 10 <= numero <= 20:
    print("O número está entre 10 e 20.")
else:
    print("O número não está entre 10 e 20.")

# verificação de idade para habilitação de dirigir:
idade = 17
if idade >= 18:
    print("Pode obter a carteira de motorista.")
else:
    print("Não pode obter a carteira de motorista.")

# checando se uma variável é igual a um valor específico:
fruta = "maçã"
if fruta == "maçã":
    print("Você escolheu uma maçã.")
elif fruta == "banana":
    print("Você escolheu uma banana.")
else:
    print("Fruta não reconhecida.")

# checando o saldo da conta bancária:
saldo = 100
if saldo >= 0:
    print("Saldo positivo.")
else:
    print("Saldo negativo.")

# verificação de status de login:
usuario_logado = True
if usuario_logado:
    print("Bem-vindo de volta!")
else:
    print("Por favor, faça o login.")

# verificação de idade para desconto em ingresso:
idade = 65
if idade >= 65:
    print("Desconto para idosos.")
else:
    print("Sem desconto.")

# verificação de validade de senha:
senha = "12345"
if len(senha) >= 6:
    print("Senha válida.")
else:
    print("Senha muito curta.")

# determinação do tipo de triângulo:
a = 3
b = 4
c = 5
if a == b == c:
    print("Triângulo equilátero.")
elif a == b or b == c or a == c:
    print("Triângulo isósceles.")
else:
    print("Triângulo escaleno.")

# checando se um valor está fora de um intervalo:
valor = 25
if valor < 10 or valor > 20:
    print("Valor fora do intervalo.")
else:
    print("Valor dentro do intervalo.")

# verificação de número positivo, negativo ou zero:
numero = 0
if numero > 0:
    print("Número positivo.")
elif numero < 0:
    print("Número negativo.")
else:
    print("Número é zero.")

# checando se um número é múltiplo de 3 e 5:
numero = 15
if numero % 3 == 0 and numero % 5 == 0:
    print("O número é múltiplo de 3 e 5.")
elif numero % 3 == 0:
    print("O número é múltiplo de 3.")
elif numero % 5 == 0:
    print("O número é múltiplo de 5.")
else:
    print("O número não é múltiplo de 3 nem de 5.")

# condicionais aninhadas

# verificação de idade e se a pessoa é estudante:
idade = 20
estudante = True
if idade >= 18:
    if estudante:
        print("Você é um estudante adulto.")
    else:
        print("Você é um adulto não estudante.")
else:
    print("Você é menor de idade.")

# verificação de temperatura e umidade:
temperatura = 30
umidade = 70
if temperatura > 25:
    if umidade > 60:
        print("Clima quente e úmido.")
    else:
        print("Clima quente e seco.")
else:
    print("Clima fresco.")

# checagem de aprovação em um curso:
nota = 85
presença = 90
if nota >= 70:
    if presença >= 75:
        print("Aprovado no curso.")
    else:
        print("Reprovado por falta de presença.")
else:
    print("Reprovado por nota.")

# verificação de acesso com senha e nível de usuário:
senha = "admin123"
nivel_usuario = "admin"
if senha == "admin123":
    if nivel_usuario == "admin":
        print("Acesso total concedido.")
    else:
        print("Acesso limitado concedido.")
else:
    print("Senha incorreta.")

# verificação de idade para entrada em evento e se possui convite:
idade = 25
convite = True
if idade >= 18:
    if convite:
        print("Entrada permitida ao evento.")
    else:
        print("Você precisa de um convite para entrar.")
else:
    print("Você não tem idade suficiente para entrar.")

# checagem de valor de desconto e valor total da compra:
valor_total = 150
desconto = 10  # em porcentagem
if valor_total > 100:
    if desconto > 5:
        print("Desconto aplicado.")
    else:
        print("Desconto não suficiente para aplicar.")
else:
    print("Compra abaixo do valor mínimo para desconto.")

# verificação de saldo bancário e status da conta:
saldo = 2000
conta_ativa = True
if conta_ativa:
    if saldo >= 1000:
        print("Conta com saldo suficiente.")
    else:
        print("Saldo insuficiente.")
else:
    print("Conta não está ativa.")

# verificação de idade para compra de bebida alcoólica e estado de residência:
idade = 22
estado = "SP"
if idade >= 21:
    if estado == "SP" or estado == "RJ":
        print("Você pode comprar bebida alcoólica.")
    else:
        print("Restrições de compra no seu estado.")
else:
    print("Você não pode comprar bebida alcoólica.")

# verificação de validade de voucher e valor da compra:
valor_compra = 50
voucher_valido = True
if voucher_valido:
    if valor_compra >= 40:
        print("Voucher aplicado com sucesso.")
    else:
        print("Valor da compra não atende aos requisitos do voucher.")
else:
    print("Voucher inválido.")

# checagem de disponibilidade de produto e status de entrega:
produto_em_estoque = True
status_entrega = "em trânsito"
if produto_em_estoque:
    if status_entrega == "em trânsito":
        print("Produto disponível e em entrega.")
    else:
        print("Produto disponível, mas entrega não iniciada.")
else:
    print("Produto fora de estoque.")
```

<details>
<summary>Lista de Exercícios</summary>

## int e float

1. Exercícios Iniciais
    1. Crie uma variável x com o valor 10 e uma variável y com o valor 5. Imprima a soma de x e y.
    1. Crie uma variável a com o valor 8 e uma variável b com o valor 4. Imprima o resultado da subtração de a por b.
    1. Crie uma variável x com o valor 7 e uma variável y com o valor 3. Imprima o resultado da multiplicação de x por y.
    1. Crie uma variável x com o valor 20 e uma variável y com o valor 4. Imprima o resultado da divisão de x por y.
    1. Crie uma variável x com o valor 10 e outra variável y com o valor 4. Imprima o resto da divisão de x por y.
    1. Crie uma variável a com o valor 15. Imprima o valor de a elevado ao quadrado.
    1. Crie uma variável a com o valor 9 e outra variável b com o valor 2. Imprima a divisão inteira de a por b.
    1. Crie uma variável x com o valor 5.5 e uma variável y com o valor 2.2. Imprima a soma de x e y.
    1. Crie uma variável x com o valor 3.7 e uma variável y com o valor 1.2. Imprima o resultado da subtração de x por y.
    1. Crie uma variável x com o valor 4.5 e uma variável y com o valor 2. Imprima o resultado da multiplicação de x por y.
1. Exercícios Intermediários
    1. Crie uma variável a com o valor 25 e outra variável b com o valor 7. Imprima o resultado da divisão de a por b, com 2 casas decimais.
    1. Crie uma variável x com o valor 6.7 e uma variável y com o valor 3.1. Imprima a soma de x e y, com 1 casa decimal.
    1. Crie uma variável a com o valor 16 e outra variável b com o valor 4. Crie uma terceira variável resultado que armazene a raiz quadrada de a dividida por b. Imprima resultado.
    1. Crie uma variável x com o valor 12.5 e uma variável y com o valor 2.5. Imprima a diferença entre x e y e verifique se é maior que 8.
    1. Crie uma variável a com o valor 3.14 e outra variável b com o valor 2. Crie uma variável resultado que armazene a multiplicação de a por b, e imprima o resultado com 3 casas decimais.
    1. Crie uma variável x com o valor 45.9 e outra variável y com o valor 15.1. Imprima o resultado da divisão de x por y, com 4 casas decimais.
    1. Crie uma variável a com o valor 0.5 e outra variável b com o valor 0.25. Imprima a soma de a e b, multiplicada por 100.
    1. Crie uma variável x com o valor 8.2 e uma variável y com o valor 3.4. Imprima o resultado da multiplicação de x por y e verifique se é menor que 30.
    1. Crie uma variável a com o valor 17 e outra variável b com o valor 3. Crie uma variável resultado que armazene a soma de a com o resto da divisão de a por b. Imprima resultado.
    1. Crie uma variável x com o valor 5.6 e outra variável y com o valor 2.3. Imprima o resultado da subtração de x por y, arredondado para o inteiro mais próximo.
1. Exercícios Avançados
    1. Crie uma variável x com o valor 9 e uma variável y com o valor 4. Imprima o resultado da expressão (x ** 2 + y ** 2) / (x - y).
    1. Crie uma variável x com o valor 10.5 e uma variável y com o valor 2.7. Imprima o resultado da expressão (x * y) - (x / y).
    1. Crie uma variável a com o valor 12 e uma variável b com o valor 5. Crie uma variável resultado que armazene a soma de a e b, elevada ao quadrado. Imprima resultado.
    1. Crie uma variável x com o valor 6.8 e uma variável y com o valor 2.4. Imprima a soma de x com y, multiplicada pelo resto da divisão de x por y.
    1. Crie uma variável a com o valor 20 e outra variável b com o valor 7. Crie uma variável resultado que armazene a média de a e b. Imprima resultado com 2 casas decimais.
    1. Crie uma variável x com o valor 15.75 e uma variável y com o valor 3.5. Imprima o resultado da expressão x / y somado ao quadrado de y.
    1. Crie uma variável a com o valor 8 e uma variável b com o valor 3. Crie uma variável resultado que armazene a diferença entre a e b, e verifique se o quadrado do resultado é maior que 20. Imprima resultado.
    1. Crie uma variável x com o valor 7.5 e uma variável y com o valor 3.2. Imprima o resultado da expressão (x + y) / (x - y) com 2 casas decimais.
    1. Crie uma variável a com o valor 25 e uma variável b com o valor 5. Crie uma variável resultado que armazene o valor absoluto da diferença entre o quadrado de a e o cubo de b. Imprima resultado.
    1. Crie uma variável x com o valor 10.4 e uma variável y com o valor 3.6. Imprima a expressão (x ** 2 + y ** 2) / (x * y) e verifique se é maior que 5.
    1. Crie uma variável a com o valor 8 e outra variável b com o valor 3. Crie uma variável resultado que armazene a soma de a e b, e imprima o resultado dividido pela raiz quadrada de a.
    1. Crie uma variável x com o valor 11.2 e uma variável y com o valor 5.7. Imprima o resultado da expressão (x - y) * (x + y), com 2 casas decimais.
    1. Crie uma variável a com o valor 30 e outra variável b com o valor 4. Crie uma variável resultado que armazene a diferença entre a e b, elevada ao cubo. Imprima resultado.
    1. Crie uma variável x com o valor 8.5 e uma variável y com o valor 2.3. Imprima a expressão (x * y) + (x / y) e verifique se é menor que 20.
    1. Crie uma variável a com o valor 18 e uma variável b com o valor 7. Crie uma variável resultado que armazene o valor absoluto da diferença entre a e o produto de b por 2. Imprima resultado.
    1. Crie uma variável x com o valor 14.7 e uma variável y com o valor 6.3. Imprima o resultado da expressão (x + y) / (x - y) e verifique se é maior que 2.
    1. Crie uma variável a com o valor 12 e uma variável b com o valor 5. Crie uma variável resultado que armazene a soma de a e b, multiplicada pela raiz quadrada de a. Imprima resultado.
    1. Crie uma variável x com o valor 9.8 e uma variável y com o valor 4.2. Imprima a expressão ((x + y) * 2) / (x - y), com 2 casas decimais.
    1. Crie uma variável a com o valor 7 e outra variável b com o valor 2. Crie uma variável resultado que armazene o valor absoluto do quadrado de a subtraído do cubo de b. Imprima resultado.
    1. Crie uma variável x com o valor 5.5 e uma variável y com o valor 2.2. Crie uma variável resultado que armazene a soma de x e y, e imprima o resultado elevado ao quadrado.
    1. Crie uma variável a com o valor 21 e uma variável b com o valor 3. Crie uma variável resultado que armazene a diferença entre o quadrado de a e o cubo de b, dividido por b. Imprima resultado.
    1. Crie uma variável x com o valor 20.5 e uma variável y com o valor 3.2. Imprima o resultado da expressão (x - y) * (x + y), com 1 casa decimal.
    1. Crie uma variável a com o valor 18 e uma variável b com o valor 7. Crie uma variável resultado que armazene a soma de a com o produto de b e 2. Imprima resultado dividido pela raiz quadrada de a.
    1. Crie uma variável x com o valor 12.4 e uma variável y com o valor 2.5. Imprima a expressão ((x * y) + (x / y)) - (y ** 2), com 2 casas decimais.
    1. Crie uma variável a com o valor 14 e uma variável b com o valor 5. Crie uma variável resultado que armazene o quadrado da soma de a e b, dividido pelo cubo de b. Imprima resultado.
    1. Crie uma variável x com o valor 25.7 e uma variável y com o valor 8.3. Imprima o resultado da expressão (x / y) * ((x + y) / (x - y)), com 2 casas decimais.
    1. Crie uma variável a com o valor 30 e uma variável b com o valor 7. Crie uma variável resultado que armazene o produto de a por b, dividido pela diferença entre a e b. Imprima resultado.
    1. Crie uma variável x com o valor 10.5 e uma variável y com o valor 3.7. Imprima a expressão ((x * y) + (x / y)) - (x ** 2), com 2 casas decimais.
    1. Crie uma variável a com o valor 15 e uma variável b com o valor 4. Crie uma variável resultado que armazene a soma de a e b, elevada ao cubo, e depois subtraia 100. Imprima resultado.
    1. Crie uma variável x com o valor 9.9 e uma variável y com o valor 2.2. Imprima a expressão ((x ** 2) + (y ** 2)) / ((x * y) - y), com 2 casas decimais.

## str

1. Exercícios Simples
    1. Crie duas variáveis str1 e str2 com os valores "Hello" e "World". Imprima a soma das duas strings.
    1. Crie uma variável texto com o valor "Python". Imprima a string "PythonPython" usando a multiplicação de strings.
    1. Crie uma variável frase com o valor "Python Programming". Imprima os primeiros 6 caracteres da string.
    1. Crie uma variável texto com o valor "Hello, World!". Imprima os caracteres da posição 7 até o final da string.
    1. Crie uma variável mensagem com o valor "Python". Imprima os primeiros 3 caracteres.
    1. Crie uma variável palavra com o valor "Data". Imprima a string "DataDataData" usando a multiplicação de strings.
    1. Crie uma variável texto com o valor "Python". Imprima os caracteres do índice 1 ao 4.
    1. Crie duas variáveis prefixo e sufixo com os valores "Hello" e "World". Imprima a soma das duas strings com um espaço entre elas.
    1. Crie uma variável nome com o valor "Alice". Imprima a string "AliceAlice" usando a multiplicação de strings.
    1. Crie uma variável mensagem com o valor "Data Science". Imprima os caracteres do índice 5 até o final da string.
1. Exercícios Intermediários
    1. Crie uma variável texto com o valor "Learn Python". Imprima os caracteres do índice 6 ao 11.
    1. Crie uma variável frase com o valor "Hello World". Imprima a string "HelloHello" usando a multiplicação de strings.
    1. Crie uma variável texto com o valor "Programming". Imprima os primeiros 4 caracteres.
    1. Crie uma variável mensagem com o valor "String Manipulation". Imprima os caracteres do índice 8 ao 15.
    1. Crie duas variáveis part1 e part2 com os valores "Python" e "Rocks". Imprima a soma das duas strings com um espaço entre elas.
    1. Crie uma variável palavra com o valor "Machine Learning". Imprima a string "Machine LearningMachine Learning" usando a multiplicação de strings.
    1. Crie uma variável texto com o valor "Artificial Intelligence". Imprima os caracteres do índice 3 ao 8.
    1. Crie uma variável mensagem com o valor "Data Analysis". Imprima os caracteres do índice 5 ao 10.
    1. Crie uma variável frase com o valor "Learn to Code". Imprima a string "Learn to CodeLearn to Code" usando a multiplicação de strings.
    1. Crie uma variável texto com o valor "Statistics". Imprima os caracteres do índice 4 até o final da string.
1. Exercícios Avançados
    1. Crie uma variável frase com o valor "Welcome to the World of Python". Imprima os caracteres do índice 11 ao 20.
    1. Crie uma variável texto com o valor "Programming is Fun". Imprima a string "ProgrammingProgramming" usando a multiplicação de strings.
    1. Crie uma variável mensagem com o valor "Learn Python Basics". Imprima os caracteres do índice 0 ao 4.
    1. Crie uma variável frase com o valor "Data Science and Machine Learning". Imprima os caracteres do índice 17 ao 30.
    1. Crie duas variáveis str1 e str2 com os valores "Data" e "Science". Imprima a soma das duas strings com um espaço entre elas.
    1. Crie uma variável texto com o valor "Advanced Python Techniques". Imprima a string "Advanced Python TechniquesAdvanced Python Techniques" usando a multiplicação de strings.
    1. Crie uma variável mensagem com o valor "Artificial Intelligence Overview". Imprima os caracteres do índice 14 até o final da string.
    1. Crie uma variável texto com o valor "Introduction to Programming". Imprima os caracteres do índice 5 ao 25.
    1. Crie uma variável frase com o valor "Exploring Data Science" e imprima a string "Exploring Data ScienceExploring Data Science" usando a multiplicação de strings.
    1. Crie uma variável texto com o valor "Big Data Analytics". Imprima os caracteres do índice 3 ao 12.
    1. Crie uma variável mensagem com o valor "Data Visualization Techniques". Imprima os caracteres do índice 10 ao 25.
    1. Crie duas variáveis prefixo e sufixo com os valores "Machine Learning" e " in Python". Imprima a soma das duas strings com um espaço entre elas.
    1. Crie uma variável texto com o valor "Deep Learning Models". Imprima a string "Deep Learning ModelsDeep Learning Models" usando a multiplicação de strings.
    1. Crie uma variável frase com o valor "Data Driven Insights". Imprima os caracteres do índice 4 ao 12.
    1. Crie uma variável texto com o valor "Programming for Data Science". Imprima os caracteres do índice 12 até o final da string.
    1. Crie uma variável mensagem com o valor "Exploring Machine Learning Algorithms". Imprima a string "Exploring Machine Learning AlgorithmsExploring Machine Learning Algorithms" usando a multiplicação de strings.
    1. Crie uma variável texto com o valor "Advanced Data Analytics Techniques". Imprima os caracteres do índice 8 ao 28.
    1. Crie uma variável frase com o valor "Understanding Data Science Principles". Imprima os caracteres do índice 18 ao 35.
    1. Crie duas variáveis parte1 e parte2 com os valores "Introduction" e " to Python". Imprima a soma das duas strings com um espaço entre elas.
    1. Crie uma variável texto com o valor "Machine Learning Fundamentals". Imprima a string "Machine Learning FundamentalsMachine Learning Fundamentals" usando a multiplicação de strings.
    1. Crie uma variável mensagem com o valor "Data Science Applications". Imprima os caracteres do índice 5 ao 20.
    1. Crie uma variável texto com o valor "Artificial Intelligence Applications". Imprima os caracteres do índice 22 até o final da string.
    1. Crie uma variável frase com o valor "Deep Learning for AI". Imprima a string "Deep Learning for AIDeep Learning for AI" usando a multiplicação de strings.
    1. Crie uma variável texto com o valor "Introduction to Machine Learning". Imprima os caracteres do índice 0 ao 15.
    1. Crie uma variável mensagem com o valor "Python for Data Science and Analytics". Imprima os caracteres do índice 10 ao 35.
    1. Crie duas variáveis str1 e str2 com os valores "Deep Learning" e " in Python". Imprima a soma das duas strings com um espaço entre elas.
    1. Crie uma variável texto com o valor "Understanding Data Science Techniques". Imprima a string "Understanding Data Science TechniquesUnderstanding Data Science Techniques" usando a multiplicação de strings.
    1. Crie uma variável frase com o valor "Introduction to Data Visualization". Imprima os caracteres do índice 11 ao 30.
    1. Crie uma variável texto com o valor "Advanced Machine Learning Techniques". Imprima os caracteres do índice 10 ao 35.
    1. Crie uma variável mensagem com o valor "Data Science Fundamentals Overview". Imprima a string "Data Science Fundamentals OverviewData Science Fundamentals Overview" usando a multiplicação de strings.

## if-elif-else

1. Exercícios Simples
    1. Crie uma variável idade com o valor 18. Imprima "Maior de idade" se a idade for maior ou igual a 18. Caso contrário, imprima "Menor de idade".
    1. Crie uma variável preco com o valor 150. Imprima "Carro caro" se o preço for maior que 100, e "Carro barato" caso contrário.
    1. Crie uma variável nota com o valor 7.5. Imprima "Aprovado" se a nota for maior ou igual a 7.0. Caso contrário, imprima "Reprovado".
    1. Crie uma variável temperatura com o valor 22.5. Imprima "Quente" se a temperatura for maior que 25. Caso contrário, imprima "Frio".
    1. Crie uma variável nome com o valor "Ana". Imprima "Olá Ana" se o nome for "Ana", e "Olá desconhecido" caso contrário.
    1. Crie uma variável altura com o valor 1.75. Imprima "Altura adequada" se a altura for maior ou igual a 1.70. Caso contrário, imprima "Altura inadequada".
    1. Crie uma variável produto com o valor "livro". Imprima "Produto disponível" se o produto for "livro", e "Produto não disponível" caso contrário.
    1. Crie uma variável idade com o valor 65. Imprima "Aposentado" se a idade for maior ou igual a 65. Caso contrário, imprima "Não aposentado".
    1. Crie uma variável x com o valor 10. Imprima "Positivo" se x for maior que 0, e "Não positivo" caso contrário.
    1. Crie uma variável n com o valor 4. Imprima "Par" se n for divisível por 2, e "Ímpar" caso contrário.
1. Exercícios Intermediários
    1. Crie uma variável nota com o valor 5. Crie um bloco if-elif-else para imprimir "Aprovado" se a nota for maior ou igual a 7, "Recuperação" se a nota for entre 5 e 6, e "Reprovado" caso contrário.
    1. Crie uma variável idade com o valor 20. Crie um bloco if-elif-else para imprimir "Adulto" se a idade for entre 18 e 60, "Idoso" se a idade for maior que 60, e "Jovem" se a idade for menor que 18.
    1. Crie uma variável salario com o valor 3000. Imprima "Imposto alto" se o salário for maior que 2500, e "Imposto baixo" caso contrário.
    1. Crie uma variável nota com o valor 8.5. Imprima "Excelente" se a nota for maior ou igual a 9, "Bom" se a nota estiver entre 7 e 8.9, e "Suficiente" caso contrário.
    1. Crie uma variável numero com o valor 15. Imprima "Divisível por 3" se numero for divisível por 3, e "Não divisível por 3" caso contrário.
    1. Crie uma variável tempo com o valor 30. Crie um bloco if-elif-else para imprimir "Tempo curto" se o tempo for menor que 20, "Tempo médio" se estiver entre 20 e 40, e "Tempo longo" caso contrário.
    1. Crie uma variável nome com o valor "Carlos". Crie um bloco if-elif-else para imprimir "Nome é Carlos" se o nome for "Carlos", "Nome começa com C" se começar com "C", e "Nome diferente" caso contrário.
    1. Crie uma variável ano com o valor 2024. Imprima "Ano bissexto" se o ano for divisível por 4, mas não por 100, ou se for divisível por 400. Caso contrário, imprima "Ano não bissexto".
    1. Crie uma variável altura com o valor 1.65. Crie um bloco if-elif-else para imprimir "Baixa" se a altura for menor que 1.60, "Média" se estiver entre 1.60 e 1.80, e "Alta" caso contrário.
    1. Crie uma variável idade com o valor 30. Imprima "Jovem adulto" se a idade for entre 20 e 30, "Adulto" se estiver entre 31 e 50, e "Meia-idade" caso contrário.
1. Exercícios Avançados
    1. Crie uma variável dia com o valor "Sábado". Imprima "Fim de semana" se o dia for "Sábado" ou "Domingo", e "Dia de semana" caso contrário.
    1. Crie uma variável idade com o valor 16. Crie um bloco if-elif-else para imprimir "Infantil" se a idade for menor que 12, "Juvenil" se estiver entre 12 e 18, e "Adulto" caso contrário.
    1. Crie uma variável mes com o valor "Julho". Imprima "Verão" se o mês for "Junho", "Julho", ou "Agosto", e "Não é verão" caso contrário.
    1. Crie uma variável temperatura com o valor 10. Imprima "Frio" se a temperatura for menor que 15, "Agradável" se estiver entre 15 e 25, e "Quente" caso contrário.
    1. Crie uma variável nota com o valor 9.5. Crie um bloco if-elif-else para imprimir "Excelente" se a nota for maior ou igual a 9, "Muito bom" se estiver entre 7 e 8.9, e "Suficiente" caso contrário.
    1. Crie uma variável preco com o valor 90. Crie um bloco if-elif-else para imprimir "Desconto alto" se o preço for maior que 100, "Desconto médio" se estiver entre 50 e 100, e "Sem desconto" caso contrário.
    1. Crie uma variável idade com o valor 70. Crie um bloco if-elif-else para imprimir "Idoso" se a idade for maior ou igual a 65, "Adulto" se estiver entre 18 e 64, e "Jovem" caso contrário.
    1. Crie uma variável salario com o valor 4000. Crie um bloco if-elif-else para imprimir "Classe alta" se o salário for maior que 3000, "Classe média" se estiver entre 1500 e 3000, e "Classe baixa" caso contrário.
    1. Crie uma variável x com o valor 8. Crie um bloco if-elif-else para imprimir "Múltiplo de 2" se x for divisível por 2, "Múltiplo de 4" se x for divisível por 4, e "Não é múltiplo" caso contrário.
    1. Crie uma variável nome com o valor "Pedro". Imprima "Bem-vindo Pedro" se o nome for "Pedro", "Nome começando com P" se começar com "P", e "Nome diferente" caso contrário.
    1. Crie uma variável dia com o valor 10. Crie um bloco if-elif-else para imprimir "Início do mês" se o dia for menor ou igual a 10, "Meio do mês" se estiver entre 11 e 20, e "Fim do mês" caso contrário.
    1. Crie uma variável idade com o valor 45. Crie um bloco if-elif-else para imprimir "Meia-idade" se a idade for entre 40 e 60, "Adulto" se estiver entre 20 e 39, e "Jovem" caso contrário.
    1. Crie uma variável velocidade com o valor 90. Crie um bloco if-elif-else para imprimir "Velocidade alta" se a velocidade for maior que 80, "Velocidade média" se estiver entre 50 e 80, e "Velocidade baixa" caso contrário.
    1. Crie uma variável ponto com o valor 10. Crie um bloco if-elif-else para imprimir "Nota máxima" se o ponto for igual a 10, "Nota alta" se estiver entre 7 e 9, e "Nota baixa" caso contrário.
    1. Crie uma variável altura com o valor 1.90. Crie um bloco if-elif-else para imprimir "Muito alto" se a altura for maior que 1.85, "Médio" se estiver entre 1.60 e 1.85, e "Baixo" caso contrário.
    1. Crie uma variável preco com o valor 200. Crie um bloco if-elif-else para imprimir "Caro" se o preço for maior que 150, "Médio" se estiver entre 100 e 150, e "Barato" caso contrário.
    1. Crie uma variável tempo com o valor 60. Crie um bloco if-elif-else para imprimir "Tempo curto" se o tempo for menor que 30, "Tempo médio" se estiver entre 30 e 60, e "Tempo longo" caso contrário.
    1. Crie uma variável senha com o valor "12345". Crie um bloco if-elif-else para imprimir "Senha correta" se a senha for "12345", "Senha curta" se tiver menos de 6 caracteres, e "Senha incorreta" caso contrário.
    1. Crie uma variável percentual com o valor 85. Crie um bloco if-elif-else para imprimir "Excelente" se o percentual for maior ou igual a 90, "Bom" se estiver entre 70 e 89, e "Regular" caso contrário.
    1. Crie uma variável x com o valor 2. Crie um bloco if-elif-else para imprimir "Número primo" se x for 2 ou 3, "Número par" se for divisível por 2, e "Número ímpar" caso contrário.
    1. Crie uma variável dia com o valor "Quarta-feira". Imprima "Dia útil" se o dia for "Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", ou "Sexta-feira", e "Fim de semana" caso contrário.
    1. Crie uma variável peso com o valor 65. Crie um bloco if-elif-else para imprimir "Peso normal" se o peso estiver entre 50 e 70, "Abaixo do peso" se for menor que 50, e "Acima do peso" caso contrário.
    1. Crie uma variável sabor com o valor "Chocolate". Imprima "Sabor favorito" se o sabor for "Chocolate", "Sabor agradável" se for "Baunilha", e "Sabor não listado" caso contrário.
    1. Crie uma variável ponto com o valor 45. Crie um bloco if-elif-else para imprimir "Nota alta" se o ponto for maior que 40, "Nota média" se estiver entre 20 e 40, e "Nota baixa" caso contrário.
    1. Crie uma variável status com o valor "ativo". Crie um bloco if-elif-else para imprimir "Ativo" se o status for "ativo", "Inativo" se for "inativo", e "Status desconhecido" caso contrário.
    1. Crie uma variável altura com o valor 1.55. Crie um bloco if-elif-else para imprimir "Baixa" se a altura for menor que 1.60, "Média" se estiver entre 1.60 e 1.75, e "Alta" caso contrário.
    1. Crie uma variável distancia com o valor 15. Crie um bloco if-elif-else para imprimir "Curta" se a distância for menor que 10, "Média" se estiver entre 10 e 20, e "Longa" caso contrário.
    1. Crie uma variável idade com o valor 25. Crie um bloco if-elif-else para imprimir "Adulto jovem" se a idade for entre 20 e 30, "Adulto" se estiver entre 31 e 50, e "Meia-idade" caso contrário.
    1. Crie uma variável quantidade com o valor 12. Crie um bloco if-elif-else para imprimir "Quantidade alta" se a quantidade for maior que 15, "Quantidade média" se estiver entre 5 e 15, e "Quantidade baixa" caso contrário.
    1. Crie uma variável temp com o valor 5. Crie um bloco if-elif-else para imprimir "Muito frio" se a temperatura for menor que 10, "Agradável" se estiver entre 10 e 25, e "Quente" caso contrário.
</details>

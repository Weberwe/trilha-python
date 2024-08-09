Índice Lista e While

* [lista](#lista)
* [str e list](#str-e-list)
* [exercícios lista](#exercícios-lista)

# lista e while

## lista

Uma lista é uma coleção de itens ordenados e mutáveis. Isso significa que podemos adicionar, remover ou alterar os itens de uma lista após a sua criação. No Python, uma lista é representada por colchetes `[]` e os itens dentro dela são separados por vírgulas. O tipo lista é representado por `list`.

### criando uma lista

Você pode criar uma lista simplesmente colocando uma série de valores entre colchetes.

Veja alguns exemplos de criação de lista :

```python
# criando uma lista de números inteiros
numeros = [1, 2, 3, 4, 5]

# criando uma lista de floats
mais_numeros = [3.14, 2.77, 1.00001]

# criando uma lista de strings
planetas = ["Mercúrio", "Vênus", "Terra", "Marte"]

# criando uma lista mista
misto = [42, 3.14, 'uma string', False, "outra string"]

# criando uma lista com outra variáveis dentro
nome = "Arnold"
valor = 42
lista_mista = [42, nome, 'Schwarzenegger', True, "olá", valor]
```

### acessando itens da lista

Cada item de uma lista tem uma posição (ou índice). No Python, os índices começam em 0. Isso significa que o primeiro item tem índice 0, o segundo item tem índice 1, e assim por diante.

Veja abaixo como fica o acesso :

```python
print('Planeta no índice 0 :', planetas[0])  # saída : Mercúrio
print('Planeta no índice 2 :', planetas[2])  # saída : Terra
print('Número no índice 1 :', numeros[1])  # saída : 2
```

### modificando itens da lista

Como as listas são mutáveis, você pode alterar qualquer item da lista usando o índice:

```python
planetas[2] = 'Saturno'
print(planetas)  # saída : ['Mercúrio', 'Vênus', 'Saturno', 'Marte']
```

### adicionando itens à lista

Há diversas formas de adicionar itens a uma lista.

- **método `append()`** :

    Adiciona um item ao **final** da lista.
    ```python
    planetas.append("Plutão")
    print(planetas)  # saída : ['Mercúrio', 'Vênus', 'Saturno', 'Marte', 'Plutão']
    ```

- **método `insert()`** :

    Adiciona um item em uma posição específica.
    ```python
    # insere a string "Júpiter" no índice 1 da lista
    planetas.insert(1, "Júpiter")
    print(planetas)  # saída : ['Mercúrio', 'Júpiter', 'Vênus', 'Saturno', 'Marte', 'Plutão']
    ```
    Se for usado um índice maior que o tamanho da lista, então ele será adicionado ao final dela.
    ```python
    planetas.insert(100, "Terra")
    print(planetas)  # saída : ['Mercúrio', 'Júpiter', 'Vênus', 'Saturno', 'Marte', 'Plutão', 'Terra']
    ```

### removendo itens da lista

Assim como a inserção, há algumas formas de remover um ou mais itens da lista.

- **método `remove()`** :

    Remove a primeira ocorrência de um item específico.
    ```python
    planetas.remove("Plutão")
    print(planetas)  # saída : ['Mercúrio', 'Júpiter', 'Vênus', 'Saturno', 'Marte', 'Terra']
    ```
    Se o item removido não estiver na lista, então irá levantar um erro.

- **método `pop()`** :

    Remove um item pela sua posição (índice) e retorna esse item. Se nenhum índice for fornecido, ele remove o último item.
    ```python
    ultimo = planetas.pop()
    print(ultimo)  # saída : "Terra"
    print(planetas)  # saída : ['Mercúrio', 'Júpiter', 'Vênus', 'Saturno', 'Marte']

    especifico = planetas.pop(2)
    print(especifico)  # saída : "Vênus"
    print(planetas)  # saída : ['Mercúrio', 'Júpiter', 'Saturno', 'Marte']
    ```
    Se o índice passado não existir, então irá ocorrer um erro.

- **palavra-chave `del`** :

    Remove um item pela sua posição ou remove uma fatia (parte) da lista.
    ```python
    del planetas[1]
    print(planetas)  # saída : ['Mercúrio', 'Saturno', 'Marte']

    del planetas[1:]
    print(planetas)  # saída : ['Mercúrio']
    ```

## str e list

Strings e listas tem algumas características em comum, como ambas serem compostas de mais de um item. Uma string é composta por um ou mais caracteres, tão somente. Enquanto que uma lista é composta por diferentes tipos.

Por conta disso, elas possuem alguns comportamentos em comum.

### comprimento

Tanto para as strings quanto para as listas, é possível saber o tamanho usando a função `len()`. Veja abaixo :

```python
planetas = ["Mercúrio", "Vênus", "Terra", "Marte"]
sobrenome = 'Schwarzenegger'

print(len(planetas))  # saída : 4
print(len(planetas[2]))  # saída (tamanho da palavra Terra) : 5
print(len(sobrenome))  # saída : 14
```

### verificando a presença de um item

Para verificar se um item está em uma lista ou uma string em uma outra string, usa-se a palavra-chave `in` :

```python
print("Marte" in planetas)  # saída : True
print("Uranus" in planetas)  # saída : False

print('w' in sobrenome)  # saída : True
print('s' in sobrenome)  # saída : False
print("gg" in sobrenome)  # saída : True
```

### juntando e multiplicando listas

Assim como nas strings, o operadore `+` é usado para juntar (concatenar) duas listas e o operador `*` é usado para multiplicar o conteúdo de uma lista :

```python
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
junta = lista1 + lista2
print(junta)  # saída : [1, 2, 3, 4, 5, 6]

multiplica = lista1 * 2
print(multiplica)  # saída : [1, 2, 3, 1, 2, 3]
```

### fatiamento

O fatiamento das listas funcionam exatamente como o fatiamento das strings :

```python
print(planetas[::2])  # saída : ['Mercúrio', 'Terra']
print(planetas[1:])  # saída : ['Vênus', 'Terra', 'Marte']
print(planetas[2:4])  # saída : ['Terra', 'Marte']
print(planetas[:3])  # saída : ['Mercúrio', 'Vênus', 'Terra']
```

## exercícios lista

<details>
<summary>Lista de Exercícios</summary>

1. Exercícios Simples
    1. Crie uma lista com três números inteiros e exiba o primeiro elemento.
    1. Crie uma lista com três strings e exiba o último elemento.
    1. Crie uma lista com cinco números decimais e exiba o terceiro elemento.
    1. Crie uma lista com quatro valores booleanos e exiba o segundo elemento.
    1. Crie uma lista com três strings e altere o primeiro elemento para "Python".
1. Exercícios Simples com if-elif-else
    1. Crie uma lista com três números inteiros. Se o primeiro elemento for maior que 10, altere o segundo elemento para 20. Caso contrário, altere o segundo elemento para 5.
        ```python
        numeros = [1, 2, 3]
        # numeros = [100, 2, 3]

        print('numeros :', numeros)

        if numeros[0] > 10:
            numeros[1] = 20
        else:
            numeros[1] = 5

        print('numeros :', numeros)
        ```
    1. Crie uma lista com três strings. Se a lista contiver a string "Python", exiba "Encontrado". Caso contrário, exiba "Não encontrado".
    1. Crie uma lista com cinco números decimais. Se o terceiro elemento for maior que 2.5, altere o último elemento para 0. Caso contrário, altere o primeiro elemento para 1.
    1. Crie uma lista com quatro valores booleanos. Se o primeiro elemento for True, altere o segundo elemento para False. Caso contrário, altere o terceiro elemento para True.
    1. Crie uma lista com três strings. Se a lista não contiver a string "Hello", adicione "Hello" no final da lista. Caso contrário, remova o último elemento.
1. Exercícios Intermediários
    1. Crie uma lista com seis números inteiros e exiba a quantidade de elementos na lista.
    1. Crie uma lista com cinco strings e exiba a string no índice 2.
    1. Crie uma lista com sete números decimais e insira o número 3.14 no índice 4.
    1. Crie uma lista com quatro valores booleanos e remova o terceiro elemento.
    1. Crie uma lista com três números inteiros e adicione o número 7 no final da lista.
1. Exercícios Intermediários com if-elif-else
    1. Crie uma lista com seis números inteiros. Se o comprimento da lista for maior que 5, exiba o primeiro e o último elemento. Caso contrário, exiba "Lista pequena".
    1. Crie uma lista com cinco strings. Se a lista contiver a string "Python", altere o último elemento para "Coding". Caso contrário, adicione "Learning" no final da lista.
    1. Crie uma lista com sete números decimais. Se o quarto elemento for maior que 1.5, remova o primeiro elemento. Caso contrário, insira o número 0 no início da lista.
    1. Crie uma lista com quatro valores booleanos. Se a lista contiver o valor True, exiba "True encontrado". Caso contrário, exiba "Nenhum True".
    1. Crie uma lista com três números inteiros. Se a soma dos elementos for maior que 20, adicione o número 5 no final da lista. Caso contrário, remova o último elemento.
1. Exercícios Avançados
    1. Crie uma lista com cinco números inteiros e troque o primeiro e o último elemento de lugar.
    1. Crie uma lista com quatro strings e adicione uma nova string na segunda posição.
    1. Crie uma lista com seis números decimais e remova o número no índice 3.
    1. Crie uma lista com três valores booleanos e adicione o valor True no início da lista.
    1. Crie uma lista com cinco números inteiros e insira o número 10 na penúltima posição.
1. Exercícios Avançados com if-elif-else
    1. Crie uma lista com cinco números inteiros. Se a lista contiver o número 5, remova-o. Caso contrário, adicione o número 5 no final da lista.
    1. Crie uma lista com quatro strings. Se o segundo elemento for "Python", altere o terceiro elemento para "Programação". Caso contrário, insira "Estudo" na terceira posição.
    1. Crie uma lista com seis números decimais. Se a soma dos elementos for maior que 10, remova o último elemento. Caso contrário, adicione o número 1.1 no início da lista.
    1. Crie uma lista com três valores booleanos. Se a lista contiver dois valores True, altere o último elemento para False. Caso contrário, adicione True no final da lista.
    1. Crie uma lista com quatro números inteiros. Se o comprimento da lista for igual a 4, exiba o segundo e o terceiro elemento. Caso contrário, exiba "Lista incorreta".
1. Exercícios Complexos
    1. Crie uma lista com cinco números inteiros e substitua todos os números pares por zero.
    1. Crie uma lista com quatro strings e converta todas as strings para maiúsculas.
    1. Crie uma lista com seis números decimais e insira o número 2.5 após cada número maior que 2.
    1. Crie uma lista com três valores booleanos e adicione um valor booleano alternado após cada elemento.
    1. Crie uma lista com cinco números inteiros e remova todos os números ímpares.
1. Exercícios Complexos com if-elif-else
    1. Crie uma lista com cinco números inteiros. Se todos os números forem positivos, substitua o último número por -1. Caso contrário, adicione -1 no final da lista.
    1. Crie uma lista com quatro strings. Se a lista contiver a string "Python", altere todas as strings para "Code". Caso contrário, adicione "Python" no final da lista.
    1. Crie uma lista com seis números decimais. Se a média dos números for maior que 3, remova o primeiro e o último elemento. Caso contrário, adicione 0.5 no início e no final da lista.
    1. Crie uma lista com três valores booleanos. Se a lista contiver dois valores False, altere o primeiro elemento para True. Caso contrário, insira False no início da lista.
    1. Crie uma lista com quatro números inteiros. Se a soma dos elementos for maior que 15, remova o número no índice 2. Caso contrário, insira o número 7 na posição 1.
1. Exercícios Muito Complexos
    1. Crie uma lista com cinco números inteiros e inverta a ordem dos elementos.
    1. Crie uma lista com quatro strings e remova todas as strings que contêm a letra "a".
    1. Crie uma lista com seis números decimais e insira um número aleatório após cada elemento.
    1. Crie uma lista com três valores booleanos e remova todos os valores False.
    1. Crie uma lista com cinco números inteiros e substitua cada elemento pelo seu quadrado.
1. Exercícios Muito Complexos com if-elif-else
    1. Crie uma lista com cinco números inteiros. Se a lista contiver números negativos, remova todos eles. Caso contrário, adicione -1 no início e no final da lista.
    1. Crie uma lista com quatro strings. Se a lista tiver mais de uma string com a letra "e", remova todas essas strings. Caso contrário, adicione "No e" no final da lista.
    1. Crie uma lista com seis números decimais. Se a soma dos números for menor que 10, insira o número 5.5 no meio da lista. Caso contrário, remova o número no meio da lista.
    1. Crie uma lista com três valores booleanos. Se todos os valores forem True, altere o segundo elemento para False. Caso contrário, adicione True no final da lista.
    1. Crie uma lista com quatro números inteiros. Se a soma dos elementos for maior que 20, remova todos os números pares. Caso contrário, adicione 2 após cada número ímpar.

</details>

## while

A estrutura de repetição `while` em Python é usada para executar um bloco de código repetidamente, desde que uma condição seja verdadeira. A cada iteração (a cada repetição), a condição é avaliada; se continuar sendo verdadeira, o loop continua, caso contrário, ele para.

Veja a sintaxe básica :

```python
while condicao:
    # Bloco de código a ser repetido
```

- **`condicao`**: uma expressão que será avaliada como `True` ou `False`;
- **bloco de código**: o conjunto de instruções que será executado repetidamente enquanto a condição for `true`;

### exemplo de contagem

Veja como fica uma contagem simples, iniciando em 1 e terminando em 5 :

```python
contador = 1

while contador <= 5:
    print("Contagem : ", contador)
    contador = contador + 1
```

O código inicia com a definição da variável `contador` e o valor 1 é atribuída a ela. Em seguida, o comando `while` testa a condição especificada nele, se `contador <= 5`. Enquanto a condição for verdadeira, seu bloco de código interno será executado. No bloco de código, é utilizado um `print` para exibir uma string e o valor da variável `contador`. Logo depois, é somado 1 ao conteúdo da variável contador usando `contador = contador + 1`.

Esse código terá como resultado :

```
Contagem : 1
Contagem : 2
Contagem : 3
Contagem : 4
Contagem : 5
```

Após `contador` chegar a 6, a condição `contador <= 5` se tornará `False`, e o loop será interrompido.

### exemplo com entrada do usuário

O `while` é frequentemente usado para repetir ações até que o usuário forneça uma resposta específica.

```python
resposta = ""

while resposta != "sair":
    resposta = input("Digite algo (ou 'sair' para encerrar): ")
    print('Você digitou :', resposta)
```

- O loop continuará pedindo uma entrada do usuário e imprimindo-a até que o usuário digite "sair";
- Quando a entrada for "sair", a condição `resposta != "sair"` será `False`, e o loop será interrompido;

### exemplo com uma condição complexa

Às vezes, a condição dentro de um `while` pode ser mais complexa e envolver múltiplas variáveis.

```python
numero = 10
divisor = 2

while numero % divisor == 0:
    print(numero, 'é divisível por', divisor)
    numero = numero / 2
```

- A condição `numero % divisor == 0` verifica se `numero` é divisível por `divisor`;
- Enquanto o `numero` for divisível por `2`, ele será dividido por 2 a cada iteração, e a mensagem será impressa;
- O loop para quando `numero` não for mais divisível por 2;

### cuidados com o `while`

Um cuidado importante ao usar `while` é evitar loops infinitos, que acontecem quando a condição nunca se torna `False`. Por exemplo:

```python
contador = 1

while contador <= 5:
    print("Contagem : ", contador)
    # Esquecemos de incrementar o contador!
```

Esse código nunca sairá do loop porque `contador` nunca muda, fazendo com que a condição seja sempre verdadeira. Isso pode travar o programa.

## contador e acumulador

Os conceitos de **acumulador** e **contador** são amplamente usados em loops, especialmente com `while`, para realizar operações repetitivas como somar valores ou contar ocorrências.

### contador

Um **contador** é uma variável que é usada para contar quantas vezes um evento ocorre. Geralmente, ele é incrementado por um valor fixo (como 1) a cada iteração do loop.

É possível contar quantas vezes um loop `while` é executado. Veja o código abaixo :

```python
contador = 0
resposta = ''

while resposta != "sair":
    resposta = input("Digite algo (ou 'sair' para encerrar): ")
    print('Você digitou :', resposta)
    contador = contador + 1

print('o loop while foi executado', contador, 'vezes')
```

O código acima começa declarando as variáveis `contador` e `resposta`. Em seguida, o comando `while` testa se a resposta é diferente a `sair`. Enquanto a condição for verdadeira, o bloco de código dentro do `while` é executado. Dentro dele, a cada iteração, é feita uma pergunta (`input("Digite algo (ou 'sair' para encerrar): ")`) para o usuário e salvar o for digitado na variável `resposta`. Em seguida, é mostrado o que o usuário digitou com usando um `print` e o contador é incrementado em 1.

Ao final, quando o usuário finalmente digitar **sair**, o loop (laço de repetição) será encerrado e o `print` final irá mostrar a quantidade de vezes que a pergunta fora feita ao usuário.

### acumulador

Um **acumulador** é uma variável que acumula valores ao longo das iterações de um loop. Geralmente, ele começa em um valor inicial (como 0) e a cada iteração, um novo valor é adicionado a ele.

Veja como somar os números de 1 a 5 usando um acumulador :

```python
soma = 0
numero = 1

while numero <= 5:
    soma = soma + numero
    print(f"Adicionando {numero}, soma agora é {soma}")
    print('Adicionando', numero, ', a soma agora é', soma)
    numero = numero + 1

print('a soma final é', soma)
```

A variável `soma` é inicializada com o valor 0 e a variável `numero` é inicializada com o valor 1. Depois, o comando `while` testa se a condição `numero <= 5` é verdadeira. Enquanto for, o bloco de código é executado. Dentro dele, a cada iteração, o valor e `numero` é adicionado a `soma` (`soma = soma + numero`). Em seguida, o `numero` é incrementado em 1 a cada iteração.

Ao final, é mostrado o valor final da variável `soma`.

### acumulador e contador

É possível combinar um contador e um acumulador no mesmo loop.

Considere o seguinte, é preciso somar os números pares de 1 a 10 e contar quantos números pares existem nesse intervalo.

```python
contador_pares = 0
soma_pares = 0
numero = 1

while numero <= 10:
    if numero % 2 == 0:
        contador_pares = contador_pares + 1
        soma_pares = soma_pares + numero
    numero = numero + 1

print('Quantidade de números pares :', contador_pares)
print('Soma dos números pares :', soma_pares)
```

O código acima inicia com a declaração das variáveis `contador_pares`, `soma_pares` e `numero`. O comando `while` testa se `numero <= 10` é verdadeiro, se for o bloco de código é executado. Em seguida, é feito um testes para número par (`numero % 2 == 0`). Quando o teste der verdadeiro, o `contador_pares` é incrementado em 1 e a `soma_pares` é somado com o valor da variável `numero`. Em seguida, mesmo que a condição do `if` seja falsa, a variável `numero` é incrementada em 1.

Ao finalizar o loop, é mostrado os valores das variáveis `contador_pares` e `soma_pares`.

Veja agora um uso de um acumulador, mas agora usando com multiplicação :

```python
# algoritmo para calcular o fatorial de 5
produto = 1
numero = 1

while numero <= 5:
    produto *= numero
    print(f"Multiplicando por {numero}, produto agora é {produto}")
    numero += 1

print('o fatorial de 5 é', produto)
```

## exercícios while

<details>
<summary>Lista de Exercícios</summary>

1. Nível Simples
    1. Crie um programa que peça ao usuário para digitar um número inteiro positivo e continue pedindo até que o número digitado seja maior que 10.
    1. Crie um programa que peça ao usuário para digitar números inteiros e some esses números até que o usuário digite um número negativo.
    1. Crie um programa que peça ao usuário para digitar uma senha (string) até que ele acerte a senha correta "Python123".
    1. Crie um programa que peça ao usuário para digitar um número decimal até que ele digite um valor maior que 0.5.
    1. Crie um programa que exiba "Olá!" 5 vezes utilizando um while e uma variável contador.
1. Nível Simples com if-elif-else
    1. Crie um programa que peça ao usuário para digitar números inteiros até que ele digite um número maior que 50. Se o número for ímpar, exiba "Ímpar". Caso contrário, exiba "Par".
    1. Crie um programa que peça ao usuário para digitar palavras até que ele digite "sair". Se a palavra contiver a letra "a", exiba "Contém a letra 'a'". Caso contrário, exiba "Não contém a letra 'a'".
    1. Crie um programa que peça ao usuário para digitar números decimais até que a soma dos números seja maior que 100. Se o número digitado for maior que 10, exiba "Número grande". Caso contrário, exiba "Número pequeno".
    1. Crie um programa que peça ao usuário para digitar valores booleanos (True ou False) até que ele digite "False". Se for "True", exiba "Verdadeiro". Caso contrário, exiba "Falso".
    1. Crie um programa que peça ao usuário para digitar números inteiros até que ele digite um número negativo. Se o número for divisível por 3, exiba "Divisível por 3". Caso contrário, exiba "Não divisível por 3".
1. Nível Intermediário
    1. Crie um programa que peça ao usuário para digitar números inteiros até que ele digite um número maior que 20. Em seguida, exiba todos os números digitados em uma lista.
    1. Crie um programa que peça ao usuário para digitar números decimais até que ele digite um número menor que 1.5. Em seguida, exiba a média dos números digitados.
    1. Crie um programa que peça ao usuário para digitar palavras até que ele digite "stop". Em seguida, exiba todas as palavras em uma única string concatenada.
    1. Crie um programa que peça ao usuário para digitar valores booleanos (True ou False) até que ele digite "True". Em seguida, exiba quantas vezes o valor "False" foi digitado.
    1. Crie um programa que peça ao usuário para digitar números inteiros e adicione-os a uma lista até que a lista tenha 5 elementos. Em seguida, exiba a lista completa.
1. Nível Intermediário com if-elif-else
    1. Crie um programa que peça ao usuário para digitar números inteiros até que ele digite um número par. Se o número for maior que 10, adicione-o a uma lista de "números grandes". Caso contrário, adicione-o a uma lista de "números pequenos". Exiba as duas listas ao final.
    1. Crie um programa que peça ao usuário para digitar palavras até que ele digite "fim". Se a palavra tiver mais de 5 caracteres, adicione-a a uma lista de "palavras longas". Caso contrário, adicione-a a uma lista de "palavras curtas". Exiba as duas listas ao final.
    1. Crie um programa que peça ao usuário para digitar números decimais até que ele digite um número negativo. Se o número for maior que 1, exiba "Grande". Se for menor que 1, exiba "Pequeno". Se for igual a 1, exiba "Igual a 1".
    1. Crie um programa que peça ao usuário para digitar valores booleanos (True ou False) até que ele digite "False" duas vezes seguidas. Exiba quantas vezes "True" foi digitado.
    1. Crie um programa que peça ao usuário para digitar números inteiros até que ele digite um número maior que 100. Se o número for múltiplo de 5, adicione-o a uma lista de "múltiplos de 5". Caso contrário, adicione-o a uma lista de "não múltiplos de 5". Exiba as duas listas ao final.
1. Nível Avançado
    1. Crie um programa que peça ao usuário para digitar números inteiros até que ele digite um número primo. Exiba todos os números digitados até então.
    1. Crie um programa que peça ao usuário para digitar números decimais até que ele digite um número igual a 0. Em seguida, exiba o maior número digitado.
    1. Crie um programa que peça ao usuário para digitar palavras até que ele digite uma palavra que comece com a letra "z". Em seguida, exiba a palavra mais longa digitada.
    1. Crie um programa que peça ao usuário para digitar valores booleanos (True ou False) até que ele digite "True" três vezes. Exiba a quantidade total de valores digitados.
    1. Crie um programa que peça ao usuário para digitar números inteiros até que ele digite um número negativo. Em seguida, exiba a soma de todos os números digitados.
1. Nível Avançado com if-elif-else
    1. Crie um programa que peça ao usuário para digitar números inteiros até que ele digite um múltiplo de 7. Se o número for par, adicione-o a uma lista de "pares". Se for ímpar, adicione-o a uma lista de "ímpares". Exiba as duas listas ao final.
    1. Crie um programa que peça ao usuário para digitar palavras até que ele digite "exit". Se a palavra contiver a letra "e", adicione-a a uma lista de "palavras com e". Caso contrário, adicione-a a uma lista de "palavras sem e". Exiba as duas listas ao final.
    1. Crie um programa que peça ao usuário para digitar números decimais até que ele digite um número menor que 0. Se o número for positivo, exiba "Positivo". Se for negativo, exiba "Negativo". Se for zero, exiba "Zero".
    1. Crie um programa que peça ao usuário para digitar valores booleanos (True ou False) até que ele digite "False" três vezes seguidas. Exiba a quantidade total de "True" digitados.
    1. Crie um programa que peça ao usuário para digitar números inteiros até que a soma dos números seja maior que 50. Se o número digitado for maior que 10, exiba "Grande". Caso contrário, exiba "Pequeno".
1. Nível Complexo
    1. Crie um programa que peça ao usuário para digitar números inteiros até que ele digite um número divisível por 4. Em seguida, exiba o menor número digitado.
    1. Crie um programa que peça ao usuário para digitar números decimais até que ele digite um número entre 0 e 1. Em seguida, exiba a média dos números digitados.
    1. Crie um programa que peça ao usuário para digitar palavras até que ele digite "fim". Em seguida, exiba as palavras digitadas em ordem inversa.
    1. Crie um programa que peça ao usuário para digitar valores booleanos (True ou False) até que ele digite "True" cinco vezes. Em seguida, exiba quantas vezes "False" foi digitado.
    1. Crie um programa que peça ao usuário para digitar números inteiros até que a soma dos números seja maior que 100. Em seguida, exiba todos os números digitados que sejam divisíveis por 5.
1. Nível Complexo com if-elif-else
    1. Crie um programa que peça ao usuário para digitar números inteiros até que ele digite um número primo. Se o número for maior que 50, adicione-o a uma lista de "números grandes". Caso contrário, adicione-o a uma lista de "números pequenos". Exiba as duas listas ao final.
    1. Crie um programa que peça ao usuário para digitar palavras até que ele digite uma palavra que tenha exatamente 5 letras. Se a palavra começar com "a", adicione-a a uma lista de "palavras com a". Caso contrário, adicione-a a uma lista de "outras palavras". Exiba as duas listas ao final.
    1. Crie um programa que peça ao usuário para digitar números decimais até que ele digite um número menor que 0. Se o número for maior que 5, adicione-o a uma lista de "números altos". Caso contrário, adicione-o a uma lista de "números baixos". Exiba as duas listas ao final.
    1. Crie um programa que peça ao usuário para digitar valores booleanos (True ou False) até que ele digite "True" quatro vezes seguidas. Se o valor for "True", adicione-o a uma lista de "verdadeiros". Caso contrário, adicione-o a uma lista de "falsos". Exiba ambas as listas ao final.
    1. Crie um programa que peça ao usuário para digitar números inteiros até que ele digite um número que seja a soma dos dois números anteriores. Se o número digitado for maior que 20, adicione-o a uma lista de "números grandes". Caso contrário, adicione-o a uma lista de "números pequenos". Exiba as duas listas ao final.
1. Nível Muito Complexo
    1. Crie um programa que peça ao usuário para digitar números inteiros até que ele digite um número que seja divisível por todos os números anteriormente digitados. Exiba a lista completa de números ao final.
    1. Crie um programa que peça ao usuário para digitar números decimais até que ele digite um número que seja a média de todos os números anteriormente digitados. Exiba o maior e o menor número digitado ao final.
    1. Crie um programa que peça ao usuário para digitar palavras até que ele digite uma palavra que tenha as mesmas letras (em qualquer ordem) que a primeira palavra digitada. Em seguida, exiba a quantidade total de palavras digitadas.
    1. Crie um programa que peça ao usuário para digitar valores booleanos (True ou False) até que ele digite uma sequência de "True", "False", "True", "False". Exiba quantas vezes "True" e "False" foram digitados ao final.
    1. Crie um programa que peça ao usuário para digitar números inteiros até que a soma dos números digitados seja igual ao produto dos números digitados. Em seguida, exiba todos os números digitados e a soma total.
1. Nível Muito Complexo com if-elif-else
    1. Crie um programa que peça ao usuário para digitar números inteiros até que ele digite um número que seja divisível pelo número de elementos já digitados. Se o número for maior que 100, adicione-o a uma lista de "números muito grandes". Caso contrário, adicione-o a uma lista de "outros números". Exiba ambas as listas ao final.
    1. Crie um programa que peça ao usuário para digitar palavras até que ele digite uma palavra que tenha um número de letras igual ao número total de palavras digitadas anteriormente. Se a palavra começar com uma vogal, adicione-a a uma lista de "palavras com vogal". Caso contrário, adicione-a a uma lista de "palavras com consoante". Exiba ambas as listas ao final.
    1. Crie um programa que peça ao usuário para digitar números decimais até que ele digite um número que seja o dobro de algum dos números já digitados. Se o número for maior que 10, adicione-o a uma lista de "números grandes". Caso contrário, adicione-o a uma lista de "números pequenos". Exiba ambas as listas ao final.
    1. Crie um programa que peça ao usuário para digitar valores booleanos (True ou False) até que ele digite um padrão alternado de "True" e "False" três vezes seguidas. Exiba a quantidade total de "True" e "False" digitados ao final.
    1. Crie um programa que peça ao usuário para digitar números inteiros até que ele digite um número que seja múltiplo da soma dos dígitos de um dos números anteriormente digitados. Se o número for par, adicione-o a uma lista de "pares". Caso contrário, adicione-o a uma lista de "ímpares". Exiba ambas as listas ao final.
</details>


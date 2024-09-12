Índice

1. [o que é](#o-que-é)
1. [para que server](#para-que-serve)
1. [como funciona](#como-funciona)
1. [cuidados](#cuidados)
1. [exercícios](#exercícios)

# operador walrus

O operador **Walrus** (`:=`) foi introduzido no Python 3.8 como parte da **PEP 572**. Também conhecido como o operador de "atribuição em expressão", ele permite atribuir valores a variáveis enquanto elas são usadas dentro de expressões. Isso pode tornar o código mais conciso, especialmente em loops ou condições.

## o que é

O operador Walrus é uma forma de **atribuição dentro de uma expressão**. Em Python, antes do operador Walrus, você não podia atribuir um valor a uma variável e ao mesmo tempo utilizá-lo dentro de uma expressão como em um `if`, `while`, `for`, ou até mesmo em compreensões de listas. O operador Walrus resolve esse problema ao permitir que se faça essas duas coisas de uma vez só.

## para que serve

Ele tem diversos usos, e o principal objetivo é tornar o código mais **eficiente e legível** ao permitir:
- evitar a necessidade de fazer uma atribuição em uma linha e usar essa variável em uma condição em outra linha;
- evitar cálculos redundantes quando uma mesma expressão precisa ser calculada várias vezes em uma condição e dentro do bloco de código;
- melhorar a performance em certos cenários, como em loops que dependem de um valor que você só quer calcular uma vez por iteração;

## como funciona

Abaixo há diversos exemplos de como usar e como funciona.

1. **atribuição dentro de um `while`**

Tradicionalmente, ao escrever um loop `while`, o valor usado na condição seria separado da atribuição. Com o operador Walrus, pode-se unificar esses dois passos.

```python
# sem o operador Walrus
n = 0
while n < 10:
    print(n)
    n += 1

# com o operador Walrus
n = 0
while (n := n + 1) < 10:
    print(n)
```

Aqui, o operador Walrus permite que o valor de `n` seja atualizado e utilizado diretamente dentro da condição do `while`.

2. **evitar duplicação de expressões em `if`**

Antes do Python 3.8, se tivesse uma função ou cálculo que precisasse ser utilizado tanto na condição de um `if` quanto dentro do bloco `if`, teria que se chamar a função duas vezes ou armazenar o valor antes de entrar no `if`. O operador Walrus facilita isso:

```python
# sem o operador Walrus
dados = input("Digite algo: ")
if len(dados) > 3:
    print(f"Dado tem {len(dados)} caracteres")

# com o operador Walrus
if (n := len(input("Digite algo: "))) > 3:
    print(f"Dado tem {n} caracteres")
```

Neste exemplo, o uso do operador Walrus evita que a função `len()` seja chamada duas vezes.

3. **compreensões de listas**

O operador Walrus também pode ser útil em compreensões de listas para evitar cálculos repetidos ou criar filtros baseados em valores calculados no meio da compreensão.

```python
# sem o operador Walrus
resultados = []
for i in range(10):
    quadrado = i * i
    if quadrado > 20:
        resultados.append(quadrado)

# com o operador Walrus
resultados = [quadrado for i in range(10) if (quadrado := i * i) > 20]
```

Aqui, a compreensão de lista com o operador Walrus é mais compacta, e o valor `quadrado` é calculado apenas uma vez por iteração.

4. **evitar chamadas de funções repetidas**

Imagine que se tenha uma função cara (que demora para ser processada) e precisa tanto do resultado dela quanto de seu uso para alguma lógica. O Walrus ajuda aqui também:

```python
def pega_dados():
    print("Buscando dados")
    return [1, 2, 3, 4, 5]

# sem o operador Walrus
data = pega_dados()
if data:
    print(f"Dados obtidos: {data}")

# com o operador Walrus
if (data := pega_dados()):
    print(f"Dados obtidos: {data}")
```

Nesse caso, com o operador Walrus, evitamos fazer duas chamadas para `fetch_data()`, economizando processamento.

## cuidados

Embora o operador Walrus possa tornar o código mais eficiente, **ele deve ser usado com cuidado** para não comprometer a legibilidade.

Aqui estão algumas dicas:
- **legibilidade acima de tudo** : não sacrifique a clareza do código apenas para usar o walrus. ele deve melhorar a legibilidade, não complicá-la;
- **use em expressões onde economiza processamento** : se houver um cálculo que será repetido várias vezes em uma expressão, considere usar o walrus para atribuir o valor uma vez e reutilizá-lo;
- **cuidado com expressões complexas** : o operador walrus pode levar a expressões complicadas que são difíceis de depurar. se perceber que o código está ficando muito difícil de entender, divida-o em partes menores;
- **útil em loops e condições** : o maior benefício do walrus geralmente é visto em loops (`for` ou `while`) e condições (`if`), especialmente quando se quer evitar a repetição de cálculos ou verificar condições ao mesmo tempo que atribui valores;

Por exemplo, evite escrever algo como:

```python
if (temp := pega_temperatuda()) and (hum := pega_humidade()) and (pres := pega_pressao()):
    print(f"Condições: {temp}°C, {hum}%, {pres}hPa")
```

Este código é válido, mas pode se tornar difícil de entender rapidamente.

## exercícios

<details>
<summary>Lista de Exercícios</summary>

1. Exercícios Simples
    1. Escreva um programa que leia números do usuário repetidamente, usando um `while`. O loop deve parar se o usuário digitar um número negativo. Use o operador Walrus para armazenar e verificar o número.
    1. Faça um programa que leia uma string do usuário e verifique se o comprimento da string é maior que 5. Se for, imprima a string e seu comprimento. Use o operador Walrus.
    1. Crie um código que leia a idade do usuário e, se a idade for maior que 18, imprima "Maior de idade". Utilize o operador Walrus na condição.
    1. Use o operador Walrus para verificar se um número inserido pelo usuário é divisível por 7. Se for divisível, imprima o número.
    1. Escreva um programa que receba um número e imprima o quadrado desse número, **apenas** se ele for maior que 10. Use o operador Walrus para realizar a atribuição e a verificação.
1. Exercícios de Loops
    1. Implemente um loop `while` que leia a entrada do usuário até que ele digite "sair". Utilize o operador Walrus para armazenar a entrada e verificar a condição de saída.
    1. Crie um programa que receba números do usuário até que um número maior que 100 seja inserido. Utilize o operador Walrus para atribuir e comparar o valor no `while`.
    1. Use o operador Walrus em um loop `while` que leia uma lista de números do usuário, pare ao encontrar um número zero, e imprima todos os números inseridos até o momento.
    1. Faça um código que leia números do usuário e armazene-os em uma lista. O loop deve parar quando o usuário digitar um número menor que 5. Use o Walrus no `while`.
    1. Crie um loop que leia o nome de uma pessoa e, se o nome contiver mais de 8 caracteres, exiba o nome. Utilize o operador Walrus para verificar essa condição e sair do loop quando o nome for "finalizar".
1. Exercícios com Compreensão de Listas
    1. Crie uma lista de quadrados de números de 1 a 10, mas somente se o quadrado for maior que 20. Use o operador Walrus dentro de uma compreensão de listas.
    1. Gere uma lista de números de 1 a 100, filtrando apenas os números que, quando multiplicados por 3, resultam em valores maiores que 50. Use o operador Walrus para realizar a filtragem.
    1. Dada uma lista de números, crie uma nova lista que contenha apenas os números cuja raiz quadrada seja maior que 2. Use o operador Walrus para atribuir e filtrar os valores.
    1. Usando uma compreensão de lista e o operador Walrus, crie uma lista de strings que tenham mais de 4 caracteres a partir de uma lista fornecida.
    1. Crie uma lista de comprimentos de palavras a partir de uma lista de strings, mas só inclua palavras que tenham mais de 6 letras. Use o Walrus para calcular o comprimento e realizar a verificação.
1. Exercícios com Funções e Filtros
    1. Escreva uma função que receba uma lista de números e retorne apenas os números pares cujo valor ao quadrado seja maior que 30. Use o operador Walrus dentro da função.
    1. Use o operador Walrus dentro de uma função `map()` para multiplicar todos os números de uma lista por 2 e filtrar aqueles que resultem em valores maiores que 10.
    1. Escreva uma função que receba uma lista de strings e retorne apenas aquelas que começam com a letra "A" e tenham mais de 5 caracteres. Use o Walrus na verificação.
    1. Faça uma função que receba uma lista de números e retorne a soma dos quadrados dos números que são maiores que 10. Use o Walrus para evitar a repetição de cálculos.
    1. Escreva uma função que retorne o primeiro número de uma lista que seja divisível por 5 e maior que 50. Use o Walrus para realizar a filtragem.
1. Exercícios com Condições
    1. Crie um programa que peça para o usuário digitar um número. Se o número for maior que 50, imprima "Número muito alto" e pare o programa. Use o operador Walrus.
    1. Use o operador Walrus para pedir que o usuário insira um número e, se o número for par, imprima "Número par". Caso contrário, imprima "Número ímpar".
    1. Escreva um código que leia o nome e a idade do usuário, e só imprima o nome se a idade for maior que 30. Use o operador Walrus na verificação.
    1. Crie um programa que receba um valor numérico e verifique se ele é positivo. Se for, imprima "Positivo" e o valor. Use o operador Walrus para atribuir e verificar.
    1. Faça um programa que leia um número do usuário e, se o número for divisível por 3 e maior que 15, imprima "Aceito". Use o Walrus para fazer a verificação na condição do `if`.
1. Exercícios com Manipulação de Dados
    1. Dada uma lista de números, use o operador Walrus para imprimir os números que, quando divididos por 4, resultam em valores maiores que 5. Faça isso dentro de um loop `for`.
    1. Escreva um programa que leia uma lista de strings e imprima apenas as strings que contenham mais de 3 vogais. Use o Walrus para contar as vogais e fazer a verificação.
    1. Crie uma lista de números de 1 a 20. Usando o operador Walrus, filtre e crie uma nova lista com apenas os números que, multiplicados por 2, são menores que 25.
    1. Faça um programa que leia números do usuário e armazene-os em uma lista. O loop deve parar quando o usuário inserir um número negativo. Imprima a soma dos números armazenados usando o Walrus.
    1. Escreva um código que leia a idade de várias pessoas e armazene as idades em uma lista. O loop deve parar quando for inserida uma idade menor que 0. Ao final, imprima a média das idades usando o Walrus para calcular a soma e a contagem de idades.

</details>

Índice Input e Lista

* [input](#input)
* [exercícios inpur](#exercícios-input)
* [lista](#lista)
* [str e list](#str-e-list)
* [exercícios lista](#exercícios-lista)

# input e lista

## input
A função `input` do Python é uma ferramenta fundamental para receber dados do usuário durante a execução de um programa. Ela é usada para ler uma linha de texto digitada pelo usuário e pode ser armazenada em uma variável para uso posterior no código.

Quando usada, a função `input` exibe uma mensagem (prompt) ao usuário e pausa a execução do programa até que o usuário digite algo e pressione a tecla Enter, finalizando assim a entrada de dados. **TUDO** o que o usuário digitar é retornado como uma `string`.

Veja um uso básico

```python
msg = input("Mensagem para o usuário: ")
```

O que acontece é o seguinte :
1. O Python exibe a "Mensagem para o usuário: ";
1. O usuário digita uma resposta e pressiona Enter;
1. A resposta do usuário é armazenada na variável `msg`;

Veja alguns exemplos de uso :

```python
# recebendo o nome do usuário
nome = input("Digite seu nome: ")
print("Olá, " + nome + "!")
```

No algoritmo anterior :
1. O programa pede que o usuário digite seu nome;
1. O usuário digita o nome e pressiona Enter;
1. O programa armazena o nome na variável `nome`;
1. O programa imprime uma mensagem de saudação usando o nome fornecido pelo usuário;

```python
# recebendo dois números
numero1 = input("Digite o primeiro número: ")
numero2 = input("Digite o segundo número: ")

# convertendo as entradas para inteiros
numero1 = int(numero1)
numero2 = int(numero2)

soma = numero1 + numero2
print("A soma dos números é :", soma)
```

No algoritmo acima :
1. O programa pede que o usuário digite dois números;
1. As entradas são inicialmente strings, então precisamos convertê-las para inteiros usando a função `int`;
1. Depois de converter, somamos os números e exibimos o resultado;

### dados recebidos

Por padrão, a função `input` ***SEMPRE*** retorna uma string. Se o valor esperado for um número, é necessário converter a string para o tipo de dado adequado (por exemplo, `int` ou `float`).

Aqui estão alguns exemplos :

```python
# recebendo um valor decimal
altura = input("Digite sua altura (em metros): ")
altura = float(altura)
print("Sua altura é :", altura, "metros")

# recebendo um valor inteiro
idade = int(input("Digite sua idade: "))
print("Sua idade é:", idade)
```

É necessário ter cuidado quando se está convertendo um tipo string para inteiro ou float. Pois se o conteúdo não puder ser convertido apropriadamente, irá levantar um erro. Por hora, não será visto como tratar isso.

## exercícios input

<details>
<summary>Lista de Exercícios</summary>

1. String
    1. Peça ao usuário para digitar seu nome e exiba uma saudação personalizada.
    1. Peça ao usuário para digitar uma palavra e exiba o primeiro e o último caractere.
    1. Peça ao usuário para digitar uma frase e exiba a quantidade de caracteres na frase.
    1. Peça ao usuário para digitar duas palavras e exiba-as concatenadas.
    1. Peça ao usuário para digitar uma frase e exiba a frase invertida.
1. String com if-elif-else
    1. Peça ao usuário para digitar uma palavra e verifique se a palavra contém a letra "a". Exiba uma mensagem apropriada.
    1. Peça ao usuário para digitar uma frase e verifique se a frase tem mais de 20 caracteres. Exiba uma mensagem apropriada.
    1. Peça ao usuário para digitar seu nome. Se o nome começar com a letra "A", exiba "Seu nome começa com A". Caso contrário, exiba "Seu nome não começa com A".
    1. Peça ao usuário para digitar uma palavra. Se a palavra for "Python", exiba "Linguagem de programação". Caso contrário, exiba "Palavra comum".
    1. Peça ao usuário para digitar uma frase. Se a frase terminar com um ponto (.), exiba "Frase completa". Caso contrário, exiba "Frase incompleta".
1. Int
    1. Peça ao usuário para digitar sua idade e exiba uma mensagem dizendo quantos anos ele terá em 10 anos.
    1. Peça ao usuário para digitar dois números inteiros e exiba a soma deles.
    1. Peça ao usuário para digitar um número inteiro e exiba o quadrado desse número.
    1. Peça ao usuário para digitar um número inteiro e exiba a metade desse número.
    1. Peça ao usuário para digitar dois números inteiros e exiba o produto deles.
1. Int com if-elif-else
    1. Peça ao usuário para digitar um número inteiro. Se o número for positivo, exiba "Positivo". Se for negativo, exiba "Negativo". Se for zero, exiba "Zero".
    1. Peça ao usuário para digitar dois números inteiros e exiba o maior deles.
    1. Peça ao usuário para digitar um número inteiro. Se o número for par, exiba "Par". Caso contrário, exiba "Ímpar".
    1. Peça ao usuário para digitar sua idade. Se a idade for maior ou igual a 18, exiba "Maior de idade". Caso contrário, exiba "Menor de idade".
    1. Peça ao usuário para digitar um número inteiro. Se o número for múltiplo de 3, exiba "Múltiplo de 3". Se for múltiplo de 5, exiba "Múltiplo de 5". Se for múltiplo de ambos, exiba "Múltiplo de 3 e 5".
1. Float
    1. Peça ao usuário para digitar um número decimal e exiba o dobro desse número.
    1. Peça ao usuário para digitar dois números decimais e exiba a média deles.
    1. Peça ao usuário para digitar um número decimal e exiba a raiz quadrada desse número.
    1. Peça ao usuário para digitar um número decimal e exiba o cubo desse número.
    1. Peça ao usuário para digitar dois números decimais e exiba a divisão do primeiro pelo segundo.
1. Float com if-elif-else
    1. Peça ao usuário para digitar um número decimal. Se o número for maior que 100, exiba "Maior que 100". Caso contrário, exiba "Menor ou igual a 100".
    1. Peça ao usuário para digitar dois números decimais e exiba o maior deles.
    1. Peça ao usuário para digitar um número decimal. Se o número for positivo, exiba "Positivo". Se for negativo, exiba "Negativo".
    1. Peça ao usuário para digitar um número decimal. Se o número for maior que 50 e menor que 100, exiba "Entre 50 e 100". Caso contrário, exiba "Fora do intervalo".
    1. Peça ao usuário para digitar um número decimal. Se o número for maior que 0,5, exiba "Maior que meio". Caso contrário, exiba "Menor ou igual a meio".
1. Bool
    1. Peça ao usuário para digitar "True" ou "False" e exiba o valor booleano correspondente.
    1. Peça ao usuário para digitar uma resposta "sim" ou "não" e exiba o valor booleano correspondente.
    1. Peça ao usuário para digitar se ele gosta de programação (sim ou não) e exiba a resposta como booleano.
    1. Peça ao usuário para digitar se ele é maior de idade (sim ou não) e exiba a resposta como booleano.
    1. Peça ao usuário para digitar se ele tem um pet (sim ou não) e exiba a resposta como booleano.
1. Bool com if-elif-else
    1. Peça ao usuário para digitar "True" ou "False". Se for "True", exiba "Verdadeiro". Se for "False", exiba "Falso".
    1. Peça ao usuário para digitar se ele está estudando (sim ou não). Se for "sim", exiba "Estudando". Caso contrário, exiba "Não estudando".
    1. Peça ao usuário para digitar se ele está trabalhando (sim ou não). Se for "sim", exiba "Trabalhando". Caso contrário, exiba "Não trabalhando".
    1. Peça ao usuário para digitar se ele gosta de esportes (sim ou não). Se for "sim", exiba "Gosta de esportes". Caso contrário, exiba "Não gosta de esportes".
    1. Peça ao usuário para digitar se ele usa óculos (sim ou não). Se for "sim", exiba "Usa óculos". Caso contrário, exiba "Não usa óculos".
1. Exercícios Mistos
    1. Peça ao usuário para digitar seu nome e idade. Exiba uma mensagem dizendo quantos anos ele terá em 5 anos.
    1. Peça ao usuário para digitar dois números inteiros e um número decimal. Exiba a soma dos três números.
    1. Peça ao usuário para digitar uma frase e um número inteiro. Exiba a frase repetida o número de vezes digitado.
    1. Peça ao usuário para digitar uma palavra e um número decimal. Exiba a palavra concatenada com o número decimal convertido para string.
    1. Peça ao usuário para digitar uma frase e um valor booleano (sim ou não). Exiba a frase concatenada com a string "Verdadeiro" ou "Falso", dependendo do valor booleano.
1. Exercícios Mistos com if-elif-else
    1. Peça ao usuário para digitar um número inteiro e um número decimal. Se a soma for maior que 100, exiba "Soma maior que 100". Caso contrário, exiba "Soma menor ou igual a 100".
    1. Peça ao usuário para digitar seu nome e idade. Se a idade for maior ou igual a 18, exiba "Maior de idade". Caso contrário, exiba "Menor de idade".
    1. Peça ao usuário para digitar uma palavra e um valor booleano (sim ou não). Se o valor booleano for "sim", exiba a palavra em maiúsculas. Caso contrário, exiba a palavra em minúsculas.
    1. Peça ao usuário para digitar dois números decimais. Se o primeiro for maior que o segundo, exiba "Primeiro maior". Caso contrário, exiba "Segundo maior ou igual".
    1. Peça ao usuário para digitar uma frase e um número inteiro. Se o número for positivo, exiba a frase com a quantidade de caracteres igual ao número. Se for negativo, exiba a frase invertida.

</details>


# Estruturas Condicionais em Python

## estrutura sequencial

A estrutura sequencial de um algoritmo corresponde ao fato de que um conjunto de ações será executado em uma sequência linear de cima para baixo e da esquerda para a direita.

Veja um exemplo :

```python
# como calcular o valor de x de uma função quadrática usando a fórmula de
# Bhaskara
# considere a equação quadrática : x^2 + 2x - 3 = 0, encontre os dois valores
# possíveis para o X
a = 1
b = 2
c = -3

delta = b ** 2 - 4 * a * c

x1 = (-b + (delta ** (1/2))) / (2 * a)
x2 = (-b - (delta ** (1/2))) / (2 * a)

print('Os valores de X são',x1,'e',x2,'.')
```

Nesse exemplo, pode-se ver que o algoritmo inicia na primeira linha, executa sucessivamente cada uma e termina quando chega na última linha. Nenhuma linha foi ignorada.

Há algumas estruturas das linguagens de programação que permitem alterar esse fluxo.

Provavelmente a estrutura condicional mais conhecida seja a `if-else`.

## if

Em Python, o `if` é usado para fazer uma decisão baseada em uma condição. A palavra `if` significa **se** em inglês. Quando usamos `if` em Python, estamos dizendo ao computador para fazer algo **se** uma determinada condição for verdadeira.

Veja sua estrutura básica :

```python
if <condição>:
    # código a ser executado se a condição for verdadeira
```

- **condição**: uma expressão que o Python avalia como verdadeira (True) ou falsa (False);
- **código a ser executado**: um bloco de código que será executado apenas se a condição for verdadeira;

Agora veja alguns exemplos simples :

```python
idade = 18

if idade >= 18:
    print('Você já pode dirigir.')
```

Neste exemplo, a condição `idade >= 18` é verdadeira, pois a variável `idade` é igual a 18. Portanto, o Python executa o código dentro do bloco `if` e imprime "Você já pode dirigir."

```python
idade = 15

if idade >= 18:
    print('Você já pode dirigir.')
```

Neste outro exemplo, a condição `idade >= 18` é falsa, pois a variável `idade` é igual a 15. Portanto, o Python não irá executar o código dentro do bloco `if`.

## else

O `else` é usado em conjunto com o `if` para definir o que deve ser feito quando a condição do `if` não é verdadeira. A palavra `else` significa **senão** em inglês. Portanto, estamos dizendo ao computador para fazer algo se a condição do `if` for falsa.

Veja sua estrutura básica :

```python
if condição:
    # código a ser executado se a condição for verdadeira
else:
    # código a ser executado se a condição for falsa
```

- **código a ser executado se a condição for falsa**: um bloco de código que será executado apenas se a condição do `if` for falsa;

Veja agora alguns exemplos :

```python
idade = 15

if idade >= 18:
    print("Você já pode dirigir.")
else:
    print("Você está proibido de dirigir.")
```

Neste exemplo, a condição `idade >= 18` é falsa, pois a variável `idade` é igual a 15. Portanto, o Python não executa o código dentro do bloco `if`, mas sim o código dentro do bloco `else`, imprimindo "Você está proibido de dirigir."

## elif

Em Python, o `elif` é uma combinação de `else` e `if`, que significa `senão se` em inglês. Ele permite verificar múltiplas condições em uma estrutura condicional, adicionando alternativas ao `if` inicial. Se a condição do `if` for falsa, o Python verifica a condição do `elif`. Você pode usar quantos `elif` precisar para cobrir todas as possibilidades.

Veja sua estrutura básica :

```python
if condição1:
    # código a ser executado se condição1 for verdadeira
elif condição2:
    # código a ser executado se condição1 for falsa e condição2 for verdadeira
elif condição3:
    # código a ser executado se condição1 e condição2 forem falsas e condição3 for verdadeira
else:
    # código a ser executado se todas as condições anteriores forem falsas
```

- **condição1, condição2, condição3, ...**: expressões que o Python avalia como verdadeiras (True) ou falsas (False);
- **código a ser executado**: blocos de código que serão executados se a condição correspondente for verdadeira;

Veja um exemplo simples :

```python
nota = 75

if nota >= 90:
    print("Você tirou um A.")
elif nota >= 80:
    print("Você tirou um B.")
elif nota >= 70:
    print("Você tirou um C.")
else:
    print("Você está de recuperação.")
```

Neste exemplo, o Python verifica a condição `nota >= 90`. Como ela é falsa, ele passa para a próxima condição `nota >= 80`, que também é falsa. Em seguida, ele verifica `nota >= 70`, que é verdadeira. Portanto, ele executa o código dentro desse bloco "elif" e imprime "Você tirou um C.".

É possível usar quantos "elif" precisar para cobrir todas as possíveis condições. Veja um exemplo mais detalhado:

```python
dia_da_semana = "quarta-feira"

if dia_da_semana == "segunda-feira":
    print("Hoje é segunda-feira.")
elif dia_da_semana == "terça-feira":
    print("Hoje é terça-feira.")
elif dia_da_semana == "quarta-feira":
    print("Hoje é quarta-feira.")
elif dia_da_semana == "quinta-feira":
    print("Hoje é quinta-feira.")
elif dia_da_semana == "sexta-feira":
    print("Hoje é sexta-feira.")
else:
    print("Hoje é fim de semana.")
```

Neste exemplo, o Python verifica cada condição `elif` na ordem em que aparecem. Quando ele encontra a condição verdadeira (`dia_da_semana == "quarta-feira"`), ele executa o bloco de código correspondente e ignora os demais.

<details>
    <summary>Lista de Exercícios</summary>

1. Exercícios Simples
    1. Verifique se um número é positivo. Caso seja, exiba "Positivo".
    1. Verifique se um número é negativo. Caso seja, exiba "Negativo".
    1. Verifique se um número é igual a zero. Caso seja, exiba "Zero".
    1. Verifique se um número é maior que 10. Caso seja, exiba "Maior que 10".
    1. Verifique se um número é menor que 5. Caso seja, exiba "Menor que 5".
    1. Verifique se um número é par. Caso seja, exiba "Par".
    1. Verifique se um número é ímpar. Caso seja, exiba "Ímpar".
    1. Verifique se uma pessoa é maior de idade (idade >= 18). Caso seja, exiba "Maior de idade".
    1. Verifique se uma pessoa é menor de idade (idade < 18). Caso seja, exiba "Menor de idade".
    1. Verifique se um número é positivo, negativo ou zero. Exiba a mensagem correspondente.
1. Exercícios Intermediários
    1. Verifique se um número é maior que outro. Caso seja, exiba "Maior".
    1. Verifique se um número é menor que outro. Caso seja, exiba "Menor".
    1. Verifique se dois números são iguais. Caso sejam, exiba "Iguais".
    1. Verifique se um número é maior ou igual a outro. Caso seja, exiba "Maior ou igual".
    1. Verifique se um número é menor ou igual a outro. Caso seja, exiba "Menor ou igual".
    1. Verifique se um número está entre 1 e 10. Exiba "Entre 1 e 10" ou "Fora do intervalo".
    1. Verifique se uma pessoa pode votar (idade >= 16). Exiba "Pode votar" ou "Não pode votar".
    1. Verifique se um número é divisível por 3. Exiba "Divisível por 3" ou "Não é divisível por 3".
    1. Verifique se um ano é bissexto (divisível por 4, mas não por 100, exceto se for divisível por 400). Exiba "Bissexto" ou "Não bissexto".
    1. Verifique se um número é positivo, negativo ou zero e exiba a mensagem correspondente.
1. Exercícios Avançados
    1. Verifique se a média das notas de um aluno é maior ou igual a 7. Caso seja, exiba "Aprovado". Caso contrário, exiba "Reprovado".
    1. Verifique se a temperatura está abaixo de 0. Caso esteja, exiba "Congelante". Se estiver entre 0 e 20, exiba "Frio". Se estiver acima de 20, exiba "Quente".
    1. Verifique se um número é par ou ímpar, e se é maior ou menor que 10. Exiba as mensagens correspondentes.
    1. Verifique se um aluno passou de ano. As notas finais de três matérias devem ser todas maiores ou iguais a 6. Caso seja, exiba "Passou". Caso contrário, exiba "Não passou".
    1. Verifique se um número está entre 1 e 100. Se estiver entre 1 e 50, exiba "Entre 1 e 50". Se estiver entre 51 e 100, exiba "Entre 51 e 100". Caso contrário, exiba "Fora do intervalo".
    1. Verifique se uma pessoa é maior de idade (idade >= 18) e se é aposentada (idade >= 65). Exiba "Maior de idade" ou "Aposentado" ou "Menor de idade".
    1. Verifique se um número é múltiplo de 5 ou de 10. Exiba "Múltiplo de 5", "Múltiplo de 10" ou "Não é múltiplo de 5 nem de 10".
    1. Verifique se a nota final de um aluno é maior ou igual a 7. Se for, exiba "Aprovado". Se for menor que 5, exiba "Reprovado". Se estiver entre 5 e 7, exiba "Recuperação".
    1. Verifique se a temperatura está abaixo de 0. Caso esteja, exiba "Congelante". Se estiver entre 0 e 15, exiba "Frio". Se estiver entre 16 e 30, exiba "Agradável". Se estiver acima de 30, exiba "Quente".
    1. Verifique se uma pessoa pode votar (idade >= 16) e se é obrigada a votar (idade >= 18 e < 70). Exiba "Não pode votar", "Pode votar" ou "Obrigada a votar".
1. Exercícios Complexos
    1. Verifique se um triângulo é equilátero, isósceles ou escaleno com base nos comprimentos de seus lados.
    1. Verifique se uma pessoa pode se aposentar. Ela deve ter pelo menos 65 anos ou ter trabalhado por pelo menos 30 anos. Exiba "Pode se aposentar" ou "Não pode se aposentar".
    1. Verifique se uma nota está entre 0 e 10. Se estiver fora, exiba "Nota inválida". Caso contrário, verifique se é maior ou igual a 7 (Aprovado), entre 5 e 6.9 (Recuperação) ou menor que 5 (Reprovado).
    1. Verifique se um ponto (x, y) está dentro, fora ou sobre a borda de um círculo de raio 5 centrado na origem.
    1. Verifique se um número é positivo, negativo ou zero. Além disso, verifique se é par ou ímpar e exiba as mensagens correspondentes.
    1. Verifique se uma data (dia, mês, ano) é válida. Considere anos bissextos e meses com diferentes números de dias. Exiba "Data válida" ou "Data inválida".
    1. Verifique se um ano é bissexto. Se for, exiba "Bissexto". Caso contrário, verifique se é par ou ímpar e exiba a mensagem correspondente.
    1. Verifique se três valores podem formar um triângulo. Caso possam, verifique se é equilátero, isósceles ou escaleno.
    1. Verifique se um número é par ou ímpar. Além disso, verifique se está entre 1 e 100 e exiba as mensagens correspondentes.
1. Exercícios Muito Complexos
    1. Verifique se uma data (dia, mês, ano) é válida. Caso seja, verifique se é uma data futura, passada ou presente em relação à data atual.
    1. Verifique se uma pessoa pode dirigir. Ela deve ter pelo menos 18 anos e ter passado no exame de direção. Exiba "Pode dirigir" ou "Não pode dirigir".
    1. Verifique se um aluno está aprovado, em recuperação ou reprovado com base em suas notas em três provas e uma prova final. As regras de aprovação são: média >= 7 (Aprovado), média entre 5 e 6.9 (Recuperação), média < 5 (Reprovado).
    1. Verifique se um ano é bissexto. Caso seja, verifique se a data 29/02/ano é válida. Exiba "Data válida" ou "Data inválida".

</details>

# revisão

## contador e acumulador

Acumuladores e contadores são muito comuns em estruturas de repetição.

- **contador** é usado para realizar uma determinada contagem na repetição;
- **acumulador** é usado para realizar uma operação onde os valores se acumulam ao longo das repetições;

```python
# declarando as variáveis antes do loop while
contador = 0  # via de regra se inicia em 0, mas não é obrigatório
acumulador = 0  # aqui, terá o comportamento de somar a cada repetição
controlador = 10  # usada para controlar a quando a condição no while será falsa

while controlador < 43:
    # mostra cada valor em cada repetição
    print(f'{contador = }')
    print(f'{acumulador = }')
    print(f'{controlador = }\n')

    // incrementa o acumulador com o valor do contador
    acumulador = acumulador + controlador

    // incrementa o controlador
    controlador = controlador + 3

    // aumenta o contador em 1
    contador = contador + 1

print(f'o while repetiu {contador}x')
print(f'o acumulador somou {acumulador}.')
```

## iterando sobre uma lista

Há diversas formas de se iterar (passar por cada element) sobre uma lista.

Quando se usa o loop `while`, é preciso manualmente definir uma variável de controle de suas repetições. Se é preciso que ele passe por uma lista de 4 palavras (como no exemplo abaixo), então é comum usar uma variável de índice (chamada de `indice` ou apenas `i`) para que, ao mesmo tempo que é usada como condição de parada do `while`, é usada para passar por todos os elementos da lista.

Quando se usa o loop `for`, ele precisa que uma variável seja especificada. Essa variável irá, a cada repetição, receber um valor da lista. Sempre o seguinte. Ele faz isso automaticamente a cada repetição. Dessa forma, torna-se desnecessário criar uma variável de controle, pois o `for` controla quando o final do iterável é atingido.

Entende-se por iterável no Python qualquer tipo de variável onde seja possível passar por seus subelementos individualmente.

```python
lista_palavras = ['uma', 'dois', 'tres', 'quatro']

print('for loop')
for uma_palavra in lista_palavras:
    print(f'{uma_palavra = }')

print('\nwhile loop')
i = 0
while i < len(lista_palavras):
    uma_palavra = lista_palavras[i]
    print(f'{uma_palavra = }')
    i = i + 1
```

Eventualmente, pode ser necessário que o loop seja repetido infinitamente. Então, pode-se usar um `True` na sua condição, mas é necessário que seja criada uma forma de interromper a repetição. No exemplo abaixo, enquando a resposta não for igual a `sim`, a repetição irá acontecer indefinidamente.

```python
sair = False
while not sair:
    resposta = input('quer sair ?')
    if resposta == 'sim':
        sair = True
```

## formas de mostrar o valor das variáveis

Existem várias formas de mostrar o valor de uma variável.
No exemplo abaixo, as formas 1 e 2 são as mais antigas.
- a forma 1, apesar de funcionar perfeitamente, ela não permite muita formatação na hora de exibir o valor de suas variáveis, além de deixar a leitura do código mais complicada, por conta de todas as vírgulas e aspas necessárias entre as strings e variáveis.
- a forma 2, apesar de ainda funcionar, não é mais usada.
- a forma 3 já permite uma maior flexibilidade na hora de exibir os valores das variáveis.
- a forma 4 é a mais moderna de todas. Ela permite uma leitura muito mais fluída do código, além de facilitar saber que variável está indo aonde.

```python
v1 = 10
v2 = 12
v3 = 15

print('v1 =',v1,'\nv2 =',v2,'\nv3 =',v3)  # forma 1
print()
print('v1 = %d\nv2 = %d\nv3 = %d' % (v1,v2,v3))  # forma 2
print()
print('v1 = {}\nv2 = {}\nv3 = {}'.format(v1,v2,v3))  # forma 3
print()
print(f'v1 = {v1}\nv2 = {v2}\nv3 = {v3}')  # forma 4
```

## índices nas strings

As strings nada mais são que agrupamentos de letras (caracteres). Então, é possível iterar sobre elas de modo a obter seus caracteres individualmente.

```python
# posicoes na string
#            01234567890123
sobrenome = 'Schwarzenegger'
i = 0

while i < len(sobrenome):
    letra = sobrenome[i]

    if i in (9, 10):
        print(f'{letra = }')
    else:
        print('nao sei')

    i = i + 1
```

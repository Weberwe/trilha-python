# revisão


```python
contador = 0
acumulador = 0  # somador
controlador = 10

while controlador < 43:
    print(f'{controlador = }')

    acumulador = acumulador + controlador

    controlador = controlador + 3
    contador = contador + 1


print(f'o while repetiu {contador}x.')
print(f'o acumulador somou {acumulador}.')

```


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

sair = False
while not sair:
    resposta = input('quer sair ?')
    if resposta == 'sim':
        sair = True
```

```python
v1 = 10
v2 = 12
v3 = 15

print('v1 =',v1,'\nv2 =',v2,'\nv3 =',v3)
print()
print('v1 = %d\nv2 = %d\nv3 = %d' % (v1,v2,v3))
print()
print('v1 = {}\nv2 = {}\nv3 = {}'.format(v1,v2,v3))
print()
print(f'v1 = {v1}\nv2 = {v2}\nv3 = {v3}')
```

```python
# posicoes na string
            #01234567890123
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

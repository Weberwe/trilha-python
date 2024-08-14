# 1.
#   um programa que peça um número inteiro positivo e;
#   some todos os valores de zero até o número informado;

valor = int(input('Digite um número inteiro positivo : '))

if valor >= 0:
    print('numero valido')

    somatorio = 0
    contador = 0

    while contador <= valor:
        somatorio = somatorio + contador
        contador = contador + 1
        print(somatorio)

else:
    print('numero invalido')

# 2.
#   um programa que peça dois números inteiros distintos e
#   depois some todos os números no intervalo especificado;

n1 = int(input("Digite um numero : "))
n2 = int(input("Digite outro numero : "))

if n1 != n2:
    print('sao diferentes')
    somatorio = 0
    contador = 0
    if n1 > n2:
        print('n1 eh maior que n2')
        contador = n2
        while contador <= n1:
            somatorio = somatorio + contador
            contador = contador + 1
        print('intervalo de',n1,'e',n2,'somado eh',somatorio)
    else:
        print('n2 eh maior que n1')
        contador = n1
        while contador <= n2:
            somatorio = somatorio + contador
            contador = contador + 1
        print('intervalo de',n1,'e',n2,'somado eh',somatorio)
else:
    print('sao iguais')

# 3.
#   um programa que peça dez números inteiros,
#   depois peça um novo número inteiro
#   e verifique se ele já foi digitado anteriormente;

numeros = []
contador = 0

# pede 10 numeros inteiros
while contador < 10:
    print('digite um',contador + 1,'de 10')
    valor = int(input('>>> '))
    numeros.append(valor)
    contador = contador + 1

novo_valor = int(input('digite um numero para buscar : '))

if novo_valor in numeros:
    print('o numero esta na lista')
else:
    print('o numero nao esta na lista')


# conversao de temperatura

print('''
\tEscolha a conversao de acordo com o numero :
    1. Kelvin -> Celsius
    2. Kelvin -> Fahrenheit
    3. Celsius -> Kelvin
    4. Celsius -> Fahrenheit
    5. Fahrenheit -> Celsius
    6. Fahrenheit -> Kelvin
''')

opcao = input('>>> ')

if opcao == '1':
    print('Kelvin -> Celsius')
    temp_k = float(input('digite a temp : '))
    temp_c = temp_k - 273
    print(temp_k,'kelvin eh ',temp_c,'celsius')

elif opcao == '2':
    print('Kelvin -> Fahrenheit')
    temp_k = float(input('digite a temp : '))
    temp_f = (temp_k - 273) * 1.8 + 32
    print(temp_k,'kelvin eh ',temp_f,'fahrenheit')

elif opcao == '3':
    print('Celsius -> Kelvin')
    temp_c = float(input('digite a temp : '))
    temp_k = temp_c + 273
    print(temp_c,'celsius eh ',temp_k,'kelvin')

elif opcao == '4':
    print('Celsius -> Fahrenheit')
    temp_c = float(input('digite a temp : '))
    temp_f = temp_c * 1.8 + 32
    print(temp_c,'celsius eh ',temp_f,'fahrenheit')

elif opcao == '5':
    print('Fahrenheit -> Celsius')
    temp_f = float(input('digite a temp : '))
    temp_c = (temp_f - 32) / 1.8
    print(temp_f,'fahrenheit eh ',temp_c,'celsius')

elif opcao == '6':
    print('Fahrenheit -> Kelvin')
    temp_f = float(input('digite a temp : '))
    temp_k = (temp_f - 32) * (5/9) + 273
    print(temp_f,'fahrenheit eh ',temp_k,'kelvin')

else:
    print('opcao desconhecida')


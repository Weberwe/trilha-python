# modelo de cálculo do IMC enviado por um aluno para mostrar em aula
X = float (input('Digite sua altura em metros:     '))
Y = float (input('Digite seu peso em kg:       '))
Idade = int (input('Digite sua idade:        '))
Divisão = X/Y/Y
IMC = Divisão
IMC = round(IMC, 2)

print(f'O seu IMC é de   {IMC}   ')

if 60 >= Idade >= 20:
    if 18.5 <= IMC <= 24.9:
        print('Sua classificação é Eutrofia')

    if 17 <= IMC < 18.5:
        print('Sua classificação é Magreza Grau I')

    if 16 <= IMC <= 17:
        print('Sua classificação é Magreza Grau II')

    if IMC < 16:
        print('Sua classificação é Magreza Grau III')

    if 24.9 < IMC <= 29.9:
        print('Sua classificação é Sobrepeso')

    if 29.9 < IMC <= 34.9:
        print('Sua classificação é Obesidade Grau I')

    if 34.9 < IMC <= 39.9:
        print('Sua classificação é Obesidade Grau II')

    if IMC > 39.9:
        print('Sua classificação é Obesidade Grau III')

if Idade > 60:
    if IMC < 23:
        print('Sua classificação é Baixo Peso')

    if 23 <= IMC <= 27.9:
        print('Sua classificação é Eutrofia')

    if 28 < IMC <= 29.9:
        print('Sua classificação é Risco de Obesidade')

    if IMC > 30:
        print('Sua classificação é Obesidade')

if Idade < 20:
    print('Não foi possível classificar seu IMC, o sistema ainda não está \
        adaptado para pessoas com')

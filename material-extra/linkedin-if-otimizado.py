# modelo de cálculo do IMC enviado por um aluno para mostrar em aula
altura = float (input('Digite sua altura em metros:     '))
peso = float (input('Digite seu peso em kg:       '))
idade = int (input('Digite sua idade:        '))

imc = peso / altura ** 2
imc = round(imc, 2)

print(f'O seu IMC é de   {imc}   ')

# idade
# idade entre 20 e 60 anos
# idade > 60
# idade < 20

if idade > 60:
    print('idade maior que 60')
    if imc > 30:
        print('Sua classificação é Obesidade')
    elif imc > 28:
        print('Sua classificação é Risco de Obesidade')
    elif imc >= 23:
        print('Sua classificação é Eutrofia')
    else:
        print('Sua classificação é Baixo Peso')

elif idade < 20:
    print('Não foi possível classificar seu IMC, o sistema ainda não está \
        adaptado para pessoas com')
else:
    if imc < 16:
        print('Sua classificação é Magreza Grau III')
    elif imc <= 17:
        print('Sua classificação é Magreza Grau II')
    elif imc <= 18.5:
        print('Sua classificação é Magreza Grau I')
    elif imc <= 24.9:
        print('Sua classificação é Eutrofia')
    elif imc <= 29.9:
        print('Sua classificação é Sobrepeso')
    elif imc <= 34.9:
        print('Sua classificação é Obesidade Grau I')
    elif imc <= 39.9:
        print('Sua classificação é Obesidade Grau II')
    else:
        print('Sua classificação é Obesidade Grau III')



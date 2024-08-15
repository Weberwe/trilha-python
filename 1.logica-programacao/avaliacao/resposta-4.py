# constantes com os nomes das casas
GRIF = 'Grifinória'
LUFA = 'Lufa-Lufa'
CORV = 'Corvinal'
SONS = 'Sonserina'
CASAS = [GRIF, LUFA, CORV, SONS]

# constantes dos pontos
GOL = 10
POMO_DE_OURO = 150

print('Equipes de Quadribol\n')
print('\t', GRIF)
print('\t', LUFA)
print('\t', CORV)
print('\t', SONS)

casa_1 = ''
casa_2 = ''

# repetição para escolher as equipes
while casa_1 == casa_2:
    casa_1 = input('\nDigite o nome da primeira casa : ')
    casa_2 = input('Digite o nome da segunda casa : ')

    if casa_1 not in CASAS or casa_2 not in CASAS:
        print('Digite o nome da casa corretamente!')
    else:
        if casa_1 == casa_2:
            print('Escolha duas casas diferentes')

fim_partida = False
pontuacao = []

# repetição da partida
while not fim_partida:
    print('\nCasa 1 -', casa_1)
    print('Casa 2 -', casa_2)
    pont_casa = input('Que casa pontuou (1 ou 2) : ')

    if pont_casa not in ('1', '2'):
        print('\n\tcasa errada')
    else:
        ponto = []
        eh_pomo = input('É o Pomo de Ouro (s ou n) : ')
        if eh_pomo == 's':
            ponto.append(pont_casa)
            ponto.append(POMO_DE_OURO)
            fim_partida = True
        else:
            ponto.append(pont_casa)
            ponto.append(GOL)
        pontuacao.append(ponto)

# contabilização dos pontos
i = 0
pont_casa_1 = 0
pont_casa_2 = 0
while i < len(pontuacao):
    lista = pontuacao[i]
    if lista[0] == '1':
        pont_casa_1 = pont_casa_1 + lista[1]
    else:
        pont_casa_2 = pont_casa_2 + lista[1]
    i = i + 1

# mostra a casa vencedora
if pont_casa_1 > pont_casa_2:
    print('\n\nA casa', casa_1, 'venceu com', pont_casa_1, 'pontos.')
    print('A casa', casa_2, 'perdeu com', pont_casa_2, 'pontos.')
else:
    print('\n\nA casa', casa_2, 'venceu com', pont_casa_2, 'pontos.')
    print('A casa', casa_1, 'perdeu com', pont_casa_1, 'pontos.')

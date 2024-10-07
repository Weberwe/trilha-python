"""
modulo para sortear um exercicio

versão : v1.0.0
autor : Guto Hertzog
"""
import os
import random
import sys

DEV = False
if DEV:
    RAIZ = 'material-python'
else:
    RAIZ = 'trilha-python'

PASTA = '2.programacao-python'
TAG_INICIO = '<details>'
TAG_FIM = '</details>'

def limpa_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


if __name__ == '__main__':
    local_atual = os.getcwd()
    print(f'{local_atual = }')

    if os.name == 'nt':
        lista = local_atual.split('\\')
    else:
        lista = local_atual.split('/')

    if lista[-1] != RAIZ:
        print(f'coloque este modulo dentro da pasta {RAIZ}')
        sys.exit(1)

    if PASTA not in os.listdir():
        print(f'certifique-se que a pasta {PASTA} existe')
        sys.exit(1)

    pasta_exercicios = os.path.join(local_atual, PASTA)
    os.chdir(pasta_exercicios)
    arquivos_md = os.listdir()

    while True:
        limpa_tela()
        print('\n\t\tBuscador de Exercicio')
        print('\nDigite Ctrl+C para sair\n')
        arquivo = random.sample(arquivos_md, k=1)

        exercicios = []
        with open(arquivo[0], 'r', encoding='utf-8') as arq:
            achou = False
            for linha in arq.readlines():
                linha = linha.strip()
                if linha == TAG_INICIO:
                    achou = True
                    continue
                if linha == TAG_FIM:
                    achou = False
                    continue

                if achou:
                    if '1. ' not in linha:
                        continue
                    if '1. EXERCÍCIOS' in linha.upper():
                        continue
                    if '1. NÍVEL' in linha.upper():
                        continue
                    linha = linha.replace('`','')
                    linha = linha.replace('*','')
                    exercicios.append(linha)


        if not exercicios:
            continue
        escolha = random.sample(exercicios, k=1)
        print(escolha[0])
        try:
            input('\ndigite Enter para outro exercicio')
        except KeyboardInterrupt:
            limpa_tela()
            print('\n\t\tate a proxima')
            sys.exit(0)

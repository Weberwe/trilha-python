# Ele gostaria que criem um algoritmo para calcular a média de um aluno de alguma disciplina da escola.

# As notas são passadas usando letras, mas cada uma tem uma pontuação específica, conforme a tabela abaixo :

# | nota | valor numérico || nota | valor numérico || nota | valor numérico |
# | A+ | 10.0 || A | 9.7 || A- | 9.3 |
# | B+ | 8.9 || B | 8.4 || B- | 7.9 |
# | C+ | 7.4 || C | 6.9 || C- | 6.4 |
# | D+ | 5.9 || D | 3.9 || D- | 2.0 |
# | F  | 0.0 |

# Ele quer que vocês criem um programa que peça o nome do aluno, sua casa, uma disciplina da lista (Transfiguração, Herbologia, Poções, Astronomia, Defesa Contra as Artes das Trevas e Trato das Criaturas Mágicas) e 5 notas do aluno (A, B-, etc). Depois, calcule sua média.

# Se a média for maior ou igual 9.5, exiba a mensagem "Nível Auror". Se a média for menor que 9.5 e maior que 8.4, exiba a mensagem "Ótimo". Média menor que 8.5 e maior que 7.4, "Excede Expectativas". Média menor que 7.4 e maior que 5.9, "Aceitável". Média menor que 6.0 e e maior que 3.9, "Péssimo (Recuperação)". Média menor que 4.0 e maior que 1.9, "Deplorável". Média menor que 2.0, "Trasgo".

# Por fim, exiba o nome do aluno, a sua casa, a disciplina, sua lista de suas notas, a média atingida e a respectiva mensagem.
GRIF = 'Grifinória'
LUFA = 'Lufa-Lufa'
CORV = 'Corvinal'
SONS = 'Sonserina'
CASAS = [GRIF, LUFA, CORV, SONS]

TRAN = 'Transfiguração'
HERB = 'Herbologia'
POCO = 'Poções'
ASTR = 'Astronomia'
DCAT = 'Defesa Contra as Artes das Trevas'
TRCM = 'Trato das Criaturas Mágicas'
DISCIPLINAS = [TRAN, HERB, POCO, ASTR, DCAT, TRCM]

QTD_NOTAS = 5

NOTAS = [
    ['A+', 10.0], ['A', 9.7], ['A-', 9.3],
    ['B+', 8.9], ['B', 8.4], ['B-', 7.9],
    ['C+', 7.4], ['C', 6.9], ['C-', 6.4],
    ['D+', 5.9], ['D', 3.9], ['D-', 2.0],
    ['F', 0.0]
]

print(CASAS)
print(DISCIPLINAS)
print(NOTAS)

# Ela possui uma Mandrágora que tem 0.50m e cresce 2cm por ano e um Visgo do Diabo que tem 0.10m e cresce 3cm por ano. Ela gostaria que vocês construissem um algoritmo que calculasse e mostrasse quantos anos serão necessários para que o Visgo do Diabo seja maior que a Mandrágora.

mandragora = 0.5
visgo_diabo = 0.1

tx_cres_mad = 0.02
tx_cres_vis = 0.03

ano = 1

while visgo_diabo <= mandragora:
    print('Ano :', ano)
    print('Mandragora :', round(mandragora,2))
    print('Visgo do Diabo :', round(visgo_diabo,2))

    mandragora = mandragora + tx_cres_mad
    visgo_diabo = visgo_diabo + tx_cres_vis

    ano = ano + 1

print('vai levar',ano,'anos no total')


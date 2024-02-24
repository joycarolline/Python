'''6. Escreva um programa que calcule o tempo de uma viagem.
 Faça um comparativo do mesmo percurso de avião, carro e ônibus.
Levando em consideração:
● avião = 600 km/h
● carro = 100 km/h
● ônibus = 80 km/h'''

print("Descubra o tempo de viagem de avião, carro ou ônibus de um mesmo percurso \n")

km = int(input("Digite a distancia em quilometros: \n"));

tempo_aviao = km/600
tempo_carro = km/100
tempo_onibus = km/80

print(f"O tempo de viagem de avião é: {tempo_aviao:.2f}h, de carro é {tempo_carro:.2f}h e de ônibus é {tempo_onibus:.2f}h")


'''3. Faça um Programa que peça a quantidade de quilômetros, 
transforme em metros, centímetros e milímetros.'''

print("Transforme quilometros em metros, centimetros e milímetros:  \n")

km = int(input("Digite o quilometro: "));

metro = km*1000
centimetro = km*100000
milimetro = km*1000000

print(f"{km} em metros é: {metro}, em centimetros é {centimetro} e em milimetros é {milimetro}")
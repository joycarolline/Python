'''4. Receba do usuário a quantidade de litros de combustível consumidos e a 
distância percorrida. Calcule e imprima o consumo médio em km/l.'''

print("Descubra o consumo médio de combustível:  \n")

litros = int(input("Digite a quantidade de litros: " ));
km = int(input("Digite a distância pecorrida: " ));

consumo = km/litros

print(f"O consumo médio é: {consumo:.2f}km/l")
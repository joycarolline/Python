'''7. Solicite ao usuário o peso em kg e a altura em metros.Calcule e imprima o 
Índice de Massa Corporal (IMC) usando a fórmula: IMC = peso / (altura x altura)'''

print("Descubra seu Indice de Massa Corporal (IMC):  \n")

peso = float(input("Digite o seu peso: "));
altura = float(input("Digite a sua altura: "));

imc = peso/(altura*altura)

print(f"\nO seu Índice de Massa Corporal(IMC) é: {imc:.2f}")
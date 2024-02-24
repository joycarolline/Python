'''8. Faça um Programa que pergunte quanto você ganha por hora e o número de 
horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.'''

print("Descubra quanto você ganhará este mês:  \n")

hora_valor = float(input("Digite o valor da sua hora de trabalho: "));
hora_trabalhada = float(input("Digite a quantidade de horas trabalhadas: "))

total = hora_valor * hora_trabalhada

print(f"\nO total de salario este mês será: {total}")
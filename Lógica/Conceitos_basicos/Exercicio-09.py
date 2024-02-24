'''9. Solicite ao usuário o número de horas de exercício físico por semana.
Calcule o total de calorias queimadas em um mês, considerando uma média de 5 
calorias por minuto de exercício.'''

print("Descubra a quantidade de calorias queimadas em um mês:  \n")

horas_exercicios = int(input("Digite o total de horas de exercicio fisico esta semana: \n"));

minutos = horas_exercicios * 60
calorias_queimadas = minutos * 5
total_mes = calorias_queimadas * 4

print(f"Voce queimou {total_mes} calorias este mês")
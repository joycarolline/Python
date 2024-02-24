'''5. Escreva um programa que calcule o salário líquido. Lembrando de declarar o salário bruto e o percentual de desconto do Imposto de Renda.
● Renda até R$ 1.903,98: isento de imposto de renda;
● Renda entre R$ 1.903,99 e R$ 2.826,65: alíquota de 7,5%;
● Renda entre R$ 2.826,66 e R$ 3.751,05: alíquota de 15%;
● Renda entre R$ 3.751,06 e R$ 4.664,68: alíquota de 22,5%;
● Renda acima de R$ 4.664,68: alíquota máxima de 27,5%.'''

print("Descubra o seu salário líquido:  \n")

salario = int(input("Digite o seu salário bruto: "));

if salario <= 1903.98:
  desconto_IR = 0

elif salario >= 1903.99 and salario <= 2826.65:
  desconto_IR = salario * (7.5 / 100)

elif salario >= 2826.66 and salario <= 3751.05:
  desconto_IR = salario * (20 / 100)

elif salario >= 3751.06 and 4554.68:
  desconto_IR = salario * (22.5 / 100)

else:
  desconto_IR = salario * (27.5 / 100)

salario_liquido = salario - desconto_IR

print(
    f"\n Salário bruto    R${salario:.2f}"
    f"\n Desconto imposto de renda R${desconto_IR:.2f}"
    f"\n Salário líquido  R${salario_liquido:.2f}"
)
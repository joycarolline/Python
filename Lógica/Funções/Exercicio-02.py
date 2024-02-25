'''2. Reverso do número. Faça uma função que retorne o reverso de um número 
inteiro informado. Por exemplo: 127 -> 721.'''

def reverso():
    num_reverso = num[::-1]
    return (num_reverso)

print(reverso(int(input('Digite o numero pra ver seu reverso: '))))
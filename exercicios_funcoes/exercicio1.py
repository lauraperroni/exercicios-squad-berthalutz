'''
Faça um programa, com uma função que necessite de três
argumentos, e que forneça a soma desses três argumentos.

Responsável: Mariana Choratto
'''

numero1 = int(input("Vamos digitar 3 numeros. \n Digite o primeiro número: "))
numero2 = int(input(" Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

def soma(numero1, numero2, numero3):
    calculo = numero1 + numero2 + numero3
    return calculo

resultado = soma(numero1, numero2, numero3)
print(f'O resultado da soma é {resultado}.')

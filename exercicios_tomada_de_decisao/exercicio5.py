'''
Desenvolva um programa que solicite ao usuário os comprimentos dos três
lados de um triângulo e classifique-o como equilátero, isósceles ou escaleno.
equilátero: todos os lados com o mesmo valor
isósceles: dois lados com o mesmo valor
escaleno: todos os lados com medidas distintas.

Responsável: Raissa Carneiro Castro
'''
lado_1 = int(input("Digite o primeiro lado do triângulo:"))
lado_2 = int(input("Digite o segundo lado do triângulo:"))
lado_3 = int(input("Digite o terceiro lado do triângulo:"))

if lado_1 == lado_2 and lado_2 == lado_3:
    print("O triângulo é equilátero.")
elif lado_1 == lado_2 or lado_2 == lado_3 or lado_1 == lado_3:
    print("O triângulo é isósceles.") 
else:
    print("O triângulo é escaleno")

    

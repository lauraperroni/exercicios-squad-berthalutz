'''
  Criar um programa em Python que solicite três números ao usuário, utilize
estruturas condicionais para determinar o maior entre eles e apresente o
resultado

Responsável: Claudia Azambuja
'''


umeros = [float(input(f"Digite o {i+1}º número: ")) for i in range(3)]

maior_numero = numeros[0]
for numero in numeros[1:]:
    if numero > maior_numero:
        maior_numero = numero

print(f"O maior número entre os digitados é: {maior_numero}")
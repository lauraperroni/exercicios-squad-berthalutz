'''
Faça um programa que lê três números inteiros e os mostra em ordem
crescente.

Responsável: Erika Alves Malaquias Silva
'''
n1 = int(input("Insira o primerio número:"))
n2 = int(input("insira o segundo número: "))
n3 = int(input("insira o terceiro número: "))

listaNum = [n1, n2, n3]


listaNum.sort()
print("Números em ordem crescente:", listaNum[0], listaNum[1], listaNum[2])      


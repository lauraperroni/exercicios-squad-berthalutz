'''
Faça um Programa que peça a quantidade de quilômetros, transforme
em metros, centímetros e milímetros.

Responsável: Elizabeth
'''
nroKM = float(input('Digite um valor em km: '))

nroM = nroKM * 1000
nroCM = nroKM * 100000
nroMM = nroKM * 1000000

print('Transformação de Km para m, cm e mm')
print(f'km: {nroKM}')
print(f'm: {nroM}')
print(f'cm: {nroCM}')
print(f'mm: {nroMM}')
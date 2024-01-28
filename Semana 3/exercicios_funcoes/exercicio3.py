'''
Escreva um script que pergunta ao usuário se ele deseja converter
uma temperatura de grau Celsius para Fahrenheit ou vice-versa. Para
cada opção, crie uma função

Plus: Crie uma terceira, que é um menu para o usuário escolher a opção
desejada, onde esse menu chama a função de conversão correta.

Responsável: Laura Perroni Quadros da Silva
'''

grau = input('Você quer converter Fahrenheit para Celsius (FC) ou Celsius para Fahrenheit (CF)?')

def converterCF(temp1) :
    temp2 = (temp1 * (9/5) + 32)
    print(f'{temp1:.1f}ºC = {temp2:.1f}ºF')

def converterFC(temp1) :
    temp2 = (temp1 - 32) * 5/9 
    print(f'{temp1:.1f}ºF = {temp2:.1f}ºC')

if grau == 'cf' :
    temp1 = float(input('Digite a temperatura em Celsius: '))
    converterCF(temp1)
elif grau =='fc' :
    temp1 = float(input('Digite a temperatura em Fahrenheit: '))
    converterFC(temp1)
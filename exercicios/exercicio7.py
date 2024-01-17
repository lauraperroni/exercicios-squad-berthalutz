'''
Solicite ao usuário o peso em kg e a altura em metros. Calcule e
imprima o Índice de Massa Corporal (IMC) usando a fórmula:
IMC = peso / (altura x altura).

Responsável: Laura Perroni Quadros da Silva
'''


print('=========== CALCULADORA DE IMC ===========')

peso = float(input('Digite seu peso (em kg): '))
altura = float(input('Digite sua altura (em metros): '))
IMC = peso / (altura*altura)

print(f'Seu IMC é {IMC:.2f}')

if IMC <= 16.9 :
    print('Você está muito abaixo do peso!')
elif IMC > 16.9 and IMC < 18.4 : 
    print('Você está abaixo do peso!')
elif IMC > 18.5 and IMC < 24.9 : 
    print('Você Tem um peso normal.')
elif IMC > 25.0 and IMC < 29.9 : 
    print('Você está acima do peso!')
elif IMC > 30.0 and IMC < 34.9 : 
    print('Você tem obesidade de grau I!')
elif IMC > 35.0 and IMC < 40.0 : 
    print('Você tem obesidade de grau II!')
elif IMC > 40.0 : 
    print('Você tem obesidade de grau III!')

print('=========================================')
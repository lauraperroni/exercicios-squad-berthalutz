'''
 Faça um programa que peça uma nota, entre zero e dez. Mostre uma
mensagem caso o valor seja inválido e continue pedindo até que o usuário
informe um valor válido.

Responsável: Elizabeth
'''
nota=float(input('Digite uma nota de 0 a 10: '))
while nota < 0 or nota > 10:
    print('Nota inválida, nota precisa ser entre 0 e 10')
    nota=float(input('Digite uma nota de 0 a 10: '))
print(f'A nota é {nota}')
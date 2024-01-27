'''
Implemente um programa que classifique um aluno com base em sua
pontuação em um exame. O programa deverá solicitar uma nota de 0 a 10. Se
a pontuação for maior ou igual a 7, o aluno é aprovado; caso contrário, é
reprovado.

Responsável: Gabriela Sampaio da Silva
'''

print('Programa de classificação de notas.')
print('\n')

nota = float(input('Digite uma nova entre 0 e 10: '))

if nota >= 7:
    print('Parabéns, você foi aprovado!')
elif nota < 7:
    print('Dessa vez você foi reprovado.')
'''
Solicite ao usuário o número de horas de exercício físico por semana.
Calcule o total de calorias queimadas em um mês, considerando uma
média de 5 calorias por minuto de exercício.

Responsável: Erika Alves Malaquias Silva
'''


horasSem = int(input("Quantas horas de exercicio físico você faz por semana?"))
calHora = 300
calSem = calHora * horasSem
calMes = calSem * 4
print(f"Você gasta {calMes} calorias por mês!")


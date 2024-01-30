'''
Faça um Programa que pergunte quanto você ganha por hora e o
número de horas trabalhadas no mês.Calcule e mostre o total do seu
salário no referido mês.

Responsável: Claudia Azambuja
'''
salario_hora = float(input("Quanto você ganha por hora? R$ "))
horas_trabalhadas = float(input("Quantas horas você trabalhou no mês? "))

salario_total = salario_hora * horas_trabalhadas

# Exibe o resultado
print(f"Seu salário no referido mês é: R$ {salario_total:.2f}")
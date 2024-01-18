'''Utilizando listas faça um programa que faça 5 perguntas para uma
pessoa sobre um crime.
As perguntas são:
""Telefonou para a vítima?""
""Esteve no local do crime?""
""Mora perto da vítima?""
""Devia para a vítima?""
""Já trabalhou com a vítima?""

O programa deve no final emitir uma classificação sobre a participação
da pessoa no crime.

Se a pessoa responder positivamente a 2 questões ela deve ser
classificada como ""Suspeita"", entre 3 e 4 como ""Cúmplice"" e 5 como
""Assassino"".
Caso contrário,ele será classificado como""Inocente""

Responsável: Laura Perroni Quadros da Silva
'''

calc = 0
lista = ['Telefonou para a vítima?', 'Esteve no local do crime?', 'Mora perto da vítima?', 'Devia para a vítima?', 'Já trabalhou com a vítima?']

print('Bem vinda ao nosso interrogatório sobre o assassinato do Sr. Fulaninho. Me responda com Y/N, vamos lá...')

for q in lista :
    q5 = input(f'{q}')
    if q5 == 'Y':
        calc += 1
    print(calc)

if calc < 2 :
    print('Inocente')
elif calc >= 2 and calc < 3 :
        print('Suspeita')
elif calc >= 3 and calc < 4 :
        print('Cúmplice')
elif calc >= 5 :
        print('Assassina')
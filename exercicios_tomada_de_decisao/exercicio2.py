'''
 Faça um Programa que pergunte em que turno você estuda. Peça para
digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom
Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

Responsável: Mariana Choratto
'''
resposta = input('Em que turno você estuda? \n Digite M para Matutino. \n Digite V para vespertino. \n Ou N para noturno.').upper()


if resposta == "M": 
    print("Bom dia!")
elif resposta == "V":
    print('Boa Tarde!')
else:
    print('Boa noite!')
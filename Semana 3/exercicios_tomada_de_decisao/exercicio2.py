'''
Faça um Programa que pergunte em que turno você estuda. Peça para
digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom
Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

Responsável = Adriana
'''

while True:
    print("Informe o turno que você estuda:")
    print("M - matutino")
    print("V - vespertino")
    print("N - noturno")

    turno = input("Digite a opção: ")

    if turno.upper() == 'M':
        print("Bom Dia!")
    elif turno.upper() == 'V':
        print("Boa Tarde!")
    elif turno.upper() == 'N':
        print("Boa Noite!")
    else:
        print("Valor Inválido!")

    continuar = input("Deseja informar outro turno? (s/n): ")

    if continuar.lower() != 's':
        print("Até logo!")
        break

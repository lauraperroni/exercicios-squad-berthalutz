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
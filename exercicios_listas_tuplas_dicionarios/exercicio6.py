'''
 Faça um programa que permita ao usuário digitar o seu nome e
em seguida mostre o nome do usuário de trás para frente
utilizando somente letras maiúsculas. Dica: lembre−se que ao
informar o nome o usuário pode digitar letras maiúsculas ou
minúsculas.

Responsável: Leidejane
'''


def inverter_nome(nome):
    nome_invertido = nome[::-1].upper()
    return nome_invertido


# Solicitação do nome ao usuário
nome_usuario = input("Digite o seu nome: ")

# Inverte e converte para letras maiúsculas
nome_invertido = inverter_nome(nome_usuario)

# Mostra o nome invertido
print(f"Seu nome de trás para frente: {nome_invertido}")

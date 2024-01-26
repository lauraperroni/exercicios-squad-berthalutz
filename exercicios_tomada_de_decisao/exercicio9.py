'''
O programa deve calcular e apresentar a quantidade de números pares e
ímpares inseridos. O processo de leitura deve ser encerrado quando o usuário
informar o valor zero. Certifique-se de incluir validações para garantir que
apenas números positivos sejam considerados na contagem e cálculos.

Responsável: Laura Perroni Quadros da Silva
'''

numero = int(input('Digite um número: '))
pares = 0
impares = 0

if numero == 0 :
    while numero == 0 :
        print('Você precisa digitar um número inteiro maior que zero para começar a contagem')
        numero = int(input('Digite um número: '))

while numero != 0 :
    if numero % 2 == 0 :
        print('É um número par')
        pares += 1
    else :
        print('É um número ímpar')
        impares += 1
    numero = int(input('Digite um número: '))
print(f'Pares = {pares}, Ímpares = {impares}')
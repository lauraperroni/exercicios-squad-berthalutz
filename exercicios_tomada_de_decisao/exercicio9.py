'''
O programa deve calcular e apresentar a quantidade de números pares e
ímpares inseridos. O processo de leitura deve ser encerrado quando o usuário
informar o valor zero. Certifique-se de incluir validações para garantir que
apenas números positivos sejam considerados na contagem e cálculos.

Responsável: Laura Perroni Quadros da Silva
'''

numero = int(input('Digite um número: '))

if numero < 0 :
    print('Este número não é positivo.')
else:    
    while numero != 0 :
    
        if numero % 2 == 0 :
            print('É um número par')
        else :
            print('É um número ímpar')
        numero = int(input('Digite um número: '))

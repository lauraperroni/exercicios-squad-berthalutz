'''
 Reverso do número. Faça uma função que retorne o reverso de um
número inteiro informado. Por exemplo: 127 -> 721.

Responsável: Claudia
'''

# M A D
# % + //

num = int(input('Digite um número: '))
rev = 0                                 # o número reverso
temp = num                              # variável temporária para usar nosso número inicial, sem alterá-lo

def reverter(num, rev, temp) :                   # função para reverter o número 
    while temp != 0 : #                          # enquanto nosso número não for zero
        ultimo_num = temp % 10                   # o último dígito é o resto do número dividido por 10 
        rev = rev * 10 + ultimo_num      # o número reverso é ele mesmo * 10 + o último número
        temp = temp // 10                        # o número temporário é dividido por 10   
    print(f'O número ao contrário é: {rev}')    


reverter(num, rev, temp)
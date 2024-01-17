'''
 Vamos construir um jogo de forca. O programa escolherá
aleatoriamente uma palavra secreta de uma lista predefinida. 

A palavra secreta será representada por espaços em branco, um para cada letra
da palavra. 

O jogador terá um número limitado de 6 tentativas. Em cada
tentativa, o jogador pode fornecer uma letra. 

Se a letra estiver presente na palavra secreta, ela será revelada nas posições correspondentes. Se
a letra não estiver na palavra, uma mensagem de erro deverá ser
informada. 

Após um número máximo de erros, o jogador perde. O jogo
continua até que o jogador adivinhe a palavra ou exceda o número
máximo de tentativas.

Dica: Você precisará importar uma biblioteca para resolver esse
exercício

Responsável: Laura Perroni Quadros da Silva
'''

palavra_secreta = "laurinha"
chutadas = []
tentativas = 6
ganhou = False

#--------------------------------------------------------------------------------------------------------

while True:                                # rodar infinitamente até chegar no fim (break)

                                          # aqui imprimimos os tracinhos e letras da palavra caso forem acertadas
    for letra in palavra_secreta :        # para cada letra da palavra secreta             
        if letra.lower() in chutadas :    # se a letra foi chutada,
            print(letra, end=' ')         # imprima a letra
        else:                             # se não, imprima um tracinho
            print('_', end=' ')

#--------------------------------------------------------------------------------------------------------
            
    print(f'Você tem {tentativas} chutes sobrando')      # imprime a quantidade de chutes que a usuária ainda tem
    chute = input('Digite uma letra: ')                  # pedimos uma letra para a usuária
    chutadas.append(chute.lower())                       # adicionamos essa letra à lista de chutes feitos

                                                           
    if chute.lower() not in palavra_secreta.lower():        # se o chute não estiver na palavra secreta
        tentativas -= 1                                     # a usuária perde uma tentativa

                                                # Aqui verificamos tem alguma letra que ainda não foi acertada:  
    ganhou = True                               # transformamos o ganhou em true
    for letra in palavra_secreta:               # para cada letra da palavra secreta
        if letra.lower() not in chutadas:       # se qualquer letra da palavra secreta não estiver entre os chutes da usuária
            ganhou = False                      # ela não ganhou ainda, então ganhou volta a ser False pra continuar o jogo

    if tentativas == 0 or ganhou :              # Se ela esgotou as tentativas ou ganhou(se o ganhou for True): o jogo acaba
        break
                                                # Se o ganhou não for true, mas ela ainda tiver tentativas, voltamos pro inicio do while!
#--------------------------------------------------------------------------------------------------------
    
if ganhou:                                      # aqui imprimimos o resultado final do jogo
    print('Você ganhou!!')
else: 
    print('Você perdeu!!') 
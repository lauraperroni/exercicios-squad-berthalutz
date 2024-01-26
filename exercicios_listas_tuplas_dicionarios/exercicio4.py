'''
 Crie um dicionário representando contatos (nome, telefone).
Permita ao usuário procurar por um contato pelo nome.

Responsável: Carme
'''
lista = []

while True:
    print('1) Adicionar Contato')
    print('2) Remover Contato')
    print('3) Exibira agenda')
    print('0) Sair')
    menu = int(input("Digite uma opção de [0-3]: "))

    if menu == 0:
        break

        #adiciona contato
    elif menu == 1:
        nome = input('Digite o nome do contato: ')
        telefone = input('Digite o telefone do contato: ')
        contato = {'nome':nome, 'telefone':telefone} #variável que representa o dicionário
        lista.append(contato)  #adiciona o contato na lista
        print(f'{nome} foi adicionado.')
        

        #Remove contato
    elif menu == 2:
        nome = input('Digite o nome do contato que deseja remover: ')
        
        contato_encontrado = False
        for contato in lista:
            if contato['nome'] == nome:
                lista.remove(contato)
                print(f'{nome} foi removido.')
                contato_encontrado = True
                break

        if contato_encontrado == False:
            print(f'{nome} não foi encontrado')

    elif menu == 3:
        print('\nLista de contatos: ')
        for contato in lista:
             print(f'Nome: {contato["nome"]}')
             print(f'Telefone: {contato["telefone"]}')
    
    else:
         print('Opção inválida')

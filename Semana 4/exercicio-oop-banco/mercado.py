# import sqlite3 
from datetime import datetime

from classes import Cliente, Produto, cursor, conexao


# CLASSE MERCADO 

class Mercado:
    while True:
        #Início do programa
        print('Bem vindo ao mercado Dev!')

        #Parte 1: Você é cliente? Se não, seu cadastro será adicionado na tabela clientes 
        doesClienteExiste = input('Você já é cliente? Digite S ou N:  ').upper()
        if doesClienteExiste == 'S':
            nome_cliente = input('Digite seu nome:    ').lower()
            dados = cursor.execute(f'SELECT * FROM clientes WHERE nome="{nome_cliente}" ')
            cliente_fetch = dados.fetchone() ## retorna uma tupla
            if cliente_fetch == None:
                print('Error: Esse nome não existe no banco de dados. Se cadastre agora:')
                doesClienteExiste ='N'
            else:
                print(cliente_fetch) 
                # print(cliente_fetch[2])
                cliente_atual = Cliente(cliente_fetch[0], cliente_fetch[1], cliente_fetch[2], cliente_fetch[3])
                print(cliente_atual)

        if doesClienteExiste == 'N':
            # id_cliente = int(input('Digite o ID do cliente: '))
            nome_cliente = input('Digite o nome do cliente:   ')
            telefone_cliente = int(input('Digite o telefone do cliente:   '))
            endereco_cliente = input('Digite o endereço do cliente:   ')
            cursor.execute(f'INSERT INTO clientes(nome, endereco, telefone) VALUES("{nome_cliente}","{endereco_cliente}", "{telefone_cliente}" );')
            print(f"Cliente cadastrado: Nome: {nome_cliente}, telefone: {telefone_cliente} endereço:{endereco_cliente}")
            print("Parabéns, você foi cadastrado!")

        #Parte 2:Compra do Produto
            #Ao final do código, o produto comprado diminuirá o estoque e a compra será anexada à tabela registros
        escolha_produto = int(input(f'Qual produto você quer comprar? Digite o número: \n 1-Notebook A300 Android, \n 2-MacBook Apple, \n 3-Smart TV 32 Samsung \n 4-Smart TV 40 Philco Android TV \n 5-Samsung Galaxy A14 \n 6-Smartphone Xiaomi Redmi 12 \n 7-Tablet Lenovo Tab M9 \n 8-Tablet Samsung Galaxy Tab S6 \n' ))
        dados = cursor.execute(f'SELECT * FROM produtos WHERE id={escolha_produto}')
        produtos_fetch = dados.fetchone()
        produto_comprado = Produto(produtos_fetch[0], produtos_fetch[1], produtos_fetch[2], produtos_fetch[3], produtos_fetch[4])
        print(produto_comprado)

        #variável necessária para adicionar o valor na tabela registro
        produto_nome = produtos_fetch[1]
        # uso da função datetime para registrar a compra
        data_hoje = data_hoje = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        #Chamda da função para diminuir o estoque
        diminuir_estoque = int(input("Você quer comprar quantas unidades deste produto?  "))
        produto_comprado.diminuirEstoque(diminuir_estoque)
        dados = cursor.execute(f'INSERT INTO registros(cliente, data_da_compra, nome_produto, quantidade) VALUES("{nome_cliente}", "{data_hoje}", "{produto_nome}", "{diminuir_estoque}")')

        #Looping do código
        fim= input('Você quer comprar mais algum produto? Digite S para sim e N para não    ').upper()

        if fim == 'N':
            break

    conexao.commit()
    conexao.close()
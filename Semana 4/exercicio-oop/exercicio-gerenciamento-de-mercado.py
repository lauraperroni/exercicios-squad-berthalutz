'''
GERENCIAMENTO DE MERCADO

Vamos criar um sistema orientado a objetos para representar um
sistema de mercado seguindo os requisitos fornecidos:

1. Cada produto pode ter um ou mais fornecedores.

2. O mercado controla apenas o nome, o telefone e o endereço de
cada cliente.

3. Cada produto tem um nome, uma lista de categorias às quais
pertence e uma quantidade disponível em estoque.

4. Quando um produto é comprado, sua quantidade disponível em
estoque é reduzida.

5. O mercado mantém um registro de todas as transações
realizadas, incluindo detalhes como data da compra, cliente
envolvido e quantidade de produtos comprados.

Responsáveis: 

'''
# ---------------------------------------------------------------------

# Criando a classe Cliente
class Cliente:
    #Construtor da classe cliente
    def __init__(self, nome_cliente, id_cliente, telefone_cliente, endereco_cliente):
        self.nome_cliente = nome_cliente
        self.id_cliente = id_cliente
        self.telefone_cliente = telefone_cliente
        self.endereco_cliente = endereco_cliente

    # Criando Getters e Setters 
        
    # Nome -------------------------------------------
    def nome_clienteGet(self):
        return self.nome_cliente

    def nome_clienteSet(self, nome_cliente):
        self.nome_cliente = nome_cliente

    # ID ----------------------------------------------
    def id_clienteGet(self):
        return self.nome_cliente

    def id_clienteSet(self, id_cliente):
        self.id_cliente = id_cliente

    # Telefone ----------------------------------------
    def telefone_clienteGet(self):
        return self.telefone_cliente

    def telefone_clienteGet(self, telefone_cliente):
        self.telefone_cliente = telefone_cliente

    # Endereço ----------------------------------------
    def endereco_clienteGet(self):
        return self.endereco_cliente

    def endereco_clienteSet(self, endereco_cliente):
        self.endereco_cliente = endereco_cliente    

    # Criando a função STR
    def __str__(self):
        return f'Cliente {nome_cliente}, de ID {id_cliente}, telefone {telefone_cliente} e endereço {endereco_cliente}'

# ---------------------------------------------------------------------
        

# Criando a classe Produto
class Produto:
    # Fazendo Construtor
    def __init__(self, nome_produto, categorias, qnt_disponivel):
        self.nome_produto = nome_produto,
        self.categorias = categorias
        self.qnt_disponivel = qnt_disponivel

    # Fazendo função de diminuir o estoque
    def _DiminuirEstoque_(self, quantidade_diminuida):
        self.qnt_disponivel = self.qnt_disponivel - quantidade_diminuida

    # Criando Getters e Setters do Produto
        
    # Nome -------------------------------------------
    def nome_produtoGet(self):
        return self.nome_produto

    def nome_produtoSet(self, nome_produto):
        self.nome_produto = nome_produto

    # Categorias ----------------------------------------------
    def categoriasGet(self):
        return self.categorias

    def categoriasSet(self, categorias):
        self.categorias = categorias

    # Quantidade Disponível ----------------------------------------
    def qnt_disponivelGet(self):
        return self.qnt_disponivel

    def qnt_disponivelGet(self, qnt_disponivel):
        self.qnt_disponivel = qnt_disponivel
    

# ---------------------------------------------------------------------


# Criando a classe Fornecedor
class Fornecedor:
    # Fazendo o Contrutor
    def __init__(self, nome_fornecedor, endereco_fornecedor, telefone_fornecedor):
        self.nome_fornecedor = nome_fornecedor
        self.endereco_fornecedor = endereco_fornecedor
        self.telefone_fornecedor = telefone_fornecedor


    # Criando Getters e Setters do Fornecedor

    # Nome --------------------------------------------
    def nome_fornecedorGet(self):
        return self.nome_fornecedor

    def nome_fornecedorSet(self, nome_fornecedor):
        self.nome_fornecedor = nome_fornecedor

    # Endereço ----------------------------------------
    def endereco_fornecedorGet(self):
        return self.endereco_fornecedor

    def endereco_fornecedorSet(self, endereco_fornecedor):
        self.endereco_fornecedor = endereco_fornecedor

    # Telefone ----------------------------------------
    def telefone_fornecedorGet(self):
        return self.telefone_fornecedor

    def telefone_fornecedorGet(self, telefone_fornecedor):
        self.telefone_fornecedor = telefone_fornecedor

# ---------------------------------------------------------------------


print('Bem vindo ao mercado!')
clientes = []
nome_cliente = input('Digite o nome do cliente:   ')
telefone_cliente = int(input('Digite o telefone do cliente:   '))
endereco_cliente = input('Digite o endereço do cliente:   ')
id_cliente = int(input('Digite o ID do cliente: '))
clientes.append(Cliente(nome_cliente, telefone_cliente, endereco_cliente, id_cliente))


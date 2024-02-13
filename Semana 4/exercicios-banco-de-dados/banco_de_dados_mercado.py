'''
Responsáveis: 

Esse exercício está dividido em 4 partes.
'''

'''
1. Criação das Tabelas:
- Utilizando SQL, crie as tabelas necessárias para armazenar as
informações do sistema. Defina as chaves primárias e
estrangeiras conforme apropriado.

'''
import sqlite3 

conexao = sqlite3.connect('mercado')
cursor = conexao.cursor()

# CRIANDO A TABELA CLIENTES:
# cursor.execute("CREATE TABLE clientes ( id INTEGER PRIMARY KEY AUTOINCREMENT, nome varchar(30) UNIQUE, endereco varchar(50), telefone INT );")

# CRIANDO A TABELA DE FORNECEDORES
# cursor.execute("CREATE TABLE fornecedores ( id INTEGER PRIMARY KEY AUTOINCREMENT, nome varchar(30), endereco varchar(20), telefone integer);")

#CRIANDO A TABELA PRODUTOS 
# cursor.execute("CREATE TABLE produtos ( id INTEGER PRIMARY KEY AUTOINCREMENT, nome_do_produto varchar(30), categoria varchar(20), quantidade int, id_fornecedor integer, FOREIGN KEY (id_fornecedor) REFERENCES fornecedores(id) );")

#CRIANDO TABELA REGISTROS 
# cursor.execute('CREATE TABLE registros ( id INTEGER PRIMARY KEY AUTOINCREMENT, cliente TEXT, data_da_compra DATE, nome_produto INTEGER, quantidade INTEGER, FOREIGN KEY (cliente) REFERENCES clientes(nome), FOREIGN KEY (id_produto) REFERENCES produtos(id));')

'''
2. Inserção de Dados:
- Insira dados de exemplo nas tabelas para simular um ambiente de
venda de eletrônicos. Certifique-se de incluir uma variedade de
produtos e clientes
'''
#INSERINDO PRODUTOS NA TABELA 
# cursor.execute('INSERT INTO produtos(nome_do_produto, categoria, quantidade, id_fornecedor) VALUES("Notebook A300 Android", "Notebooks", 100, 1 )')
# cursor.execute('INSERT INTO produtos(nome_do_produto, categoria, quantidade, id_fornecedor) VALUES("MacBook Apple", "Notebooks", 100, 1 )')
# cursor.execute('INSERT INTO produtos(nome_do_produto, categoria, quantidade, id_fornecedor) VALUES("Smart TV 32 Samsung", "Smart TV", 100, 2 )')
# cursor.execute('INSERT INTO produtos(nome_do_produto, categoria, quantidade, id_fornecedor) VALUES(""Smart TV 40 Philco Android TV", "Smart TV", 100, 1 )')
# cursor.execute('INSERT INTO produtos(nome_do_produto, categoria, quantidade, id_fornecedor) VALUES("Samsung Galaxy A14", "Celulares", 100, 2 )')
# cursor.execute('INSERT INTO produtos(nome_do_produto, categoria, quantidade, id_fornecedor) VALUES("Smartphone Xiaomi Redmi 12", "Celulares", 100, 2)')
# cursor.execute('INSERT INTO produtos(nome_do_produto, categoria, quantidade, id_fornecedor) VALUES("Tablet Lenovo Tab M9", "Tablets", 100, 1 )')
# cursor.execute('INSERT INTO produtos(nome_do_produto, categoria, quantidade, id_fornecedor) VALUES("sTablet Samsung Galaxy Tab S6", "Tablets", 100, 2)')

#INSERINDO FORNECEDORES NA TABELA 
# cursor.execute('INSERT INTO fornecedores(nome, endereco, telefone) VALUES("Alfredinho", "rua das bromélias", 12345)')
# cursor.execute('INSERT INTO fornecedores(nome, endereco, telefone) VALUES("Joãozinho", "rua das camélias", 97854)')


'''
3. Consultas SQL:
- Escreva consultas SQL para realizar as seguintes operações:
- Listar todos os produtos em estoque.
- Encontrar as vendas realizadas por um cliente específico.
- Calcular o total de vendas por categoria de produto.
- Identificar os produtos mais vendidos.

'''

#Escreva o codigo aqui

'''
4. Atualizações e Exclusões:
- Escreva consultas SQL para atualizar e excluir registros do banco
de dados, por exemplo, para atualizar a quantidade em estoque
após uma venda ou remover um cliente.
'''

#Escreva o codigo aqui


conexao.commit()
conexao.close()
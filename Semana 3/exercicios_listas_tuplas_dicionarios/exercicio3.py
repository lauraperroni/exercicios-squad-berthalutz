'''
 Crie um dicionário representando um carrinho de compras.
Adicione produtos (chaves) e quantidades (valores) ao carrinho.
Calcule o total do carrinho de compra.

Responsável: Mariana Choratto
'''

lista_de_compras = {
    'arroz': 26,
    'feijao': 12,
    "ovo": 6, 
    "alface": 3, 
    "tomate": 4.5
}

preco_das_compras = lista_de_compras.values()

soma_dos_valores = sum(preco_das_compras)

print(f'O valor das compras foi de: {"{:.2f}".format(soma_dos_valores)}')
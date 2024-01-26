'''
 Crie um programa que leia quanto dinheiro uma pessoa tem na
carteira, e calcule quanto poderia comprar de cada moeda estrangeira.
Considere a tabela de conversão abaixo:
Dólar Americano: R$ 4,91
Peso Argentino: R$ 0,02
Dólar Australiano: R$ 3,18
Dólar Canadense: R$ 3,64
Franco Suiço: R$ 0,42
Euro: R$ 5,36
Libra esterlina: R$ 6,21

Responsável: Carme
'''

# Tabela de conversão de moedas
tabela_conversao = {
    'Dólar Americano': 4.91,
    'Peso Argentino': 0.02,
    'Dólar Australiano': 3.18,
    'Dólar Canadense': 3.64,
    'Franco Suiço': 0.42,
    'Euro': 5.36,
    'Libra esterlina': 6.21
}

# Entrada de dinheiro na carteira
dinheiro_na_carteira = float(input("Digite quanto dinheiro você tem na carteira (em R$): "))

# Calcula e exibe o valor equivalente em cada moeda estrangeira
print("\nValor equivalente em cada moeda estrangeira:")
for moeda, taxa_conversao in tabela_conversao.items():
    valor_em_moeda = dinheiro_na_carteira / taxa_conversao
    print(f"{moeda}: {valor_em_moeda:.2f}")

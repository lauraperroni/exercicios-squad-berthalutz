def contar_vogais(frase):
    # Inicializa o contador de vogais
    total_vogais = 0

    # Lista de vogais para verificar se um caractere é uma vogal
    vogais = "aeiouAEIOU"

    # Itera sobre cada caractere na frase
    for char in frase:
        # Verifica se o caractere é uma vogal
        if char in vogais:
            total_vogais += 1

    # Retorna o total de vogais encontradas na string
    return total_vogais

# Solicita ao usuário para inserir uma frase
frase_usuario = input("Digite uma frase: ")

# Chama a função contar_vogais e exibe o resultado
resultado = contar_vogais(frase_usuario)
print(f"A frase '{frase_usuario}' possui {resultado} vogais.")

'''
 Desenvolver um programa que solicite a idade do usuário e identifique se
ele é uma criança, um adolescente, adulto ou idoso.

Responsavel: Vivian Rosana Carrillo Cuentas 
'''

#Se considera criança a partir de 2 anos  ate 12 
#Se considera adolescente a partir de 12 ate os 18 
#Se considera adulto a partir dos 18 
# se considera idoso a partir de 60 pra cima 

def classificar_idade(idade):
    
    if 2 <= idade < 12:
        return "Criança"
    elif 12 <= idade < 18:
        return "Adolescente"
    elif 18 <= idade < 60:
        return "Adulto"
    else:
        return "Idoso"
    
    
    # Solicitando a idade ao usuário
idade = int(input('Digite sua idade: '))

# Chamando a função e exibindo o resultado
classificacao = classificar_idade(idade)
print(f'Você é um(a) {classificacao}.')
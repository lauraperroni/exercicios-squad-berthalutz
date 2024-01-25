'''
  Crie um programa que solicite ao usuário um login e uma senha. O
programa deve permitir o acesso apenas se o usuário for "admin" e a senha
for "admin123", caso contrário imprima uma mensagem de erro.

Responsável:  Leidejane
'''


def verificar_acesso(login, senha):
    if login == "admin" and senha == "admin123":
        return True
    else:
        return False


# Solicitação de login e senha ao usuário
login_usuario = input("Digite o seu login: ")
senha_usuario = input("Digite a sua senha: ")

# Verifica o acesso
if verificar_acesso(login_usuario, senha_usuario):
    print("Acesso permitido! Bem-vindo, admin.")
else:
    print("Login ou senha incorretos. Acesso negado.")

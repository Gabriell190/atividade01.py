#Crie um sistema de login que não permite que o nome de usuário e a senha sejam iguais.

user = input("Informe seu login: ")
senha = input("Informe sua senha: ")

while user == senha:
    print("Sua senha e login não podem ser iguais. Tente novamente.")
    user = input("Informe seu login: ")
    senha = input("Informe sua senha: ")

print("Conta criada com sucesso!")

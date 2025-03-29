#Dado um salário inicial e um aumento percentual que dobra a cada ano, calcule o
#salário atual após vários anos.

salario_inicial = float(input("Informe seu salário inicial: R$ "))
tempo = int(input("Informe o tempo que você trabalha (em anos): "))

if salario_inicial <= 0 or tempo < 0:
    print("Por favor, insira valores positivos para o salário e o tempo.")
else:
    salario_final = salario_inicial * (2 ** tempo)

    print(f"Seu salário após {tempo} anos de serviço será: R$ {salario_final:.2f}.")

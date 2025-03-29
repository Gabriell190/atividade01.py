#Solicite um número inteiro maior que 1 e verifique se ele é primo.

n = int(input("Diga um número inteiro maior que 1: "))

if n <= 1:
    print("Por favor, insira um número maior que 1.")
else:
    primo = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            primo = False
            break

    if primo:
        print("Este número é primo.")
    else:
        print("Este número não é primo.")

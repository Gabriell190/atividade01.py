#Solicite um número ímpar ao usuário e calcule a diferença entre o quadrado do
#número anterior e do próximo número ímpar.

while True:
    numero = int(input("Diga um número ímpar: "))
    if numero % 2 != 0:
        break
    print("Por favor, digite um número ímpar.")

anterior = numero - 2
posterior = numero + 2

dif_quadrados = posterior**2 - anterior**2

print(f"Diferença entre os quadrados do próximo e do anterior: {dif_quadrados}.")

#Peça três números ao usuário e informe qual é o maior e qual é o menor.

n1 = int(input("Diga um número: "))
n2 = int(input("Diga outro número: "))
n3 = int(input("Diga mais outro número: "))

numeros = [n1, n2, n3]

maior = max(numeros)
menor = min(numeros)

print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")

#Crie um programa que gere e exiba os 100 primeiros números primos.

import itertools

def analise_primo(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

primos = []
for num in itertools.count(2):
    if analise_primo(num):
        primos.append(num)
        if len(primos) == 100:
            break

for i in range(0, 100, 10):
    print(" ".join(f"{p:3}" for p in primos[i:i+10]))

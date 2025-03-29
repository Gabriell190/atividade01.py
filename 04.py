# Um cliente alugou um carro e rodou alguns quilômetros por um certo número de dias.
# O custo diário é de R$90. Se ele rodou mais de 100 km, há uma taxa extra de R$12 por km adicional.

distancia = float(input("Digite a quantidade de km rodados: "))
tempo = int(input("Digite o número de dias de aluguel: "))

valor_base = tempo * 90

if distancia > 100:
    excedente = distancia - 100
    taxa_extra = excedente * 12
else:
    taxa_extra = 0

valor_total = valor_base + taxa_extra

print("\nResumo do Aluguel:")
print(f"Valor base (diárias): R${valor_base:.2f}")
print(f"Taxa extra por km excedente: R${taxa_extra:.2f}")
print(f"Valor total a pagar: R${valor_total:.2f}")

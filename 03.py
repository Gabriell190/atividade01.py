# Peça ao usuário o valor total das mercadorias compradas
# Se for menor que R$500, não há imposto
# Caso contrário, aplique uma taxa de 50% sobre o valor que ultrapassar R$500

valor = float(input("Diga o valor das compras: R$"))

if valor > 500:
    excedente = valor - 500
    taxa = excedente * 0.5 
    valor_total = valor + taxa

    print(f"\nValor original: R${valor:.2f}")
    print(f"Imposto sobre excedente: R${taxa:.2f}")
    print(f"Valor total com imposto: R${valor_total:.2f}")

else:
    print("\nCompra livre de taxa. Total a pagar: R${:.2f}".format(valor))

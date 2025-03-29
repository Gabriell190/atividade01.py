# Imprime os 100 primeiros números naturais formatados corretamente

for i in range(1, 101):
    if i % 10 == 0:
        print(i)
    else:
        print(i, end=", ")

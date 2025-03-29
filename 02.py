# Solicite um valor em segundos e converta para dias, horas, minutos e segundos restantes

tempo = int(input("Diga o valor em segundos: "))

dias = tempo // 86400
resto = tempo % 86400

horas = resto // 3600
resto = resto % 3600

minutos = resto // 60
segundos = resto % 60

print(f"Dias: {dias}, Horas: {horas}, Minutos: {minutos}, Segundos: {segundos}")

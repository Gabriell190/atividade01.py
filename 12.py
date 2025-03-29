#Peça ao usuário a quantidade de turmas e a quantidade total de alunos. Informe a
#média de alunos por turma, mas avise se alguma turma tiver mais de 40 alunos.

turmas = int(input("Informe a quantidade de turmas: "))
alunos = int(input("Informe a quantidade total de alunos: "))

if turmas <= 0:
    print("A quantidade de turmas deve ser maior que zero.")
else:
    media = alunos / turmas

    if media > 40:
        print(f"Atenção! A média de alunos por turma é superior a 40, sendo {media:.1f} alunos.")
    else:
        print(f"A média de alunos por turma é {media:.1f}.")

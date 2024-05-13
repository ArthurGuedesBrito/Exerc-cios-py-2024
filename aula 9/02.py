nomes_presentes = ["Mayara","Luiz Carlos","Luiz Gustavo","Arthur","Anderson","Gabriel","Luana","Higor","Pedro","Luiz Felipe","Felipe"]

nomes_presentes.append("Adrian")

contador = 0

for i in nomes_presentes:
    print(i)

    if i[0] == "A":
        contador += 1

print("Há",contador,"nomes com 'A' no início!")






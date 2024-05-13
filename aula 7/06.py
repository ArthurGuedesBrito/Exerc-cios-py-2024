contagem = 0

for i in range(5):
    numero = int(input("Digite um número: "))
    if numero > 10:
        contagem += 1

print("Há",contagem,", maiores que 10.")

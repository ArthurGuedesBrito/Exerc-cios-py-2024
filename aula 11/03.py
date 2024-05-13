vetor_1 = [] # A variavel fica sem nada pelo fato que os valores ainda não foram adicionados.
vetor_2 = [] # A variavel fica sem nada pelo fato que os valores ainda não foram adicionados.

print("Digite 5 números para o primeiro vetor:") # imprima os 5 números para o primeiro vetor.

for i in range(5): # faça linha em sequencia(range) 5 vezes.
    num = int(input("Digite um número:")) # Variavel num guardando o valor de numero.
    vetor_1.append(num) # Aqui está adicionando valor na ultima posição dentro da variavel vetor.

print("Digite 5 números para o segundo vetor:")
for i in range(5):
    num = int(input("Digite um número:"))
    vetor_2.append(num)

intersecao = []

for num in vetor_1:
    esta_na_intersec = False
    for val in vetor_2:
        if num==val:
            esta_na_intersec = True

if esta_na_intersec:
    ja_esta_na_intersec = False
    for val in intersecao:
        if num==val:
            ja_esta_na_intersec = True

if not ja_esta_na_intersec:
    intersecao.append(num)

print("A interseção entre os dois vetores é:")
for num in intersecao:
    print(num)
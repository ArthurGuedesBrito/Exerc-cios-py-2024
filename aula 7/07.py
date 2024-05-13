numero = int(input("Digite um número:"))
fatorial = numero

for i in range(numero -1,1,-1):
    fatorial = fatorial*i

print("O fatorial de", numero, "é", fatorial, ".")

 
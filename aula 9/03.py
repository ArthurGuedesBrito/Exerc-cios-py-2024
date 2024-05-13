print("Números na ordem crescente:")
num = [0]*5

for i in range(len(num)):
    num[i] = int(input("Informe um valor:"))


num_ivertido = []
for i in range(len(num)):
    num_ivertido.append(num[-i-1])

print("Números na ordem decrecente:")
print(num_ivertido)
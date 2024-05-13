primeiro_número = int(input("Digite um valor:"))
segundo_número = int(input("Digite um valor:"))

print("1. para +")
print("2. para -")
print("3. para *")
print("4. para /")


soma = int(input("Digite o sinal que voçe deseja usar:"))

match soma:
    case 1:
        print(primeiro_número + segundo_número)
    case 2:
        print(primeiro_número-segundo_número)
    case 3:
        print(primeiro_número*segundo_número)
    case 4:
        print(primeiro_número/segundo_número)
    case _:
        print("Opção invalida")




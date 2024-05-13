numero_1 = int(input("informe o primeiro número:"))
numero_2 = int(input("informe o segundo número:"))
numero_3 = int(input("informe o terceiro número:"))


if numero_1>numero_2:
    temp = numero_1
    numero_1 = numero_2
    numero_2 = temp
if numero_2>numero_3:
    temp = numero_2
    numero_2 = numero_3
    numero_3 = temp
if numero_1>numero_2:
    temp = numero_1
    numero_1 = numero_2
    numero_2 = temp

print(numero_1,numero_2,numero_3)

    

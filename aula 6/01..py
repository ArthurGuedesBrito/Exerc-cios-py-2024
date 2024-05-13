sexo = input("Por favor, insira seu sexo (M para masculino, F para feminino): ")
altura = float(input("Por favor, insira sua altura em metros: "))

if sexo.upper() == "M" and altura >= 1.70:
    print("Você está apto para o alistamento no exército.")
elif sexo.upper() == "F" and altura >= 1.60:
    print("Você está apta para o alistamento no exército.")
else:
    print("Você não está apto para o alistamento no exército.")

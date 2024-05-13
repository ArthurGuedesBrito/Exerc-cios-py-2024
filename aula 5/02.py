sexo = input("Defina seu sexo com 'F' para Feminino e 'M' para Masculino: ").upper()

#lower() = transforma todo texto em minusculo
#upper() = transforma todo texto em maiusculo

match sexo:
    case "F":
        print("Foi selecionado o sexo Feminino")
    case "M":
        print("Foi selecionado o sexo Masculino")
    case _:
        print("Sexo não definido")

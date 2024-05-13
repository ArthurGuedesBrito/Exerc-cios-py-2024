
print("1. Fazer check-in")
print("2. Chamar serviço de quarto")
print("3. Fazer pedido")
print("4. Fazer Check-out")

cliente = int(input("Escolha uma opção:"))

match cliente:
    case 1:
        print("Foi selecionado fazer check-in!")
    case 2:
        print("Foi selecionado Serviço de Quarto!")
    case 3:
        print("Foi selecionado Fazer Pedido!")
    case 4:
        print("Foi selecionado Fazer Check-out!")
    case _:
        print("Essa opção não se encontra no menu!")
    

print("Escolha uma das opções abaixo:")
print("1 - Converter de Celsius para Fahrenheit")
print("2 - Converter de Fahrenheit para Celsius")

opcao = int(input("Digite sua opção (1 ou 2): "))

if opcao == 1:
    celsius = float(input("Digite a temperatura em Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"A temperatura em Fahrenheit é: {fahrenheit}°F")
elif opcao == 2:
    fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"A temperatura em Celsius é: {celsius}°C")
else:
    print("Opção inválida. Por favor, escolha 1 ou 2.")

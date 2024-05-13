valores = [] # variavel valor - ta sem nada pq os valores ainda vão ser adicionados!

for i in range(5): # faça linha em repetição por 5 vezes!
    print("Digite o valor", i, ":") # imprima ("digite o valor", linha,":")
    num = float(input())  # variavel (numero) é usado float para números dicimais ( quebrados)
    valores.append(num) # variavel.adicione o valor em último(variavel número) onde estão guardados os numeros

maior_valor = valores[0] # variavel maior número = variavel valor[0] começando em 0. está guardando o maior valor. está com um 0 pelo fato de que nenhum valor ainda foi adicionado
menor_valor = valores[0] # variavel menor número = variavel valor[0] começando em 0. está guardando o menor valor. está com um 0 pelo fato de que nenhum valor ainda foi adicionado
posicao_maior = 0 # posição do maior número. está com um 0 pelo fato de que nenhum valor ainda foi adicionado
posicao_menor = 0 # posição do menor número. está com um 0 pelo fato de que nenhum valor ainda foi adicionado

for i in range(1,5): # faça linha em repetição por 5 vezes (o 1 significa inicio, o 5 significa final)
    if valores[i] > maior_valor: # se valores[linha] for maior que a variavel maior valor:
        maior_valor = valores[i]  # maior valor = valores[linha], ou seja maior valor é a mesma coisa que valor linha
        posicao_maior = i # posição maior = linha
    if valores[i] < menor_valor: # se valor[linha] for menor que a variavel menor valor:
        menor_valor = valores[i] # menor valor = valores [linha], ou seja, os valores são os mesmos
        posicao_menor = i # posição menor = [linha]

print("O maior valor é", maior_valor, "e está na posição", posicao_maior) # imprima("O maior valor é", maior_valor, "e está na posição", posicao_maior")
print("O menor valor é",menor_valor,"e está na posição", posicao_menor) # imprime("O menor valor é",menor_valor,"e está na posição", posicao_menor")



vetor = [0,0,3,0,9,6,0,7,0,0] # vetor guardando os valores


vetor_compactado = [] #variavel vetor compactado para receber os valores diferentes de 0, fica sem nada pelo fato que os valores ainda não foram adicionados


for valor in vetor:  # faça valor em vetor
    if valor != 0: # se valor for desigual a zero.
        vetor_compactado.append(valor) #variavel vetor compactado.append(O append é usado para adicionar um valor no final da lista) (valor)- representando a variavel com os valores.

print(vetor_compactado) # imprima ( a variavel vetor compactado) no caso os valores diferentes de 0
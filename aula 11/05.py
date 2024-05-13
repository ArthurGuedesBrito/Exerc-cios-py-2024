# Criando a primeira matriz:

matriz1 = [[1, 2, 3, 4],
           [5, 6, 7, 8],
           [9, 10, 11, 12],
           [13, 14, 15, 16]]

# Criando a segunda matriz:
matriz2 = [[16, 15, 14, 13],
           [12, 11, 10, 9],
           [8, 7, 6, 5],
           [4, 3, 2, 1]]

# Criando a terceira matriz com os maiores valores de cada posição das matrizes lidas(1 e 2):
matriz3 = [[0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0]]


for i in range(4): # faça em linha  4 vezes
    for j in range(4):  # faça em coluna 4 vezes
        if matriz1[i][j] > matriz2[i][j]:  #if = se       #matriz 1[linha][coluna] > matriz2[linha][coluna]
            matriz3[i][j] = matriz1[i][j]                 #matriz 3[linha][coluna] = matriz1[linha][coluna]
        else:    # else = senão
            matriz3[i][j] = matriz2[i][j]    # Senão matriz3[linha][coluna] = matriz2[linha][coluna]

# O que acontece é que o if faz a verificação se matriz3 é igual a matriz1, no else e como ja fala (se não) matriz3[linha][coluna] é igual a matriz2[linha][coluna], exatamente pelo fato de que o matriz3 poder ser diferente de matriz1.


for linha in matriz3:  # faça linha em matriz3 (ou melhor dizendo, faça os valores em matriz3 ) nesse caso o for está determinando que os valores maiores de cada linha da matriz1 e 2 seja levada para matriz3.
    print(linha) # Está imprimindo as linhas.

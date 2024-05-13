
matriz = [[0 for _ in range(5)] for _ in range(5)] # Aqui estamos criando uma matriz 5 por 5, a primeira parte onde começa com 0 é a parte onde começa a fazer a matriz(linhas), já na segunda parte onde cria as colunas


for i in range(5): # faça linha em sequencia(range significa criar sequencia)
    for j in range(5): # faça coluna em sequencia(range significa criar sequencia)
        matriz[i][j] = i * j   # matriz[linha][coluna] = (linha) * (coluna), nesse caso está multiplicando linha por coluna


for linha in matriz: #faça linha em matriz(faça linha por linha na matriz)
    print(linha) # Imprima linha.

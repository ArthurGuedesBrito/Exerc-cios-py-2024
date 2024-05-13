maior_valor = -1
posicao_maior_valor = (-1, -1)

matriz = [[0,0,0],
          [0,0,0],
          [0,0,0]]


for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input("Insira o valor para a posição:"))


for i in range(3):
    for j in range(3):
       if matriz[i][j] > maior_valor:
          maior_valor = matriz[i][j]
          posicao_maior_valor = (i,j)
    
print("O maior valor é:", maior_valor, "na posição:", posicao_maior_valor) 
contador = 0

matriz = [[0,0,0],
          [0,0,0],
          [0,0,0],
          [0,0,0]]


for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input("Insira o valor para a posição:"))


for i in range(3):
    for j in range(3):
       if matriz[i][j] > 10:
          contador += 1
    
print("O número de valores maior que 10 na matriz é:",contador) 







    
matriz = [[1,2,3],
          [4,5,6],
          [7,8,9],
          [1,1,1]]

'''print(matriz[1][2])
matriz[1][0] = 14
print(matriz[1][0])'''

'''for i in range(3):
    for j in range(3):
        print(matriz[i][j])'''

for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        print(matriz[i][j])
          
download = int(input("qual o tamanho do arquivo?")) #bytes
download_bit = download*8                               #bit
 
minutos = download_bit/60

print("Um arquivo de:",download,"bytes, demora", minutos,"minutos para baixair o arquivo")
# basicamente eu fiz um programa que pede o tamanho de um arquivo em byte e transforma em bits
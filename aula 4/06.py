print("Responda com 'sim' ou 'não'.")

pergunta_1 = input("Telefonou para a vítima?")
pergunta_2 = input("Esteve no local do crime?")
pergunta_3 = input("Mora perto da vítima?")
pergunta_4 = input("Devia para a vítima?")
pergunta_5 = input("Já trabalhou com a vítima?")

resposta_positiva = 0

if pergunta_1 == "sim" or pergunta_1 == "sim":
    resposta_positiva += 1
if pergunta_2 == "sim" or pergunta_2 == "sim":
    resposta_positiva += 1 
if pergunta_3 == "sim" or pergunta_2 == "sim":
    resposta_positiva += 1
if pergunta_4 == "sim" or pergunta_4 == "sim":
    resposta_positiva += 1 
if pergunta_5 == "sim" or pergunta_5 == "sim":
    resposta_positiva += 1 

if resposta_positiva == 2:
    print("suspeito(a)")
elif resposta_positiva == 3 or resposta_positiva == 4:
    print("cúmplice")
elif resposta_positiva == 5:
    print("Assasino")
else:
    print("Inocente")

#fiz um programa que fez perguntas para uma pesssoa sobre um crime, o programa no final emitiu uma classificação para o interrogado, 2 respostas positivas é um suspeito(a), 3 e 4 respostas positivas é um cúmplice, 5 respostas positivas  é um assasino.
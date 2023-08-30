vetor = [] #armazenamento dos números

#Loop para ler os números
for i in range(5):
    numero = int(input("Digite um número: "))
    vetor.append(numero) #Adiciona o número à lista

#Exibe os números
    print("os números digitados foram: ")
    for numero in vetor:
        print(numero)

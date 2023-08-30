num1 = float(input("Digite o 1º número: "))
num2 = float(input("Digite o 2º número: "))
num3 = float(input("Digite o 3º número: "))

if num1 > num2:
    if num1 < num3:
        mediana = num1
    elif num2 > num3:
        mediana = num2
    else:
        mediana = num3

else:
    if num1 > num3:
       mediana = num1
    elif num2 < num3:
       mediana = num2
    else:
       mediana = num3

print("Mediana= ", mediana)
       

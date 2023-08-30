import sys; '''Importar módulo para uso da função sys.exit()'''
i = float(input(" Insira o valor de i: "))

if(i<=0):
  print("insira um valor inteiro e positivo: ")
  sys.exit(); '''Finaliza o programa caso o usuário digite valores negativos'''
if(i>0): '''Caso seja digitado um valor maior que zero, os comandos serão executados'''

a = int(input("insira o valor de a: "))
b = int(input("insira o vlaor de b: ")) 
c = int(input("insira o valor de c: "))

if((i % 2) == 0): '''Caso i seja par, calcular a média aritimética'''
media_arit = ((a + b + c)/3)
print("Média aritimética: ", media_arit)

if(i>10):
 media_pond = ((2 * a + 3 * b + 4 * c)/9)
 print("Média ponderada: " ,media_pond)
    

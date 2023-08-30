print('\t ---Cálculo de novo salário---')

salario_atual=float(input('informe seu salário atual: '))

if (salario_atual<500):
    salario_novo = salario_atual+(salario_atual*0.15)
    print('O reajuste é de ' '=', salario_novo)

elif (salario_atual>=500) and (salario_atual<=1000):
     salario_novo = salario_atual+(salario_atual*0.10)
     print('O reajuste é de ' '=', salario_novo)

elif (salario_atual>=1000):
     salario_novo = salario_atual+(salario_atual*0.05)
     print('O reajuste é de ' '=', salario_novo)

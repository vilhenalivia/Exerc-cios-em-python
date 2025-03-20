A = int(input('Informe os dias para atividade A: '))
B = int(input('Informe os dias para atividade B: '))
C = int(input('Informe os dias para atividade C: '))

dias_totais = A + B + C

if A < 0 or B < 0 or C < 0:
    print('Os dias não podem ser negativos!')
else:
    print(f'Dias totais: {dias_totais}')
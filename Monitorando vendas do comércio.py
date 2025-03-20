macas = int(input('Digite a quantidade de maçãs vendidas: '))
bananas = int(input('Digite a quantidade de bananas vendidas: '))

if macas > bananas:
    print('As maçâs tiveram mais vendas!')
elif macas == bananas:
    print('Maçãs e bananas tiveram a mesma quantidade de vendas!')
else:
    print('As bananas tiveram mais vendas!')

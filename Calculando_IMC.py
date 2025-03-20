peso = float(input('Digite seu peso (kg): '))
altura = float(input('Digite sua altura (m): '))

IMC = peso / (altura ** 2)

print(IMC)

if IMC < 18.5 :
    print('Você está abaixo do peso.')
elif IMC < 25:
    print('Você está no peso ideal')
else:
    print('Você está acima do peso.')
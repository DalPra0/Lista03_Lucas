somaPar = int(0)
somaImpar = int(0)
numImpar = int(0)
numPar = int(0)
while numPar != 5 or somaImpar < 30:
    numero = int(input('Digite um numero inteiro: '))
    if numero > 0:
        calculo = numero % 2
        if calculo == 0:
            print(f'O numero {numero} é par')
            somaPar += numero
            numPar += 1
        else:
            print(f'O numero {numero} é impar')
            somaImpar += numero
            numImpar += 1
    if numPar == 5 or somaImpar > 30:
            break    
    elif numero < 0:
        print('Digite um numero maior que 0')
print(f'Total de numeros pares digitados: {numPar}, total de numeros impares digitados: {numImpar}')
print(f'Soma dos numeros pares: {somaPar}, Soma dos numeros impares: {somaImpar}')   
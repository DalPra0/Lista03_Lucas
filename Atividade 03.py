somaPar = 0  # Corrigido para iniciar em 0 ao invés de usar int()
somaImpar = 0  # Corrigido para iniciar em 0 ao invés de usar int()
numImpar = 0
numPar = 0

while numPar < 5 and somaImpar < 30:  # Corrigido a condição do while
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
    elif numero < 0:
        print('Digite um numero maior que 0')

print(f'Total de numeros pares digitados: {numPar}, total de numeros impares digitados: {numImpar}')
print(f'Soma dos numeros pares: {somaPar}, Soma dos numeros impares: {somaImpar}')

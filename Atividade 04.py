const = int(1)
n = int(0)
quantidade = int(input('Digite a quantidade de numeros: '))
soma = int()
while n != quantidade:
    numero = float(input(f'Digite o numero {const}: '))
    if numero >= 10:
        soma += numero
        n += 1
        const += 1
    else:
        print('Não aceita numero menor que 10')
    if n == quantidade:
        break
print(f'A soma dos numeros resulta em: {soma}')
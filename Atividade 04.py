const = 1
n = 0
quantidade = int(input('Digite a quantidade de numeros: '))
soma = 0

while n < quantidade and const <= quantidade:
    numero = float(input(f'Digite o numero {const}: '))
    if numero >= 10:
        soma += numero
        n += 1
    else:
        print('Não aceita numero menor que 10')
    const += 1

print(f'A soma dos numeros resulta em: {soma}')
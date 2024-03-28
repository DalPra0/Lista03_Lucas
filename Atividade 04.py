const = 1
n = 0
quantidade = int(input('Digite a quantidade de numeros: '))
soma = 0  # Corrigido para iniciar em 0 ao invés de usar int()

while n < quantidade:  # Corrigido para usar operador de comparação correto
    numero = float(input(f'Digite o numero {const}: '))
    if numero >= 10:
        soma += numero
        n += 1
        const += 1
    else:
        print('Não aceita numero menor que 10')

print(f'A soma dos numeros resulta em: {soma}')

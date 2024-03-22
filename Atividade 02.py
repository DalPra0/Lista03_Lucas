soma = 0
contador = 0

while contador < 10:
    nota = float(input("Digite uma nota: "))
    soma = soma + nota
    contador = contador + 1

media = soma/contador

print("A media das", contador, "notas é",  media)
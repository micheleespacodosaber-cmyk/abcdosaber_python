soma = 0
quantidade = 0
numeros = []

# entrada de dados
for i in range(5):
    numero = int(input("Digite um valor inteiro: "))
    numeros.append(numero)

# processamento
for numero in numeros:
    if numero >= 0:
        soma = soma + numero
    else:
        quantidade = quantidade + 1

# saída de dados
print("Soma dos valores positivos:", soma)
print("Quantidade de valores negativos ou zero:", quantidade)





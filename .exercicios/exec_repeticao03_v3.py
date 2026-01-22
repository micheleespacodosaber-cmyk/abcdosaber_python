soma = 0
quantidade = 0
numeros = []
continua = 1

# entrada de dados
while continua != 0:
    numero = int(input("Digite um valor inteiro: "))
    numeros.append(numero)
    
    continua = int(input("Deseja continuar? (1-Sim / 0-Não): "))


# processamento
for numero in numeros:
    if numero >= 0:
        soma = soma + numero
    else:
        quantidade = quantidade + 1

# saída de dados
print("Soma dos valores positivos:", soma)
print("Quantidade de valores negativos ou zero:", quantidade)





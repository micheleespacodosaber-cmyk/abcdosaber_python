# entrada de dados
numeros = []
resultados = []

for i in range(4):
    numero = int(input(f"Digite o {i+1}o. número inteiro: "))
    numeros.append(numero)

# processamento
for numero in numeros:
    if numero % 2 == 0 and numero % 3 == 0:
        resultados.append(f"O número {numero} é divisível por 2 e 3")

# saída de dados
print(resultados)

for resultado in resultados:
    print(resultado)



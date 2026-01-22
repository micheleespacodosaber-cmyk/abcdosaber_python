# entrada de dados
numero = int(input("Digite um número inteiro: "))

# processamento
resultado = ""
if numero > 0:
    resultado = "positivo"
elif numero < 0:
    resultado = "negativo"
else:
    resultado = "zero"

# saída de dados
print(resultado)
# entrada de dados
numero = int(input("Digite um número inteiro: "))

# processamento
resultado = ""
if numero > 0:
    resultado = "positivo"

if numero < 0:
    resultado = "negativo"

if numero == 0:
    resultado = "zero"

# saída de dados
print(resultado)
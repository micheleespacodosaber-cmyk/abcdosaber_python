# entrada de dados
numero = int(input("Digite um número inteiro: "))

# processamento
resultado = ""
a=0
b=5

if numero > 0:
    resultado = "positivo"  
      
else:
    if numero < 0:
        resultado = "negativo"
    else: 
        resultado = "zero"

# saída de dados
print(resultado)
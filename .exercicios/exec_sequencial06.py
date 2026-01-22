# entrada de dados
qtd_dolar = float(input("Digite a quantidade de dólares: "))
cotacao_dolar = float(input("Digite a cotação do dólar: "))

# processamento
qtd_reais = qtd_dolar * cotacao_dolar

# saída de dados
print(f"O valor em reais é R$ {qtd_reais:.2f}.")
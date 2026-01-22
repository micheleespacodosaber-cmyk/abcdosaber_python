# entrada de dados
preco_custo = float(input("Digite o preço de custo: "))
percentual_acrescimo = float(input("Digite o percentual de acréscimo (%): "))

# processamento
acrescimo = preco_custo * (percentual_acrescimo / 100)
valor_venda = preco_custo + acrescimo

# saída de dados
print(f"O valor de venda é R$ {valor_venda:.2f}.")
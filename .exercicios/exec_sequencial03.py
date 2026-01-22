# entrada de dados
produto = input("Digite o nome do produto: ")
valor = float(input("Digite o valor do produto: "))

# processamento
desconto = valor * 0.09
novo_valor = valor - desconto

# saída de dados
print("O produto {0} com valor original de R$ {1:.2f} " \
      "com desconto de 9% fica por R$ {2:.2f}.".format(produto, valor, novo_valor))

print(f"O produto {produto} com valor original de R$ {valor:.2f} " \
      f"com desconto de 9% fica por R$ {novo_valor:.2f}.")



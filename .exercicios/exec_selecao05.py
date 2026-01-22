# entrada de dados
total_ganhos = float(input("Digite o total de seus ganhos: "))

# processamento
if total_ganhos <= 500.00:
    aliquota_desconto = 0
elif total_ganhos >= 500.01 and total_ganhos <= 1500.00:    
    aliquota_desconto = 10/100
elif total_ganhos >= 1500.01 and total_ganhos <= 2500.00:    
    aliquota_desconto = 15/100
else:
    aliquota_desconto = 20/100

desconto = total_ganhos * aliquota_desconto

# saída de dados
print(f"O desconto do IR para o seu total de ganhos é: {desconto:.2f}")
print(f"O total a receber após o desconto do IR é: {(total_ganhos - desconto):.2f}")


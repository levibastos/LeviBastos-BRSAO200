'''2- Calculadora de Desconto
Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

* Nome do produto: "Camiseta"
* Preço original: R$ 50.00
* Porcentagem de desconto: 20%
O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.'''


nome_produto = "Camiseta"
preco_original = 50.00
percent_desc = 20  # Representa 20%

valor_desconto = (preco_original * percent_desc) / 100 #Calcular o valor do desconto (20% de R$ 50.00)

preco_final = preco_original - valor_desconto #calcular o preço final

print("--- Detalhes do Desconto ---")
print(f"Nome do produto: {nome_produto}")
print(f"Preço original: R$ {preco_original:.2f}")
print(f"Desconto: {percent_desc}%")
print("-" * 30)
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Preço Final a pagar: R$ {preco_final:.2f}")

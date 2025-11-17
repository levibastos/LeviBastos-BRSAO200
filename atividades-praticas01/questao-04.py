"""4- Calculadora de Preço Total
* Desenvolva um programa que calcula o preço total de uma compra. Use as seguintes informações:

* Nome do produto: "Cadeira Infantil"
* Preço unitário: R$ 12.40
* Quantidade: 3
O programa deve calcular o preço total e exibir todas as informações, incluindo o resultado final."""

nome_produto = "Cadeira Infantil"
preco_uni = 12.40
qtd = 3

preco_total = preco_uni * qtd

print("--- Detalhes da Compra ---")
print(f"Nome do produto: {nome_produto}")
print(f"Preço unitário: R$ {preco_uni:.2f}")  #:.2f = formata o valor com 2 casas decimais
print(f"Quantidade: {qtd}")
print("-" * 25) #Adicionar traços como linha separadora
print(f"Preço Total: R$ {preco_total:.2f}")  
"""1- Conversor de Moeda
Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:

* Valor em reais: R$ 100.00
* Taxa do dólar: R$ 5.20
* Taxa do euro: R$ 6.15
O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais."""

valor_reais = 100.00
taxa_dolar = 5.20
taxa_euro = 6.15

valor_dolar = valor_reais / taxa_dolar
valor_euro = valor_reais / taxa_euro

print(f"Valor em Reais: R$ {valor_reais:.2f}") # Formatar para 2 casas decimais;
print("-" * 25) #Adicionando -- como linha separadora;
print(f"Taxa do dólar (R$): {taxa_dolar:.2f}")
print(f"Taxa do euro  (R$): {taxa_euro:.2f}")
print("-" * 45) 
print(f"R$100 convertidos para Dólares (USD) = ${valor_dolar:.2f}")
print(f"R$100 convertidos para Euros (EUR)   = €{valor_euro:.2f}")
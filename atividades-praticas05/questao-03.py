#3 - Programa para calcular o preço final de um produto após aplicar um desconto percentual:

def calcular_valor_desconto(preco_original: float, porcentagem_desconto: float) -> float:
    """
    a - Calcula o valor monetário do desconto baseado no preço e na porcentagem.
    """
    valor_desconto = preco_original * (porcentagem_desconto / 100)
    return valor_desconto

def calcular_preco_final(preco_original: float, valor_desconto: float) -> float:
    """
    b - Determina o novo preço após subtrair o valor do desconto.
    """
    preco_final = preco_original - valor_desconto
    return preco_final

# --- Interação com Usuário e Programa Principal ---

if __name__ == "__main__":
    print("--- Calculadora de Desconto de Produto ---")

    while True:
        try:
            #Pede o preço original ao usuário:
            preco_input = input("Digite o preço original do produto (R$): ")
            preco_original = float(preco_input)
            
            #Pede a porcentagem de desconto:
            desconto_input = input("Digite a porcentagem de desconto (ex: 10 para 10%): ")
            porcentagem_desconto = float(desconto_input)

            # Validações básicas de entrada para não acetar valores negativos.
            if preco_original < 0 or porcentagem_desconto < 0:
                print("Erro: Preço e desconto não podem ser negativos. Tente novamente.")
                continue

            # 1. Calcular o valor do desconto chamando a função (a)
            valor_do_desconto = calcular_valor_desconto(preco_original, porcentagem_desconto)

            # 2. Calcular o preço final chamando a função (b)
            preco_com_desconto = calcular_preco_final(preco_original, valor_do_desconto)

            # 3. Exibir o resultado formatado:
            print("\n--- Resultado ---")
            print(f"Preço original:       R$ {preco_original:.2f}")
            print(f"Desconto aplicado:        {porcentagem_desconto:.1f}%")
            print(f"Valor do desconto:    R$  {valor_do_desconto:.2f}")
            print(f"----------------------------------")
            print(f"Preço final a pagar:  R$ {preco_com_desconto:.2f}")

            break

        except ValueError:
            print("\nErro: Entrada inválida. Digite apenas números válidos.")
            print("-" * 40)
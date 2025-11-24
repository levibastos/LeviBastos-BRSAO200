#1 - Calculadora de gorjeta:

def calcular_gorjeta(valor_conta: float, porcentagem_gorjeta: float) -> float:
    valor_gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return valor_gorjeta

if __name__ == "__main__":
    print("--- Calculadora de Gorjeta ---")
    
    #Loop para garantir que o usuário insira valores válidos
    while True:
        try:
            #a - Solicita o valor total da conta
            valor_conta_input = input("Digite o valor total da conta (ex: 150.00): R$ ")
            valor_conta = float(valor_conta_input)
            
            #b - Solicita a porcentagem da gorjeta
            porcentagem_input = input("Digite a porcentagem da gorjeta desejada (ex: 10 para 10%): ")
            porcentagem_gorjeta = float(porcentagem_input)
            
            #Validação simples para evitar valores negativos
            if valor_conta < 0 or porcentagem_gorjeta < 0:
                print("Erro: Os valores não podem ser negativos. Tente novamente.")
                continue

            #Chama a função para calcular o valor da gorjeta
            gorjeta_calculada = calcular_gorjeta(valor_conta, porcentagem_gorjeta)
            
            #Calcula o valor total a pagar (conta + gorjeta)
            total_a_pagar = valor_conta + gorjeta_calculada

            #Exibe o resultado final
            print("\n--- Resumo ---")
            print(f"Valor da conta:         R$ {valor_conta:.2f}")
            print(f"Porcentagem da gorjeta:     {porcentagem_gorjeta:.1f}%")
            print(f"Valor da gorjeta:       R$  {gorjeta_calculada:.2f}")
            print(f"-----------------------------------")
            print(f"Total a pagar:          R$ {total_a_pagar:.2f}")
            
            break #Sai do loop se tudo ocorreu bem

        except ValueError:
            #Captura o erro se o usuário digitar texto em vez de números
            print("Entrada inválida. Certifique-se de digitar apenas números válidos.")
            print("-" * 30)
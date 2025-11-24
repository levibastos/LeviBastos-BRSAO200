#4 - Analisador de Números Pares e Ímpares

print("--- Analisador de Pares e Ímpares ---")
print("Digite números inteiros. Digite 'fim' para exibir o resultado final.")

# Contadores para cada tipo de número
cont_pares = 0
cont_impares = 0

while True:
    try:
        entrada = input("Digite um número inteiro (ou 'fim'): ").strip().lower()

        # Condição de saída
        if entrada == 'fim':
            break
        
        # Converte a entrada para um número inteiro
        numero = int(entrada)

        # Classificação usando o operador de módulo (%)
        # Se o resto da divisão por 2 for 0, o número é par
        if numero % 2 == 0:
            print(f"O número {numero} é PAR.")
            cont_pares += 1
        else:
            print(f"O número {numero} é ÍMPAR.")
            cont_impares += 1

    except ValueError:
        # Captura o erro se o usuário não digitar um número inteiro ou 'fim'
        print("Entrada inválida. Por favor, digite um número inteiro válido ou 'fim'.")
        
# Fim da coleta, exibe o resumo
print("\n--- Resumo da Análise ---")
print(f"Total de números pares inseridos: {cont_pares}")
print(f"Total de números ímpares inseridos: {cont_impares}")
print(f"Total geral de números analisados: {cont_pares + cont_impares}")
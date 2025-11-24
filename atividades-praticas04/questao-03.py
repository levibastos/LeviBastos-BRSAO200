#3 - Verificador de Segurança de Senha

print("--- Verificador de Segurança de Senha ---")

while True:
    senha = input("Digite uma senha para verificação: ")

    # Variáveis de controle para os critérios
    tem_oito_caracteres = False
    tem_numero = False
    
    # a - Verificar se tem pelo menos 8 caracteres
    if len(senha) >= 8:
        tem_oito_caracteres = True
    
    # b - Verificar se contém pelo menos um número
    # Itera sobre cada caractere (c) na senha e checa se é um dígito (isdigit())
    # 'any()' retorna True se pelo menos um caractere for um dígito
    if any(c.isdigit() for c in senha):
        tem_numero = True

    # Avaliação final dos critérios
    if tem_oito_caracteres and tem_numero:
        print(f"\nSenha válida! A senha atende a todos os critérios de segurança básicos.")
        break  # Sai do loop porque a senha é válida
    else:
        print("\nSenha inválida. Por favor, tente novamente.")
        print("Critérios necessários:")
        if not tem_oito_caracteres:
            print("- Deve ter pelo menos 8 caracteres.")
        if not tem_numero:
            print("- Deve conter pelo menos um número.")
        print("-" * 30)
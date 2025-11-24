#1 - Gera uma senha aleatória com letras, números e símbolos, de um dado tamanho.

import random
import string

def gerar_senha_segura(tamanho: int) -> str:
        
    # Conjunto de caracteres disponíveis associados a variáveis
    caracteres_letras = string.ascii_letters # A-Z e a-z
    caracteres_numeros = string.digits       # 0-9
    caracteres_simbolos = string.punctuation # !, ", #, $, etc.

    #Combina todos os caracteres disponíveis para o pool principal
    pool_total_caracteres = caracteres_letras + caracteres_numeros + caracteres_simbolos
    
    #Garante que pelo menos um caractere de cada tipo esteja na senha
    # Isso impede que uma senha de 8 caracteres seja só de números, por exemplo
    senha = []
    senha.append(random.choice(caracteres_letras))
    senha.append(random.choice(caracteres_numeros))
    senha.append(random.choice(caracteres_simbolos))
    
    # Preenche o restante da senha com caracteres aleatórios do pool total
    # (tamanho - 3) porque já adicionamos 3 caracteres obrigatórios
    for _ in range(tamanho - 3):
        senha.append(random.choice(pool_total_caracteres))
        
    # Mistura a lista de caracteres para garantir que a ordem seja aleatória
    random.shuffle(senha)
    
    # Converte a lista de caracteres de volta para uma string
    return "".join(senha)

# --- Interação com Usuário e Programa Principal ---

if __name__ == "__main__":
    print("--- Gerador de Senhas Seguras ---")

    while True:
        try:
            # Pede o tamanho da senha ao usuário
            tamanho_input = input("Digite o tamanho desejado para a senha (mínimo 8): ")
            tamanho_senha = int(tamanho_input)
            
            if tamanho_senha < 8:
                print("O tamanho mínimo recomendado é 8 caracteres. Tente novamente.")
                continue

            # Chama a função para gerar a senha
            nova_senha = gerar_senha_segura(tamanho_senha)
            
            # Exibe o resultado
            print(f"Senha gerada: {nova_senha}")
            
            break
            
        except ValueError:
            print("Entrada inválida. Digite um número inteiro válido para a quantidade de carcteres da senha.")
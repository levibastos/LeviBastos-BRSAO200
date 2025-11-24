#2- Programa para verificar se um palavra é palíndromo:

import re # Importa o módulo de expressões regulares para ajudar na limpeza da string

def verificar_palindromo(texto: str) -> bool:
    """
    Verifica se uma palavra ou frase é um palíndromo, ignorando espaços e pontuação.

    Parâmetros:
    texto (str): A string a ser verificada.

    Retorna:
    bool: True se for um palíndromo, False caso contrário.
    """
    
    # 1. Limpeza: Converte para minúsculas
    texto_limpo = texto.lower()
    
    # 2. Limpeza: Remove caracteres não alfanuméricos (incluindo espaços e pontuação)
    # Usa-se expressão regular [^a-z0-9] para manter apenas letras e números
    texto_limpo = re.sub(r'[^a-z0-9]', '', texto_limpo)
    
    # 3. Verificação: Compara a string limpa original com sua versão invertida
    # [::-1] é um "slice" em Python que inverte a string
    texto_invertido = texto_limpo[::-1]
    
    # Retorna True se forem idênticas, False caso contrário
    return texto_limpo == texto_invertido

# --- Programa Principal ---

if __name__ == "__main__":
    print("--- Verificador de Palíndromo ---")
    
    # Pede a frase ou palavra ao usuário
    palavra = input("Digite uma palavra: ")
    
    # Chama a função e armazena o resultado booleano (True/False)
    eh_palindromo = verificar_palindromo(palavra)
    
    # Exibe a resposta formatada como "Sim" ou "Não"
    print("\nAnalisando a frase...")
    
    if eh_palindromo:
        print(f'"{palavra}" é um palíndromo!')
    else:
        print(f'"{palavra}" não é um palíndromo!')
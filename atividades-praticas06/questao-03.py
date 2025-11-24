#3 - Consulta as informações de um CEP na API ViaCEP.

import requests
import json

def consultar_cep(cep):
    
    url = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        # Faz a requisição GET para a API
        response = requests.get(url)

        # Verifica se a requisição foi bem-sucedida (código de status 200)
        if response.status_code == 200:
            dados = response.json()
            
            # A API ViaCEP retorna um campo 'erro': True se o CEP não existir, mesmo com status 200
            if 'erro' in dados and dados['erro']:
                print(f"Erro: O CEP '{cep}' não foi encontrado ou é inválido.")
                return None
            else:
                return dados
        else:
            print(f"Erro: Falha na requisição. Código de status: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        # Captura exceções relacionadas à conexão (ex: sem internet, URL inválida)
        print(f"Erro de conexão: {e}")
        return None
    except json.JSONDecodeError:
        # Captura erro se a resposta não for um JSON válido
        print("Erro: Não foi possível decodificar a resposta da API.")
        return None

def main():
    # Solicita o CEP ao usuário e remove espaços/hífens
    cep_digitado = input("Digite o CEP para consulta (apenas números): ").strip().replace("-", "")

    # Validação básica do formato do CEP (8 dígitos numéricos)
    if not cep_digitado.isdigit() or len(cep_digitado) != 8:
        print("Erro: Formato de CEP inválido. Digite 8 dígitos numéricos.")
        return

    # Consulta o CEP
    dados_endereco = consultar_cep(cep_digitado)

    # Exibe os resultados ou a mensagem de falha
    if dados_endereco:
        print("\n--- Resultado da Consulta ---")
        print(f"Logradouro: {dados_endereco.get('logradouro', 'N/A')}")
        print(f"Bairro: {dados_endereco.get('bairro', 'N/A')}")
        print(f"Cidade: {dados_endereco.get('localidade', 'N/A')}")
        print(f"Estado (UF): {dados_endereco.get('uf', 'N/A')}")
        print("-----------------------------")
    else:
        print("\nNão foi possível obter os dados do endereço.")

if __name__ == "__main__":
    main()
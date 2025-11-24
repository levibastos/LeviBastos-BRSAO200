#2 - Programa para consumir informações de uma determinada API

import requests
import sys

def buscar_usuario_aleatorio():
    url = "https://randomuser.me/api/"
    
    try:
        # Tenta fazer a requisição GET para a API
        response = requests.get(url, timeout=5) # Define um timeout para evitar espera infinita
        response.raise_for_status() # Lança uma exceção para códigos de status HTTP 4xx/5xx
        
        # Se a requisição for bem-sucedida, processa os dados JSON
        data = response.json()
        
        # Extrai as informações necessárias
        usuario = data['results'][0]
        nome = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario['email']
        pais = usuario['location']['country']
        
        # Exibe as informações
        print("-" * 30)
        print(f"Nome: {nome}")
        print(f"E-mail: {email}")
        print(f"País: {pais}")
        print("-" * 30)
        
    except requests.exceptions.ConnectionError:
        # Captura erros de conexão (DNS, firewall, rede indisponível, etc.)
        print("Falha na conexão: Não foi possível conectar ao servidor da API.")
        print("Verifique sua conexão com a internet ou tente novamente mais tarde.")
    except requests.exceptions.Timeout:
        # Captura erros de timeout (servidor demorou muito a responder)
        print("Falha na conexão: A requisição excedeu o tempo limite.")
    except requests.exceptions.HTTPError as e:
        # Captura outros erros HTTP (404, 500, etc.)
        print(f"Falha na requisição HTTP: {e}")
    except requests.exceptions.RequestException as e:
        # Captura quaisquer outros erros da biblioteca requests
        print(f"Ocorreu um erro inesperado durante a requisição: {e}")
    except (KeyError, IndexError, TypeError) as e:
        # Captura erros se a estrutura da resposta JSON for inesperada
        print(f"Erro ao processar os dados da API. A estrutura da resposta pode ter mudado. Detalhes: {e}")

if __name__ == "__main__":
    buscar_usuario_aleatorio()
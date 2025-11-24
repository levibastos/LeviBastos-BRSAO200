#4 - Consulta a cotação de uma moeda em relação ao Real (BRL).

import requests
from datetime import datetime

def consultar_cotacao(moeda):

    url = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
    
    try:
        response = requests.get(url, timeout=10)
        
        # Verifica se a requisição foi bem-sucedida
        if response.status_code == 200:
            dados = response.json()
            chave = f"{moeda}BRL"
            
            if chave in dados:
                cotacao = dados[chave]
                return {
                    'moeda': cotacao['code'],
                    'nome': cotacao['name'],
                    'valor_atual': float(cotacao['bid']),
                    'maxima': float(cotacao['high']),
                    'minima': float(cotacao['low']),
                    'data_hora': cotacao['create_date']
                }
            else:
                return None
        else:
            return None
            
    except requests.exceptions.Timeout:
        print("Erro: Tempo de requisição excedido.")
        return None
    except requests.exceptions.ConnectionError:
        print("Erro: Falha na conexão com a API.")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")
        return None
    except Exception as e:
        print(f"Erro inesperado: {e}")
        return None

def formatar_data_hora(data_hora_str):
    """Formata a data e hora para um formato mais legível."""
    try:
        dt = datetime.strptime(data_hora_str, "%Y-%m-%d %H:%M:%S")
        return dt.strftime("%d/%m/%Y às %H:%M:%S")
    except:
        return data_hora_str

def exibir_cotacao(moeda):
    """Exibe a cotação de uma moeda de forma formatada."""
    print(f"\n{'='*60}")
    print(f"Consultando cotação: {moeda.upper()}/BRL")
    print(f"{'='*60}")
    
    resultado = consultar_cotacao(moeda.upper())
    
    if resultado:
        print(f"\n📊 Moeda: {resultado['nome']} ({resultado['moeda']})")
        print(f"💰 Valor Atual: R$ {resultado['valor_atual']:.4f}")
        print(f"📈 Máxima: R$ {resultado['maxima']:.4f}")
        print(f"📉 Mínima: R$ {resultado['minima']:.4f}")
        print(f"🕒 Última atualização: {formatar_data_hora(resultado['data_hora'])}")
    else:
        print(f"\n❌ Erro: Moeda '{moeda.upper()}' não encontrada ou erro na requisição.")
        print("Verifique se o código da moeda está correto (ex: USD, EUR, GBP, JPY)")
    
    print(f"{'='*60}\n")

def main():
    """Função principal do programa."""
    print("\n" + "="*60)
    print("        CONSULTA DE COTAÇÕES DE MOEDAS - BRL")
    print("="*60)
    
    while True:
        moeda = input("\nDigite o código da moeda (ex: USD, EUR, GBP, JPY) ou 'sair' para encerrar: ").strip()
        
        if moeda.lower() == 'sair':
            print("\n👋 Encerrando o programa. Até logo!")
            break
        
        if not moeda:
            print("❌ Por favor, digite um código de moeda válido.")
            continue
        
        exibir_cotacao(moeda)
        
        # Pergunta se deseja consultar outra moeda
        continuar = input("Deseja consultar outra moeda? (s/n): ").strip().lower()
        if continuar != 's':
            print("\n👋 Encerrando o programa. Até logo!")
            break

if __name__ == "__main__":
    main()
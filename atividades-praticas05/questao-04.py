#4 - Programa para calcular quantos dias a pessoa já viveu:

import datetime

def calcular_dias_vivos(data_nascimento: datetime.date) -> int:
    """
    Calcula o número de dias entre a data de nascimento e a data atual.

    Parâmetros:
    data_nascimento (datetime.date): A data de nascimento da pessoa.

    Retorna:
    int: O número total de dias vividos.
    """
    data_hoje = datetime.date.today()
    diferenca = data_hoje - data_nascimento
    
    # O objeto 'diferenca' tem um atributo '.days' que retorna o total de dias
    return diferenca.days

# --- Interação com Usuário e Programa Principal ---

if __name__ == "__main__":
    print("--- Calculadora de Dias Vivos ---")
    print("Por favor, digite sua data de nascimento.")

    while True:
        try:
            # Solicita a data de nascimento nos formatos esperados
            dia = int(input("Dia (ex: 15): "))
            mes = int(input("Mês (ex: 3): "))
            ano = int(input("Ano (ex: 2002): "))

            # Cria um objeto de data usando datetime.date()
            data_nascimento_obj = datetime.date(ano, mes, dia)
            
            # Validação simples: a data de nascimento não pode ser no futuro
            if data_nascimento_obj > datetime.date.today():
                print("Erro: Data de nascimento não pode ser no futuro. Tente novamente.")
                continue

            # Chama a função para fazer o cálculo
            dias_vivos = calcular_dias_vivos(data_nascimento_obj)

            # Exibe o resultado final
            print("\n--- Resultado ---")
            print(f"Você nasceu em: {data_nascimento_obj.strftime('%d/%m/%Y')}")
            print(f"Até hoje: {datetime.date.today().strftime('%d/%m/%Y')}, você já viveu {dias_vivos} dias.")

            break

        except ValueError:
            # Captura erros se o usuário digitar algo que não é um número
            print("Entrada inválida. Certifique-se de digitar números válidos para dia, mês e ano.")
        except OverflowError:
            # Captura erros se a data for totalmente inválida (ex: mês 30)
            print("Data inválida. Verifique se o dia/mês/ano estão corretos.")
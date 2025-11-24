#3- Conversor de Temperatura:

print("--- Conversor Simples de Temperatura (Celsius - °C ou Fahrenheit - °F) ---")

temperatura = float(input("Digite a temperatura: ")) #Solicita a temperatura e converte para float

unidade_origem = input("Unidade de origem (C° ou F°): ").strip().upper() #Solicita a unidade de origem (C° ou F°) e converte para maiúsculo

if unidade_origem == 'C':
    resultado = (temperatura * 9/5) + 32 #Converte Celsius para Fahrenheit
    unidade_destino = 'F'
    print(f"\n{temperatura:.2f} °C equivalem a {resultado:.2f} °F.")

elif unidade_origem == 'F':
    resultado = (temperatura - 32) * 5/9 #Converte Fahrenheit para Celsius
    unidade_destino = 'C'
    print(f"\n{temperatura:.2f} °F equivalem a {resultado:.2f} °C.")

else:
    print("\nErro: Unidade de origem inválida. Digite apenas '°C' ou '°F'.") #Caso o usuário digite uma letra diferente de C ou F

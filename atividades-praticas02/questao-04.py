"""4- Calculadora de Consumo de Combustível
Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:

* Distância percorrida: 300 km
* Combustível gasto: 25 litros
O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, incluindo o resultado final arredondado para duas casas decimais."""

distancia_percorrida = 300  #em km
combustivel_gasto = 25  #em litros

consumo_medio = distancia_percorrida / combustivel_gasto #O consumo médio é a distância total dividida pelo combustível gasto.

print("--- Consumo de Combustível ---")
print(f"Distância percorrida: {distancia_percorrida} km")
print(f"Combustível gasto: {combustivel_gasto} litros")
print("-" * 28) # Linha separadora
# Formata o resultado para duas casas decimais
print(f"Consumo médio: {consumo_medio:.2f} km/l")
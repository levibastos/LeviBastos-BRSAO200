'''3- Calculadora de Média Escolar
Crie um programa que calcula a média escolar de um aluno. Use as seguintes notas:

* Nota 1: 7.5
* Nota 2: 8.0
* Nota 3: 6.5
O programa deve calcular a média e exibir todas as notas e o resultado final, arredondando para duas casas decimais.'''

nota1 = 7.5
nota2 = 8.0
nota3 = 6.5

total_notas = 3
soma_notas = nota1 + nota2 + nota3
media = soma_notas / total_notas #A média aritmética é a soma de todas as notas dividida pelo número total de notas.

print("--- Boletim do Aluno ---")
print(f"Nota 1: {nota1:.2f}")
print(f"Nota 2: {nota2:.2f}")
print(f"Nota 3: {nota3:.2f}")
print("-" * 25) 
print(f"Média Final: {media:.2f}")
print("-" * 25) 
print("OBS: Média mínima para passar >= 7.0")
if media >= 7.0:
    print("Situação: Aprovado(a)!!!")
else:
    print("Situação: Reprovado(a)!!!")
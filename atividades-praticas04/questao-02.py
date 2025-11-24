#2 - Registro de Notas e Média da Turma

print("--- Calculadora de Média da Turma ---")

notas = [] #Lista para armazenar as notas dos alunos
soma_notas = 0 #Variável para controlar a soma total das notas

while True:
    try:
        nota_input = input("Digite a nota do aluno (ou 'fim' para terminar): ").strip().lower() #Loop infinito que permite adicionar múltiplas notas

        if nota_input == 'fim': #Condição de saída do loop
            break

        nota = float(nota_input) #Tenta converter a entrada para um número decimal (float)

        if 0 <= nota <= 10: #Validação de nota (numero no intervalo entre 0 e 10)
            notas.append(nota)  # Adiciona a nota à lista
            soma_notas += nota  # Adiciona à soma total
            print(f"Nota {nota} registrada.")
        else:
            print("Nota inválida. Digite um valor entre 0 e 10.")

    except ValueError:
        print("Entrada inválida. Por favor, digite um valor numérico ou 'fim'.") #Mensagem mostrada ao usuário caso não digite um número ou 'fim'

print("\n--- Resultados Finais ---") #Fim da coleta de notas

if len(notas) > 0: #Verifica se alguma nota foi registrada antes de calcular a média
    numero_de_alunos = len(notas) #Pega o numero de notas digitadas e conta como se cada nota fosse 1 aluno
    media_turma = soma_notas / numero_de_alunos

    print(f"Total de alunos registrados: {numero_de_alunos}")
    print(f"Soma total das notas: {soma_notas:.2f}")
    print(f"Média da turma: {media_turma:.2f}")
else:
    print("Nenhuma nota foi registrada. Não foi possível calcular a média da turma.")
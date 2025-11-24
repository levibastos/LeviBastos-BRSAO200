#1 - Calculadora com Tratamento de funções básicas:

print("--- Calculadora Básica (+, -, *, /) ---")

try:
    #Tenta solicitar e converter os números. Se falhar, o bloco 'except ValueError' é executado.
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    operacao = input("Escolha a operação (+, -, *, /): ").strip() #Se a conversão for bem-sucedida, continua pedindo a operação

    #Executa a operação com base na escolha do usuário
    if operacao == '+':
        resultado = num1 + num2
        print(f"\nResultado: {resultado:.2f}")

    elif operacao == '-':
        resultado = num1 - num2
        print(f"\nResultado: {resultado:.2f}")

    elif operacao == '*':
        resultado = num1 * num2
        print(f"\nResultado: {resultado:.2f}")

    elif operacao == '/':
        if num2 == 0:
            print("\nErro: Não é possível dividir por zero.")
        else:
            resultado = num1 / num2
            print(f"\nResultado: {resultado:.2f}")

    else:
        print("\nErro: Operação inválida. Use +, -, * ou /.")

except ValueError:
    print("\nErro: Entrada inválida. Certifique-se de digitar números válidos para o cálculo.") #É executado caso a conversão float() falhar

#4- Verificador de Ano Bissexto

print("--- Verificador de Ano Bissexto ---")

ano = int(input("Digite o ano (ex: 2024): ")) #Solicita o ano e converte diretamente para inteiro.

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0): #(Divisível por 4 E não divisível por 100) OU (Divisível por 400)
    print(f"\nO ano {ano} é bissexto.") #Se a condição acima for verdadeira, imprime que é bissexto
else:
    print(f"\nO ano {ano} não é bissexto.")#Caso contrário, imprime que não é bissexto
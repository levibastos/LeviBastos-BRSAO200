#1- Classificador de Idade:

idade = int(input("Por favor, digite sua idade: ")) #Solicita a idade ao usuário e converte a entrada para um número inteiro (int)

#Classifica a idade por categoria:
if idade >= 0 and idade <= 12:
    categoria = "Criança"
elif idade >= 13 and idade <= 17:
    categoria = "Adolescente"
elif idade >= 18 and idade <= 59:
    categoria = "Adulto"
else:
    categoria = "Idoso acima de 60anos ou idade inválida" #Esta categoria pega 60 anos ou mais, e também qualquer idade negativa

print(f"Sua categoria é: {categoria}")
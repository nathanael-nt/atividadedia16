#ex1
numero=float(input('digite um numero:'))
if numero>0:
    print('O numero é positivo')
elif numero<0:
    print('seu numero é negativo')
else:
    print('seu numero é zero')

#ex2

idade=int(input('qual a sua idade:'))
if idade >=18:
    print('você é maior de idade')
else:
    print('você é memor de idade')

#ex3
numero=int(input("Informe o número: "))
if numero/2==0:
  print("Número par")
else:
   print("Número ímpar")

#ex4
numero1=int(input("Informe o primeiro número: "))
numero2=int(input("Informe o segundo número: "))
if numero1>numero2:
 print(f"numero maior:{numero1} ")
else:
  print(f"numero maior:{numero2} ")

#ex5
valor=int(input("insira valor da compra: "))
if valor>100:
 print(f'valor final é R%{valor*0.90}')
else:
  print(f'O valor final é R${valor}')

#ex6
numero=float(input('Digite o número: '))
if numero%5==0:
  print("Número múltplo de 5: ")
else:
  print("Número não é múltplo de 5: ")
             
#ex7
nota1=float(input("Informe a primeira nota: "))
nota2=float(input("Informe a seguna nota: "))
nota3=float(input("Informe a terceira nota: "))
media=nota1+nota2+nota3/3
print(f'{media:.2f}')

#ex8
senha='python123_EFG'
senhausuario=input('digite a senha:')
if senha == senhausuario:
        
    print('Acesso permitido')
else:
    print('Senha incorreta')
 
#ex9

# Solicita a idade do usuário
idade = int(input("Digite a sua idade: "))
if idade < 5 or idade > 60:
    print("Você tem direito a entrada gratuita!")
else:
    print("Você não tem direito a entrada gratuita.")

#ex10

nota = float(input("Digite uma nota entre 0 e 10: "))

if 0 <= nota <= 10:
    print(f"Você inseriu a nota: {nota}")
else:
    print("Erro: valor inválido! A nota deve estar entre 0 e 10.")


#ex11

idade = int(input("Digite a sua idade: "))

if idade < 12:
    print("Você é uma criança.")
elif 12 <= idade <= 17:
    print("Você é um adolescente.")
else:
    print("Você é um adulto.")
#Ex12

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

if num1 >= num2 and num1 >= num3:
    maior = num1
elif num2 >= num1 and num2 >= num3:
    maior = num2
else:
    maior = num3

print(f"O maior número é: {maior}")

#Ex13

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if num2 == 0:
    print("Divisão não é possível, o divisor não pode ser zero.")
else:
    resultado = num1 / num2
    print(f"O resultado da divisão é: {resultado}")

#ex14


numero = float(input("Digite um número: "))

if 10 <= numero <= 50:
    print("O número está entre 10 e 50.")
else:
    print("O número não está entre 10 e 50.")

#ex15

media = float(input("Digite a média do aluno: "))

if media >= 7:
    print("Aluno aprovado.")
elif 5 <= media < 7:
    print("Aluno em recuperação.")
else:
    print("Aluno reprovado.")

#ex16

peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

imc = peso / (altura ** 2)

print(f"Seu IMC é: {imc:.2f}")

if imc < 18.5:
    print("Você está abaixo do peso.")
elif 18.5 <= imc < 25:
    print("Você está com peso normal.")
else:
    print("Você está acima do peso.")

 #ex17

lado1 = float(input("Digite o primeiro lado: "))
lado2 = float(input("Digite o segundo lado: "))
lado3 = float(input("Digite o terceiro lado: "))


if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    print("Os lados formam um triângulo.")
    
    if lado1 == lado2 == lado3:
        print("O triângulo é equilátero.")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("O triângulo é isósceles.")
    else:
        print("O triângulo é escaleno.")
else:
    print("Os lados não formam um triângulo.")

#ex18
usuario = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")

if usuario == "admin" and senha == "1234":
    print("Login bem-sucedido.")
else:
    print("Nome de usuário ou senha incorretos.")

#ex19


idade = int(input("Digite a sua idade: "))
if idade >= 18:
    print("Você pode dirigir.")
else:
    anos_faltam = 18 - idade
    print(f"Você ainda não pode dirigir. Faltam {anos_faltam} anos para você poder dirigir.")

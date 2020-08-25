num1 = int(input("Informe o primeiro número: "))
num2 = int(input("Informe o segundo número: "))
num3 = int(input("Informe o terceiro número: "))

maior = num1

if (num2>maior):
        maior = num2
if (num3>maior):
        maior = num3

print("O maior número é: ",maior)

menor = num1

if (num2<menor):
        menor = num2
if (num3<menor):
        menor = num3

print("O menor número é: ",menor)

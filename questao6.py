num1 = float(input("Informe o primeiro número: "))
num2 = float(input("Informe o segundo número: "))
num3 = float(input("Informe o terceiro número: "))

if (num1>num2 and num1>num3):
    print("O maior número é: ", num1)
elif (num2>num1 and num2>num3):
    print("O maior número é: ", num2)
elif (num3>num1 and num3>num2):
    print("O maior número é: ", num3)

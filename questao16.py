a = float(input("Informe o valor 'a' da equação de segundo grau: "))
b = float(input("Informe o valor 'b' da equação de segundo grau: "))
c = float(input("Informe o valor 'c' da equação de segundo grau: "))

if(a==0):
    print("Não é uma equação de segundo grau")

else:

    delta = b*b - 4*a*c
    if(delta<0):
        print("A equação não tem raízes reais")
    elif(delta==0):
        print("A equação possui uma raiz real")
    elif(delta>0):
        print("A equação tem duas raízes reais")
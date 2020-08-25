lado1 = float(input("Informe o primeiro lado do triângulo: "))
lado2 = float(input("Informe o segundo lado do triângulo: "))
lado3 = float(input("Informe o terceiro lado do triângulo: "))

if(lado1+lado2<lado3 or lado2+lado3<lado1 or lado1+lado3<lado2):
    print("Os valores não correspondem à um triângulo")

else:

    if(lado1==lado2 and lado2==lado3):
        print("O triângulo em questão é Equilatero")

    elif(lado1==lado2)or(lado1==lado3)or(lado2==lado3):
        print("O triâÃngulo em questão é Isósceles")

    elif(lado1!=lado2)and(lado1!=lado3)and(lado2!=lado3):
        print("O triângulo em questão é Escaleno")


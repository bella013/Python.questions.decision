turno = str(input("Qual o turno em que você estuda? "))
if(turno=="M" or turno=="Matutino" or turno=="m" or turno=="matutino"):
    print("Bom Dia")

elif(turno=="V" or turno=="Vespertino" or turno=="v" or turno=="vespertino"):
    print("Bom Tarde")

elif(turno=="N" or turno=="Noturno" or turno=="n" or turno=="noturno"):
    print("Bom Noite")

else:
    print("Valor Inválido")
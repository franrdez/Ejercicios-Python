nota1=int(input("Ingrese primer nota: "))
nota2=int(input("Ingrese segunda nota: "))
nota3=int(input("Ingrese tercer nota: "))

prom=(nota1+nota2+nota3)/3
if prom>=7:
    print("Aprobado")
else:
    if prom>=4:
        print("Regular")
    else:
        print("Suspenso")

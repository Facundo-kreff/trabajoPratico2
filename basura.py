#2019_AED_TP2_Kreff_80791[1k11]


def pasada_auto():
    import random
    seleccion = random.randrange(1, 4)
    if seleccion == 1:
        tipo = "Moto"
        costo = 20
        import random
        a = random.randrange(1,3)
        if a==1:
            letras=random.choice(("ABCDEFGHYJKLMOPQRSTUVWXYZ"))+random.choice(("ABCDEFGHYJKLMOPQRSTUVWXYZ"))+random.choice(("ABCDEFGHYJKLMOPQRSTUVWXYZ"))
            numeros=str(random.randrange(10))+str(random.randrange(10))+str(random.randrange(10))
            patente=letras+str(numeros)
        else:
            letras1=random.choice(("ABCDEFGHYJKLMOPQRSTUVWXYZ"))+random.choice(("ABCDEFGHYJKLMOPQRSTUVWXYZ"))
            numeros=str(random.randrange(10))+str(random.randrange(10))+str(random.randrange(10))
            letras2=random.choice(("ABCDEFGHYJKLMOPQRSTUVWXYZ"))+random.choice(("ABCDEFGHYJKLMOPQRSTUVWXYZ"))
            patente=letras1+str(numeros)+letras2
    elif seleccion == 2:
        tipo = "Auto"
        costo = 40
        import random
        a = random.randrange(1,3)
        if a==1:
            letras=random.choice(("ABCDEFGHYJKLMOPQRSTUVWXYZ"))+random.choice(("ABCDEFGHYJKLMOPQRSTUVWXYZ"))+random.choice(("ABCDEFGHYJKLMOPQRSTUVWXYZ"))
            numeros=str(random.randrange(10))+str(random.randrange(10))+str(random.randrange(10))
            patente=letras+str(numeros)
        else:
            letras1=random.choice(("ABCDEFGHYJKLMOPQRSTUVWXYZ"))+random.choice(("ABCDEFGHYJKLMOPQRSTUVWXYZ"))
            numeros=str(random.randrange(10))+str(random.randrange(10))+str(random.randrange(10))
            letras2=random.choice(("ABCDEFGHYJKLMOPQRSTUVWXYZ"))+random.choice(("ABCDEFGHYJKLMOPQRSTUVWXYZ"))
            patente=letras1+str(numeros)+letras2
    elif seleccion == 3:
        tipo = "Camion"
        costo = 80
        import random
        a = random.randrange(1,3)
        if a==1:
            letras=random.choice(("ABCDEFGHYJKLMOPQRSTUVWXYZ"))+random.choice(("ABCDEFGHYJKLMOPQRSTUVWXYZ"))+random.choice(("ABCDEFGHYJKLMOPQRSTUVWXYZ"))
            numeros=str(random.randrange(10))+str(random.randrange(10))+str(random.randrange(10))
            patente=letras+str(numeros)
        else:
            letras1=random.choice(("ABCDEFGHYJKLMOPQRSTUVWXYZ"))+random.choice(("ABCDEFGHYJKLMOPQRSTUVWXYZ"))
            numeros=str(random.randrange(10))+str(random.randrange(10))+str(random.randrange(10))
            letras2=random.choice(("ABCDEFGHYJKLMOPQRSTUVWXYZ"))+random.choice(("ABCDEFGHYJKLMOPQRSTUVWXYZ"))
            patente=letras1+str(numeros)+letras2
    return tipo, costo, patente





def pasada_manual():
    print("Tipos de Vehiculos")
    print("1: Moto. ")
    print("2: Auto.")
    print("3: Camión.")
    seleccion=0
    while seleccion == 0 or seleccion >= 4:
        seleccion=int(input("Ingrese Numero de Opcion: "))
        if seleccion == 1:
            tipo = "Moto"
            costo = 20
        elif seleccion == 2:
            tipo = "Auto"
            costo = 40
        elif seleccion == 3:
            tipo = "Camion"
            costo = 80
        else:
            seleccion=0
            print("ERROR: Vuelva a Ingresar Numero de Opcion: ")
    return tipo, costo



a=pasada_auto()
print("Tipo de Vehiculo :",a[0])
print("Costo De Pasada :",a[1])
print("Patente: ", a[2])

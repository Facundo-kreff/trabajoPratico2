# 2019_AED_TP2_Kreff_80791[1k11]

# Funcion Opcion 2: Carga Manual De pases
def pasada_manual(n1):
    global tipo
    print("\033[1;31m"+"Tipos de Vehiculos"+'\033[0;m')
    print("\x1b[1;33m"+"1: Moto. ")
    print("2: Auto.")
    print("3: Camión." + '\033[0;m')
    seleccion = 0
    while seleccion == 0 or seleccion >= 4:
        seleccion = int(input("\033[1;31m" + "Ingrese Numero de Opcion: " + '\033[0;m'))
        if seleccion == 1:
            tipo = "Moto"
            costo = 20
            import random
            a = random.randrange(1, 3)
            if a == 1:
                letras = random.choice(("ABCDEFGHYJKLMOPQRSTUVWXYZ")) + random.choice(
                    ("ABCDEFGHYJKLMOPQRSTUVWXYZ")) + random.choice(("ABCDEFGHYJKLMOPQRSTUVWXYZ"))
                numeros = str(random.randrange(10)) + str(random.randrange(10)) + str(random.randrange(10))
                patente = letras + str(numeros)
            else:
                letras1 = random.choice(("ABCDEFGHYJKLMOPQRSTUVWXYZ")) + random.choice(("ABCDEFGHYJKLMOPQRSTUVWXYZ"))
                numeros = str(random.randrange(10)) + str(random.randrange(10)) + str(random.randrange(10))
                letras2 = random.choice(("ABCDEFGHYJKLMOPQRSTUVWXYZ")) + random.choice(("ABCDEFGHYJKLMOPQRSTUVWXYZ"))
                patente = letras1 + str(numeros) + letras2
        elif seleccion == 2:
            tipo = "Auto"
            costo = 40
            import random
            a = random.randrange(1, 3)
            if a == 1:
                letras = random.choice(("ABCDEFGHYJKLMOPQRSTUVWXYZ")) + random.choice(
                    ("ABCDEFGHYJKLMOPQRSTUVWXYZ")) + random.choice(("ABCDEFGHYJKLMOPQRSTUVWXYZ"))
                numeros = str(random.randrange(10)) + str(random.randrange(10)) + str(random.randrange(10))
                patente = letras + str(numeros)
            else:
                letras1 = random.choice(("ABCDEFGHYJKLMOPQRSTUVWXYZ")) + random.choice(("ABCDEFGHYJKLMOPQRSTUVWXYZ"))
                numeros = str(random.randrange(10)) + str(random.randrange(10)) + str(random.randrange(10))
                letras2 = random.choice(("ABCDEFGHYJKLMOPQRSTUVWXYZ")) + random.choice(("ABCDEFGHYJKLMOPQRSTUVWXYZ"))
                patente = letras1 + str(numeros) + letras2
        elif seleccion == 3:
            tipo = "Camion"
            costo = 80
            import random
            op = random.randrange(1, 3)
            if op == 1:
                letras = random.choice(("ABCDEFGHYJKLMOPQRSTUVWXYZ")) + random.choice(
                    ("ABCDEFGHYJKLMOPQRSTUVWXYZ")) + random.choice(("ABCDEFGHYJKLMOPQRSTUVWXYZ"))
                numeros = str(random.randrange(10)) + str(random.randrange(10)) + str(random.randrange(10))
                patente = letras + str(numeros)
            else:
                letras1 = random.choice(("ABCDEFGHYJKLMOPQRSTUVWXYZ")) + random.choice(("ABCDEFGHYJKLMOPQRSTUVWXYZ"))
                numeros = str(random.randrange(10)) + str(random.randrange(10)) + str(random.randrange(10))
                letras2 = random.choice(("ABCDEFGHYJKLMOPQRSTUVWXYZ")) + random.choice(("ABCDEFGHYJKLMOPQRSTUVWXYZ"))
                patente = letras1 + str(numeros) + letras2
        else:
            seleccion = 0
            print("ERROR: Vuelva a Ingresar Numero de Opcion: ")
    return tipo, costo, patente, n1


# Funcion Opcion 2: carga pases automaticamente
def pasada_auto(n1):
    import random
    seleccion = random.randrange(1, 4)
    if seleccion == 1:
        tipo = "Moto"
        costo = 20
        import random
        a = random.randrange(1, 3)
        if a == 1:
            letras = random.choice(("ABCDEFGHYJKLMOPQRSTUVWXYZ")) + random.choice(
                ("ABCDEFGHYJKLMOPQRSTUVWXYZ")) + random.choice(("ABCDEFGHYJKLMOPQRSTUVWXYZ"))
            numeros = str(random.randrange(10)) + str(random.randrange(10)) + str(random.randrange(10))
            patente = letras + str(numeros)
        else:
            letras1 = random.choice(("ABCDEFGHYJKLMOPQRSTUVWXYZ")) + random.choice(("ABCDEFGHYJKLMOPQRSTUVWXYZ"))
            numeros = str(random.randrange(10)) + str(random.randrange(10)) + str(random.randrange(10))
            letras2 = random.choice(("ABCDEFGHYJKLMOPQRSTUVWXYZ")) + random.choice(("ABCDEFGHYJKLMOPQRSTUVWXYZ"))
            patente = letras1 + str(numeros) + letras2
    elif seleccion == 2:
        tipo = "Auto"
        costo = 40
        import random
        a = random.randrange(1, 3)
        if a == 1:
            letras = random.choice(("ABCDEFGHYJKLMOPQRSTUVWXYZ")) + random.choice(
                ("ABCDEFGHYJKLMOPQRSTUVWXYZ")) + random.choice(("ABCDEFGHYJKLMOPQRSTUVWXYZ"))
            numeros = str(random.randrange(10)) + str(random.randrange(10)) + str(random.randrange(10))
            patente = letras + str(numeros)
        else:
            letras1 = random.choice(("ABCDEFGHYJKLMOPQRSTUVWXYZ")) + random.choice(("ABCDEFGHYJKLMOPQRSTUVWXYZ"))
            numeros = str(random.randrange(10)) + str(random.randrange(10)) + str(random.randrange(10))
            letras2 = random.choice(("ABCDEFGHYJKLMOPQRSTUVWXYZ")) + random.choice(("ABCDEFGHYJKLMOPQRSTUVWXYZ"))
            patente = letras1 + str(numeros) + letras2
    elif seleccion == 3:
        tipo = "Camion"
        costo = 80
        import random
        a = random.randrange(1, 3)
        if a == 1:
            letras = random.choice(("ABCDEFGHYJKLMOPQRSTUVWXYZ")) + random.choice(
                ("ABCDEFGHYJKLMOPQRSTUVWXYZ")) + random.choice(("ABCDEFGHYJKLMOPQRSTUVWXYZ"))
            numeros = str(random.randrange(10)) + str(random.randrange(10)) + str(random.randrange(10))
            patente = letras + str(numeros)
        else:
            letras1 = random.choice(("ABCDEFGHYJKLMOPQRSTUVWXYZ")) + random.choice(("ABCDEFGHYJKLMOPQRSTUVWXYZ"))
            numeros = str(random.randrange(10)) + str(random.randrange(10)) + str(random.randrange(10))
            letras2 = random.choice(("ABCDEFGHYJKLMOPQRSTUVWXYZ")) + random.choice(("ABCDEFGHYJKLMOPQRSTUVWXYZ"))
            patente = letras1 + str(numeros) + letras2
    return tipo, costo, patente, n1


# Funcion Opcion 1: Definir forma de pago
def carg_for():
    print("\033[1;33m" + "1. Manual")
    print("2. Automatico")
    op = 0
    while op == 0 or op >= 3:
        op = int(input("\033[1;31m" + "Seleccione Forma De Pago: " + '\033[0;m'))
        if op == 1:
            form_pag = "Manual"
            return form_pag
        elif op == 2:
            form_pag = "Automatico"
            return form_pag
        else:
            print("Opcion No Contemplada. vuelva a Intentar" + '\033[0;m')


# Menu
selec = 0
while selec != 4:
    print("\033[4;34m" + "Casilla De Peaje N° 1" + "\033[1;34m" + '\033[0;m')
    print("\x1b[1;33m" + "1. Definir forma de carga(Definir Antes De Entrar En La Opcion 2)")
    print("2. Procesar las pasadas")
    print("3. Ver Resultados")
    print("4. Salir" + '\033[0;m')
    form_pag0 = selec
    selec = int(input("\033[1;31m" + "Seleccione Opcion: " + '\033[0;m'))
    print()
    # Opcion 1
    if selec == 1:
        print("\033[4;34m" + "Forma de Carga" + '\033[0;m')
        form_pag = carg_for()
        print()
    # Opcion 2
    elif selec == 2:

        if form_pag0 == 0 or form_pag0 >= 2:
            print("\033[1;31m" + "Primero seleccione forma de carga" + '\033[0;m')
            print()
        elif form_pag == "Manual":
            print("\033[4;34m" + "Proceso De Carga" + '\033[0;m')
            import time

            dif = 0
            ti = time.time()
            datos = []
            while dif < 20:
                # proceso a ejecutar en cada vuelta del ciclo...
                time.sleep(1)
                tf = time.time()
                dif = int(tf - ti)
                print('Tiempo:', dif)
                print("\033[1;31m" + "Nueva Pasada?" + '\033[0;m')
                print("\x1b[1;33m""1. Si" + '\033[0;m')
                act = int(input("\033[1;31m" + "Opcion seleccionada: " + '\033[0;m'))
                if dif > 20:
                    print("\033[4;31m" + "Se Termino El Turno!" + '\033[0;m')
                    break
                elif act == 1 and dif < 20:
                    a = pasada_manual(dif)
                    datos += [a]
            print("Datos recolectados en 4: ")
            print(datos)

        elif form_pag == "Automatico":
            print("\033[4;34m" + "Proceso De Carga" + '\033[0;m')


    # Opcion 3
    elif selec == 3:
        print()
    # Opcion 4
    elif selec == 4:
        print("\033[1;42m" + "Que Tenga Un Buen Dia ;)         " + '\033[0;m')

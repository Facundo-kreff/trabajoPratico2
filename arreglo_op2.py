#2019_AED_TP2_Kreff_80791[1k11]


def carg_for():
    print("\033[1;33m"+"1. Manual")
    print("2. Automatico")
    op=0
    while op == 0 or op >= 3:
        op=int(input("\033[1;31m"+"Seleccione Forma De Pago: "+'\033[0;m'))
        if op==1:
            form_pag="Manual"
            return form_pag
        elif op==2:
            form_pag="Automatico"
            return form_pag
        else:
            print("Opcion No Contemplada. vuelva a Intentar"+'\033[0;m')


#Menu
selec=0
while selec != 4:
    print("\033[4;34m"+"Casilla De Peaje N° 1"+"\033[1;34m"+'\033[0;m')
    print("\x1b[1;33m"+"1. Definir forma de carga(Definir Antes De Entrar En La Opcion 2)")
    print("2. Procesar las pasadas")
    print("3. Ver Resultados")
    print("4. Salir"+'\033[0;m')
    print("\033[1;31m"+"")
    aaaa=selec
    selec=int(input("Ingrese Numero de Opcion: "+'\033[0;m'))

    #Opcion 1
    if selec == 1:
        form_pag=carg_for()
        form_pag1=form_pag
        asdf="none"
    #Opcion 2
    elif selec==2 :
        if aaaa == 0 or aaaa >= 2:
            print("Primero seleccione forma de carga")
        elif form_pag == "Manual":
            print(1)
        elif form_pag1 == "Automatico":
            print(2)


    #Opcion 3
    elif selec==3:
        print()
    #Opcion 4
    elif selec==4:
        print("\033[1;42m"+"Que Tenga Un Buen Dia ;)         "+'\033[0;m')







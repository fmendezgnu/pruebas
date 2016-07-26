print "Bienvenido a Calentar Agua \n"

pot=input("Inserte la potencia en W: ")
vh20=input("Inserte la cantidad de agua a calentar en litros: ")
vtot=input("Inserte volumen total del recipiente en litros: ")

#Bucle comparador de volumenes
while vtot<=vh20:
    print "\nAlgun volumen es incorrecto\n"
    elec=input("Inserte 1 para volver a escribir el volumen total o 2 para volver a poner la cantidad de agua: ")
    if elec == 1:
        vtot=input("\nInserte el volumen total del recipiente: ")
        while vtot<vh20:
            print "\nEl volumen insertado es mayor al agua a calentar, por favor inserte otro volumen \n"
            vtot=input("Inserte el volumen total del recipiente: ")
            continue
        continue
    elif elec == 2:
        vh20=input("\nInserte la cantidad de agua a calentar: ")
        while vtot<vh20:
            print "\nLa cantidad insertada es mayor a la capacidad del recipiente, ingrese correctamente la cantidad de agua a calentar \n"
            vh20=input("Inserte la cantidad de agua a calentar: ")
            continue
    else:
        elec=input("No, Inserte 1 para volver a escribir el volumen total o 2 para volver a poner la cantidad de agua: ")
        continue

tamb=input("Inserte la temperatura inicial en C: ")
tfin=input("Inserte la temperatura final en C: ")

#Comparador de temperaturas
if tfin<=tamb:
    print "\nNo necesitas calentar el agua"

#Datos Internos
#Densidad del agua en Kg/L
dens=1
#Calor Especifico del agua en J/kgK
cesp=4184
masa=dens*vh20

#Calculo Principal
if vtot>=vh20:
    if tfin>tamb:
        energia=masa*cesp*(tfin-tamb)
        tiempo=(energia/pot)/60
        print "\nEl tiempo a calentar el agua es de "+str(tiempo)+" minutos"

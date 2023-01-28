""" 4- Agregue una nueva mejora al programa para que se le pida al usuario la forma de pago y aplique un descuento o interés sobre el total según corresponda:
a- Efectivo: 5% de descuento sobre el total
b- Debito: 5% de descuento sobre el total
c- Crédito:
1 cuota: 0% de interés sobre el total
3 cuotas: 10% de interés sobre el total
6 cuotas: 25% de interés sobre el total
12 cuotas: 38% de interés sobre el total """

costo1 = 15000
costo2 = 23000
costo3 = 38000
costo4 = 55.500

destino=float( input("ingrese el numero de su destino: "))
pasajes=int(input("ingrese la cantidad de pasajes: "))
metodoDePago=input("¿efectivo, debito o credito?")

if metodoDePago=="efectivo" or metodoDePago=="debito":

    if pasajes<=2:
        if destino == 1: 
            print("usted debe abonar "+str( costo1 * pasajes*0.95) )
        elif destino==2:
            print("usted debe abonar "+str( costo2 *pasajes *0.95))
        elif destino ==3:
            print("usted debe abonar "+str( costo3*pasajes *0.95))
        elif destino ==4:
         print("usted debe abonar "+ str( costo4*pasajes *0.95))
    elif pasajes<=4:
        if destino == 1: 
            print("usted debe abonar "+str( costo1 * pasajes*0.95*0.95) )
        elif destino==2:
            print("usted debe abonar "+str( costo2 *pasajes *0.95*0.95))
        elif destino ==3:
            print("usted debe abonar "+str( costo3*pasajes *0.95*0.95))
        elif destino ==4:
            print("usted debe abonar "+ str( costo4*pasajes*0.95 *0.95))
    elif pasajes<=8:
            if destino == 1: 
                print("usted debe abonar "+str( costo1 * pasajes*0.9*0.95) )
            elif destino==2:
                print("usted debe abonar "+str( costo2 *pasajes*0.9 *0.95))
            elif destino ==3:
                print("usted debe abonar "+str( costo3*pasajes*0.9 *0.95))
            elif destino ==4:
                print("usted debe abonar "+ str( costo4*pasajes*0.9 *0.95))
    elif    8<pasajes:
            if destino == 1: 
                print("usted debe abonar "+str( costo1 * pasajes *0.85*0.95) )
            elif destino==2:
                print("usted debe abonar "+str( costo2 *pasajes *0.85*0.95))
            elif destino ==3:
                print("usted debe abonar "+str( costo3*pasajes*0.85 *0.95))
            elif destino ==4:
                print("usted debe abonar "+ str( costo4*pasajes*0.85 *0.95))
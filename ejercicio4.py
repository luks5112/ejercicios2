""" 1- Escribir un programa para una agencia de viajes la cual ofrece 4 
destinos posibles con la siguiente lista de precios:
a- destino1: $ 15.000
b- destino2: $ 23.000
c- destino3: $ 38.000
d- destino4: $55.500
Se debe pedir al usuario que ingrese el destino y se luego brindar por pantalla el precio del mismo.
2- Agregar al programa anterior la posibilidad de pedir al usuario que ingrese la 
cantidad de pasajes que desea comprar y mostrar el total a pagar.
3- Mejorar el programa para que aplique un descuento según los siguientes criterios:
a- Hasta 2 pasajes: 0% de descuento
b- De 3 a 4 pasajes: 5 % de descuento
c- De 5 a 8 pasajes: 10% de descuento
d- Mas de 8 pasajes: 15% de descuento
4- Agregue una nueva mejora al programa para que
 se le pida al usuario la forma de pago y aplique un descuento o interés sobre el total según corresponda:
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
""" Mejorar el programa para que aplique un descuento según los siguientes criterios:
a- Hasta 2 pasajes: 0% de descuento
b- De 3 a 4 pasajes: 5 % de descuento
c- De 5 a 8 pasajes: 10% de descuento
d- Mas de 8 pasajes: 15% de descuento """

costo1 = 15000
costo2 = 23000
costo3 = 38000
costo4 = 55.500

destino=float( input("ingrese el numero de su destino: "))
pasajes=int(input("ingrese la cantidad de pasajes: "))

if pasajes<=2:
    if destino == 1: 
     print("usted debe abonar "+str( costo1 * pasajes) )
    elif destino==2:
     print("usted debe abonar "+str( costo2 *pasajes ))
    elif destino ==3:
     print("usted debe abonar "+str( costo3*pasajes ))
    elif destino ==4:
        print("usted debe abonar "+ str( costo4*pasajes ))
elif pasajes<=4:
     if destino == 1: 
         print("usted debe abonar "+str( costo1 * pasajes*0.95) )
     elif destino==2:
         print("usted debe abonar "+str( costo2 *pasajes *0.95))
     elif destino ==3:
         print("usted debe abonar "+str( costo3*pasajes *0.95))
     elif destino ==4:
        print("usted debe abonar "+ str( costo4*pasajes*0.95 ))
elif pasajes<=8:
        if destino == 1: 
         print("usted debe abonar "+str( costo1 * pasajes*0.9) )
        elif destino==2:
         print("usted debe abonar "+str( costo2 *pasajes*0.9 ))
        elif destino ==3:
         print("usted debe abonar "+str( costo3*pasajes*0.9 ))
        elif destino ==4:
         print("usted debe abonar "+ str( costo4*pasajes*0.9 ))
elif    8<pasajes:
        if destino == 1: 
         print("usted debe abonar "+str( costo1 * pasajes *0.85) )
        elif destino==2:
         print("usted debe abonar "+str( costo2 *pasajes *0.85))
        elif destino ==3:
         print("usted debe abonar "+str( costo3*pasajes*0.85 ))
        elif destino ==4:
         print("usted debe abonar "+ str( costo4*pasajes*0.85 ))
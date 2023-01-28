""" 2- Agregar al programa anterior la posibilidad de pedir al usuario que ingrese
 la cantidad de pasajes que desea comprar y mostrar el total a pagar. """

costo1 = 15000
costo2 = 23000
costo3 = 38000
costo4 = 55.500

destino=float( input("ingrese el numero de su destino: "))
pasajes=int(input("ingrese la cantidad de pasajes: "))
if destino == 1: 
    print("usted debe abonar "+str( costo1 * pasajes) )
elif destino==2:
    print("usted debe abonar "+str( costo2 *pasajes ))
elif destino ==3:
    print("usted debe abonar "+str( costo3*pasajes ))
elif destino ==4:
    print("usted debe abonar "+ str( costo4*pasajes ))

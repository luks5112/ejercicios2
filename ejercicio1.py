""" 1- Escribir un programa para una agencia de viajes la cual ofrece 4 destinos 
posibles con la siguiente lista de precios:
a- destino1: $ 15.000
b- destino2: $ 23.000
c- destino3: $ 38.000
d- destino4: $55.500
Se debe pedir al usuario que ingrese el destino y se luego brindar por pantalla el precio del mismo. """

costo1 = 15000
costo2 = 23000
costo3 = 38000
costo4 = 55.500

destino=float( input("ingrese el numero de su destino "))
if destino == 1: 
    print("usted debe abonar "+str( costo1 ) )
elif destino==2:
    print("usted debe abonar "+str( costo2 ))
elif destino ==3:
    print("usted debe abonar "+str(costo3))
elif destino ==4:
    print("usted debe abonar "+ str(costo4))

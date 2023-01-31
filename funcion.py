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
destino = float( input("ingrese el numero de su destino: "))
pasajes = int(input("ingrese la cantidad de pasajes: "))
metodoPago = input("¿efectivo, debito o credito? ")


def cuantoSale( destino , pasajes):
        if destino == 1: 
            return     costo1 * pasajes
        elif destino==2:
            return     costo2 *pasajes 
        elif destino ==3:
            return     costo3* pasajes 
        elif destino ==4:
            return     costo4* pasajes 
""" consulta: si quisiera mostrar el descuento aplicado al usuario? me puede devolver dos 
cosas en un mismo return """


def conPrimerDescuento(destino, pasajes):
    if pasajes<=2:
        return  cuantoSale(destino, pasajes)
    elif  pasajes<=4:
        return  cuantoSale(destino, pasajes)*0.95
    elif pasajes<=8:
        return  cuantoSale(destino, pasajes)*0.9
    else:
        return  cuantoSale(destino, pasajes)*0.85



def cuantoPago(destino, pasajes, metodoPago):
    if metodoPago=="debito" or metodoPago=="efectivo":
        return  conPrimerDescuento(destino,pasajes)*0.95
    else:
        cuotas=int(input("¿1,3,6 o 12 cuotas?: "))
        if cuotas==1:
            return conPrimerDescuento(destino, pasajes)
        elif cuotas==3:
            return conPrimerDescuento(destino, pasajes)*1.1
        elif cuotas==6:
            return conPrimerDescuento(destino,pasajes)*1.25
        elif cuotas==12:
            return conPrimerDescuento(destino, pasajes)*1.38
            """ si el usuario diera otro numero como le digo que no puede """




sale = cuantoSale(destino, pasajes)
pagoConPrimerDescuento=conPrimerDescuento(destino, pasajes)
pago=cuantoPago(destino, pasajes, metodoPago)

print("El viaje le sale "+str(sale)+" por la cantidad de pasajes que compro figura en "+str(pagoConPrimerDescuento)+" pero por el metodo de pago termina quedando en: "+str(pago))

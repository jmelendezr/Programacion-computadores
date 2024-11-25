productos = int(input("Ingrese cuantos productos del mismo tipo lleva:"))
if (productos < 5):
    print ("No aplica descuento")
elif ((productos >=5) & (productos <10)):
    print ("El descuento es del 5%")
elif ((productos >=10) & (productos <20)):
    print ("El descuento es del 10%")
elif (productos >=20):
    print ("El descuento es del 20%")
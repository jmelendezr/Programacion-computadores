import math 
r = int(input("Ingrese el radio del circulo: "))
def area_circulo(r):
    area = math.pi * r ** 2
    return area
def perim_circulo(r):
    perim = 2 * math.pi * r
    return perim
def volum_circulo(r):
    volum = (4/3) * math.pi * r ** 3
    return volum
resultado_1 = area_circulo(r)
resultado_2 = perim_circulo(r)
resultado_3 = volum_circulo(r)
print ("El area del circulo es:" , resultado_1)
print ("El perimetro del circulo es:" , resultado_2)
print ("El volumen de la esfera es:" , resultado_3)
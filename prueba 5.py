def valor_absoluto(x):
    if x >= 0:
        valor = x
    else :
        valor = -x
    return valor
x= float(input("Ingrese un numero real x: "))
valor_abs = valor_absoluto(x)
print ("El valor absoluto de "+ str(x), end=" ")
print ("es "+ str(str(valor_abs)))
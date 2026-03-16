def perimetro(l1, l2, l3):
    res=l1+l2+l3
    return res

print('********* perimetro de un triangulo *********')
l1=int(input('ingresa el valor del primer lado:'))
l2=int(input('ingresa el valor del segundo lado:'))
l3=int(input('ingresa el valor del tercer lado:'))
print('El perimetro del triangulo es: ',perimetro(l1,l2,l3))
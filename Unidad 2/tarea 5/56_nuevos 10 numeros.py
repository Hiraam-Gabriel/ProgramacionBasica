print("*******nuevos numeros*******")
lista=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
res="si"
while res=="si":
    numero=int(input("ingresa un numero:"))
    print("deseas ingresar otro numero","si","o","no")
    lista.append(numero)
    lista.sort()
    res=input()
    print("el numero que sigue es:",lista)
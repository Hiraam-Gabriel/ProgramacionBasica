print('*******almacen********')
lista=[]
res="si"
while res=="si":
    objeto=input("ingresa el objeto:")
    print("deseas ingresar otro objeto","si","o","no")
    lista.append(objeto)
    lista.sort()
    res=input()
    
print("estos son tus objetos",lista)
print("******Crea tu lista******")
print("de que tipo es tu lista?","texto","o","numeros")
res=input()
lista=[]
if res=='texto':
    opcion=0
    while opcion<6:
        print("1.agregar valores")
        print('2.elimina valores')
        print('3.ordenar la lista modificandola diractamente')
        print("4.ordenar la lista generandola nuevamente")
        print('5.buscar elemento')
        print("6.salir")
        print('elige una opcion')
        opcion=int(input())
        if opcion==1:
            print("agrega una palabras")
            pal=input()
            lista.append(pal)
            print(lista)
        elif opcion==2:
            print("como quieres eliminar el valor?")
            print("1.por indice")
            print("2.por palabra")
            opcEliminar=int(input())
            if opcEliminar==1:
                print("que pocision quieres eliminar?")
                posicio=int(input())
                lista.pop(posicio)
                print(lista)
            else:
                print("que palabra quieres eliminar?")
                palabra=input()
                lista.remove(palabra)
                print(lista)
        elif opcion==3:
            print("ordenar la lista")
            lista.sort()
            print(lista)
        elif opcion==4:
            print("ordenar en una nueva lista")
            nueva_lista=sorted(lista)
            print(nueva_lista)
        elif opcion==5:
            print("buscar un elemento")
            busqueda=input()
            if busqueda in lista:
                print("el elemento se encuentra en la posicion",lista.index(busqueda))
            else:
                print("ese elemento no esta en la lista")
else:
    print('numero')
    opcion=0
    while opcion<7:
        print("1.agregar valores")
        print('2.elimina valores')
        print('3.ordenar la lista modificandola diractamente')
        print("4.ordenar la lista generandola nuevamente")
        print('5.buscar elemento')
        print("6.calcula la su maximo,minimo,suma y promrdio")
        print("7.salir")
        print('elige una opcion')
        opcion=int(input())
        if opcion==1:
            print("agrega una numero")
            num=float(input())
            lista.append(num)
            print(lista)
        elif opcion==2:
            print("como quieres eliminar el valor?")
            print("1.por indice")
            print("2.por palabra")
            opcEliminar=int(input())
            if opcEliminar==1:
                print("que pocision quieres eliminar?")
                posicio=int(input())
                lista.pop(posicio)
                print(lista)
            else:
                print("que numero quieres eliminar?")
                numero=input()
                lista.remove(float(numero))
                print(lista)
        elif opcion==3:
            print("ordenar la lista")
            lista.sort()
            print(lista)
        elif opcion==4:
            print("ordenar en una nueva lista")
            nueva_lista=sorted(lista)
            print(nueva_lista)
        elif opcion==5:
            print("buscar un elemento")
            busqueda=float(input())
            if busqueda in lista:
                print("el elemento se encuentra en la posicion",lista.index(busqueda))
            else:
                print("ese elemento no esta en la lista")
        elif opcion==6:
            print("1.calcula el maximo")
            print('2. calcular el minimo')
            print('3. calcula la suma')
            print('4.calcula el promedio')
            opcionCalcula=int(input())
            if opcionCalcula==1:
                maxi=max(lista)
                print("este el el valor maximo",maxi)
            elif opcionCalcula==2:
                min=min(lista)
                print('este es el valor minimo',min)
            elif opcionCalcula==3:
                suma=sum(lista)
                print("esta es la suma",suma)
            elif opcionCalcula==4:
                pro= sum(lista)/len(lista)
                print("este es el promedio",pro)
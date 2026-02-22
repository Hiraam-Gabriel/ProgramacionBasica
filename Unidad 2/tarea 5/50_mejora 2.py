print("********Almacen********")
lista_nom=["mesa","silla","refrigelador","estufa","television"]
lista_clave=[1957,6834,8642,3641,7552]
lista_piezas=[10,120,5,7,3]
res="si"
while res=='si':
    print("como deseas buscarlo")
    print("1.buscar por indice")
    print("2.busacr lista")
    resp=int(input())
    if resp==1:
        print("como deseas buscar el producto")
        print("1.indice")
        print("2.por nombre")
        print("3. por clave")
        respuesta=int(input())
        if respuesta==1:
            print("ingresa el indice")
            indice=int(input())
            if 0 <= indice< len(lista_nom):
                print("el producto es", lista_nom[indice],"su clave es",lista_clave[indice],"la cantidad del producto es",lista_piezas[indice])
            else:
                print("tu producto no existe")
        if respuesta==2:
            print("ingresa el nombre")
            nom=input()
            nomb=lista_nom.index(nom)
            print("el producto es", lista_nom[nomb],"su clave es",lista_clave[nomb],"la cantidad del producto es",lista_piezas[nomb])
        if respuesta==3:
            print("ingresa la clave")
            clave=int(input())
            clave_num=lista_clave.index(clave)
            print("el producto es", lista_nom[clave_num],"su clave es",lista_clave[clave_num],"la cantidad del producto es",lista_piezas[clave_num])
    if resp==2:
        print(f"{'producto':<15} {'clave':<12} {'piezas':<10}")
        print("-"*40)
        for fila in range(len(lista_nom)):
            print (f"{lista_nom[fila]:<15} {lista_clave[fila]:<12} {lista_piezas[fila]:<10}")
    else:
        ("no es una opcion")
    print("quieres volver a buscar si o no")
    res=input()
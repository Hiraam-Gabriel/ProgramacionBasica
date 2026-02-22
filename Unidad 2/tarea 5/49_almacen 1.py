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
        print("ingresa el indice del producto")
        indice=int(input())
        if 0 <= indice< len(lista_nom):
            print("el producto es", lista_nom[indice],"su clave es",lista_clave[indice],"la cantidad del producto es",lista_piezas[indice])
        else:
            print("tu producto no existe")
    if resp==2:
        print(f"{'producto':<15} {'clave':<12} {'piezas':<10}")
        print("-"*40)
        for fila in range(len(lista_nom)):
            print (f"{lista_nom[fila]:<15} {lista_clave[fila]:<12} {lista_piezas[fila]:<10}")
    else:
        ("no es una opcion")
    print("quieres volver a buscar si o no")
    res=input()
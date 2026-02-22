print("********Almacen********")
lista_nom=["mesa","silla","refrigelador","estufa","television"]
lista_clave=[1957,6834,8642,3641,7552]
lista_piezas=[10,120,5,7,3]
res="si"
while res=='si':
    print("ingresa el indice del producto")
    indice=int(input())
    if 0 <= indice< len(lista_nom):
        print("el producto es", lista_nom[indice],"su clave es",lista_clave[indice],"la cantidad del producto es",lista_piezas[indice])
        print("deseas buscar otro producto si o no")
        res=input()
    else:
        print("tu producto no existe")

print(f"{'producto':<15} {'clave':<12} {'piezas':<10}")
print("-"*40)
for fila in range(len(lista_nom)):
    print (f"{lista_nom[fila]:<15} {lista_clave[fila]:<12} {lista_piezas[fila]:<10}")
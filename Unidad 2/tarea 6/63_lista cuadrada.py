def Agregar(Numeros):
    Lista=[]
    for i in range(Numeros):
        Elemento=int(input('Ingrese el numero que desea agregar a la lista: '))
        Lista.append(Elemento)
        print('La lista de numeros es: ', Lista)
    print('tu lista elevada al cuadrado es:',lista_al_cuadrado(Lista))

def lista_al_cuadrado(lista):
    lista_cuadrada = []
    for i in range(len(lista)):
        lista_cuadrada.append(lista[i]**2)
    return lista_cuadrada

print('****** lista al cuadrado ******')
Numeros=int(input('Ingrese el numero de elementos que desea agregar a la lista: '))
Agregar(Numeros)

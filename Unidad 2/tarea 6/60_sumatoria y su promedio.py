def Agregar(Numeros):
    Lista=[]
    for i in range(Numeros):
        Elemento=int(input('Ingrese el numero que desea agregar a la lista: '))
        Lista.append(Elemento)
        print('La lista de numeros es: ', Lista)
        
    print('la sumatoria es:',sumatoria(Lista))
    print('el promedio es:',promedio(Lista))

def sumatoria(Lista):
    res=sum(Lista)
    return res

def promedio(Lista):
    res=sumatoria(Lista)/len(Lista)
    return res

print('********lista de numeros********')
Numeros=int(input('Ingrese el numero de elementos que desea agregar a la lista: '))
Agregar(Numeros)
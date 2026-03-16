def ordenar_creciente(miLista):
    miLista.sort()
    return miLista

def ordenar_decreciente(Lista):
    Lista.sort(reverse=True)
    return Lista
    
def pop_elemento(lista_2):
    lista_2.pop()
    return lista_2
                
def remover_elemento(lista_3):
    elemento=int(input('Que elemento de la lista deseas borrar?'))
    lista_3.remove(elemento)
    return lista_3
               
def calcular_promedio(lista_5):
    promedio=sum(lista_5)/len(lista_5)
    return promedio

def maximo(lista_6):
    res=max(lista_6)
    return res

def minimo(lista_7):
    res=min(lista_7)
    return res


print('**********funciones**********')
print("crea tu lista")
lista = []
respuesta = 'si'
opcion=0
opc_menu=0
while respuesta == 'si':
    numero = int(input('ingresa un número: '))
    lista.append(numero)
    respuesta = input('¿Deseas ingresar otro número? si/no: ')
print('tu lista es:', lista)

while opc_menu <= 6:
    print('**********funciones disponibles**********')
    print('1. ordenamiento')
    print('2. decreciente')
    print('3. pop')
    print('4. remover')
    print('5. promedios')
    print('6. salir')
    opc_menu=int(input('elige una opción: '))
    if opc_menu == 1:
       print( ordenar_creciente(lista))

    elif opc_menu == 2:
        print(ordenar_decreciente(lista))
    elif opc_menu == 3:
        print(pop_elemento(lista))
    elif opc_menu == 4:
        print(remover_elemento(lista))
    elif opc_menu == 5:
        print('el promedio de tu lista es: ',calcular_promedio(lista))
        print('el maximo de tu lista es:',maximo(lista))
        print('el minimo de tu lista es:',minimo(lista))
    elif opc_menu==6:
        break
    else:
        print('opción no válida, por favor elige una opción del 1 al 6')
        opc_menu=0
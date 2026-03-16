def factorial(numero):
    resultado=1
    for i in range(1,numero+1):
        resultado *= i
    return resultado


print('*******el factorial de los numeros*******')
lista=[]
respuesta = 'si'
while respuesta == 'si':
    numero = int(input('ingresa un número: '))
    lista.append(numero)
    print('tu resultado es:', factorial(numero))
    respuesta = input('¿Deseas ingresar otro número? (si/no): ')

print("el total de los numeros leidos es",len(lista))
    



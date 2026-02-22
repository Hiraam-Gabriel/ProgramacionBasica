print('*****elebar al cuadrado 10 numeros*****')
print('ingresa los numeros')
lista=[]
for i in range(10):
    num=float(input('dame el numero de la posision ' +str(i+1)+':'))
    lista.append(num**2)

for i in range(10):
    print('el cuadrado del nuemro es',lista[i])
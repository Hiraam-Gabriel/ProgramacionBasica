print('***********Ahorros***********')
lista_nom=[]
lista_ahor=[]
res="si"
while res=='si': 
    print("ingresa tu nombre")
    nom=input()
    print("ingresa tus ahorros")
    ahor=float(input())
    print("quieres ingresar otro usuario?","si",'o',"no")
    lista_nom.append(nom)
    lista_ahor.append(ahor)
    res=input()

for i in range(len(lista_ahor)):
    if lista_ahor[i]<1000:
        print(lista_nom[i],'no tendras para tu futuro')
    elif lista_ahor[i]>1000000:
        print(lista_nom[i],"ya casi te retiras")
def impar(numero):
    res=numero%2
    if res==0:
        return ("es par")
    else:
        return ('es impar')

print('******** el numero es primo?*******')
print('ingresa el numero que quieres identificar')
numero=int(input())
print('tu numero es',impar(numero))
print('********calcula el promedio*******')
print('cual es el nombre de la materia')
nombre=input()
lista=[]
res='si'
while res=='si':
    cali=float(input('dame el la calificacion:'))
    print('deseas ingresar otra calificacion','si','o','no')
    lista.append(cali)
    res=input()
    
promedio=sum(lista)/len(lista)
print('el nombre de la materia es:',nombre,'y tu calificacion es:',promedio)
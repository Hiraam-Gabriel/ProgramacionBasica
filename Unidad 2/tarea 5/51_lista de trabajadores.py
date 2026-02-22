print("*******Asistencia de trabajadores********")
lista=[]
asistencia=[]
res="si"
while res=="si":
    print("ingresa el nombre del trabajador")
    nom=input()
    lista.append(nom)
    print('asistio a trabajar? si o no')
    resAsistencia=input()
    if resAsistencia=="si":
        asistencia.append(1)
    else:
        asistencia.append(0)

    print('deseas ingresar otro trabajador','si','o','no')
    res=input()
for i,j in zip(lista,asistencia):
    print(f"{i} {"no asistio" if j==0 else "asistio"} a trabajar")
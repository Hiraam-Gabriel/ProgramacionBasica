def alumnos_reprobados(lista):
    reprobados = []
    for i in range(0, len(lista), 2):
        nombre = lista[i]
        calificacion = lista[i + 1]
        if calificacion <= 60:
            reprobados.append(nombre)
    return reprobados 
print('**********Alumnos reprobados**********')
list_alum_califi=['luis',50, 'maria', 90, 'juan', 30, 'ana', 70, 'carlos', 100, 'sofia', 40]
print('estos alumnos',alumnos_reprobados(list_alum_califi),'reprobaron')
def calcular_calificacion_final(nota1, nota2, nota3):
    calificacion_final = (nota1 + nota2 + nota3) / 3
    if calificacion_final<=70:
        return ("aprobaste")
    else:
        return("no aprobaste el curso")
    
print('******calcula tu calificacion final******')
nota1 = float(input('ingresa tu primera nota: '))
nota2 = float(input('ingresa tu segunda nota: '))
nota3 = float(input('ingresa tu tercera nota: '))
print("tu situacion es",calcular_calificacion_final(nota1, nota2, nota3))
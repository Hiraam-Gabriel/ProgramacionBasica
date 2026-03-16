def es_multiplo(numero1, numero2):
    if numero1 % numero2 == 0:
        return ('es multiplo')
    else:
        return('no son multiplos')

print('****** es  multiplo******')
numero1= int(input('ingresa un número: '))
numero2 = int(input('ingresa otro número: '))
print('tu numo es:',es_multiplo(numero1, numero2))
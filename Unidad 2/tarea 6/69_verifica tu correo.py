def verificacion(correo):
    if '@' in correo:
        print("es valido tu correo")
    else:
        print('no es valido tu correo')

print('*********verificador de correos*********')
print("ingresa tu correo electronico")
correo=input("")
verificacion(correo)
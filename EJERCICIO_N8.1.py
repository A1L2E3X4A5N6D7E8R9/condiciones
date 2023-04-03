numero= input("ingrese el valor")
if len(numero) !=1:
    print("solo se acepta un valor")
elif numero in "0123456789":
    print("su valor esta en el rango deseado")
else:
    print("su valor insertado no esta en el rango deseado")
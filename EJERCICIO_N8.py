print("CURSO DE PYTHON")
print("NOMBRE: SANDRO SANCHEZ")
print("FECHA: 31/03/2023")

#Escribe un programa que solicite al usuario una letra y, si es una vocal, muestre el mensaje “Es vocal”. 
# Verificar si el usuario ingresó un string de más de un carácter y, en ese caso, informarle que no se puede procesar el dato.

letra= input("ingrese una letra")
if len(letra) !=1:
    print("no se puede procesar el dato. Debe ingresar una sola letra.")
elif letra in "aeiouAEIOU":
    print("es vocal")
else:
    print("no es vocal")
    
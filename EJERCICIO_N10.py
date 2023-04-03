print("CURSO DE PYTHON")
print("NOMBRE: SANDRO SANCHEZ")
print("FECHA: 31/03/2023")

#Determinar si un año es bisiesto.
# Es divisible entre 4, pero no es divisible entre 100.
# Es divisible entre 400.
# Por ejemplo, los años 2000 y 2020 son bisiestos porque son divisibles entre 400, mientras que el año 1900 no es bisiesto porque es divisible entre 100 pero no entre 400.

año=int(input("ingresa año\n"))
if(año % 4 == 0 and año % 100 != 0 or año % 400 == 0):
 print("El año "+str(año)+" Si es bisiesto ")
else:
 print("El año "+str(año)+" No es bisiesto ")
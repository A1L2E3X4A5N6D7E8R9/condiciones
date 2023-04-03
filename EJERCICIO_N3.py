print("CURSO DE PYTHON")
print("NOMBRE: SANDRO SANCHEZ")
print("FECHA: 30/03/2023")
#Escribir un programa que almacene la cadena de caracteres <b>contraseña</b> en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
contra= "pablo123"
x= input ("ingrese la contraseña")
if x.lower()== contra:
    print("CONTTRASEÑA CORRECTA")
else:
    print("CONTRASEÑA INCORRECTA")
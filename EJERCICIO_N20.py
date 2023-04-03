print("CURSO DE PYTHON")
print("NOMBRE: SANDRO SANCHEZ")
print("FECHA: 31/03/2023")
#Escribir un programa que pregunte al usuario una cantidad de días y muestre por pantalla cuantas horas, minutos y segundos hay en dicha cantidad de días.
dia = int(input("Ingrese Cantidad de Dias : "))
hor = int(dia*24)
min = int(hor*60)
seg = int(dia * 86400)

print("HORAS   : ", hor)
print("MINUTOS : ", min)
print("SEGUNDOS: ", seg)
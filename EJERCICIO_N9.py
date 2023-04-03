print("CURSO DE PYTHON")
print("NOMBRE: SANDRO SANCHEZ")
print("FECHA: 31/03/2023")

#Calificación de un examen. Ingrese la puntuación de un examen.
# Si es >= 90 La calificación es A, si es >= 80 La calificación es B,
# si es >= 70 La calificación es C,
# si >= 60 La calificación es D,
# sino La calificación es F,

print("ejercico #9")
print("Detalles: calificacion de un examen")
calificacion= int (input( "ingrese la calificacion del examen "))
print(calificacion )
if calificacion>=90:
    print("Su clasificacion es una A")
elif calificacion>=80:
    print("Su clasificacion es una B")
elif calificacion>=70:
    print("Su clasificacion es una C")
elif calificacion>=60:
    print("Su clasificacion es una D")
else :
    print("Su clasificacion es una F")
cantidad = int(0)
cantidad =int(input("Ingrese la cantidad de saludos: "))
if cantidad <= 0:
    print("Cantidad no admitida")
else:
    for i in range(cantidad):
        print("Hola Mundo")

try:
    cantidad = int(0)
    cantidad =int(input("Ingrese la cantidad de saludos: "))
    if ((cantidad <= 0) or (type(cantidad) is not int)): raise ValueError
    
except ValueError:
     print("No se aceptan numeros menores de 0 y/o No se aceptan valores no enteros")

else:
     for i in range(cantidad):
          print("Hola Mundo")
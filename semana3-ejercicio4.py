print("EJERCICIO MAYOR DE EDAD EN FUNCION")

def edad():
    nombre=input("Por favor ingresa el nombre: ")
    validar=int(input("Por favor ingresa la edad:"))
    if validar<=18:
        print(f"{nombre} es menor de edad con {validar} años")
    else:
        print(f"{nombre} es mayor de edad con {validar} años")

edad()
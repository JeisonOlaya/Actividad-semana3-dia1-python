print("EJERCICIO FIGURA GEOMETRICA CON FUNCION")

def area():
    height= int(input("Ingresa la altura del triangulo: "))
    base= int(input("Ingresa la base del triangulo: "))
    
    calculate= (base * height)/2
    
    print(f"El area del triangulo es: {calculate}")

area()
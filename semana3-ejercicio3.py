print("EJERCICIO DE PAR O IMPAR CON FUNCION")

def numero():
    validar=int(input("Por favor ingresa un numero:")) #aca se coloca int para convertir el dato que ingresa la persona en entero
                                                        # es decir, el dato ingresa como string y lo convierte en entero
    if validar % 2==0:
        print(f"El numero {validar} es par")
    else:
        print(f"el numero {validar} es impar")
    

numero()
def composicion(func1, func2):
    """Devuelve una nueva función que es la composición de las dos funciones dadas"""
    return lambda x: func1(func2(x))

# Ejemplo de funciones para componer
def cuadrado(x):
    return x ** 2

def doble(x):
    return x * 2

# Entrada de usuario
try:
    valor = float(input("Ingresa un número para aplicar la composición de funciones: "))
    
    # Crear función compuesta
    funcion_compuesta = composicion(cuadrado, doble)
    
    # Aplicar y mostrar resultado
    resultado = funcion_compuesta(valor)
    print(f"Primero se duplica {valor}  {doble(valor)}")
    print(f"Luego se eleva al cuadrado  {resultado}")
    print(f"Resultado final: {resultado}")
except ValueError:
    print("Por favor ingresa un número válido")
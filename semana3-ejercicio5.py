print("EJERCICIO DE CONVERTIR TEMPERATURA CON FUNCION")

def temperture():
    join = float(input("Por favor ingresa la temperatura: "))
    transform = (join*1.8)+32
    
    print(f"La temperatura en grados Celsius es: {join} ")
    print(f"La temperatura en grados Fahrenhei es: {transform}")

temperture()
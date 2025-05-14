print("EJERCICIO IMPRIMIR NUMERO MAYOR DE UNA LISTA")

lista = []

def listanum():
    print("Escriba los números que deseas ingresar o 'fin' para terminar")
    while True:
        entrada = input("Por favor ingresa un numero: ")
        
        if entrada.lower() == 'fin':
            break
            
        try:
            numero = float(entrada)  # Usa float en lugar de int para decimales
            lista.append(numero)
        except ValueError:
            print("Por favor ingresa solo números o 'fin' para terminar")
    
    if lista:
        numeroMayor = max(lista)
        print(f"La lista de números es: {lista}")
        print(f"El numero mayor es: {numeroMayor}")
    else:
        print("No se ingresaron numeros")

listanum()
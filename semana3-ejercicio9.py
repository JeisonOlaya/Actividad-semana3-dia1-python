print("Ejercicio con funcion: lista de números y devuelva solo los pares.")


def filtrar(numero):
    return[num for num in numero if num % 2==0]
entrada= input("Ingresa numeros separados por espacio: ")
numero=[int(num) for num in entrada.split()]

pares= filtrar(numero)
impares= filtrar(numero)

print("Los numeros pares son: ",pares)


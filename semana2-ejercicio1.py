import random
from datetime import datetime

# Variables globales para almacenar los datos
reservas = {}
contador_reservas = 1

# Datos de las rutas disponibles
rutas = {
    "Bogotá – Medellín": {"tipo": "nacional", "precio_base": 230000},
    "Bogotá – España": {"tipo": "internacional", "precio_base": 4200000}
}

# Costos de equipaje
costos_equipaje = [
    {"limite": 20, "costo": 50000},
    {"limite": 30, "costo": 70000},
    {"limite": 50, "costo": 110000}
]

max_equipaje_mano = 13

def generar_id_compra():
    global contador_reservas
    id_compra = f"COMP{str(contador_reservas).zfill(5)}"
    contador_reservas += 1
    return id_compra

def calcular_costo_equipaje(peso):
    if peso > 50:
        return None  # Equipaje no admitido
    for costo in costos_equipaje:
        if peso <= costo["limite"]:
            return costo["costo"]
    return 0  # Sin equipaje o peso 0

def registrar_reserva():
    global reservas
    
    print("\n--- Registro de Nueva Reserva ---")
    nombre = input("Nombre del pasajero: ")
    
    print("\nRutas disponibles:")
    for i, ruta in enumerate(rutas.keys(), 1):
        print(f"{i}. {ruta} ({rutas[ruta]['tipo']}) - ${rutas[ruta]['precio_base']:,}")
    
    try:
        opcion_ruta = int(input("Seleccione el número de la ruta: ")) - 1
        ruta = list(rutas.keys())[opcion_ruta]
    except (ValueError, IndexError):
        print("Opción no válida. Intente nuevamente.")
        return
    
    fecha_viaje = input("Fecha del viaje (DD/MM/AAAA): ")
    try:
        fecha_obj = datetime.strptime(fecha_viaje, "%d/%m/%Y")
    except ValueError:
        print("Formato de fecha incorrecto. Use DD/MM/AAAA.")
        return
    
    try:
        peso_principal = float(input("Peso del equipaje principal (kg): "))
    except ValueError:
        print("Peso debe ser un número.")
        return
    
    lleva_mano = input("¿Lleva equipaje de mano? (si/no): ").lower()
    peso_mano = 0
    estado_mano = "No lleva"
    
    if lleva_mano == "si":
        try:
            peso_mano = float(input("Peso del equipaje de mano (kg): "))
        except ValueError:
            print("Peso debe ser un número.")
            return
        
        if peso_mano > max_equipaje_mano:
            estado_mano = "Rechazado (supera 13kg)"
        else:
            estado_mano = "Aceptado"
    
    # Calcular costos
    precio_base = rutas[ruta]["precio_base"]
    costo_equipaje = calcular_costo_equipaje(peso_principal)
    
    if costo_equipaje is None:
        estado_principal = "No admitido (supera 50kg)"
        costo_equipaje = 0
    elif peso_principal == 0:
        estado_principal = "Sin equipaje"
    else:
        estado_principal = f"Aceptado ({peso_principal}kg)"
    
    total = precio_base + costo_equipaje
    
    # Crear reserva
    id_compra = generar_id_compra()
    reservas[id_compra] = {
        "nombre": nombre,
        "ruta": ruta,
        "tipo": rutas[ruta]["tipo"],
        "fecha": fecha_obj,
        "peso_principal": peso_principal,
        "estado_principal": estado_principal,
        "peso_mano": peso_mano,
        "estado_mano": estado_mano,
        "precio_base": precio_base,
        "costo_equipaje": costo_equipaje,
        "total": total
    }
    
    # Mostrar resumen
    mostrar_reserva(id_compra)
    print("\n¡Reserva registrada con éxito!")

def mostrar_reserva(id_compra):
    if id_compra not in reservas:
        print("ID de reserva no encontrado.")
        return
    
    reserva = reservas[id_compra]
    print("\n--- Detalle de Reserva ---")
    print(f"ID de compra: {id_compra}")
    print(f"Nombre del pasajero: {reserva['nombre']}")
    print(f"Destino: {reserva['ruta']}")
    print(f"Fecha: {reserva['fecha'].strftime('%d/%m/%Y')}")
    print(f"Estado equipaje principal: {reserva['estado_principal']}")
    print(f"Estado equipaje de mano: {reserva['estado_mano']}")
    print(f"\nCosto total del viaje: ${reserva['total']:,}")
    print(f"  - Precio base: ${reserva['precio_base']:,}")
    print(f"  - Costo equipaje: ${reserva['costo_equipaje']:,}")

def menu_administrador():
    while True:
        print("\n--- Menú Administrador ---")
        print("1. Total recaudado en todas las compras")
        print("2. Total recaudado para una fecha específica")
        print("3. Número de pasajeros procesados")
        print("4. Pasajeros nacionales/internacionales")
        print("5. Consultar compra por ID")
        print("6. Volver al menú principal")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            total = sum(reserva['total'] for reserva in reservas.values())
            print(f"\nTotal recaudado en todas las compras: ${total:,}")
        
        elif opcion == "2":
            fecha_str = input("Ingrese la fecha a consultar (DD/MM/AAAA): ")
            try:
                fecha_consulta = datetime.strptime(fecha_str, "%d/%m/%Y")
                total = sum(
                    reserva['total'] for reserva in reservas.values()
                    if reserva['fecha'].date() == fecha_consulta.date()
                )
                print(f"\nTotal recaudado para {fecha_str}: ${total:,}")
            except ValueError:
                print("Formato de fecha incorrecto. Use DD/MM/AAAA.")
        
        elif opcion == "3":
            print(f"\nNúmero total de pasajeros procesados: {len(reservas)}")
        
        elif opcion == "4":
            nacionales = sum(1 for reserva in reservas.values() if reserva['tipo'] == 'nacional')
            internacionales = sum(1 for reserva in reservas.values() if reserva['tipo'] == 'internacional')
            print(f"\nPasajeros nacionales: {nacionales}")
            print(f"Pasajeros internacionales: {internacionales}")
        
        elif opcion == "5":
            id_compra = input("Ingrese el ID de compra a consultar: ")
            if id_compra in reservas:
                mostrar_reserva(id_compra)
            else:
                print("ID de compra no encontrado.")
        
        elif opcion == "6":
            break
        
        else:
            print("Opción no válida. Intente nuevamente.")

def menu_principal():
    while True:
        print("\n--- Sistema de Gestión y Costeo de Equipaje ---")
        print("1. Registrar nueva reserva")
        print("2. Menú administrador")
        print("3. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            registrar_reserva()
        elif opcion == "2":
            # Verificación simple de administrador
            clave = input("Ingrese la clave de administrador: ")
            if clave == "admin123":
                menu_administrador()
            else:
                print("Clave incorrecta. Acceso denegado.")
        elif opcion == "3":
            print("¡Gracias por usar el sistema!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# Ejecutar el sistema
if __name__ == "__main__":
    menu_principal()
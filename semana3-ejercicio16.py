import re

def validar_contraseña(contraseña):
    """
    Valida si una contraseña cumple con:
    - Al menos 8 caracteres
    - Al menos una mayúscula
    - Al menos una minúscula
    - Al menos un número
    - Al menos un símbolo especial
    """
    if len(contraseña) < 8:
        return False, "La contraseña debe tener al menos 8 caracteres"
    
    if not re.search(r"[A-Z]", contraseña):
        return False, "La contraseña debe contener al menos una mayúscula"
    
    if not re.search(r"[a-z]", contraseña):
        return False, "La contraseña debe contener al menos una minúscula"
    
    if not re.search(r"[0-9]", contraseña):
        return False, "La contraseña debe contener al menos un número"
    
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", contraseña):
        return False, "La contraseña debe contener al menos un símbolo especial"
    
    return True, "Contraseña válida"

# Entrada de usuario
contraseña = input("Ingresa tu contraseña: ")

# Validación y resultado
valida, mensaje = validar_contraseña(contraseña)
print(mensaje)
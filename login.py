def login(usuario, contraseña):
    """Función para autenticar usuarios"""
    if usuario and contraseña:
        return True
    return False

def logout():
    """Función para cerrar sesión"""
    print("Usuario desconectado")
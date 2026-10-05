def validar_login(usuario, password, activo, intentos):
    
    assert usuario != "", "El usuario no puede estar vacío"
    
    if password == "":
        raise ValueError("La contraseña no puede estar vacía")
    
    if activo != True:
        raise ValueError("El usuario debe estar activo para iniciar sesión")
    
    if intentos > 3:
        raise ValueError("Demasiados intentos")
    
    return True


def ejecutar_login(usuario, password, activo, intentos):
    
    try:
        resultado = validar_login(usuario, password, activo, intentos)
        assert resultado == True, "Error en la validación del login"
        print("Login correcto")
    except ValueError as error:
        print("Error:", error)


usuario = "admin"
password = "1234"
activo = True
intentos = 2

ejecutar_login(usuario, password, activo, intentos)
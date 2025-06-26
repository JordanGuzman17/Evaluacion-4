#### Prueba ###

usuarios = []
usuarios_diccionario = {}
s = "*"*5

def confirmar_contraseña(contraseña):
    if ' ' in contraseña:
        return False
    if len(contraseña) <8:
        return False
    if not any(w.isalpha() for w in contraseña):
        return False
    if not any(x.isdigit() for x in contraseña):
        return False
    return True

def crear_usuario():
    nombre = input("\nIngrese su nombre: →")
    while True:
        usuario = input("\nIngrese su nombre de usuario: →")
        if usuario in usuarios_diccionario:
            print("\n❌El nombre de usuario ya existe, ingresa un nuevo nombre🤦‍♂️")
        else:
            break
    while True:
            genero = (input("\nIngrese su sexo → M o F\n\n→")).upper()
            if genero in ['M','F']:
                break
            else:
                print("\nSolo puede ingresar M(Masculino) o F(Femenino)")
                print(s*9)
    while True: 
        contraseña = input("\nIngrese una contraseña: →")
        if confirmar_contraseña(contraseña):
            print()
            break
        else:
            print("\n❎La Contraseña no cumple con los requisitos❎")
            print("\nComo minimo debe contener 8 caracteres❗ \n Al menos debe contener una letra❗" \
            "\n Al menos debe contener un numero❗\n y no debe contener espacios❗")
    usuario_nuevo = {
        'nombre': nombre,
        'usuario':usuario,
        'genero':genero,
        'contraseña':contraseña
}
    usuarios.append(usuario_nuevo)
    usuarios_diccionario[usuario] = usuario_nuevo
    print(s*7)
    print("Usuario creado con exito ✅")
    print(s*7)

def encontrar_usuario():
    buscar_usuario = input("\nIngrese el nombre del usuario a buscar: →")
    if buscar_usuario in usuarios_diccionario:
        buscar = usuarios_diccionario[buscar_usuario]
        print(s*5)
        print(f"\n{s} Datos del usuario {buscar_usuario} {s}")
        print(f"\nNombre: {buscar['nombre']}\nNombre de usuario: {buscar['usuario']}\nSexo: {buscar['genero']}\n Contraseña:{buscar['contraseña']}")
        print(s*5)
    else:
        print("\nEl usuario no existe🚫")

def kill_usuario():
    usuario_ko = input("\nIngresa el nombre del usuario que desea eliminar: →")
    if usuario_ko in usuarios_diccionario:
        usuarios.remove(usuarios_diccionario[usuario_ko])
        del usuarios_diccionario[usuario_ko]
        print(s*8)
        print("\nUsuario Elminado con éxito👍")
    else:
        print("\n❌No fue posible eliminar el usuario❌")

finalizar = True
while finalizar:
    try:
        print(f"\n{s*3}Menu{s*3}")
        menu = int(input("\n   1.-Ingresar Usuario\n   2.-Buscar usuario.\n   3.-Eliminar usuario. \n   4.-Salir\n\n  →"))
        if menu == 1:
            crear_usuario()
        elif menu == 2:
            encontrar_usuario()
        elif menu == 3:
            kill_usuario()
        elif menu == 4:
            print("\nSaliendo......🖖🖖🖖🖖🖖🖖🖖")
            finalizar = False
        else:
            print("\n🆘Ingresa una opcion del 1 - 4.🆘")
    except ValueError:
        print("\nError: Solo se aceptan numeros❌❌❌")



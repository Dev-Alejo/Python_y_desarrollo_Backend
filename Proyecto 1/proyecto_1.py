"""
Proyecto 1: Elaborar un programa en consola que pueda gestionar estudiantes universitarios
Cursante: Alejandro Diaz

La funsion de actualizar estudiante queria hacerlo mas pro y pero no me alcansa el tiempo profe
queria hacer que se pueda seleccionar el campo que quieres editar y que solo se modifique dicho campo 
y que lo demas quede igual, pero considero de que ya esta completo :D
"""

estudiantes = []  # Esta es una lista vacía para almacenar estudiantes como diccionarios

def menu():
    print("----- GESTIÓN DE ESTUDIANTES -----")
    print("1- Listado de estudiantes")
    print("2- Registrar estudiante")
    print("3- Actualizar estudiante")
    print("4- Eliminar estudiante")
    print("5- Salir")

def listar_estudiantes():
    print("----- LISTADO DE ESTUDIANTES -----")
    if len(estudiantes) == 0:
        print("No hay estudiantes registrados.")
    else:
        for estudiante in estudiantes:
            print("Nombre:", estudiante["nombre"])
            print("Apellido:", estudiante["apellido"])
            print("Cédula:", estudiante["cedula"])
            print("Nota 1:", estudiante["nota1"])
            print("Nota 2:", estudiante["nota2"])
            print("Nota 3:", estudiante["nota3"])
            print("Promedio:", round(estudiante["promedio"], 2))
            print("---------------------------------")

def validar_nombre(texto):
    while True:
        entrada = input(texto)
        if entrada.isalpha():
            return entrada
        else:
            print("Por favor, solo ingrese caracteres alfabeticos.")

def validar_cedula():
    while True:
        cedula = input("Ingrese el número de cédula: ")
        if not cedula.isdigit():
            print("La cédula debe contener solo números.")
        else:
            cedula = int(cedula)
            if cedula < 1000000 or cedula > 50000000:
                print("La cédula no existe.")
            else:
                return cedula

def registrar_estudiante():
    print("----- REGISTRAR ESTUDIANTE -----")
    nombre = validar_nombre("Ingrese el nombre: ")
    apellido = validar_nombre("Ingrese el apellido: ")
    cedula = validar_cedula()
    nota1 = float(input("Ingrese la nota 1: "))
    nota2 = float(input("Ingrese la nota 2: "))
    nota3 = float(input("Ingrese la nota 3: "))
    promedio = (nota1 + nota2 + nota3) / 3

    estudiante = {
        "nombre": nombre,
        "apellido": apellido,
        "cedula": cedula,
        "nota1": nota1,
        "nota2": nota2,
        "nota3": nota3,
        "promedio": promedio
    }

    estudiantes.append(estudiante)
    print("Estudiante registrado exitosamente.")

def actualizar_estudiante():
    print("----- ACTUALIZAR ESTUDIANTE -----")
    cedula = input("Ingrese el número de cédula del estudiante a actualizar: ")

    for estudiante in estudiantes:
        if estudiante["cedula"] == int(cedula):
            print("Estudiante encontrado:")
            print("Nombre:", estudiante["nombre"])
            print("Apellido:", estudiante["apellido"])
            print("Cédula:", estudiante["cedula"])
            print("Nota 1:", estudiante["nota1"])
            print("Nota 2:", estudiante["nota2"])
            print("Nota 3:", estudiante["nota3"])
            print("Promedio:", estudiante["promedio"])
            print("---------------------------------")

            nombre = validar_nombre("Ingrese el nuevo nombre: ")
            apellido = validar_nombre("Ingrese el nuevo apellido: ")
            nueva_cedula = validar_cedula()
            nota1 = float(input("Ingrese la nueva nota 1: "))
            nota2 = float(input("Ingrese la nueva nota 2: "))
            nota3 = float(input("Ingrese la nueva nota 3: "))
            promedio = (nota1 + nota2 + nota3) / 3

            estudiante["nombre"] = nombre
            estudiante["apellido"] = apellido
            estudiante["cedula"] = nueva_cedula
            estudiante["nota1"] = nota1
            estudiante["nota2"] = nota2
            estudiante["nota3"] = nota3
            estudiante["promedio"] = promedio

            print("Estudiante actualizado exitosamente.")
            return

    print("No se encontró ningún estudiante con la cédula proporcionada.")

def eliminar_estudiante():
    print("----- ELIMINAR ESTUDIANTE -----")
    cedula = input("Ingrese el número de cédula del estudiante a eliminar: ")

    for estudiante in estudiantes:
        if estudiante["cedula"] == int(cedula):
            estudiantes.remove(estudiante)
            print("Estudiante eliminado exitosamente.")
            return

    print("No se encontró ningún estudiante con la cédula proporcionada.")

# El while esta al final es porque al colocarlo delante y luego definir una funcion me sale error (Funtion not defined).
while True:
    menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        listar_estudiantes()
    elif opcion == "2":
        registrar_estudiante()
    elif opcion == "3":
        actualizar_estudiante()
    elif opcion == "4":
        eliminar_estudiante()
    elif opcion == "5":
        print("¡Hasta luego!")
        break
    else:
        print("Opción incorrecta. Por favor, seleccione una opción válida.")



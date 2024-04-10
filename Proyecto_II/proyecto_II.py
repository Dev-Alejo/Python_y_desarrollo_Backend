from datetime import datetime

# 2. Filtrar tareas

def filtrar_por_codigo(codigo, tareas):
    tareas_filtradas = []
    for tarea in tareas:
        if tarea['codigo'] == codigo:
            tareas_filtradas.append(tarea)
    return tareas_filtradas

def filtrar_por_titulo(titulo, tareas):
    tareas_filtradas = []
    for tarea in tareas:
        if tarea['titulo'].lower() == titulo.lower():
            tareas_filtradas.append(tarea)
    return tareas_filtradas

def filtrar_por_fecha(fecha, tareas):
    tareas_filtradas = []
    for tarea in tareas:
        if tarea['fecha'] == fecha:
            tareas_filtradas.append(tarea)
    return tareas_filtradas

def filtrar_tareas(tareas):
    while True:
        print("----- Filtrar Tareas -----")
        print("1. Filtrar por código")
        print("2. Filtrar por título")
        print("3. Filtrar por fecha")
        print("4. Atrás")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            codigo = input("Ingrese el código de la tarea: ")
            tareas_filtradas = filtrar_por_codigo(codigo, tareas)
            mostrar_tareas(tareas_filtradas)
        elif opcion == "2":
            titulo = input("Ingrese el título de la tarea: ")
            tareas_filtradas = filtrar_por_titulo(titulo, tareas)
            mostrar_tareas(tareas_filtradas)
        elif opcion == "3":
            fecha = input("Ingrese la fecha de la tarea (en formato dd/mm/aaaa): ")
            tareas_filtradas = filtrar_por_fecha(fecha, tareas)
            mostrar_tareas(tareas_filtradas)
        elif opcion == "4":
            return
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

        input("Presione ENTER para continuar...")

# 3. Añadir tarea

def agregar_tarea_a_lista(nueva_tarea, lista_tareas):
    lista_tareas.append(nueva_tarea)

def agregar_tarea(lista_tareas):
    print("----- Agregar Nueva Tarea -----")

    if len(lista_tareas) == 0:
        codigo = "001"
    else:
        ultimo_codigo = lista_tareas[-1]["codigo"]
        nuevo_numero = int(ultimo_codigo) + 1
        codigo = str(nuevo_numero).zfill(3)

    while True:
        titulo = input("Ingrese el título de la tarea: ")
        if titulo.strip() != "":
            break
        else:
            print("El título no puede estar en blanco. Ingrese un título válido.")

    while True:
        descripcion = input("Ingrese la descripción de la tarea: ")
        if descripcion.strip() != "":
            break
        else:
            print("La descripción no puede estar en blanco. Ingrese una descripción válida.")

    while True:
        fecha = input("Ingrese la fecha de la tarea (en formato dd-mm-aaaa): ")
        try:
            datetime.strptime(fecha, "%d-%m-%Y")
            break
        except ValueError:
            print("Fecha inválida. Ingrese una fecha en el formato dd-mm-aaaa.")

    status = "pendiente"

    nueva_tarea = {
        'codigo': codigo,
        'titulo': titulo,
        'descripcion': descripcion,
        'fecha': fecha,
        'status': status
    }

    agregar_tarea_a_lista(nueva_tarea, lista_tareas)

    print("La tarea ha sido agregada correctamente.")

    input("Presione ENTER para continuar...")

# 4. Actualizar tarea

def actualizar_tarea(tareas):
    while True:
        codigo = input("Ingrese el código de la tarea a actualizar: ")

        tarea = buscar_tarea_por_codigo(codigo, tareas)

        if tarea is None:
            print("No se encontró una tarea con el código especificado.")
        else:
            while True:
                print(f"----- Actualizar Tarea [{tarea['codigo']}] -----")
                print("1. Actualizar título")
                print("2. Actualizar descripción")
                print("3. Actualizar fecha")
                print("4. Actualizar status")
                print("5. Atrás")

                opcion = input("Seleccione una opción: ")

                if opcion == "1":
                    while True:
                        nuevo_titulo = input("Ingrese el nuevo título: ")
                        if nuevo_titulo.strip() != "":
                            tarea['titulo'] = nuevo_titulo
                            print("El título ha sido actualizado correctamente.")
                            break
                        else:
                            print("El título no puede estar en blanco. Ingrese un título válido.")
                elif opcion == "2":
                    while True:
                        nueva_descripcion = input("Ingrese la nueva descripción: ")
                        if nueva_descripcion.strip() != "":
                            tarea['descripcion'] = nueva_descripcion
                            print("La descripción ha sido actualizada correctamente.")
                            break
                        else:
                            print("La descripción no puede estar en blanco. Ingrese una descripción válida.")
                elif opcion == "3":
                    while True:
                        nueva_fecha = input("Ingrese la nueva fecha (en formato dd-mm-aaaa): ")
                        try:
                            datetime.strptime(nueva_fecha, "%d-%m-%Y")
                            tarea['fecha'] = nueva_fecha
                            print("La fecha ha sido actualizada correctamente.")
                            break
                        except ValueError:
                            print("Fecha inválida. Ingrese una fecha en el formato dd-mm-aaaa.")
                elif opcion == "4":
                    if tarea['status'] == 'pendiente':
                        respuesta = input("Presione 's' para marcar la tarea como completada o 'n' para volver al menú principal: ")
                        if respuesta.lower() == 's':
                            tarea['status'] = 'completado'
                            print("La tarea ha sido marcada como completada.")
                        elif respuesta.lower() == 'n':
                            break
                        else:
                            print("Respuesta inválida. Volviendo al menú de actualizar tarea...")
                    elif tarea['status'] == 'completado':
                        respuesta = input("Presione 's' para marcar la tarea como pendiente o 'n' para volver al menú principal: ")
                        if respuesta.lower() == 's':
                            tarea['status'] = 'pendiente'
                            print("La tarea ha sido marcada como pendiente.")
                        elif respuesta.lower() == 'n':
                            break
                        else:
                            print("Respuesta inválida. Volviendo al menú de actualizar tarea...")
                    else:
                        print("El estado de la tarea es inválido.")
                elif opcion == "5":
                    return
                else:
                    print("Opción inválida. Por favor, seleccione una opción válida.")
            break

    input("Presione ENTER para continuar...")

# 5. Eliminar tarea

def buscar_tarea_por_codigo(codigo, tareas):
    for tarea in tareas:
        if tarea["codigo"] == codigo:
            return tarea
    return None

def eliminar_tarea_de_lista(tarea, tareas):
    tareas.remove(tarea)

def eliminar_tarea(tareas):
    codigo = input("Ingrese el código de la tarea a eliminar: ")

    tarea = buscar_tarea_por_codigo(codigo, tareas)

    if tarea is None:
        print("No se encontró una tarea con el código especificado.")
    else:
        confirmacion = input("¿Está seguro que desea eliminar esta tarea? (S/N): ")

        if confirmacion.upper() == "S":
            tareas.remove(tarea)
            print("La tarea ha sido eliminada correctamente.")
        else:
            print("La tarea no ha sido eliminada.")

    input("Presione ENTER para continuar...")

# 1. Lista de tareas

def mostrar_tareas(tareas):
    tareas_pendientes = []
    tareas_completadas = []

    for tarea in tareas:
        if tarea["status"] == "pendiente":
            tareas_pendientes.append(tarea)
        elif tarea["status"] == "completado":
            tareas_completadas.append(tarea)

    if len(tareas_pendientes) == 0:
        print("No hay tareas pendientes.")
    else:
        print("Tareas pendientes:")
        for tarea in tareas_pendientes:
            print(tarea)

    print()

    if len(tareas_completadas) == 0:
        print("No hay tareas completadas.")
    else:
        print("Tareas completadas:")
        for tarea in tareas_completadas:
            print(tarea)

# Menu principal

def main():
    tareas = [
    {'codigo': '001', 'titulo': 'python', 'descripcion': 'proyecto', 'fecha': '23-04-2024', 'status': 'completado'},
    {'codigo': '002', 'titulo': 'JavaScript', 'descripcion': 'tarea', 'fecha': '25-04-2024', 'status': 'pendiente'}
    ]

    while True:
        print("----- Menú Principal -----")
        print("1. Lista de tareas")
        print("2. Filtrar tareas")
        print("3. Añadir tarea")
        print("4. Actualizar tarea")
        print("5. Eliminar tarea")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_tareas(tareas)
        elif opcion == "2":
            filtrar_tareas(tareas)
        elif opcion == "3":
            agregar_tarea(tareas)
        elif opcion == "4":
            actualizar_tarea(tareas)
        elif opcion == "5":
            eliminar_tarea(tareas)
        elif opcion == "6":
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

        print()

    print("¡Gracias por usar la aplicación de tareas!")

if __name__ == "__main__":
    main()



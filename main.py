class GestorTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, descripcion, completada=False):
        tarea = {"descripcion": descripcion, "completada": completada}
        self.tareas.append(tarea)

    def listar_tareas(self):
        return self.tareas

    def completar_tarea(self, indice):
        try:
            self.tareas[indice]["completada"] = True
        except IndexError:
            print("¡Índice fuera de rango! La tarea no existe.")

    def tareas_completadas(self):
        return filter(lambda tarea: tarea["completada"], self.tareas)

    def tareas_pendientes(self):
        return filter(lambda tarea: not tarea["completada"], self.tareas)

def main():
    gestor = GestorTareas()

    while True:
        print("\n1. Agregar tarea")
        print("2. Listar tareas")
        print("3. Completar tarea")
        print("4. Mostrar tareas completadas")
        print("5. Mostrar tareas pendientes")
        print("6. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            descripcion = input("Ingrese la descripción de la tarea: ")
            gestor.agregar_tarea(descripcion)
            print("Tarea agregada exitosamente.")
        elif opcion == "2":
            tareas = gestor.listar_tareas()
            for i, tarea in enumerate(tareas):
                print(f"{i + 1}. {tarea['descripcion']} - {'Completada' if tarea['completada'] else 'Pendiente'}")
        elif opcion == "3":
            indice = int(input("Ingrese el índice de la tarea a completar: "))
            gestor.completar_tarea(indice - 1)
        elif opcion == "4":
            tareas_completadas = list(gestor.tareas_completadas())
            print("\nTareas Completadas:")
            for tarea in tareas_completadas:
                print(f"- {tarea['descripcion']}")
        elif opcion == "5":
            tareas_pendientes = list(gestor.tareas_pendientes())
            print("\nTareas Pendientes:")
            for tarea in tareas_pendientes:
                print(f"- {tarea['descripcion']}")
        elif opcion == "6":
            print("Saliendo del gestor de tareas. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()

from gestion_libros.inventario import Inventario
from gestion_libros.ventas import Ventas

def mostrar_menu():
    """Muestra el menú principal"""
    print("\n--- Menú de la tienda de libros ---")
    print("1. Agregar libro al inventario.")
    print("2. Mostrar inventario.")
    print("3. Vender libro.")
    print("4. Mostrar total de ventas.")
    print("5. Salir.")

def main():

    inventario = Inventario()
    ventas = Ventas()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-5): ")

        if opcion == '1':
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            ano_publicacion = input("Ingrese el año de publicación del libro: ")

            # Validar que el año de publicación sea un número
            while not ano_publicacion.isdigit():
                print("Por favor, ingrese un año válido.")
                ano_publicacion = input("Ingrese el año de publicación del libro: ")
            
            ano_publicacion = int(ano_publicacion)
            inventario.agregar_libro(titulo, autor, ano_publicacion)
            print("Libro agregado al inventario.")

        elif opcion == '2':
            print("\n--- Inventario ---")
            libros_inventario = inventario.mostrar_inventario()
            if libros_inventario:
                print(libros_inventario)
            else:
                print("El inventario está vacío.")

        elif opcion == '3':
            print("\n--- Inventario ---")
            libros_inventario = inventario.mostrar_inventario()
            if libros_inventario:
                print(libros_inventario)
                titulo = input("Ingrese el título del libro que desea vender: ")

                # Verificar si el libro está en el inventario
                libro = inventario.buscar_libro(titulo)
                if libro:
                    precio = input("Ingrese el precio del libro vendido: ")
                    
                    # Validar que el precio sea un número
                    while not precio.replace('.', '', 1).isdigit():
                        print("Por favor, ingrese un precio válido.")
                        precio = input("Ingrese el precio del libro vendido: ")

                    precio = float(precio)
                    ventas.vender_libro(precio)

                    # Marcar libro como vendido o eliminarlo del inventario
                    inventario.eliminar_libro(titulo)
                    print(f"Libro '{titulo}' vendido.")
                else:
                    print("El libro no se encuentra en el inventario.")
            else:
                print("No hay libros disponibles en el inventario.")

        elif opcion == '4':
            print("\n--- Total de Ventas ---")
            print(f"Total vendido: ${ventas.mostrar_total_ventas():.2f}")

        elif opcion == '5':
            print("Saliendo...")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción entre 1 y 5.")

if __name__ == "__main__":
    main()


class Libro:
    def __init__(self, titulo, autor, ano_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacion = ano_publicacion

    def __str__(self):
        return f'Título: {self.titulo}\nAutor: {self.autor}\nAño de publicación: {self.ano_publicacion}'

class Inventario:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, titulo, autor, ano_publicacion):
        """Agrega un libro al inventario."""
        libro = {
            'titulo': titulo,
            'autor': autor,
            'ano_publicacion': ano_publicacion,
            'vendido': False
        }
        self.libros.append(libro)

    def mostrar_inventario(self):
        """Muestra los libros en el inventario."""
        if not self.libros:
            return "El inventario está vacío."
        inventario = ""
        for libro in self.libros:
            estado = "Vendido" if libro['vendido'] else "Disponible"
            inventario += f"Título: {libro['titulo']}, Autor: {libro['autor']}, Año: {libro['ano_publicacion']} - {estado}\n"
        return inventario

    def buscar_libro(self, titulo):
        """Busca un libro por título en el inventario."""
        for libro in self.libros:
            if libro['titulo'].lower() == titulo.lower() and not libro['vendido']:
                return libro
        return None

    def eliminar_libro(self, titulo):
        """Marca un libro como vendido en el inventario."""
        for libro in self.libros:
            if libro['titulo'].lower() == titulo.lower() and not libro['vendido']:
                libro['vendido'] = True
                return True
        return False



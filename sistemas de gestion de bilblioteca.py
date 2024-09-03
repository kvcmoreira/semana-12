# Clase Libro
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn
        self.detalles = (autor, titulo)  # Tupla inmutable

    def __str__(self):
        return f"'{self.titulo}' por {self.autor} [Categoría: {self.categoria}, ISBN: {self.isbn}]"

# Clase Usuario
class Usuario:
    def __init__(self, nombre, user_id):
        self.nombre = nombre
        self.user_id = user_id
        self.libros_prestados = []

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)

    def __str__(self):
        return f"Usuario: {self.nombre}, ID: {self.user_id}"

# Clase Biblioteca
class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario con ISBN como clave
        self.usuarios = {}  # Diccionario con ID de usuario como clave
        self.usuarios_registrados = set()  # Conjunto para asegurar IDs únicos

    def añadir_libro(self, libro):
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            print(f"Libro añadido: {libro}")
        else:
            print(f"El libro con ISBN {libro.isbn} ya existe en la biblioteca.")

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print(f"Libro con ISBN {isbn} ha sido eliminado de la biblioteca.")
        else:
            print(f"No se encontró un libro con ISBN {isbn}.")

    def registrar_usuario(self, usuario):
        if usuario.user_id not in self.usuarios_registrados:
            self.usuarios[usuario.user_id] = usuario
            self.usuarios_registrados.add(usuario.user_id)
            print(f"Usuario registrado: {usuario}")
        else:
            print(f"El ID de usuario {usuario.user_id} ya está registrado.")

    def dar_de_baja_usuario(self, user_id):
        if user_id in self.usuarios:
            del self.usuarios[user_id]
            self.usuarios_registrados.remove(user_id)
            print(f"Usuario con ID {user_id} ha sido dado de baja.")
        else:
            print(f"No se encontró un usuario con ID {user_id}.")

    def prestar_libro(self, user_id, isbn):
        if user_id in self.usuarios and isbn in self.libros:
            usuario = self.usuarios[user_id]
            libro = self.libros[isbn]
            usuario.prestar_libro(libro)
            del self.libros[isbn]
            print(f"Libro '{libro.titulo}' prestado a {usuario.nombre}.")
        else:
            print("Usuario o libro no encontrado.")

    def devolver_libro(self, user_id, isbn):
        if user_id in self.usuarios:
            usuario = self.usuarios[user_id]
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    usuario.devolver_libro(libro)
                    self.libros[isbn] = libro
                    print(f"Libro '{libro.titulo}' devuelto por {usuario.nombre}.")
                    return
            print("El usuario no tiene ese libro prestado.")
        else:
            print("Usuario no encontrado.")

    def buscar_libro(self, criterio, valor):
        resultados = []
        for libro in self.libros.values():
            if (criterio == "titulo" and valor.lower() in libro.titulo.lower()) or \
               (criterio == "autor" and valor.lower() in libro.autor.lower()) or \
               (criterio == "categoria" and valor.lower() in libro.categoria.lower()):
                resultados.append(libro)
        if resultados:
            print("Resultados de la búsqueda:")
            for resultado in resultados:
                print(resultado)
        else:
            print("No se encontraron libros con ese criterio.")

    def listar_libros_prestados(self, user_id):
        if user_id in self.usuarios:
            usuario = self.usuarios[user_id]
            if usuario.libros_prestados:
                print(f"Libros prestados a {usuario.nombre}:")
                for libro in usuario.libros_prestados:
                    print(libro)
            else:
                print(f"{usuario.nombre} no tiene libros prestados.")
        else:
            print("Usuario no encontrado.")
# Crear objetos de libro
libro1 = Libro("1984", "George Orwell", "Distopía", "1234567890")
libro2 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "Realismo Mágico", "0987654321")

# Crear objeto de usuario
usuario1 = Usuario("Juan Pérez", "user001")

# Crear objeto de biblioteca
biblioteca = Biblioteca()

# Añadir libros a la biblioteca
biblioteca.añadir_libro(libro1)
biblioteca.añadir_libro(libro2)

# Registrar un usuario
biblioteca.registrar_usuario(usuario1)

# Prestar un libro
biblioteca.prestar_libro("user001", "1234567890")

# Listar libros prestados
biblioteca.listar_libros_prestados("user001")

# Devolver un libro
biblioteca.devolver_libro("user001", "1234567890")

# Buscar un libro por título
biblioteca.buscar_libro("titulo", "cien años")

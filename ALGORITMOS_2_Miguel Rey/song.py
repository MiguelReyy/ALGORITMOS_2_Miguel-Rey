
"""Clase Song:
    Método __init__(self, identificador, nombre, artista, duracion, fecha_lanzamiento, generos=None):
        Para cada parámetro:
            Verificar tipo y valor
        Inicializar atributos con valores dados
        
    Método agregar_genero(self, genero):
        Si el género no está en la lista de géneros:
            Agregar el género a la lista de géneros
        
    Método __eq__(self, other):
        Devolver verdadero si los identificadores de self y other son iguales; de lo contrario, falso
        
    Método __str__(self):
        Devolver una cadena que representa la canción con su artista, nombre y duración
        
    Métodos getters y setters para todos los atributos

Función main():
    Crear una instancia de Song con valores de ejemplo
    Verificar los atributos de la instancia creada
    Crear otra instancia de Song con valores de ejemplo
    Verificar la representación de la canción
    Agregar un género a la canción y verificar si se ha agregado correctamente
    Crear otra instancia de Song con valores de ejemplo
    Verificar si dos canciones son iguales
"""
from datetime import date  # Importación de date desde datetime
from enum import Enum  # Importación de Enum desde enum
from genre import GENRE  # Importación de la enumeración GENRE desde genre.py

class Song:
    def __init__(self, identificador, nombre, artista, duracion, fecha_lanzamiento, generos=None):
        """Constructor de la clase Song."""
        # Verificar los tipos y valores de los parámetros
        if not isinstance(identificador, int):
            raise TypeError("El identificador debe ser un número entero.")
        if not isinstance(nombre, str):
            raise TypeError("El nombre debe ser una cadena de caracteres.")
        if not isinstance(artista, str):
            raise TypeError("El artista debe ser una cadena de caracteres.")
        if not isinstance(duracion, int) or duracion <= 10:
            raise ValueError("La duración debe ser un número entero mayor a 10 segundos.")
        if not isinstance(fecha_lanzamiento, date) or fecha_lanzamiento > date.today():
            raise ValueError("La fecha de lanzamiento debe ser un objeto date y no puede ser en el futuro.")
        if generos is not None and not isinstance(generos, list):
            raise TypeError("Los géneros deben ser una lista de elementos GENRE.")
        
        # Asignación de atributos
        self.identificador = identificador
        self.nombre = nombre
        self.artista = artista
        self.duracion = duracion
        self.fecha_lanzamiento = fecha_lanzamiento
        self.generos = set(generos) if generos else set()
        
    def agregar_genero(self, genre):
        """Agrega un género a la canción si no está etiquetada en dicho género."""
        if genre not in self.generos:
            self.generos.add(genre)
        
    def __eq__(self, other):
        """Indica si dos canciones son iguales basadas en el identificador único."""
        return isinstance(other, Song) and self.identificador == other.identificador
        
    def __str__(self):
        """Devuelve una representación en cadena legible para humanos de la canción."""
        return f"{self.artista} tocando {self.nombre} durante {self.duracion} segundos."

    # Setters y getters
    def get_id(self):
        return self.identificador
    
    def get_name(self):
        return self.nombre
    
    def get_artist(self):
        return self.artista
    
    def get_duration(self):
        return self.duracion
    
    def get_release_date(self):
        return self.fecha_lanzamiento
    
    def get_genres(self):
        return list(self.generos)
    
    def add_genre(self, genre):
        """Agrega un género a la canción."""
        self.generos.add(genre)

def main():
    """Función principal para probar la clase Song."""
    print("=================================================================.")
    print("Test Case 1: Create a Song.")
    print("=================================================================.")
    song = Song(1, "calorro", "estopa", 189, date.today(), [GENRE.POP])

    if song.get_id() == 1:
        print("Test PASS. The parameter id has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if song.get_name() == "calorro":
        print("Test PASS. The parameter name has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if song.get_artist() == "estopa":
        print("Test PASS. The parameter artist has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if song.get_duration() == 189:
        print("Test PASS. The parameter duration has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if song.get_release_date() == date.today():
        print("Test PASS. The parameter release_date has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if song.get_genres() == [GENRE.POP]:
        print("Test PASS. The parameter genres has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    print("=================================================================.")
    print("Test Case 2: Human-readable format of the object.")
    print("=================================================================.")
    song2 = Song(2, "calorro", "estopa", 189, date.today(), [GENRE.POP])

    if str(song2) == "estopa tocando calorro during 189 seconds.":
        print("Test PASS. The human-readable format of the object has been implemented correctly.")
        print(str(song2))
    else:
        print("Test FAIL. Check the method __str__()." + " RESULT: " + str(song2))

    print("=================================================================.")
    print("Test Case 3: song add_genre")
    print("=================================================================.")
    song2.add_genre(GENRE.ROCK)
    genres = song2.get_genres()
    if genres == [GENRE.POP, GENRE.ROCK]:
        print("Test PASS. The method add_genre(genre) has been implemented correctly.")
    else:
        print("Test FAIL. Check the method add_genre(genre), "+ " RESULT: " + str(genres))
    
    print("=================================================================.")
    print("Test Case 4: Test the method __eq__")
    print("=================================================================.")
    song3 = Song(2, "calorro", "estopa", 189, date.today(), [GENRE.POP])
    if song2 == song3:
        print("Test PASS. The method __eq__ has been implemented correctly.")
    else:
        print("Test FAIL. Check the method __eq__().")
    
main()


# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()


from enum import Enum  # Importa la clase Enum desde el módulo enum

class GENRE(Enum):  # Define la enumeración GENRE como una subclase de Enum
    ROCK = "ROCK"  # Define la constante ROCK con el valor "ROCK"
    POP = "POP"  # Define la constante POP con el valor "POP"
    EDM = "EDM"  # Define la constante EDM con el valor "EDM"
    COUNTRY = "COUNTRY"  # Define la constante COUNTRY con el valor "COUNTRY"

def main():
    """Función principal para probar la enumeración GENRE."""

    print("=================================================================.")
    print("Test Case 1: Check Class GENRE - Name.")
    print("=================================================================.")

    # Comprueba si ROCK es una instancia de GENRE
    if isinstance(GENRE.ROCK, GENRE):
        print("Test PASS. The enum for ROCK has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    # Comprueba si POP es una instancia de GENRE
    if isinstance(GENRE.POP, GENRE):
        print("Test PASS. The enum for POP has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    # Comprueba si EDM es una instancia de GENRE
    if isinstance(GENRE.EDM, GENRE):
        print("Test PASS. The enum for EDM has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    # Comprueba si COUNTRY es una instancia de GENRE
    if isinstance(GENRE.COUNTRY, GENRE):
        print("Test PASS. The enum for COUNTRY has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

# Comprueba si este módulo se está ejecutando independientemente
if __name__ == "__main__":
    main()

# EOF (End of File)


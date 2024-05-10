#Recursividad para calcular el factorial de un número.

def factorial(n):
    """Calcula el factorial de un número entero positivo."""
    if not isinstance(n, int) or n < 0:
        raise ValueError("El factorial solo está definido para números enteros no negativos.")
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

    #Código a realizar.

def main():
    print("=================================================================.")
    print("Test Case 1: Check the Factorial of 5.")
    print("=================================================================.")
    print("The factorial of 5 is: ", factorial(5))

if __name__ == "__main__":
    main()
    
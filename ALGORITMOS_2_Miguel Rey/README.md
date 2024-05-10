# NOMBRE DEL ALUMNO

# Factorial Calculator

## Hipótesis

El código debe ser capaz de calcular el factorial de un número entero no negativo proporcionado como entrada.

## Precondición

Se debe proporcionar un número entero no negativo como entrada a la función `factorial`. Se asume que el número proporcionado como entrada es válido y no excede los límites de la capacidad de representación de enteros en el sistema utilizado.

## Postcondición

La función `factorial` devolverá el factorial de `n` como salida. El resultado devuelto será un número entero que representa el factorial de `n`.

## Entrada

La entrada que necesita proporcionarse al programa es un número entero no negativo `n`.

## Salida

La salida que devuelve el código es el factorial del número proporcionado como entrada.

## Efecto

El código implementa una función recursiva llamada `factorial` que calcula el factorial de un número entero no negativo. Esta función toma como entrada un número entero `n` y devuelve su factorial como salida. Utiliza recursividad para calcular el factorial, multiplicando `n` por el factorial de `n-1`. La función maneja casos especiales como el factorial de 0, que es 1.

# Bubble Sort

## Definicion 

Bubble Sort es un algoritmo de ordenación simple que funciona comparando pares de elementos adyacentes y intercambiándolos si están en el orden incorrecto. Este proceso se repite hasta que no se necesiten más intercambios, lo que significa que la lista está ordenada.

## Uso

Bubble Sort es conveniente utilizarlo en casos donde la lista de elementos es pequeña o está casi ordenada. Sin embargo, no es eficiente para listas grandes, ya que su complejidad es O(n^2), lo que significa que su rendimiento empeora considerablemente a medida que aumenta el tamaño de la lista. En general, existen algoritmos de ordenación más eficientes para listas grandes, como Merge Sort o Quick Sort.

## Ejemplo conceptual

Supongamos que tenemos la lista de números: [34, 7, 23, 32, 5].

1. Comenzamos cogiendo el primer elemento de la lista en este caso el 34 y lo comparamos con cada uno de los siguientes elementos así: 

    1. Comenzamos comparando 34 con 7. Como 34 es mayor que 7, los intercambiamos: [7, 34, 23, 32, 5].
    2. Continuamos comparando 34 con 23. Como 34 es mayor que 23, los intercambiamos: [7, 23, 34, 32, 5].
    3. Comparamos 34 con 32. Como 34 es mayor que 32, los intercambiamos: [7, 23, 32, 34, 5].
    4. Comparamos 34 con 5. Como 34 es mayor que 5, los intercambiamos: [7, 23, 32, 5, 34].

2.  Una vez comparado el 34 con todos los elementos continuamos con el siguiene elemento de la lista original siendo este el 7:

    1. Comenzamos comparando 7 con 34. Como 7 es menor que 34, no los intercambiamos: [7, 23, 32, 5, 34].
    2. Continuamos comparando 7 con 23. Como 7 es menor que 34, no los intercambiamos: [7, 23, 32, 5, 34].
    3. Comparamos 34 con 32. Como 7 es menor que 34, no los intercambiamos: [7, 23, 32, 5, 34].
    4. Comparamos 34 con 5. Como 7 es mayor que 5, los intercambiamos: [5, 7, 23, 32, 34].

3. Repetimos el proceso con el resto de numeros hasta compararlos todos y el resultado es la lista ordenada.
    1. Al final, la lista ordenada sería: [5, 7, 23, 32, 34].